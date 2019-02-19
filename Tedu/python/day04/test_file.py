#!/usr/bin/env python3
import shutil
# with open('/etc/passwd','rb') as src:
#     with open('/tmp/mima','wb') as dst:
#         shutil.copyfileobj(src,dst)

# shutil.copyfile('/etc/passwd','/tmp/mima')

# shutil.copy('/etc/shadow','/tmp')
# shutil.copy2('/etc/shadow','/tmp/sha')

# shutil.move('/tmp/sha','/root/')


# shutil.copytree('/root/day02','/tmp/day02')

# shutil.rmtree('/tmp/day02')

# shutil.copymode('/etc/shadow','/tmp/mima')

# shutil.copystat('/etc/shadow','/tmp/mima')

shutil.chown('/tmp/mima',user='adm')
# a,b = 10,20
# a,b = b,a
# print(a,b)

#import keyword
#print(keyword.kwlist)
#print(keyword.iskeyword('for'))
