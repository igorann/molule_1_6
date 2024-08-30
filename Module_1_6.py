my_dict = {'igor':1991, 'katrin':1998}
print(my_dict)
print(my_dict['igor'])
print(my_dict.get('alex'))
my_dict['roma']=1992
print(my_dict)
my_dict.update({'ivan':1986,'marina':1987})
print(my_dict)
del my_dict['katrin']
print(my_dict)

my_set = {3,2,4, 'солнце',42,2,3 }
print(my_set)
list = [3,2,4]
list = set(my_set)
print(list)
print(list.add(5))
print(list)
print(list.add(9))
print(list)
print(list.remove(4))
print(list)