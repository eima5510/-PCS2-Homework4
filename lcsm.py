data_set = open ("D:\year 2\computer science II\rosalind_lcsm.txt", "r")

sorted(data_set, key = len)
sequence = 'q'
small_sequence = data_set[0]



for start_counter in range(len(small_sequence)):
    for end_counter in range(start_counter, len(small_sequence)):
        template = small_sequence[start_counter:end_counter+1]
        the_one_pice_is_real = False
        for seq in data_set[1:]:
            if template not in seq :
                the_one_pice_is_real = False
                break
            else:
                the_one_pice_is_real = True
                
        if the_one_pice_is_real and len(template)>len(sequence):
            sequence = template
                    

print(sequence)