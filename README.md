# pdf-header-merger
Annex header made easy

## Purpose
Putting a set of pdf on top of another pdf and combine them. Useful if you have annexes in the report that need specific project header/footer. 
Instead of putting the annexes into a word file that has header, the file can be printed to pdf and combine it with the header. 

## How to use
* Print your annexes to pdf, combine it into 1 pdf files (if you have multiple files). [File A]
* Create a "blank" document with the header and footer with same number of page to the annex file. (You can add 1 extra page for the title) [File B]
* Combine File A and File B using `merge_pdf(fileA, fileB, name_of_combined_file)`


Created using [PyPDF2][1]

[1]: https://pypi.org/project/PyPDF2/ "PyPDF2 link"
