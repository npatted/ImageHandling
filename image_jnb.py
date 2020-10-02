import nbformat as nbf
import csv
nb = nbf.v4.new_notebook()
text = """\
# Working With Images
Open Image with Image Information."""

text1="""\
# Crop Image."""

text2="""\
# Copying And Pasting Images."""

code = """\
import easygui
from PIL import Image
flower=Image.open(easygui.fileopenbox(default='*.jpg'))
print(flower.size)
print(flower.filename)
print(flower.format_description)
flower"""

code1="""\
cut_flower= flower.crop((120,100,200,200))
cut_flower"""

code2="""\
flower.paste(im=cut_flower,box=(300,0))
flower"""

nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code),
               nbf.v4.new_markdown_cell(text1),
               nbf.v4.new_code_cell(code1),
               nbf.v4.new_markdown_cell(text2),
               nbf.v4.new_code_cell(code2)]
fname = 'JPG_jnb.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)