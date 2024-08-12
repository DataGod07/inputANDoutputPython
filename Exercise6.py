# Exercise 6: Write all content of a given file into a new file by skipping line number 5
filex = open('C:/Users/rahul/OneDrive/Documents/testtext.txt','r')
list_str = filex.readlines()
print(list_str)
filex.close()

filey = open('C:/Users/rahul/OneDrive/Documents/testtext1.txt','w')
count =  0
for line in list_str:
    if count == 4:
        count = count + 1
        continue
    else:
        filey.write(line)
        count+=1
        