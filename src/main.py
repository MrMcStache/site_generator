import os
import shutil
from copy_to_public import *
from extract_title import *
from generate_page import *

def main():
    #Check/clean public and copy from static
    verify_public()

    #Generate html page from template and copy to public
    generate_page("content/index.md", "template.html", "public/index.html")

    return 0

if __name__ == "__main__":
    main()
