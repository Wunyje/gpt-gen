from PyPDF2 import PdfFileReader, PdfFileWriter
import os 

def insert_bookmarks(pdf_file, outline, offset):
    # Create a temporary output file name
    output_file = pdf_file + '.temp'
    
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        # Create a PDF reader and writer object
        reader = PdfFileReader(file)
        writer = PdfFileWriter()
        
        # Add all pages from the input file to the output file
        for page in range(reader.getNumPages()):
            writer.addPage(reader.getPage(page))
        
        # Parse the outline string into a list of tuples
        outline_list = []
        for line in outline.split('\n'):
            if line.strip():
                title, page = line.rsplit('\t', 1)
                indent = len(line) - len(line.lstrip())
                outline_list.append((title.strip(), int(page.strip()), indent))
        
        # Add bookmarks to the output file
        parent_bookmarks = []
        for title, page, indent in outline_list:
            if indent == 0:
                bookmark = writer.addBookmark(title, page + offset)
                parent_bookmarks = [bookmark]
            else:
                parent = parent_bookmarks[indent - 1]
                bookmark = writer.addBookmark(title, page + offset, parent=parent)
                if len(parent_bookmarks) > indent:
                    parent_bookmarks[indent] = bookmark
                else:
                    parent_bookmarks.append(bookmark)
        
        # Write the output file
        with open(output_file, 'wb') as output:
            writer.write(output)
    
    # Replace the original file with the updated file
    os.replace(output_file, pdf_file)
