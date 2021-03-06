import config_default
import os
import sys
import shutil

os.chdir(sys.path[0])
trainval_file_path = os.path.join(os.path.pardir, config_default.configs['folder'], 'annotations', 'trainval.txt')
new_trainval_file_path = os.path.join(os.path.pardir, config_default.configs['target_folder'], 'annotations', 'trainval.txt')
xml_folder = os.path.join(os.path.pardir, config_default.configs['folder'], 'annotations', 'xmls')
image_folder = os.path.join(os.path.pardir, config_default.configs['folder'], 'images')
new_xml_folder = os.path.join(os.path.pardir, config_default.configs['target_folder'], 'annotations', 'xmls')
new_image_folder = os.path.join(os.path.pardir, config_default.configs['target_folder'], 'images')

def makeDirs():
    if(not os.path.isdir(new_xml_folder)):
        os.makedirs(new_xml_folder)

    if(not os.path.isdir(new_image_folder)):
        os.makedirs(new_image_folder)

def makeFiles():
    for xml_file_name in os.listdir(xml_folder):
        copySplitedXmlFiles(xml_file_name)

    for image_name in os.listdir(image_folder):
        copySplitedImage(image_name)

def copySplitedXmlFiles(xml_file_name):
    splited_xml_file_name_array = xml_file_name.split('_')

    for file_type, batch_name in config_default.configs['files'].items():
        if file_type != splited_xml_file_name_array[0]:
            continue

        if '*' in set(batch_name.split(',')):
            shutil.copyfile(os.path.join(xml_folder, xml_file_name), os.path.join(new_xml_folder, xml_file_name))
            makeLabel(xml_file_name)
            break

        for _batch_name in set(batch_name.split(',')):
            if _batch_name == splited_xml_file_name_array[1]:
                shutil.copyfile(os.path.join(xml_folder, xml_file_name), os.path.join(new_xml_folder, xml_file_name))
                makeLabel(xml_file_name)
                break

def copySplitedImage(image_name):
    splited_image_file_name_array = image_name.split('_')

    for file_type, batch_name in config_default.configs['files'].items():
        if file_type != splited_image_file_name_array[0]:
            continue

        if '*' in set(batch_name.split(',')):
            shutil.copyfile(os.path.join(image_folder, image_name), os.path.join(new_image_folder, image_name))
            break

        for _batch_name in set(batch_name.split(',')):
            if _batch_name == splited_image_file_name_array[1]:
                shutil.copyfile(os.path.join(image_folder, image_name), os.path.join(new_image_folder, image_name))
                break


def makeLabel(xml_file_name):
    with open(new_trainval_file_path, 'a') as trainval_file:
        trainval_file.write('%s %s %s %s\n' %
                            (xml_file_name[:-4], 
                             xml_file_name[2], 
                             1,
                             xml_file_name[2]))



if __name__ == '__main__':
    if os.path.isfile(new_trainval_file_path):
        os.remove(new_trainval_file_path)

    makeDirs()
    makeFiles()
    shutil.copyfile(new_trainval_file_path,
                    os.path.join(
                        os.path.dirname(new_trainval_file_path), 'list.txt'))
    shutil.copyfile(new_trainval_file_path,
                    os.path.join(
                        os.path.dirname(new_trainval_file_path), 'test.txt'))
