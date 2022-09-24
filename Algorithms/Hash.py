def div_hash(key, m):  # Works way better if m is a prime number, not near a power of 2.
    return hash(key) % m


def mult_hash(key, m, a=0.1):
    return round(m * (hash(key) * a % 1))


def universal_hash(key):
    """
    implement me, I'm theoretically possible
    """
    pass
