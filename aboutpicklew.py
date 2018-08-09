import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open("data1.pkl","wb")

pickle.dump(data1,output)
# Pickle dictionary using protocol 0.

pickle.dump(selfref_list,output,-1)
# Pickle the list using the highest protocol available.

output.close()