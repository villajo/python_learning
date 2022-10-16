#!/bin/python

def concat_list(list1, list2):
    concat_list = list1
    for element in list2: 
        if type(element) == "int":
            concat_list.append(str(element))
        else:
            concat_list.append(element)
    return concat_list

def main():
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]
    final_list = concat_list(list1, list2)

    print(final_list)

if __name__ == "__main__":
    main()