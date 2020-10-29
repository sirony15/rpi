import time
def lon():
    print('LED turned ON\n')

def loff():
    print('LED turned OFF\n')

def lon5():
    print('LED will ON after 5 sec\n')
    time.sleep(5)
    print('LED turned off now\n')

def loff5():
    print('LED will OFF after 5 sec\n')
    time.sleep(5)
    print('led turned off now\n')

def longr():
    print('LED will ON gradually\n')

def loffgr():
    print('LED will off gradually\n')

while True:
    print('******* Hi I am a LED *******')
    print('*     1 for on the LED      *')
    print('*     2 for off the LED     *')
    print('*  3 on the LED after 5sec  *')
    print('*  4 off the LED after 5sec *')
    print('*  5 on the LED gradually   *')
    print('*  6 off the LED gradually  *')
    print('*    9 exit the program     *')
    print('*****************************\n\n')
    time.sleep(1)
    x=int(input("Please choose your option:"))
    if x==9:
        print('we are closing the program')
        break
    elif x==1:
        lon()
    elif x==2:
        loff()
    elif x==3:
        lon5()
    elif x==4:
        loff5()
    elif x==5:
        longr()
    elif x==6:
        loffgr()
    else:
        print('Input error')
