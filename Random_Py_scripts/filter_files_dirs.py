import os
import sys
import re
'''Different ways of searching for files'''

def get_files_list_dir(path):
    list_files =[]
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)) and 'cmd' in i:
            list_files.append(i)
    return list_files
list_files_=[]


def listdir(d):
    if not os.path.isdir(d):
        list_files_.append(d)
    else:
        for item in os.listdir(d):
            listdir((d + '/' + item) if d != '/' else '/' + item)

def list_3(path):
    rx = re.compile(r'(cmd_).+\.(py)$')
    r = []
    for path, dnames, fnames in os.walk(path):
        r.extend([os.path.join(path, x) for x in fnames if rx.search(x)])
    return r


def list_4(path):
    rx = re.compile(r'(cmd_).+\.(py)$')
    r = []
    for fnames in os.listdir(path):
        if rx.search(fnames):
            r.append(os.path.join(path,fnames))
    return r

def main():
    #print(get_files_list_dir(sys.argv[1]))
    #listdir(sys.argv[1])
    #print(list_files_)
    print(list_4(sys.argv[1]))


if __name__ == "__main__":
	main()