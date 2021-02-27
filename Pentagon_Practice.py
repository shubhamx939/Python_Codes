#Taking two Strings:
print("Enter 1st String S1")
s1=input()

print("Enter 2nd String S2")
s2=input()

#Reversing the Second String so that we can traverse straight through it:
s2=s2[::-1]


#Calculating the length of the Strings:
len1=len(s1)
len2=len(s2)

#Initial values for i and maxLen:
i=0
maxLen=len1


#Checking for the bigger String to loop till last element:
if(len1>len2):
    maxLen=len1
if(len2>len1):
    maxLen=len2

#Declaring newStr which will hold the resulting String:    
newStr=""


#looping through the elements of both the String:
for i in range(maxLen):
    
    if(i<len1):
        data1=s1[i]
        newStr=newStr+data1
    if(i<len2):
        data2=s2[i]
        newStr=newStr+data2
        
    i=i+1

#Resultant Sting newStr:
print(newStr)
    
    
