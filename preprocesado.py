from os import walk
from shutil import copyfile
from cv2 import cv2
# tipo = 'maligno'

def preTest():
    path = 'D:\\CIC\\Matematicas\\ReconocedorAlfabeto\\asl_alphabet_test\\asl_alphabet_test'

    # f = []
    # dirpath, dirnames, filenames = walk(path)

    print(path)
    dst = 'D:\\CIC\\Matematicas\\ReconocedorAlfabeto\\bw\\test\\'
    for (dirpath, dirnames, filenames) in walk(path):
        # f.extend(filenames)
        # print(filenames)
        for (index, name) in enumerate(filenames):
            # print(name, index) 
            # elements = name.split('-')
            # zoom = elements[3]
            # num = elements[4]
            # print(dirpath+'\\'+name)
            gray = cv2.imread(dirpath+'\\'+name, 0)
            cv2.imwrite(dst+name, gray)
            # print('zoom = {} num={}'.format(zoom, num))
            # print(dst+zoom+'x\\maligno\\'+name)
            # copyfile(dirpath+'\\'+name, dst+'\\'+name)

            # break

def preTrain():
    path = 'D:\\CIC\\Matematicas\\ReconocedorAlfabeto\\asl_alphabet_train\\asl_alphabet_train'

    # f = []
    # dirpath, dirnames, filenames = walk(path)

    print(path)
    dst = 'D:\\CIC\\Matematicas\\ReconocedorAlfabeto\\bw\\train\\'
    for (dirpath, dirnames, filenames) in walk(path):
        # f.extend(filenames)
        # for signal in dirnames:
        
        # print(filenames)
        for (index, name) in enumerate(filenames):
            # print(name) 
            # elements = name.split('-')
            # zoom = elements[3]
            # num = elements[4]
            # print(dirpath+'\\'+name)
            # print('zoom = {} num={}'.format(zoom, num))
            # print(dst+zoom+'x\\maligno\\'+name)
            # copyfile(dirpath+'\\'+name, dst+'\\'+name)
            gray = cv2.imread(dirpath+'\\'+name, 0)
            cv2.imwrite(dst+name, gray)
            # break

# preTest()
preTrain()
print('Finish!!')
