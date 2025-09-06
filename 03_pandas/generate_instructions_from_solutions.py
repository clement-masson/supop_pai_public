"""
This script reads a Jupyter notebook file named "solutions.ipynb", processes its cells, and generates a new notebook file named "instructions.ipynb".
It removes the output from each code cell, checks if the first line of the source code contains the word "solution", and replaces the rest of the lines with a placeholder comment.
The new notebook file is saved in the same directory.
Author: Clément MASSON
Date: 2023-10-03
"""

import json

with open("solutions.ipynb", "r") as f:
    cells = json.load(f)

for cell in cells["cells"]:
    if cell["cell_type"] == "code":
        # Remove the output from the cell
        cell["outputs"] = []

        # Check if the first line of the source code contains "Solution"
        if cell["source"] and isinstance(cell["source"], list) and len(cell["source"]) > 0:
            first_line = cell["source"][0]
            if "solution" in first_line.lower():
                # Replace the rest of the lines with "insert your code here"
                cell["source"] = [first_line] + ["# insert your code here\n"]

# Save the modified notebook
with open("instructions.ipynb", "w") as f:
    json.dump(cells, f, indent=4)