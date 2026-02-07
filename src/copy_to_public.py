import os
import shutil
from textnode import *

def copy_to_public(current_dir, cur_pub_dir):
    #print(f"{current_dir}\n{cur_pub_dir}")
    current_file = None
    files = os.listdir(current_dir)
    #print(f"files in directory: {files}")
    pub_files = os.listdir(cur_pub_dir)
    #print(f"files in public directory: {pub_files}")

    for file in files:
        current_file = os.path.normpath(os.path.join(current_dir, file))
        #print(f"current file: {file}")

        if os.path.isfile(current_file):
            #print(f"{file} is a file")
            shutil.copy(current_file, cur_pub_dir)
            #print(f"{file} copied to public")
        else:
            #print(f"{file} is a directory")
            new_pub_dir = os.path.normpath(os.path.join(cur_pub_dir, file))
            os.mkdir(new_pub_dir)
            #print(f"{file} directory created in public")
            new_dir = current_file
            #print(f"current directory is {new_dir}")

            copy_to_public(new_dir, new_pub_dir)


def verify_public():
    static_dir = os.path.abspath("static")
    public_dir = os.path.abspath("docs")
    #print(static_dir)
    #print(public_dir)

#Verifies that public exists and clears it, otherwise creates public
    if os.path.exists(public_dir):
        pub_dirs = os.listdir(public_dir)
        #print(f"pub_dirs: {pub_dirs}")

        for dir in pub_dirs:
            p = os.path.normpath(os.path.join(public_dir, dir))
            #print(f"norm/join: {p}")
            if os.path.isfile(p):
                os.remove(p)
            else:
                shutil.rmtree(p)

            if os.path.exists(p):
                raise Exception(f"ERROR: {p} directory still exists after rmtree")

        if os.listdir(public_dir):
            raise Exception(f"ERROR: files/directories still in public folder")
    else:
        os.mkdir(public_dir)

#Begin copying from static to public
    current_dir = static_dir
    copy_to_public(current_dir, public_dir)
