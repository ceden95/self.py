#the program copying the content of one file to another one.
#the copied file will contain the copied content only.


def main():
    source = "C:\python course\9.2.2\9.2.2.filesCopy.txt"
    destination = "C:\python course\9.2.2\9.2.2.filesPaste.txt"
    copy_file_content(source, destination)
    #the following code is for checking.
    open_paste_for_check = open(destination, "r")
    read_for_check = open_paste_for_check.read()
    print(read_for_check)
    open_paste_for_check.close()

def copy_file_content(source, destination):
    """the funcאtion copy the information in the source to the destination file
    :param source, destination: file paths to files.
    :source, destination type: str
    :return: none."""
    opened_Copy_File = open(source, "r")
    readed_Copy_File = opened_Copy_File.read()
    opened_Paste_File = open(destination, "w")
    opened_Paste_File.write(readed_Copy_File)
    opened_Copy_File.close()
    opened_Paste_File.close()

main()
