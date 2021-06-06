rev=0
x=int(input())
while x!=0 :
  print(x%10)

  rev=(rev*10)+(x%10)
  x=x/10
print(rev)
