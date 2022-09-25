def is_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def find_prime(lower, upper):
    for i in range(upper-1, lower, -1):
        if is_prime(i):
            return i
    return -1


if __name__ == "__main__":
    assert is_prime(7)
    assert not is_prime(8)