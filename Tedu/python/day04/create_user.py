import subprocess
import randpass

def create_user(user,pwd,file):
    subprocess.call('useradd %s' %user,shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s' %(pwd,user),
        shell=True
    )
    with open(file,'a') as f:
        f.write('user:%s\npwd:%s\n' %(user,pwd))

if __name__ == '__main__':
    user = 'nsd'
    pwd = randpass.pas(16)
    file = '/tmp/a.txt'
    create_user(user,pwd,file)