import os
import click
from shutil import copy2

def get_image_count(): 
    files = os.listdir('./uploads')
    files = [file for file in files if 'jpg' in file.lower()]
    return len(files)

def copy_image(path):
    image_name = f'{get_image_count() + 1}.jpg'
    copy2(path, f'./uploads/{image_name}')
    return image_name

def get_image_config(image_name, description): 
    image_count = get_image_count()
    txt = open('index.html').read()
    config = txt.split('---')[1]
    config += f'  - image: /uploads/{image_name}\n    caption: {description}\n'
    return config

def write_index_file(new_config):
    txt = open('index.html').read()
    config = txt.split('---')
    config[1] = new_config
    txt = '---'.join(config)
    with open('index.html','w') as f:
        f.write(txt)

@click.command()
@click.argument('path')
@click.argument('description')
def main(path, description):
    image_name = copy_image(path)
    config = get_image_config(image_name, description)
    write_index_file(config)

if __name__ == '__main__':
    main() 
