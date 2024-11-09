def is_palindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]:
        print("True")
    else:
        print("False")


is_palindrome("madam")