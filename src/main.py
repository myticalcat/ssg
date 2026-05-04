import os
import shutil
from pathlib import Path
from blocknode import markdown_to_html_node 
from function_helper import extract_title

def copy_static():
    if not os.path.exists("./static"):
        print("no static path dectected!")
        return
    copy_recusive("./static", "./public", True)

def generate_contents(content_path = "./content", public_path = "./public"):
    if not os.path.exists(content_path):
        print("no content path dectected!")
        return
    for ls in os.listdir(content_path):
        fp = os.path.join(content_path, ls)
        if os.path.isfile(fp): 
            generate_page(fp, "template.html", public_path)
        else:
            generate_contents(fp,os.path.join(public_path, ls))

def copy_recusive(from_path, to_path, is_root = False):
    if is_root and os.path.exists(to_path):
        print(f"cleaning root path: {to_path}")
        shutil.rmtree(to_path)

    if not os.path.exists(to_path):
        print(f'creaing directory: {to_path}')
        os.makedirs(to_path)

    ls = os.listdir(from_path)

    for file in ls:
        file_path = os.path.join(from_path, file)
        if os.path.isfile(file_path):
            print(f"copying {file_path} -> {to_path}")
            shutil.copy(file_path, to_path)
        else:
            copy_recusive(file_path, os.path.join(to_path,file))

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = Path(from_path).read_text()
    template = Path(template_path).read_text()
    content = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
        
    with open(os.path.join(dest_path, from_path.split("/")[-1].replace(".md", ".html")), "w", encoding="utf-8") as file:
        file.write(template)


if __name__ == "__main__":
    copy_static()
    generate_contents()
