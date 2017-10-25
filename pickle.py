import pickle

man = []
other = []
try:
    with open('man_data.txt','wb') as man_file,open('other_data.txt','wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)

except IOError as err:
    print('File Error!' + str(err))

except pickle.PickleError as perr:
    print('Picking error' + str(perr))