# {'name': name, 'roll_no': roll_no, 'marks': marks}
# display record of those students who have 60+ marks

import pickle

with open("test_file.dat", "rb") as file:
    while True:
        try:
            cnt = pickle.load(file)
            if cnt[2] > 60 :
                print(cnt)
        except:
            break