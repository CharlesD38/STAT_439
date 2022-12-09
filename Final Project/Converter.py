from traitlets.config import Config
import nbformat as nbf
from nbconvert.exporters import PDFExporter
from nbconvert.preprocessors import TagRemovePreprocessor
import os
'''
Module used to convert a notebook into a pdf.
---

Can also run as a script. Asks for user input which is the file path. 
'''

def get_dir():
    return os.getcwd()      # Get the working directory


def convert(file, direct = get_dir()):
    '''

    Used in a jupyter notebook to convert the notebook it to a pdf. 

    Parameters
    ---
    file: the full name of the file as a str() we want to convert.
    direct: Optional. the directory of the file you are converting. 
        innitiated as the working directory of the file

    Output
    ---
    A converted pdf in the same directory.
    '''

    path_notebook = direct + "\\" + file                               # Creating the full path for the notebook
    path_pdf = path_notebook.replace('ipynb', 'pdf')     # Creating the full path for the pdf


    # Setup config
    c = Config()

    c.TagRemovePreprocessor.remove_input_tags = ('hide_input',)     # Reads the hide_input tag for removing code cells during conversion
    c.TagRemovePreprocessor.enabled = True
    # Configure and run out exporter
    c.PDFExporter.preprocessors = ["nbconvert.preprocessors.TagRemovePreprocessor"]

    exporter = PDFExporter(config=c)
    exporter.register_preprocessor(TagRemovePreprocessor(config=c),True)

    # Configure and run our exporter - returns a tuple - first element with html,
    # second with notebook metadata

    output = PDFExporter(config=c).from_filename(
            path_notebook)

    # Write to output html file
    with open(path_pdf ,  "wb") as f:
        f.write(output[0])

def convert_as_script(path):
    '''

    Function to use when running this file as a script.

    Parameters
    ---
    path: the entire path inclduing the file name.

    Output
    ---
    A converted pdf in the same directory.
    '''

    path_notebook = path                               # Creating the full path for the notebook
    path_pdf = path_notebook.replace('ipynb', 'pdf')     # Creating the full path for the pdf


    # Setup config
    c = Config()

    c.TagRemovePreprocessor.remove_input_tags = ('hide_input',)     # Reads the hide_input tag for removing code cells during conversion
    c.TagRemovePreprocessor.enabled = True
    # Configure and run out exporter
    c.PDFExporter.preprocessors = ["nbconvert.preprocessors.TagRemovePreprocessor"]

    exporter = PDFExporter(config=c)
    exporter.register_preprocessor(TagRemovePreprocessor(config=c),True)

    # Configure and run our exporter - returns a tuple - first element with html,
    # second with notebook metadata

    output = PDFExporter(config=c).from_filename(
            path_notebook)

    # Write to output html file
    with open(path_pdf ,  "wb") as f:
        f.write(output[0])

if __name__ == "__main__":

    working_dir = str(input('Input the full working directory to the notebook you wish to convert: ')) 

    convert_as_script(working_dir)