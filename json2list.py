#! /usr/bin/python
# coding = utf-8

import os
import sys

import binhex
import json


class ReadDict:

    def __init__(self, file_dir):
        self.file_dir = file_dir

    def read_from_json(self, mode='r'):
        dic = {}
        with open(self.file_dir, mode) as fp:
            dic = fp.read()
            dic = json.loads(dic)

        return dic


def dict2list(dic):

    data = []

    for line in dic:  # line  is the key.
        data.append(dic[line])
        line = line.replace('0x', '')

        for i in range(6 - len(line)):
            line = '0' + line

        data.append('0x' + line[-2:])
        data.append('0x' + line[-4:-2])
        data.append('0x' + line[-6:-4])

    return data


def wr_list2txt(lis, file_dir, mode='w+'):

    with open(file_dir, mode) as fp:
        fp.write('\n')

        for i in range(len(lis)):
            fp.write('data[%d] = %s' % (i, lis[i]))
            fp.write('\n')

            if (i+1) % 4 == 0:
                fp.write('\n')


def main():
    dict = ReadDict('./config.json')

    dic = dict.read_from_json(mode='r')
    data = dict2list(dic)

    wr_list2txt(data, './cache.txt', 'w+')


if __name__ == "__main__":
    main()

# script starts here.
if len(sys.argv) < 2:
    print ('No action specified.')
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':  #当命令行参数为-- version，显示版本号
        print ('Version 1.0')
    elif option == 'help':  #当命令行参数为--help时，显示相关帮助内容
        print ('''/
This program convert json file into  list and save in txt file, 
used in awg10g project.
Options include:
  --version : Prints the version number
  --help    : Display this help''')
    else:
        print ('Unknown option.')
    sys.exit()
else:
    file_dir_i = sys.argv[1]
    file_dir_o = sys.argv[2]

    dict = ReadDict(str(file_dir_i))

    dic = dict.read_from_json(mode='r')
    data = dict2list(dic)


    wr_list2txt(data, str(file_dir_o), 'w+')
        
