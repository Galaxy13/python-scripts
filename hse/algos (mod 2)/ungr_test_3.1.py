def foo(n):

    if n == 0 or n == 1 or n == 2:
        print('#')
        return 1
    print('>')
    return foo(n - 1) + 2 * foo(n - 3)


foo(6)