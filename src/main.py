import os
import shutil
from copy_to_public import *
from extract_title import *
from generate_page import *

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        #print(basepath)
    else:
        basepath = "/"

    #Check/clean docs and copy from static
    verify_public()

    #Generate html page from template and copy to docs
    generate_pages_recursive("content/", "template.html", "docs/", basepath)

    return 0

if __name__ == "__main__":
    main()
