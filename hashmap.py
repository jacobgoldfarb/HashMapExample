class HashMap:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.store = [None for _ in range(capacity)]
        self.len = 0

    def __len__(self):
        return self.len

    def __setitem__(self, key: str, value):
        idx = self._hash_idx(key)
        self.len += 1
        if self.store[idx] == None:
            self.store[idx] = [(key, value)]
        else:
            self.store[idx].append((key, value))

    def __getitem__(self, key: str):
        result = self.get(key)
        if result == None:
            raise KeyError(f"Key Error: No object in HashMap with key '{key}'")
        return result
        
    def get(self, key: str):
        idx = self._hash_idx(key)
        try:
            return [candidate for candidate in self.store[idx] if candidate[0] == key][0][1]
        except:
            return None

    def remove(self, key):
        self.len -= 1
        idx = self._hash_idx(key)
        removal_idx = [i for i, candidate in enumerate(self.store[idx]) if candidate[0] == key][0]
        self.store[idx].pop(removal_idx)

    # private

    def _hash_key(self, key: str):
        return hash(key)

    def _hash_idx(self, key: str):
        return self._hash_key(key) & (self.capacity - 1)

def test():
    NUM_ELEMENTS = 10
    NUM_BUCKETS = 10

    dict = HashMap(NUM_BUCKETS)

    # populate hash map
    for i in range(NUM_ELEMENTS):
        dict[f"Jacob{i}"] = i

    # retrieve results
    for i in range(NUM_ELEMENTS):
        print(dict[f"Jacob{i}"])
    print("-----------")

    # delete middle third
    for i in range(NUM_ELEMENTS//3, NUM_ELEMENTS//3 * 2):
        dict.remove(f"Jacob{i}")

    # retrieve again, expecting key errors
    for i in range(NUM_ELEMENTS):
        try:
            print(dict[f"Jacob{i}"])
        except KeyError as e:
            print(f"key error for idx {i}: {e}")
    print("-----------")

if __name__ == "__main__":
    test()