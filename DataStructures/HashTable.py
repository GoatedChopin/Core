from Algorithms import Hash
from LinkedList import ListNode


class HashTable:  # Uses linear probing to find values when collisions occur
    def __init__(self, m=17, hash_func=Hash.div_hash):
        self.array = [ListNode()] * m
        self.m = m
        self.hash_func = hash_func

    def insert(self, key, val):
        """
        :param key: key to access value
        :param val: value to be inserted
        :return: None

        Needs to hash key and store val at the hashed index.
        """
        hashed_key = self.hash_func(key, m=self.m)
        current_node = self.array[hashed_key]
        while current_node is not None and current_node.key is not None and current_node.key != key:
            current_node = current_node.right
        current_node.key, current_node.val = key, val

    def get(self, key):
        """
        :param key: key to lookup in hashtable
        :return: value corresponding to key if exists, else None

        Needs to hash key and look for corresponding value in array.
        """
        hashed_key = self.hash_func(key, m=self.m)
        current_node = self.array[hashed_key]
        while current_node is not None and current_node.key is not None and current_node.key != key:
            current_node = current_node.right
        if current_node is None:
            return
        return current_node.val


if __name__ == "__main__":
    import random as r
    hashtable = HashTable()
    hashtable.insert("st", 5)
    assert hashtable.get("st") == 5
    for i in range(1000):
        past_keys = set()
        sample_key, sample_val = r.randint(1, 1000), r.randint(1001, 10000)
        if not sample_key in past_keys:
            assert hashtable.get(sample_key) is None
        else:
            past_keys.add(sample_key)
            hashtable.insert(sample_key, sample_val)
            assert hashtable.get(sample_key) == sample_val