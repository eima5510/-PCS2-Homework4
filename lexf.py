import itertools

data_set = 'A B C D E F , 3'
string = data_set.split()
n = int(data_set.split())
result = list(itertools.product(string, repeat = n))
print("\n".join(["".join(x) for x in result]))