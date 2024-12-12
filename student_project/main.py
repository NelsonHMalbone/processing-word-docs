import docx
import os

directory = 'files'
output_file = 'files/merge_docs.py'

# Generate filenames
filenames = os.listdir(directory)

# Generate filepaths
filepaths = [os.path.join(directory, filename) for filename in filenames
             if filename.endswith('.docx')] # just incase other files are inside of the same file

