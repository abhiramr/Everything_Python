import sys, os
from pprint import pprint
import subprocess
from subprocess import call

#check folders and check for .git 
def __main__(*args):
    print("Directory = {}\n".format(args[0][1]))
    top = args[0][1]
    toplevel = [os.path.join(top,i) for i in (os.listdir(top))]
    toplevel_d = [i for i in toplevel if os.path.isdir(i)]
    # pprint(toplevel_d)
    script_dir = os.getcwd()
    
    for i in toplevel_d:
        if ".git" in os.listdir(i):
            print(i)
            print("----------")
            os.chdir(i)
            subprocess.run(['git', 'status'])
            os.chdir(script_dir)
            print("===========\n")

if __name__ == "__main__":
    __main__(sys.argv)