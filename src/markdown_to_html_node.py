from markdown_to_blocks import *
from block_type import *
from parentnode import *
from leafnode import *
from text_to_textnodes import *
from text_to_html import *

def text_to_children(text):
    textnodes = text_to_textnodes(text)

    html_nodes = []

    for node in textnodes:
        html_nodes.append(text_node_to_html_node(node))

    if html_nodes:
        return html_nodes
    else:
        return None

def text_to_list_children(text, m_len):
    lines = text.split("\n")

    children = []

    for line in lines:
        if line:
            line = line[m_len:]
            c = text_to_children(line)
            children.append(ParentNode("li", c))

    if children:
        return children
    else:
        return None

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    #print(f"blocks: {blocks}")

    nodes = []

    for block in blocks:
        match block_to_block_type(block):
            case BlockType.HEADING:
                n = 0
                for c in block[0:6]:
                    if c == "#":
                        n += 1

                node = LeafNode(f"h{n}", block[n + 1:])
                nodes.append(node)

            case BlockType.CODE:
                lines = block.split("\n")
                text = f'{"\n".join(lines[1:len(lines) - 1])}\n'

                node = LeafNode("code", text)
                p_node = ParentNode("pre", [node])
                nodes.append(p_node)

            case BlockType.QUOTE:
                lines = block.split("\n")

                new_lines = []

                for line in lines:
                    if line.startswith("> "):
                        new_lines.append(line[2:])
                    else:
                        new_lines.append(line[1:])

                text = " ".join(new_lines)

                node = ParentNode("blockquote", text_to_children(text))
                nodes.append(node)

            case BlockType.UNORDERED_LIST:
                node = ParentNode("ul", text_to_list_children(block, 2))
                nodes.append(node)

            case BlockType.ORDERED_LIST:
                node = ParentNode("ol", text_to_list_children(block, 3))
                nodes.append(node)

            case _:
                node = ParentNode("p", text_to_children(block.replace("\n", " ")))
                nodes.append(node)

    #print(f"nodes: {nodes}")

    parent_node = ParentNode("div", nodes)

    return parent_node
