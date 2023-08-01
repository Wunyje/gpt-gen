# EBook-Bookmarks-Insert
## Requirement
```
pip install PyPDF2
pip install pytesseract
```
## Program Outline
This software coded in *Python* can auxiliarily insert bookmarks or outlines for PDF ebook.
* Main function:
* * 1 Extract the table of the content about the ebook, get the raw text about titles and page number.
* * * 1.1 For photocopy PDF, use OCR to scan out the table of the content.
* * * 1.2 For pure text PDF, copy the table of the content out of the PDF files.
* * 2 Modify the raw text about table of content, to generate a PDF file's outline in proper format.
* * 3 Insert bookmarks with offset.

* Expectation:
* * 1 Automatically locate the table of content.
* * 2 For files that don't have table of content, automatically recongnize the titles within the file.

## More in detial
1.  **Extract the table of contents**: Depending on the type of PDF (photocopy or pure text), I would use different methods to extract the table of contents. For photocopy PDFs, I would use an OCR library such as Tesseract or PyTesseract to scan the table of contents and extract the raw text. For pure text PDFs, I would use a PDF library such as PyPDF2 or pdfrw to extract the text directly from the PDF file.
    
2.  **Process the raw text**: Once I have the raw text of the table of contents, I would process it to extract the titles and page numbers. This could involve using regular expressions or string manipulation methods to identify and extract the relevant information.
    
3.  **Generate the outline**: With the titles and page numbers extracted, I would use a PDF library such as PyPDF2 or pdfrw to generate an outline in the proper format for the PDF file.
    
4.  **Insert bookmarks with offset**: Finally, I would use the same PDF library to insert bookmarks into the PDF file at the appropriate locations, taking into account any specified offset.


## File structure
```
my_project/
├── main.py
├── pdf_processor/
│   ├── __init__.py
│   ├── extractor.py
│   ├── formatter.py
│   └── inserter.py
└── utils/
    ├── __init__.py
    └── ocr.py
```
The `main.py` file would contain the main logic of the program, such as parsing command-line arguments and coordinating the different components of the software.

The `pdf_processor` package would contain modules related to processing PDF files, such as extracting the table of contents (`extractor.py`), formatting the outline (`formatter.py`), and inserting bookmarks (`inserter.py`). Each module would have a specific, well-defined responsibility, leading to high cohesion within the package.

The `utils` package would contain utility modules that could be used by other parts of the program. In this case, it contains an `ocr.py` module that provides functionality for performing OCR on photocopy PDFs.

This structure promotes high cohesion by grouping related functionality into separate modules and packages. It also promotes low coupling by minimizing the dependencies between different parts of the program. For example, the `pdf_processor` package does not need to know about the details of how OCR is performed; it can simply use the functionality provided by the `ocr` module in the `utils` package.
