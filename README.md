# Library DIY Button Creator

overview of what this is
![](img/example_button.png)

## Dependencies

- python 3
- inkscape

## Usage

### Specifying the button content

You can configure what text you want in your buttons. Just create a .txt file in the same directory as this README. Type each button text on a separate line of the file.

For example, consider a file named `some_buttons.txt` that contains

```
I am looking for a specific article

I want to find or browse journals by subject

```

[Running the batch button creator](Running-the-script) will create a new directory `some buttons`, in which two button images will be created as shown

![](img/specific_article.png)
![](img/journals_by_subj.png)

### Running the script

In a terminal, navigate to this project's root directory and run

```
python batch_button_maker.py
```

## Current limitations
- for current limitations, see [Issues](https://github.com/selegra/library_diy/issues)