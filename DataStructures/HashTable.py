from Algorithms import Hash, Prime
from LinkedList import ListNode


class HashTable:  # Uses linear probing to find values when collisions occur
    def __init__(self, size=32, m=31, hash_func=Hash.div_hash):
        self.size = size
        self.array = [None] * size
        self.m = m
        self.hash_func = hash_func
        self.keys = 0

    def insert(self, key, val):
        """
        :param key: key to access value
        :param val: value to be inserted
        :return: None
        """
        hashed_key = self.hash_func(key, m=self.m)
        current_node = self.array[hashed_key]
        if current_node is None:
            self.array[hashed_key] = ListNode()
            self.array[hashed_key].key, self.array[hashed_key].val = key, val
            self.keys += 1
            return
        while current_node is not None and current_node.key is not None and current_node.key != key:
            current_node = current_node.right
        if current_node.right is None:
            current_node.right = ListNode()
        if current_node is not None and not current_node.key == key:
            self.keys += 1
        current_node.key, current_node.val = key, val
        print(self)
        if self.keys >= self.size:
            self.resize(self.size * 2)

    def get(self, key):
        """
        :param key: key to lookup in hashtable
        :return: value corresponding to key if exists, else None
        """
        hashed_key = self.hash_func(key, m=self.m)
        current_node = self.array[hashed_key]
        while current_node is not None and current_node.key is not None and current_node.key != key:
            current_node = current_node.right
        if current_node is None:
            return
        return current_node.val

    def remove(self, key):
        hashed_key = self.hash_func(key, m=self.m)
        current_node = self.array[hashed_key]
        while current_node is not None and current_node.key is not None and current_node.key != key:
            current_node = current_node.right
        if current_node.key is None:
            return
        if current_node.left is not None:
            prev = current_node.left
            prev.right = current_node.right
        elif current_node.right is not None:
            self.array[hashed_key] = current_node.right
            del current_node
        else:
            self.array[hashed_key] = ListNode()
        self.keys -= 1
        if self.keys <= self.size / 4:
            self.resize(self.size // 2)

    def resize(self, size):
        print("Resizing to {}".format(size))
        old_array = self.array
        self.array = [ListNode()] * size
        self.size = size
        self.m = Prime.find_prime(self.size // 2, self.size)
        self.keys = 0
        for slot in range(self.size // 2):
            current_node = old_array[slot]
            while current_node is not None:
                self.insert(current_node.key, current_node.val)
                current_node = current_node.right

    def __str__(self):
        out = "{\n"
        for slot in range(self.size):
            current_node = self.array[slot]
            while current_node is not None:
                if current_node.key is not None:
                    out = out + "{} -> {}\n".format(current_node.key, current_node.val)
                current_node = current_node.right
        out = out + "}"
        return out


if __name__ == "__main__":
    hashtable = HashTable()
    hashtable.insert("st", 5)
    assert hashtable.get("st") == 5
    for i in range(10):
        past_keys = set()
        sample_key, sample_val = i, i*2
        if sample_key not in past_keys:
            past_keys.add(sample_key)
            hashtable.insert(sample_key, sample_val)
            assert hashtable.get(sample_key) == sample_val
            # hashtable.remove(sample_key)
            # if hashtable.get(sample_key) is not None:
            #     print("{} -> {}".format(sample_key, hashtable.get(sample_key)))
            # assert hashtable.get(sample_key) is None
