from enum import Enum
import re

class BlockType(Enum):
    PAR = "paragraph"
    HEAD = "heading"
    QUOTE = "quote"
    CODE = "code"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

def block_to_block_type(block : str) -> BlockType:
    heading_prefix = [(i * "#")+" " for i in range(1, 7)]
    for sw in heading_prefix:
        if block.startswith(sw):
            return BlockType.HEAD
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        return BlockType.QUOTE
    
    if block.startswith("-"):
        return BlockType.U_LIST
    
    if re.findall(r"^[0-9]*\. ", block):
        return BlockType.O_LIST
    
    return BlockType.PAR