import os
from cairosvg import svg2png

# define the name of the template file. Template file must be in the same folder as this .py file.
my_template_file_name = "LibraryDIYTileTemplate.svg"

# define a function that generates a new svg file with the desired text.
def duplicate_tile_with_new_text(template_file_name, text, output_dir):
    """ duplicate SVG file, replacing template text with new text

    Paramaters
    ----------
    template_file_name: string
        filename of template svg file
    text: string
        text that will be used to replace the placeholder text value
    output_dir: string
        relative path of desired output directory

    """
    fin = open(template_file_name, "rt")
    output_svg_filename = text + ".svg"
    output_svg_path = os.path.join(output_dir, output_svg_filename)
    fout = open(output_svg_path, "wt")

    for line in fin:
	    fout.write(line.replace('placeholder_button_text', text))
	
    fin.close()
    fout.close()
    return  output_svg_path

# process each text file in this direcory
for filename in os.listdir('./'):
    if filename[-4:] == '.txt':
        # check to see if a directory exists with the same name. If not, make one
        if not os.path.isdir(filename[:-4]):
            os.mkdir(filename[:-4])

        # process the lines in this text file
        fin = open(filename, "rt")
        for line in fin:
            if line.rstrip() != "": # skip empty lines
                # create new svg file with replacement text
                out_svg_path = duplicate_tile_with_new_text(my_template_file_name, line.rstrip(), filename[:-4])
                # convert output file to png
                with open(out_svg_path) as svg_fin:
                    out_png_path = out_svg_path.replace('.svg', '.png')
                    with open(out_png_path, 'wb') as png_fout:
                        svg2png(bytestring=bytes(svg_fin.read(),'UTF-8'), write_to=png_fout)
        print("Finished processing " + filename)

print("done")
