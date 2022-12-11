data_set='96 20'


info = data_set.split()
arr = [0]*int(info[1])
arr[1] = 1; arr[0] = 1


timer = int(info[0])-2
family = len(arr)


while timer >=0:
    tmp = arr[0]
    new_offspring = 0
    for count in range(1, family):
        new_offspring += arr[count]
    for cou in range(family-1, 1, -1):
       arr[cou] = arr[cou-1]
    arr[1] = tmp
    arr[0]= new_offspring
    timer-=1
print (arr[0])