from enum import Enum

class BlockType(Enum):
    PAR = "paragraph"
    HEAD = "heading"
    QUOTE = "quote"
    CODE = "code"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"