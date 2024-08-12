# Exercise 9: Check file is empty or not
File1 = open('C:/Users/rahul/OneDrive/Documents/empt.txt','r')
list_data = []
for ln in File1:
    list_data.append(ln)
File1.close()
if len(list_data) == 0:
    print('File is empty')
else:
    print('File is not empty')
