"""
    Sock Merchant Problem
"""

from collections import defaultdict


n = 9
socks_list = [10, 20, 20, 10, 10, 30, 50, 10, 20]


def sock_merchant_1(n, socks_list):
    """
        Using SET
        socks_list > {10, 20, 30, 50}

    """
    # convert the list into set
    socks_set = set(socks_list)
    pair_count = 0

    # loop over individual socks and compute
    # their respective counts in the provided list
    # and add to pair count
    for sock in socks_set:
        pair_count += socks_list.count(sock) // 2

    return pair_count


def sock_merchant_2(n, socks_list):
    # https://www.geeksforgeeks.org/defaultdict-in-python/
    #     
    sock_dict = defaultdict(int)
    pair_count = 0

    # it loops over all the sock colours
    # and then increments by 1 the count of occurences
    # for each colour
    for sock in socks_list:
        sock_dict[sock] += 1


    # loop over all the values in the dictionary
    # and find out the number of pairs
    for _ in sock_dict.values():
        pair_count += _ // 2
    
    return pair_count

result = sock_merchant_1(n, socks_list)
result = sock_merchant_2(n, socks_list)
print(f"The number of Pairs are: {result}")
