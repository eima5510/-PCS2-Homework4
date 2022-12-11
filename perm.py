def Permutation(n):
    import itertools
    first_list = []
   
   
    for i in range(n):
        first_list.append(i + 1)
    second_list = list(itertools.permutations(first_list, n))
    print(len(second_list))
    
    
    for l in second_list:
        print(" ".join([str(i) for i in l]))

if __name__ == "__main__":
    data_set='6'
    n = int(data_set)
    Permutation(n)