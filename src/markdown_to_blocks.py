def markdown_to_blocks(markdown):
    stripped = markdown.strip()
    blocks = stripped.split('\n\n')

    new_blocks = []

    for block in blocks:
        new_blocks.append(block.strip())
        #print(block)

    #print(new_blocks)
    return new_blocks
