sub=[]
sub.append("maths")
sub.append("english")
sub.append("marathi")    #append function
sub.append("eco")
sub.append("physic")
sub.append("chem")
print(sub)
print(type(sub))
sub.insert(2,"biology") #insert function
print(sub)
print(sub.remove("biology")) #remove function
sub.sort()                    #sort function
print(sub)
sub.reverse()                  #reverse function
print(sub)
print(len(sub))                #len fuction
print(max(sub))                #max function
print(min(sub))                 #min function
print(sub[1:2])                  #range function
print(sub.pop())                 #pop function :which pickup any random element
print(sub.pop())              
print(sub.split(","))    