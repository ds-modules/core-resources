import json
import autopep8
import sys
import re

file_path = sys.argv[1]
notebook = json.load(open(file_path, 'r'))

for c in notebook['cells']:
    if c['cell_type'] == 'code':
        cell_code = ''.join(c['source'])
        pep8_code = autopep8.fix_code(cell_code)
        pep8_cell = re.split(r'(\n)', pep8_code)
        pep8_cell = [x for x in pep8_cell if len(x) > 0]

        if len(pep8_cell) > 0 and pep8_cell[-1] == "\n":
            pep8_cell = pep8_cell[:-1]

        c['source'] = pep8_cell

new_file_path = file_path[:-6] + '-PEP8.ipynb'
json.dump(notebook, open(new_file_path, "w"))
