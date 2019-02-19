adict = {'name':'bob','age':24}
# bdict = dict(['ab',['qq','62121878'],('phone','13828456471')])
# cdict = {}.fromkeys(('ab','ls','cd'),8)
# print(adict)
# print(bdict)
# print(cdict)
#
# print(len(adict))
# for key in adict:
#     print('%s:%s' %(key,adict[key]))
# print('%(name)s is %(age)s year old' %adict)
#
# for key in adict.keys():
#     print(key)
# for val in adict.values():
#     print(val)
#
# for key,val in adict.items():
#     print(key,val)
#
# print(adict.get('qq'))
# print(adict.get('qq','not found'))
# print(adict.get('name','not found'))
#
# print(len(adict))
#
# print(adict.hash)

bdict = adict
print(id(adict))
print(id(bdict))

cdict = adict.copy()
print(id(cdict))

adict['email'] = 'tedu@tedu.cn'

print(adict)
print(bdict)
print(cdict)