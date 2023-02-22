#!/usr/bin/env python
# coding: utf-8

# # Assignment_10-02-2023

# ## 1. Which Function is used to open a file ? What are the different modes of opening a file?Explain each mode of file opening.
# 
# ### Ans:-
# 
#             In Python, you can use the built-in function open() to open a file. The open() function returns a file object,
#             which you can use to read from or write to the file.
# 
#             The open() function takes two arguments: the name of the file you want to open and the mode in which you want 
#             to open it. The modes for opening a file are as follows:
#             
#             1.'r': read mode - This mode is used when you want to read from a file. It is the default mode, so if you don't
#                                specify a mode, the file will be opened in read mode.
#             2.'w': write mode - This mode is used when you want to write to a file. If the file already exists, the old 
#                                 contents will be deleted and replaced with the new content. If the file doesn't exist, 
#                                 a new file will be created.
#             3.'a': append mode - This mode is used when you want to add content to an existing file. The new content will 
#                                  be added to the end of the file.
#             4.'x': exclusive creation mode - This mode is used when you want to create a new file but don't want to 
#                                  overwrite an existing file. If the file already exists, a FileExistsError will be raised. 
#                                  
#             5.'b': binary mode - This mode is used when you want to read or write binary data, such as images or audio 
#                                  files.
#             6.'t': text mode - This mode is used when you want to read or write text data, such as a plain text file. 
#                                This is the default mode if you don't specify a mode.
#                                
#             
#             You can combine modes by specifying them as a string, such as 'wb' for write mode and binary mode.
# 
#                 Here's an example of how to open a file in write mode and write to it:---------->>>>
#                 
#                 file = open('filename.txt','w')
#                 file.write  ('Manas,Pandey!')
#                 file.close()
#                 
#                 Alternatively, you can use a with statement to automatically close the file when you're done with it:
#                 
#                 with open('filename.txt','w')as file:
#                      file.write('Manas,Pandey!')
#                      
#                      
# 

# ## 2. Why close() function used? Why it is important to close a file.
# 
# ### Ans:-
# 
#           In Python, it is important to close a file using the close() function 
#           
#           When a file is opened, the operating system creates a connection between the file and the program that opened it.
#           This connection requires system resources, and if the connection is not closed properly, those resources can be 
#           tied up, potentially leading to performance issues or even crashes. Additionally, if the program exits without 
#           closing the file, any data that has not been written to the file may be lost.
#           
#           The close() function is used to terminate the connection between the program and the file, releasing any system
#           resources that were being used by the connection. It also ensures that any changes made to the file are saved 
#           before the connection is terminated.
#           
#           Here's an example of how to use the close() function to close a file after writing to it:
#           
#           file = open ('example.txt','w')
#           file.write  ('This is an example')
#           file.close()
#           
#           
# 

# ## 3. Write a python program to create a text file.write 'I want become a Data Scientist ' in that file. then close the file and read the content of the file.
# 
# ### Ans:-
# 

# In[1]:


# Open the file in write mode
with open('my_file.txt', 'w') as f:
    # Write the string to the file
    f.write('I want to become a Data Scientist')

# Open the file in read mode
with open('my_file.txt', 'r') as f:
    # Read the contents of the file
    file_contents = f.read()

# Print the contents of the file
print(file_contents)


# ## 4. Explain the following with python code : read(),readline() and readlines().
# 
# ### Ans:-
#             In Python, there are three methods that can be used to read data from a file: read(), readline(), and 
#             readlines(). Here's an explanation of each method, along with some examples:
#             
# ## 1. read()
#           The read() method reads the entire contents of the file as a string. If you don't specify an argument, it will 
#           read the entire file. You can also specify how many bytes you want to read:
#               
#                   # Open the file in read mode
#                     file = open('example.txt', 'r')
#                 # Read the entire contents of the file
#                     content = file.read()
#                     print(content)
#                 # Close the file
#                     file.close()
# ## 2. readline()
#            The readline() method reads a single line from the file. If you call it again, it will read the next line, 
#            and so on until the end of the file. Here's an example:
#            
#            # Open the file in read mode
#                 file = open('example.txt', 'r')
# 
#            # Read the first line of the file
#                 line1 = file.readline()
#                 print(line1)
# 
#            # Read the second line of the file
#                 line2 = file.readline()
#                 print(line2)
# 
#             # Close the file
#                 file.close()
#                 
# ## 3. readlines()
#           The readlines() method reads the entire contents of the file and returns a list of strings, where each string
#           represents a single line in the file. Here's an example:
#           
#           # Open the file in read mode
#                 file = open('example.txt', 'r')
# 
#           # Read the entire file and store the lines in a list
#                 lines = file.readlines()
#                 print(lines)
# 
#          # Close the file
#                 file.close()
#           
#           
#           
#           
#           

# ## 5.Explain why with statement is used with open().what is the advantage of using with statement and open together?
# 
# ### Ans:-
# 
#         The with statement in Python is used in conjunction with the open() function to provide a more concise and secure 
#         way of working with files.
#         
#         When you use the with statement to open a file, Python automatically handles the opening and closing of the file
#         ensuring that the file is closed properly when you're done with it. This can be particularly useful when working 
#         with large or complex programs, as it helps to reduce the risk of memory leaks, and ensures that 
#         you don't accidentally leave a file open and tie up system resources.
#         
#         with open('example.txt', 'r') as file:
#         content = file.read()
#         print(content)
#         
#         One advantage of using the with statement with open() is that it eliminates the need to explicitly close the file
#         using the close() method. This can make your code more concise and easier to read, since you don't have to worry 
#         about remembering to close the file. Additionally, the with statement ensures that the file is closed properly 
#         even if an error occurs, which can help to prevent bugs and other issues.
#         
#         Overall, using the with statement in conjunction with the open() function is a best practice when working with 
#         files in Python. It provides a more secure and convenient way of working with files, and can help to ensure that 
#         your code is easier to read and less error-prone.
# 

# ## 6. Explain the write() and writelines() functions.Give a suitable example.
# 
# ### Ans:-
# 
#         In Python, write() and writelines() are methods for writing data to a file. The write() method is used to write 
#         a single string to a file, while the writelines() method is used to write a list of strings to a file.
# 
#         The write() method takes a single string argument and writes that string to the file. It returns the number of 
#         characters written. If the file is opened in text mode, the string is expected to be a Unicode string, while if 
#         the file is opened in binary mode, it is expected to be a bytes-like object.
# 
#         Here's an example of how to use the write() method:
#         
#         with open('example.txt', 'w') as f:
#         f.write('Hello, world!')
#         
#         The writelines() method, on the other hand, takes a list of strings as an argument and writes each string to 
#         the file, one by one. It does not add any separator between the strings. Like write(), writelines() returns 
#         the number of characters written.
# 
#         Here's an example of how to use the writelines() method:
#         
#         with open('example.txt', 'w') as f:
#         lines = ['This is the first line\n', 'This is the second line\n', 'This is the third line\n']
#         f.writelines(lines)
#         
#         
# 
