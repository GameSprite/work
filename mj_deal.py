#coding=utf8
#author:cgz

import os
import random
'''
1.对于png,mp3,jpg末尾都随机出2个字节的内容追加到文件尾
2.对于json文件,在最后添加一个新键值，因为程序中只读第一个键值对。键和值都是单个字符
3.tmx文件是标准xml文件，在文件末尾随机出一个注释<!--xy--> xy是随机出来的单个字符
4.js文件在末尾追加 //2个字节的内容
5.ccbi文件是非标准的非文本文件，无法处理
6.atlas fnt是文本文件，无法加入额外信息不可以修改
7.ccbi和atlas要修改，需要引擎修改文件读入代码
'''
__WORKPATH__ = ''
fileNum = 0
CHARNUM = 2 #选用多少字节插入
FUNCSTR = ''

def getStrWithRandomChar(num):
    re = ''
    for i in range(num):
        re += chr(65 + int(25 * random.random()))
    return re    
def dispose_png_jpg_mp3_file(absFilePath):
    with open(absFilePath,'a') as file:
        file.write(getStrWithRandomChar(CHARNUM))
def dispose_js_file(absFilePath):
    with open(absFilePath,"a") as file:
        file.write("//"+getStrWithRandomChar(CHARNUM))
        file.write(FUNCSTR)
def dispose_json_file(absFilePath):
    with open(absFilePath,"a",newline='\n') as file:
        #excel工具导出的json文件换行符全部是\n(0x0a)
        appendStr =',\n"'+getStrWithRandomChar(2)+'":'+'"'+getStrWithRandomChar(CHARNUM)+'"\n}'
        os.lseek(file.fileno(),-1,os.SEEK_END)
        file.truncate()
        file.write(appendStr)
def dispose_xml_file(absFilePath):
    #tmx文件换行符是0x0D0A
    with open(absFilePath,'a') as file:
        appendStr = '<!--' + getStrWithRandomChar(CHARNUM) + '-->'
        file.write(appendStr)
if __name__ == '__main__':
    __WORKPATH__ = input("input the folder that need to be disposed:").strip()
    assert os.path.isdir(__WORKPATH__),"inputed :"+__WORKPATH__+"is not a folder"
    with open(os.path.join(__WORKPATH__,'func.txt'),'rU') as file:
        FUNCSTR = '\n'+file.read()
    for root, dirs, files in os.walk(__WORKPATH__):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            abspath = os.path.abspath(os.path.join(root,file))
            fileNum += 1
            if ext == '.png' or ext == '.jpg' or ext == '.mp3':
                dispose_png_jpg_mp3_file(abspath)
            elif ext == '.json':
                dispose_json_file(abspath)
            elif ext == '.tmx' or ext == '.plist':
                dispose_xml_file(abspath)
            elif ext == '.js' or ext == '.fsh':
                dispose_js_file(abspath)
            else:
                fileNum -= 1

    print('disposed %d files'%fileNum)            



