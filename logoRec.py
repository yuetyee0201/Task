import io
#import pandas as pd    #actually I never use this
import os
import argparse
from tqdm.auto import tqdm
from google.cloud import vision_v1 as vision


def main():
    args = parser()
    fileList = getFiles(args.path)
    processImgs(fileList, args.key, args.outfile)


def getFiles(path):
    if not os.path.exists(path):
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


def processImgs(fileList, key, outfile): # Should I use multi-processing? nvm.
    if os.path.isfile(outfile): # outfile exists? You don't want to overwrite it.
        print('[-] Outfile already exists.')
        exit(1)
        
    client = vision.ImageAnnotatorClient.from_service_account_json(key) # set credential
    if fileList == []:
        print('[*] No img were found.')
    bar = tqdm(total=len(fileList))    # init the BAR
    
    outCsv = open(outfile, 'w')
    
    result = []
    for f in fileList:
        img = open(f,'rb')
        imgHandler = vision.Image(content=img.read())
        response = client.logo_detection(image=imgHandler)
        logos = response.logo_annotations
        print("Logos:")
        for logo in logos:
            result.append(f'{f}-----{logo.description}')
            outCsv.write(f'{f},"{logo.description}"\n')
        if response.error.message:
            raise Exception(
                print(f"[-]: {response.error.message}")
            )
        bar.update(1)
        img.close()
    bar.close()
    outCsv.close()
    print('\n'.join(result))

def parser():
    parser = argparse.ArgumentParser(description='Logo recognition tool with Google API(json key)')
    parser.add_argument("path", help="Path to img file/dir with imgs")
    parser.add_argument("-k", "--key",required=True, help="Path to your [JSON key] from service account")
    parser.add_argument("-o", "--outfile", default='./output_logo_detection_2024.csv', help="Path to output csv")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()

