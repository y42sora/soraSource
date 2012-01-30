# -*- coding: utf-8 -*-
'''
hacker cup B問題
実際にソートして，元の並び順との対応づけを見る

Created on 2012/01/29

@author: y42sora
'''

import math

debug = []
d_num = 0

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # arr is indexed 0 through n-1, inclusive
    mid = int(math.floor(n/2))
    
    first_half = merge_sort(arr[0:mid])
    second_half = merge_sort(arr[mid:n])
    return merge(first_half, second_half)

def merge(arr1, arr2):
    global debug
    global d_num
    result = []
    while len(arr1) > 0 and len(arr2) > 0:
        if debug[d_num] == "1":
            result.append(arr1[0])
            arr1.pop(0)
        else:
            result.append(arr2[0])
            arr2.pop(0)
        d_num += 1
            
    result += arr1
    result += arr2
    return result

def checksum(arr):
    result = 1
    for i in arr:
        result = (31 * result + i ) % 1000003
    return result

file = open('in.txt', 'r')
t = int(file.readline())

out = open('out.txt', 'w')

for i in range(t):
    n = int(file.readline())
    debug = file.readline()
    d_num = 0;
    
    sorted = merge_sort(range(n))
    
    ans_list = []
    for x in range(n):
        ans_list.append(sorted.index(x) + 1)
        
    out.write("Case #%d: %d\n" % ((i+1), checksum(ans_list)))
    
out.close()
