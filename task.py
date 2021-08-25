import os
import subprocess
import time
ch ="date"
while(ch != "exit"):
	ch = input("please enter command you want to run ")
	print(subprocess.getoutput(ch))

print("See you soon ....BBYe!!")
