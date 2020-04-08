# Library DIY Button Creator

![](img/example_button.png)

This python script batch-creates button images that can then be uploaded to a LibGuide or other content management system to create a Library DIY framework. Library DIY is a self-guided research help tool originally created by Portland State University Library. To access their orignial Drupal/PHP-based solution, visit the [PSU Library GitHub](https://github.com/pdxlibrary/Library-DIY).

## Dependencies

- python 3
- inkscape

## Usage

### Specifying the button content

You can configure the text so the buttons read whatever is most useful for your needs. Just create a .txt file in the same directory as this README. Type each button's text on a separate line of the .txt file.

For example, consider a file named `some_buttons.txt` that contains

```
I am looking for a specific article

I want to find or browse journals by subject

```

[Running the batch button creator](Running-the-script) will create a new directory `some buttons`, in which two button images (.svg and .png) will be created as shown

![](img/specific_article.png)
![](img/journals_by_subj.png)

### Running the script

In a terminal, navigate to this project's root directory and run

```
python batch_button_maker.py
```

## Current limitations
- for current limitations, see [Issues](https://github.com/selegra/library_diy/issues)