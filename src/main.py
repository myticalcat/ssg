from textnode import TextNode, TextType
import os
import shutil

def copy_static():
    if not os.path.exists("./static"):
        print("no static path dectected!")
        return
    if not os.path.exists("./public"):
        print("no public path dectected!")
        return
    copy_recusive("./static", "./public", True)

def copy_recusive(from_path, to_path, is_root = False):
    print(os.listdir(from_path))


if __name__ == "__main__":
    copy_static()
    # print(TextNode("hello",TextType.LINK, "mytical.cat"))