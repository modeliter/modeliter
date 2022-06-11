import pickle

# x = 10
# y = x * 2
# with open ("y.pickle", "wb") as f:
#     pickle.dump(y, f)

with open("y.pickle", "rb") as f:
    print(pickle.load(f))
