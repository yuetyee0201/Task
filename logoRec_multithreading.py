import io
#import pandas as pd    #actually I never use this
import os
import argparse
#from tqdm.auto import tqdm

from tqdm.contrib.concurrent import thread_map  # consider about multithreading
from functools import partial

from google.cloud import vision_v1 as vision


def main():
    args = parser()
    if os.path.isfile(args.outfile): # outfile exists? You don't want to overwrite it.
        print('[-] Outfile already exists.')
        exit(1)
    
    fileList = getFiles(args.path)
    if fileList == []:  # ...could happen
        print('[*] No img were found in given path.')
        
    client = vision.ImageAnnotatorClient.from_service_account_json(args.key) # set credential
    partialProcessImgs = partial(processImgs, client=client)
    results = thread_map(partialProcessImgs, fileList, max_workers=args.thread)
    
    output(results, args.outfile)
    

def output(results, outfile):
    outCsv = open(outfile,'w')
    for imgResult in results:  # single img from all img
        for r in imgResult:    # single logo result from all logos of img
            imgPath = r[0]
            brand = r[1]
            score = r[2]
            position = ''.join(str(r[3]).split())
            print(f"{imgPath}-----{brand}")
            outCsv.write(f'"{imgPath}","{brand}",{score},{position}\n')
    outCsv.close()


def getFiles(path):
    if not os.path.exists(path):    # assert...could we more graceful?
        print('[-] No such file or directory')
        exit(1)
        
    fileList = []
    if os.path.isfile(path):    # single file
        if _isImage(path):
            fileList.append(path)
        else:
            print('[-] Not a supported format')
        return fileList
    
    tmpList = os.listdir(path) # List files, it's not a file, so we process as a dir(batch mode).
    for f in tmpList:
        f = path+'/'+f  # assemble path of file
        if _isImage(f):
            fileList.append(f)            
    return fileList


def _isImage(path): # check images by magic header of file. PIL too slow, imghdr will be deprecated. 
    try:
        with open(path, 'rb') as f:
            header = f.read(10)
            if header.startswith(b'\xff\xd8'):  # JPEG
                return True
            elif header.startswith(b'\x89PNG\r\n\x1a\n'):  # PNG
                return True
            elif header[:6] in (b'GIF87a', b'GIF89a'):  # GIF
                return True
            elif header.startswith(b'BM'):  # BMP
                return True
            elif header.startswith(b'II*\x00') or header.startswith(b'MM\x00*'):  # TIFF
                return True
            elif header.startswith(b'RIFF') and b'WEBP' in header:  # WEBP
                return True
            else:
                return False
    except IOError:
        return False


def processImgs(imgPath, client): # Should I use multi-processing? nvm.
    result = []
    img = open(imgPath,'rb')
    imgHandler = vision.Image(content=img.read())
    response = client.logo_detection(image=imgHandler)
    logos = response.logo_annotations
    for logo in logos:
        result.append((imgPath, logo.description, logo.score, logo.bounding_poly))
    if response.error.message:
        raise Exception(
            print(f"[-]: {response.error.message}")
        )
    img.close()
    return result
    
def parser():
    parser = argparse.ArgumentParser(description='Logo recognition tool with Google API(json key)')
    parser.add_argument("path", help="Path to img file/dir with imgs")
    parser.add_argument("-k", "--key",required=True, help="Path to your [JSON key] from service account")
    parser.add_argument("-o", "--outfile", default='./output_logo_detection_2024.csv', help="Path to output csv")
    parser.add_argument("-t", "--thread", default=4,
                        type=lambda x: int(x) if 1 <= int(x) <= 12 else argparse.ArgumentTypeError("Threads number must be an int and between 1<=t<=12"),
                        help="Number of threads, 1<=t<=12")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()

