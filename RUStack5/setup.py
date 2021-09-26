import os
import site

dir=site.USER_SITE
filename=site.USER_SITE+"/RUStack5.pth"
if not os.path.exists(dir):
    os.makedirs(dir)

f=open(filename,mode='w')
f.write(os.path.abspath(os.getcwd()))
f.close()

print("RUStack5 path added in: "+dir)
print("After resetting the kernel you should be able to import RUStack5.")