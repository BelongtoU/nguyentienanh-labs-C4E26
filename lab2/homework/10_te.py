def get_even_list(l):
    e_l = []
    for i in l :
        if i % 2 == 0 :
            e_l.append(i)
    return e_l

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")