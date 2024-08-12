# Exercise 10: Read line number 4 from the following file
File1 = open('C:/Users/rahul/OneDrive/Documents/testtext.txt','r')
count = 0
list_line = []
for line in File1:
    if count == 4:
        list_line.append(line)
        count+=1
        continue
    else:
        count+=1
print(File1.close())
print(File1.closed)
print(list_line)