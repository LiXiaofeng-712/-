#!/usr/bin/env python3
import sys
def copy(src_path,dst_path):
    f1 = open(src_path, 'rb')
    f2 = open(dst_path, 'wb')
    while True:
        #with open(src_path,'rb') as f1:
        data = f1.read(4096)
        if not data:
            break
        #with open(dst_path,'wb') as f2:
        f2.write(data)
    f2.close()
    f1.close()
copy(sys.argv[1],sys.argv[2])