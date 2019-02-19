import random
import string

all = string.ascii_letters + string.digits
alist = [random.choice(all) for i in range(8)]
pas = ''.join(alist)
print(pas)