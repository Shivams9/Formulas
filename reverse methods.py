#left < right   (left hmesa right se chota hota hai coding me ---   on page once,tens,etc right se suru hota hai coding me left se right hota hai)
#self created fuction of position for replace position
def reverse(p,left,right):
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

a = [1, 2, 3, 4, 5, 6, 7]
print(a)
reverse(a,0,2)      #(a = array(input) 0=position 2=end position jo replace karega)
print(a)




#------method
a = [1,2,3,4,5]
a.reverse()
print(a)

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
