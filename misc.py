L=False     # logical variable for checking if
St=""       # input list 1
St1=""      # input list 2
St2=[]      # list of words present in both input lists

def limited_input(length):
    # input of given length, returns two strings
    len1=length+3
    while len1>length:
        output1 = input("Enter up to 60 symbols for string 1: ")
        len1=len(output1)
    len2=length+3
    while len2>length:
        output2 = input("Enter up to 60 symbols for string 2: ")
        len2=len(output2)
    return output1, output2

St, St1 = limited_input(60)
St = " " + St + " "
St1 = " " + St1 + " "

for word in St.split():
    if ' '+word+' ' in St1:
        St2.append(word)

if St2 == []:
    L = False
else:
    L = True

print()
print("St  string consists of: \t\t", St)
print("St1 string consists of: \t\t", St1)
print("St2 list is filled with common words: \t", St2)

print()
print("L is equal to: \t", L)
if L:
    print("common words: \t", *St2)