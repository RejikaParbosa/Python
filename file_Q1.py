#python program to read the content from the text file "file.txt" line by line and display the same on the screen.

f=open('file.txt','r')
t=f.readlines()
for i in t:
    print(i, end ='')
f.close()

#python program to count and display the total number of words in a text file "file.txt".
fname=open('file.txt','r')
num_words=0
with open('file.txt','r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("\nNumber of words: ")
print(num_words)

