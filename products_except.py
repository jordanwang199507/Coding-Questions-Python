def get_products_of_all_except_index(int_list):
    if len(int_list) < 2:
        print ("Error")
        return None

    new_list = [None]*len(int_list)

    index = 0
    cur = 1
    while index < len(int_list):
        new_list[index]=cur
        cur = cur*int_list[index]
        index=index+1

    index = len(int_list)-1
    cur = 1
    while index >=0:
        new_list[index]= new_list[index]*cur
        cur = cur * int_list[index]
        index= index-1

    return new_list


int_list = [2,4,6,8,10]
print(get_products_of_all_except_index(int_list))