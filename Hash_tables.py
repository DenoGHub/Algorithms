class Hash:
    def __init__(self):
        self._container = [None] * 20

    def _hash_function(self, key):
        h = hash(key)
        idx = h % len(self._container)
        print(f"key={key}; hash_bucket={h}; index={idx}")
        return idx

    def add_data(self, key, value):
        idx = self._hash_function(key)
        self._container[idx] = value

    def get(self, key):
        idx = self._hash_function(key)
        return self._container[idx]

    def print_container(self):
        print(f"container={self._container}")

    def __repr__(self):
        return 'bla'


ht = Hash()
ht.add_data('John', 2)
ht.add_data('Tom', 5)
print("-"*50)
ht.print_container()
print('John:', ht.get('John'))
print('Tom:', ht.get('Tom'))