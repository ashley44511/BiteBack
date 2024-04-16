import pickle

# hash class here
class Hash:
    def __init__(self):
        pass



if __name__ == "__main__":

    hash = Hash()

    # after hash data is loaded and saved
    with open("data/data_hash.pickle", "wb") as file:
        pickle.dump(hash, file) 
        print("Hash map successfully pickled!")