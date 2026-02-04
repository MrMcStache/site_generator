from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    #print(new_nodes)

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            #print(f"added {node}: {new_nodes}")

        if delimiter in node.text:
            split_node = node.text.split(delimiter, maxsplit=2)
            #print(f"split = {split_node}")

            if len(split_node) != 3:
                raise Exception("ERROR: Uneven delimiters in node")

            for n in range(len(split_node)):
                if n == 1:
                    new_nodes.append(TextNode(split_node[n], text_type))
                    #print(f"added {text_type}: {new_nodes}")
                else:
                    new_nodes.append(TextNode(split_node[n], TextType.TEXT))
                    #print(f"added TEXT: {new_nodes}")
        else:
            new_nodes.append(node)

    return new_nodes
