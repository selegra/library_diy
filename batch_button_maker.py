# define the name of the template file. Template file must be in the same folder as this .py file.
my_template_file_name = "LibraryDIYTileTemplate.svg"

# define the name of the text lines file. file must be in the same folder as this .py file.
text_lines_file_name = 'library_diy_tile_text.txt'

# define a function that generates a new svg file with the desired text.
def duplicate_tile_with_new_text(template_file_name, text):
    fin = open(template_file_name, "rt")
    fout = open(text + ".svg", "wt")

    for line in fin:
	    fout.write(line.replace('placeholder_button_text', text))
	
    fin.close()
    fout.close()

# open the text lines files
fin = open(text_lines_file_name, "rt")
for line in fin:
	duplicate_tile_with_new_text(my_template_file_name, line.rstrip())

print("done")

# data types:
# char: "a" or "1" or "$"
# string: a string of characters, e.g. "kittis 4$ 4 salze"
# int: 4
# float: 4.234