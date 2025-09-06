import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_path", help="chemin vers le fichier à convertir")
parser.add_argument("output_path", help="chemin vers le fichier à générer")
args = parser.parse_args()

with open(args.input_path, "r") as f:
    content = f.read().upper()

with open(args.output_path, "w") as f:
    f.write(content)