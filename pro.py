f=open('super.txt','w')
l=10
from datetime import datetime
import random


for i in range(0,l):
    a=random.randint(0,100)
    hes=hex(a)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    dataaa=str(i)+","+current_time+","+str(hes)+" \n"
    f.write(dataaa)

f.close()
