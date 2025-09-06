input_path = "remplacer par le chemin de votre fichier"
output_path = "remplacer par le chemin de votre fichier"

with open(input_path, "r") as f:
    content = f.read().upper()

with open(output_path, "w") as f:
    f.write(content)