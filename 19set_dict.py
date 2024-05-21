# Given a piece of text, write a program to build a frequency listing of words and displaythem in a sorted order on 'key'.

n=str(input("enter text: "))
alphabet={} #dictionary
temp=[]  #list

#for sorting the text in temporary list
for k in n: #k=key 
    ch=k
    if k not in temp and k !=" ":
        temp.append(k)
#sort the text
temp.sort()

#append in the dictionary with the frequency
for k in temp: #k=key 
    ch=k
    if ch not in alphabet:
        alphabet[ch]=n.count(k)
print(alphabet)


