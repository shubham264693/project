text="Where are you? Meet me near the play station"
test_list = text.split()

index_list1 = [0, 3, 6]
index_list2 = [1, 4, 7]
index_list3 = [2, 5, 8]


  
# printing original lists 
print ("Original list : " + str(test_list)) 
print()
print ("Original index list : " + str(index_list1)) 
print()
# using list comprehension to  
# elements from list  
res_list = [test_list[i] for i in index_list1] 
      
# printing result 
print ("Resultant list : " + str(res_list))
print()
#for replacing Vowels

def replace_vowel(mlist):
    vowels="aeiou"
    newlist=[]
    for word in mlist:
        for char in word:
            if char in vowels:
                word=word.replace(char,'%')
        newlist.append(word)
    return newlist
print (replace_vowel(res_list))
print('\n')

print ("Original list : \n " + str(test_list) + "\n")
print ("Original index list : \n " + str(index_list2))

res_list1 = [test_list[i] for i in index_list2]

print ("Resultant list : \n " + str(res_list1) + "\n")

def replace_consonants(plist):
    consonants="bcdfghjklmnopqrstuvwxyz"
    newtlist=[]
    for word1 in plist:
        for char in word1:
            if char in consonants:
                word1=word1.replace(char,'#')
        newtlist.append(word1)
    return newtlist
print (replace_consonants(res_list1))

print('\n')

print("Original List : " + str(test_list) + "\n")
print("Index Of REquired Vaule \n" + str(index_list3) + '\n')

res_list2 = [test_list[i] for i in index_list3]

print("Resultant Values are \n " + str(res_list2)) 

res_list3 = [x.upper() for x in res_list2]

print(str(res_list3))

