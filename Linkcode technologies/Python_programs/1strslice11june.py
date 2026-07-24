x="India is my country!"
print(x[6:9])
print(x[12:17])
print(x[7:10])
print(x[16:])
print(x[::-1])

#palindrome
y=input("Enter the string:")
if y==y[::-1]:
   print("Palindrome")
else:
   print("not palindrome")

#count the no. of digits and char in string
x="abc1234"
ct_digit=0
ct_char=0
for ch in x:
    if(ch>='0' and ch<='9'):
      ct_digit+=1
    elif(ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
      ct_char+=1
print("count of digit is:",ct_digit)
print("count of char is:",ct_char)


#using isalpha and isdigit
#count the no. of digits and char in string
x="abc1234"
ct_digit=0
ct_char=0
for ch in x:
    if ch.isdigit():
      ct_digit+=1
    elif ch.isalpha():
      ct_char+=1
print("count of digit is:",ct_digit)
print("count of char is:",ct_char)



#from ascii to char and char to ascii
print(ord('a'))
print(chr(97))

#a-z: 97-122 , A-Z: 65-90
#if lower to upper: -32 and 32 for upper to lower
x="abc"
for ch in x:
    out=ord(ch)-32
    print(chr(out))


#C-c
print(chr(ord('C')+32))

#for lower to upper and upper to lower
x="hello"
new_str=''
for i in x:
    if i>='a' and i<='z':
        new_str+=chr(ord(i)-32)
print(new_str)

#sWapCaSe---->swapcase using function
Str="sWapCaSe"
print(Str.lower())

#sWapCaSe---->SwAPcAsE using Ascii
str="sWapCaSe"
new_s=''
for i in str:
    if i>='a' and i<='z':
        new_s+=chr(ord(i)-32)
    elif i>='A' and i<='Z':
        new_s+=chr(ord(i)+32)
print(new_s)

#even char
x="programming"
for i in x:
    if ord(i)%2!=0:
        print(i,ord(i))
        


#use of in and not in
s="Hello"
print('H'in s)

#Another example
S=" hi"
print(len(S))
new=""
for ch in S:
    if ' ' not in ch:
        new+=ch
print("ans: ",new,len(new))

#removing the duplicate char
d="Programming"
uni=""
for ch in d:
    if ch not in uni:
        uni+=ch
    print(uni) #for every iteration
print(uni) # if we want to give direct output


#count the no. of words
r="I like python programming"
cnt=1
for ch in r:
    if ch==" ":
        cnt+=1
print(cnt)
















        












