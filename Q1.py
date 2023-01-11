#slicing
listl= [1,2,3,4,5,6]
print(listl[1:5])



#palindrome
list2=["ab", "abc", "aba"]
for element in list2:
    if (element==element[::-1]):
        print(f"yes, {element} is a palindrome!")



#repeated characters
list3=["aab","abc", "def"]
for ele in list3:
    if len(ele)!=len(set(ele)):
        print(f"{ele} contains repeated characters")



#variable no. of arguments -> SLICER
def slicer(*args):
    print(args[1:5])
slicer(1,3,4,5,6)
slicer(1,3,5,6,4,2,4,6)
slicer(1312,323,5,433464,645,66,4,2,4,6)   
   
   
#variable no. of arguments -> PALINDROME CHECKER
def checker(*args):
    for element in args:
        if (element==element[::-1]):
            print(f"yes, {element} is a palindrome!")
            
checker("ab", "abc", "aba")  
checker("aa","avs","avc","abba")


#variable no. of arguments -> REPEATED CHARACTERS
def repeated(*args):
    for ele in args:
        if len(ele)!=len(set(ele)):
            print(f"{ele} contains repeated characters")
    
repeated("ab", "abc", "aba")  
repeated("aa","avs","avc","abba")