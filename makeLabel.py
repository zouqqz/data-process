# -*- coding: utf-8 -*-

"""
生成label.txt文件，文件内容类似
105_03_629 5 1 5
105_03_613 5 1 5
105_03_668 5 1 5
105_03_501 5 1 5
"""

import os
import sys
import config_default
import shutil

os.chdir(sys.path[0])
xml_folder = os.path.join(os.path.pardir, config_default.configs['folder'], 'annotations', 'xmls')
image_folder = os.path.join(os.path.pardir, config_default.configs['folder'], 'images')
data_folder = os.path.join(os.path.pardir, config_default.configs['folder'])
trainval_file_path = os.path.join(data_folder, 'annotations', 'trainval.txt')

def compare(xml_list, image_list):
    ret_list = []
    xml_list_with_no_ext = []
    image_list_with_no_ext = []

    for x in image_list:
        if os.path.splitext(x)[1] not in ('.jpg', '.png'):
            continue

        image_name = os.path.splitext(x)[0]
        image_list_with_no_ext.append(image_name)

    for x in xml_list:
        if os.path.splitext(x)[1] not in ('.xml',):
            continue

        file_name = os.path.splitext(x)[0]
        xml_list_with_no_ext.append(file_name)

    for x in xml_list_with_no_ext:
        if x not in image_list_with_no_ext:
            ret_list.append(x)

    for x in image_list_with_no_ext:
        if x not in xml_list_with_no_ext:
            ret_list.append(x)

    if len(ret_list) > 0:
        print('The following label is missing:')
        print(ret_list)

def makeLabels(xml_list):
    if os.path.isfile(trainval_file_path):
        os.remove(trainval_file_path)

    with open(trainval_file_path, 'a') as trainval_file:
        for x in xml_list:
            if os.path.splitext(x)[1] not in ('.xml',):
                continue

            trainval_file.write('%s %s %s %s\n' % (x[:-4], x[2], 1, x[2]))
    
    shutil.copyfile(trainval_file_path, os.path.join(os.path.dirname(trainval_file_path), 'list.txt'))
    shutil.copyfile(trainval_file_path, os.path.join(os.path.dirname(trainval_file_path), 'test.txt'))


if __name__ == "__main__":
    xml_list = os.listdir(xml_folder)
    image_list = os.listdir(image_folder)

    compare(xml_list, image_list)
    makeLabels(xml_list)