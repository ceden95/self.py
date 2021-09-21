#the program answer True if the two files are equal or False if not.

def main():
    file1 = r"C:\python course\9.1.1\file1_for_filesComparison.txt" 
    file2 = r"C:\python course\9.1.1\file2_for_filesComparison.txt"  
    trueOrFalse = are_files_equal(file1, file2)
    print(trueOrFalse)

def are_files_equal(file1, file2):
    """the function return True if the two files are equal or False if not.
    :param file1, file2: strings to files path
    :file1, file2 types: str
    :return: True if the two files are equal or False if not
    :rtype: boolean"""
    a = open(file1, "r")
    b = open(file2, "r")
    c = a.read()
    print(c)
    d = b.read()
    print(d)
    if c==d:
        return True
    else:
        return False 
    a.close()
    b.close()

main() 