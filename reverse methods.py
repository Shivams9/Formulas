

#-----method
a = [1, 2, 3, 4, 5, 6, 7]
n = len(a)
for i in range(0, n // 2):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]

print(a)



#------method 

a = [1,2,3,4,5]
while a:
  print(a.pop())
