import os
import shutil
from markdown_to_html_node import *
from extract_title import *

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
        shutil.mkdir(dest_dir)

    with open(dest_path, "w") as h:
        h.write(page)
