import os
import shutil
from markdown_to_html_node import *
from extract_title import *
from copy_to_public import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    dest_dir = os.path.dirname(dest_path)

    with open(from_path, "r") as m:
        markdown = m.read()

    with open(template_path, "r") as t:
        template = t.read()

    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    lines = template.split("\n")
    new_lines = []

    for line in lines:
        #print(line)
        if line.strip().startswith("<title>"):
            #print(line.replace("{{ Title }}", title))
            new_lines.append(line.replace("{{ Title }}", title))
            continue

        if line.strip().startswith("<article>"):
            #print(line.replace("{{ Content }}", html))
            new_lines.append(line.replace("{{ Content }}", html))
            continue

        new_lines.append(line)

    page = "\n".join(new_lines)

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    with open(dest_path, "w") as h:
        h.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)

    for file in files:
        current_file = os.path.normpath(os.path.join(dir_path_content, file))
        #print(f"Current file: {current_file}")

        if os.path.isfile(current_file):
            if file.endswith(".md"):
                fname = f"{file[0:len(file) - 3]}.html"
                fpath = os.path.normpath(os.path.join(dir_path_content, file))
                dpath = os.path.normpath(os.path.join(dest_dir_path, fname))

                generate_page(fpath, template_path, dpath)
        else:
            new_cont_path = os.path.normpath(os.path.join(dir_path_content, file))
            new_dest_path = os.path.normpath(os.path.join(dest_dir_path, file))
            #print(f"New content path: {new_cont_path}")
            #print(f"New destination path: {new_dest_path}")

            if not os.path.exists(new_dest_path):
                os.mkdir(new_dest_path)

            generate_pages_recursive(new_cont_path, template_path, new_dest_path)
