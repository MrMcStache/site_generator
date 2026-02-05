from textnode import *
from extract_markdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    #print(new_nodes)

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if delimiter in node.text:
                split_node = node.text.split(delimiter)
                #print(f"split = {split_node}")

                if len(split_node) % 2 == 0:
                    raise Exception("ERROR: Uneven delimiters in node")

                for n in range(len(split_node)):
                    #print(f"current node: {split_node[n]}")
                    if split_node[n] == "":
                        continue
                    elif n % 2 == 0:
                        new_nodes.append(TextNode(split_node[n], TextType.TEXT))
                        #print(f"added TEXT: {new_nodes}")
                    else:
                        new_nodes.append(TextNode(split_node[n], text_type))
                        #print(f"added {text_type}: {new_nodes}")
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
            #print(f"added {node}: {new_nodes}")

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            matches = extract_markdown_images(text)

            for i in range(len(matches)):
                before, after = text.split(f"![{matches[i][0]}]({matches[i][1]})", 1)
                text = after

                if before != "":
                    new_nodes.append(TextNode(before, TextType.TEXT))

                new_nodes.append(TextNode(matches[i][0], TextType.IMAGE, matches[i][1]))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            matches = extract_markdown_links(text)

            for i in range(len(matches)):
                before, after = text.split(f"[{matches[i][0]}]({matches[i][1]})", 1)
                text = after

                if before != "":
                    new_nodes.append(TextNode(before, TextType.TEXT))

                new_nodes.append(TextNode(matches[i][0], TextType.LINK, matches[i][1]))

    return new_nodes
