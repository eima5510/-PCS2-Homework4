def rabbits(n, k):
   if n == 0:
       return 0
   if n == 1:
       return 1
   else:
       return rabbits(n-1, k) + k*rabbits(n-2, k)

#data_set='36,4'
print (rabbits(36,4))