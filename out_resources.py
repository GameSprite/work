#!python2.6
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 下午9:35
# @Author  : ChenGuanzhou
# @File    : out_resources.py

import os
import re
import shutil


__CCBDIR__ = ''
__AllResSet__ = set()
__resourceFolder__ = ''
__deleteResDir__ = ''
'''
deal with the file with name: fname

return resource filename string(unique) {List}
'''

def dealFile(fname):
    with open(fname,'rU') as in_f:
        for line in in_f.readlines():
            mobj = re.search('(\w+/)*\w+\.(png|fnt)',line)
            if mobj:
                restr = mobj.group()
                if restr[-3:] == 'fnt':
                    __AllResSet__.add(restr.replace('/','\\'))    
                    with open(__resourceFolder__+"\\"+restr,'rU') as fntFile:
                        for fntline in fntFile.readlines():
                            fnt_picMobj = re.search("\w+\.png",fntline)
                            if fnt_picMobj:
                                restr = os.path.dirname(restr)+'\\' + fnt_picMobj.group()
                                __AllResSet__.add(restr.replace('/','\\'))
                else:
                    __AllResSet__.add(restr.replace('/','\\'))    
                    


if __name__ == "__main__":
    #dir input
    __CCBDIR__ = raw_input('input directory of ccb files :').strip()
    assert os.path.isdir(__CCBDIR__), 'the ccb dir: ' + __CCBDIR__ + ' is not a directory really.'

    __resourceFolder__ = raw_input('input directory of resource files:').strip()
    assert os.path.isdir(__resourceFolder__), 'the dir: ' + __resourceFolder__ + ' is not a directory really.'

    __deleteResDir__ = raw_input('input folder dir contains deleted picture files:').strip()
    assert os.path.isdir(__resourceFolder__), 'the dir: ' + __deleteResDir__ + ' is not a directory really.'

    for parent, dirnames, filenames in os.walk(__CCBDIR__):
        #get files ext is ccb
        for file in filenames:
            if os.path.splitext(file)[1] == '.ccb':
                dealFile(parent+'\\'+file)

    # copy resources file into result folder
    delfileNum = 0
    with open(__deleteResDir__+'/deleteFilenames.txt','w') as delFileTxt:
        for parent, dirnames, filenames in os.walk(__resourceFolder__):
            for file in filenames:
                fileExt = os.path.splitext(file)[1]
                if  fileExt == '.png' or fileExt == '.fnt':
                    fname = parent + '\\' + file

                    compareFname = fname[fname.index('ccbResources'):]
                    
                    if compareFname not in __AllResSet__:
                        delfileNum += 1
                        #record in txt
                        delFileTxt.writelines(fname+'\n')

                        os.system("@echo off")
                        os.system("move  " + fname + "  " + __deleteResDir__)

    print('delete files : %d'%(delfileNum))

    #os.system('pause')