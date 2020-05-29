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
