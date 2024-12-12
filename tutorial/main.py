"combining word documents to one document with python"
# need to install with pip install python-docx
import docx

# our input is the two files in files folder
docpath1 = 'files/panda1.docx'
docpath2 = 'files/panda2.docx'

# creating a special class from the docx library
"need for however many docs you need to go thur"
doc1 = docx.Document(docpath1)
doc2 = docx.Document(docpath2)

# read and print out the first file
paragraphs = doc1.paragraphs

# extracting text
para1 = paragraphs[0]  # first paragraph
para_text = para1.text  # the text from para1