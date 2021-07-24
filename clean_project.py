import argparse
import os
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', metavar='I', type=str)
parser.add_argument('--output_dir', metavar='O', type=str)
parser.add_argument('--file_extension', metavar='F', type=str)
#parser.add_argument('--node_types', type=str, help='a list of node types to be selected')
opt = parser.parse_args()

def main(opt):
    input_dir = opt.input_dir
    output_dir = opt.output_dir
    file_extension = opt.file_extension
    for subdir, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(subdir, file)
                full_file_name = file_path.replace("/", "_")
                full_file_name = full_file_name.replace(".._", "")
                full_file_name = full_file_name.replace("___", "_")
                target_path = os.path.join(output_dir,full_file_name)
                shutil.copy2(file_path, target_path)


if __name__ == "__main__":
    opt = parser.parse_args()
    main(opt)
