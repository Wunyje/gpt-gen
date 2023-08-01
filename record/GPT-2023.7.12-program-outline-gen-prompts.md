```
Assuming that you are a master in coding C and using Gstreamer. Convert this to Gstreamer C API :```gst-launch-1.0 v4l2src device=/dev/video41 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! autovideosink```
```

```	
There is a requirement of implementing a sofware
"
This software coded in *Python* can auxiliarily insert bookmarks or outlines for PDF ebook.
* Main function:
* * 1 Extract the table of the content about the ebook, get the raw text about titles and page number.
* * * 1.1 For photocopy PDF, use OCR to scan out the table of the content.
* * * 1.2 For pure text PDF, copy the table of the content out of the PDF files.
* * 2 Modify the raw text about table of content, to generate a PDF file's outline in proper format.
* * 3 Insert bookmarks with offset.
"
How would you do that? Tell your thought step by step.
```
```
I noticed that the points in program outline are seperated and isolated, make outline more intergral about the whole program to form a complete solution, relate the points in the outline, after all, the eventual program is an *intergral application*
```
```
Give me the possible file composition and file structure under the rules of *High cohesion, low coupling*. Think step by step**
```
```
Try to write the pseudo code of all the files of the program, revealing the dynamic invoking relationship between these files
```
```
Write a Python script to generate the files with pseudo code in the file structure you've designed.
```