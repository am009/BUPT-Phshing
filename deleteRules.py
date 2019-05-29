import os

dele = "sudo iptables -t nat -D PREROUTING 1" 
show = 'sudo iptables -t nat -L'

content = os.popen(show).read()

#print(os.system(dele))
#content.split('\n')[2] == ''
flag = True
while(flag):
    flag = (os.system(dele) == 0)
