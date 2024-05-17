# WAP that reads name of two python files and strips the extension. the file names are then concatenated to form a single string.
# The program then prints 'True' if the newly generated string is palindrome, or prints 'False' otherwise.

file1=input("enter the name of first python file: ")
file2=input("Enter the name of second  file: ")
file1_name = file1.split(".")[0]
file2_name = file2.split(".")[0]

concatenated_string = file1_name+file2_name
is_palindrome = concatenated_string.lower() == concatenated_string.lower()[::-1]
print(is_palindrome)
            
