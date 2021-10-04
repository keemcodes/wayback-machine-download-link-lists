import os
import time

home_dir = os.system("cd ~")
print("`cd ~` ran with exit code %d" % home_dir)

file = open('remix2.txt', 'r')
lines = file.readlines()

for index, line in enumerate(lines):
    print("Download Log: ",index, line.strip())
    home_dir = os.system("waybackpack {} -d ~/Downloads/lala/{}".format(line.strip(), index))
    print(home_dir)
    time.sleep(3)


    
file.close()
# update22