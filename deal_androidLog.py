# -*- coding:UTF-8 -*-
import  os

def dealLine(_str,packName):
    if _str.find(packName) > -1:
        return _str
    else:
        return False

if __name__ == "__main__":
    filePath = raw_input("input the filePath :")
    filePath = os.path.abspath(filePath)
    packageName = raw_input("input the packageName:")
    if os.path.exists(filePath) and os.path.isfile(filePath):
        tempArr = os.path.splitext(filePath)
        outputFile = tempArr[0] + "_deal" + tempArr[1]
        with open(filePath,'rU') as in_f:
            with open(outputFile,'w') as out_f:
                for line in in_f.readlines():
                    lineRes = dealLine(line,packageName)
                    if lineRes:
                        out_f.writelines(lineRes)
    else:
        print filePath+" is not exists or not a file"
        os.system('pause')
