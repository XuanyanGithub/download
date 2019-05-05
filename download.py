#pip3 install wget

import wget
import zipfile

def download(ur1):
    filename=wget.download(ur1)
    print("\n",filename,"downloaded!\n")
    return filename

def unzip(filename,path=None): #只有.zip格式的压缩文件才能解压
    with zipfile.ZipFile(filename,"r") as zip_ref:
        if not path:
            zip_ref.extract()
        else:
            zip_ref.extract(path)
    print("\n",filename,"unzipped!\n")

if __name__=="__main__":
    ur1="https://dl.dropboxusercontent.com/s/y5b2kj7ci7iwjb2/lut_rainbow.png?dl=0"
    file_name=download(ur1)
    #unzip(file_name)