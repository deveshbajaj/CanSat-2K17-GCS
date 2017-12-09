"""import random
#for trail store some data in file  for testing `
x=open("ironman.txt",'w')
for i in range(50):
    x=open("ironman.txt",'a')
    q,w,e,r,t,y=str(random.randint(1,10)),str(random.randint(1,10)),str(random.randint(1,10)),str(random.randint(1,10)),str(random.randint(1,10)),str(random.randint(1,10))
    c=q+',glider,'+w+','+e+','+r+','+t+','+y
    x.write(c)
    x.write("\n")
    x.close()
    x=open("ironman.txt",'a')
    q,w,e,r,t,y=str(random.randint(1,10)),str(random.randint(1,10)),str(random.randint(1,10)),str(random.randint(1,10)),str(random.randint(1,10)),str(random.randint(1,10))
    c=q+',container,'+w+','+e+','+r+','+t+','+y
    x.write(c)
    x.write("\n")
    x.close()



#for real cansat
"""

import serial
import time

ser = serial.Serial('com8',9600)

#reading

time.sleep(1.5)
x=open("seds_rock.txt",'w')
#f=open("ironman.txt",'r')
x_g=open("glider_DEV.txt",'w')
x_c=open("container_DEV.txt",'w')

container_altitide=open("container_altitude.txt",'w')
container_temprature=open("container_temprature.txt",'w')


glider_temprature=open("glider_temprature.txt",'w')
glider_altitude=open("glider_altitude.txt",'w')
glider_pressure=open("glider_pressure.txt",'w')
glider_speed=open("glider_speed.txt",'w')
glider_voltage=open("glider_voltage.txt",'w')

while(1):
    if (ser.inWaiting()>0):
        main=open("seds_rock.txt",'a')
        main_1=open("seds_temp.txt",'w')
        
        xx=ser.readline()
        xx=xx.decode()
        
        main_1.write(xx)
        main_1.close()
        
        main.write(xx)
        main.close()
        
        print(xx)
        data=[dat for dat in xx.split(',')]
        if data[1]=="GLIDER":
            x_g=open("glider_DEV.txt",'a')
            x_g.write(xx)
            x_g.close()
            
            glider_temprature=open("glider_temprature.txt",'a')
            glider_temprature.write(data[2])
            glider_temprature.write("\n")
            glider_temprature.close()
            
            glider_altitude=open("glider_altitude.txt",'a')
            glider_altitude.write(data[3])
            glider_altitude.write("\n")
            glider_altitude.close()
            
            glider_pressure=open("glider_pressure.txt",'a')
            glider_pressure.write(data[4])
            glider_pressure.write("\n")
            glider_pressure.close()
            
            glider_speed=open("glider_speed.txt",'a')
            glider_speed.write(data[5])
            glider_speed.write("\n")
            glider_speed.close()
            
            glider_voltage=open("glider_voltage.txt",'a')
            glider_voltage.write(data[6])
            glider_voltage.write("\n")
            glider_voltage.close()
            
            
        else:
            x_c=open("container_DEV.txt",'a')
            x_c.write(xx)
            x_c.close()
            
            container_altitide=open("container_altitude.txt",'a')
            container_altitide.write(data[2])
            container_altitide.write("\n")
            container_altitide.close()
            
            container_temprature=open("container_temprature.txt",'a')
            container_temprature.write(data[3])
            container_temprature.write("\n")
            container_temprature.close()

            
        
        
        time.sleep(1)
