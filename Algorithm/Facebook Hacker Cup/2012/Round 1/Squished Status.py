# -*- coding: utf-8 -*-

'''
hacker cup C問題
メモ化再帰

Created on 2012/01/29

@author: y42sora
'''
   
def check(string):
    global dic
    global max_num
    
    if string in dic:
        return dic[string]
    
    if len(string) == 0:
        return 1

    if string[0] == '0':
        return 0
    
    if int(string) <= max_num:
        return 1
    else:
        return 0

file = open('in.txt', 'r')
t = int(file.readline())

out = open('out.txt', 'w')

for x in range(t):
    line = file.readline()
    s = line.split(" ")
    max_num = int(s[0])
    
    if len(s) == 1:
        s = file.readline().rstrip()
    else:
        s = s[1].rstrip()
    
    ans = 1
    
    for string in s.split(" "):
        dic = dict([])
        dic[''] = 1
            
        dic[string[0:1]] = check(string[0:1])
        dic[string[1:2]] = check(string[1:2])
        dic[string[0:2]] = check(string[0:2]) + dic[string[0:1]] * dic[string[1:2]]
    
        for i in range(3, len(string)+1):
            num = 0
            num += dic[string[0:i-1]] * check(string[i-1:i])
            num += dic[string[0:i-2]] * check(string[i-2:i])
            num += dic[string[0:i-3]] * check(string[i-3:i])
            dic[string[0:i]] = num
        
        ans *= dic[string] 
    
    out.write("Case #%d: %d\n" % ((x+1),ans))
    
out.close()
