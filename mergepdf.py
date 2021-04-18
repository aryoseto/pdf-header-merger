''' 
Merging two pdf files, content and project header


'''

__author__      = "Aryo Wicaksono - Ramzitech"
__copyright__   = "Copyright 2021, Ramzitech"
__version__ = "0.0.1"


import PyPDF2


def merge_pdf(path_header, path_content, path_output,  skipfirst=False) :

    with open(path_content, 'rb') as handler_cont :
        cont = PyPDF2.PdfFileReader(handler_cont)

        # Check how many pages
        cont_num_pages = cont.getNumPages()

        with open(path_header, 'rb') as handler_head :
            head = PyPDF2.PdfFileReader(handler_head)

            # Check how many pages
            head_num_pages = head.getNumPages()

            # Check if the have the same pages
            statusrun = False
            if skipfirst :
                if cont_num_pages ==  head_num_pages - 1 :
                    statusrun = True 
                    print("Skip first is True")
                    print("Head file page number: " + str(head_num_pages))
                    print("Content file page number: " + str(cont_num_pages))
                else :
                    raise Exception("Number of pages do not match, header file should be one more or same with content") 
                
            else :
                if cont_num_pages ==  head_num_pages :
                    statusrun = True 
                    print("Skip first is false")
                    print("Head file page number: " + str(head_num_pages))
                    print("Content file page number: " + str(cont_num_pages))
                else :
                    raise Exception("Number of pages do not match, header file should be one more or same with content")    

            # Pdf object to put all the new pages
            pdf_writer = PyPDF2.PdfFileWriter()

            if skipfirst :
                    for pageno in range(head_num_pages) :

                        if pageno == 0 :
                            page_head = head.getPage(pageno)
                            pdf_writer.addPage(page_head)
                
                        else :
                            page_head = head.getPage(pageno)
                            page_cont = cont.getPage(pageno - 1)

                            page_head.mergePage(page_cont)
                            pdf_writer.addPage(page_head)
            else :
                    for pageno in range(head_num_pages) :

                            page_head = head.getPage(pageno)
                            page_cont = cont.getPage(pageno)

                            page_head.mergePage(page_cont)
                            pdf_writer.addPage(page_head)

            with open(path_output, "wb") as handler_out:
                # write the merged file into new file
                pdf_writer.write(handler_out)

if __name__ == "__main__":
    filename_head = "Document1.pdf"
    filename_cont = "Document2.pdf"
    filename_out  = "Merged_Doc.pdf"

    merge_pdf(filename_head, filename_cont, filename_out, skipfirst=True)
