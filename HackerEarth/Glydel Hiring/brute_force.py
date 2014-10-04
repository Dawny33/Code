def is_cube(n):
    if isinstance(n, int) and n > 0:
        root = 0
        while root**3 < n:
            root += 1
            if root**3 == n:
                return root
                break
        else:
            return False


print is_cube(26)
