# in third line enter name of documents
# in forth line enter number of archive
text_doc_name = input("name of document?:")
archive_num = int(input("number of archive?:"))
the_most_important_files = input("important files?:")
#create important files in txt format!
output = ("your name of text documents %s\n number of archive files %i\n your important files %s\n " % (text_doc_name, archive_num, the_most_important_files) )
#created txt files!
#open and write txt information in this file!
files = open("doc.txt", 'w')
files.write(output)
files.close()
# the end of the process!