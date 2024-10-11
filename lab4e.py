#!/usr/bin/env python3
# Author ID: Thuan Le

def is_digits(sobj):
    # place code here - loop through each character in sobj
    for char in sobj:

        if char in '0,1,2,3,4,5,6,7,8,9':
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
