import os
from shlex import quote
# define the name of the template file. Template file must be in the same folder as this .py file.
my_template_file_name = "LibraryDIYTileTemplate.svg"
png_export_dpi = 300
inkscape_exec_mac = "/Applications/Inkscape.app/Contents/Resources/bin/inkscape"

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

    Returns
    -------
    string
        path of output svg file
    """
    fin = open(template_file_name, "rt")
    output_svg_filename = text + ".svg"
    output_svg_path = os.path.join(output_dir, output_svg_filename)
    fout = open(output_svg_path, "wt")

    for line in fin:
        fout.write(line.replace('placeholder_button_text', text))

    fin.close()
    fout.close()
    return output_svg_path


# process each text file in this direcory
for filename in os.listdir('./'):
    if filename[-4:] == '.txt':
        # check to see if a dir exists with the same name. If not, make one.
        if not os.path.isdir(filename[:-4]):
            os.mkdir(filename[:-4])

        # process the lines in this text file
        fin = open(filename, "rt")
        for line in fin:
            if line.rstrip() != "":  # skip empty lines
                svg_out_path = duplicate_tile_with_new_text(my_template_file_name, line.rstrip(), filename[:-4])
                svg_out_path = os.path.abspath(svg_out_path)
                # use inkscape to convert to svg
                png_out_path = svg_out_path.replace(".svg", ".png")
                os.system("{} -z {} -e {} -d {}".format(
                    inkscape_exec_mac,
                    quote(svg_out_path),
                    quote(png_out_path),
                    png_export_dpi))
        print("Finished processing " + filename)

print("done")
