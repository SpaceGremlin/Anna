import os

RBC = [100,25600]
while True:
    ecode = os.system("python main.py")
    print("Exit code is: " +str(ecode))
    if ecode in RBC:
        print("rebooting")
        continue
    break
