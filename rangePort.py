#!/usr/bin/python3
# File Name: sock_t_range.py
# Author: Jin LI
# mail: jin.li366@outlook.com
# Created Time: 2019-02-27 00:29:10

import sys, time, os

def port_range():
    av_lst = set()
    for i in range(1025,65535+1):
        av_lst.add(i)
        
    res = os.popen("netstat -autlp").readlines()
    for r in res:
        r = r.strip().split()[3]
        if ":" in r:
            r = r.split(":")[1]
            if r.isdigit():
                av_lst.discard(int(r))
    
    #print(av_lst)

    start = min(av_lst)
    end = max(av_lst)
    dis = 0
    print_flag = True
    while(start <= end):
        if print_flag and (start in av_lst):
            cur = start
            print(cur, end="")
            print("-->", end="")
            print_flag = False

        if start not in av_lst or start == end:
            print(start-1,end="\t")
            print(": " + str(start-cur))
            print_flag = True
            
        start = start + 1

if __name__=='__main__':
    port_range()