# Write a program that reads full name as an input and returns abbreviations of the first and middle names except the last name. (Note that the abbreviations must be in
# capitals.Also only the first letter in the surname must be in uppercase)

def acronym(word):
   n=word.split()
   acronym=""
   for i in range(len(n)):
       if i < len(n) -1:
          acronym += n[i][0].upper() + ". "
       else:
            acronym += n[i].capitalize()
            return acronym

s=input("Enter your name:")
result= acronym(s)
print(result)

