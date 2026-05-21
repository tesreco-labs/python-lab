import array as arr
a= arr.array("i")

for i in range(5):
 x=int(input("Enter number:"))
 a.append(x)

print(a)
e,f = 0,4
while(e<f):
 a[e]= a[f]
 e+=1
 f-=1
print("reverse array")

for i in a:
 print(i)
 
