#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    #Dict = {}
    #for number in range(len(list_keys)):
    #    Dict.update({list_keys[number]:list_values[number]})
    #return Dict
    Dictionary = {}
    i = 0
    while i < len(list_keys):
        key = keys[i]
        value = values[i]
        Dictionary.update({key:value})
        i += 1
    return Dictionary

def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below
    d1 = set(dict1.values())
    d2 = set(dict2.values())
    return d1.intersection(d2)

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
