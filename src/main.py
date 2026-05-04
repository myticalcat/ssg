import os
import shutil

def copy_static():
    if not os.path.exists("./static"):
        print("no static path dectected!")
        return
    copy_recusive("./static", "./public", True)

def copy_recusive(from_path, to_path, is_root = False):
    if is_root and os.path.exists(to_path):
        print(f"cleaning root path: {to_path}")
        shutil.rmtree(to_path)

    if not os.path.exists(to_path):
        print(f'creaing directory: {to_path}')
        os.mkdir(to_path)

    ls = os.listdir(from_path)

    for file in ls:
        file_path = os.path.join(from_path, file)
        if os.path.isfile(file_path):
            print(f"copying {file_path} -> {to_path}")
            shutil.copy(file_path, to_path)
        else:
            copy_recusive(file_path, os.path.join(to_path,file))

if __name__ == "__main__":
    copy_static()
