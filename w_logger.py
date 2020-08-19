#help module to send print output to a file
#https://stackoverflow.com/questions/14906764/how-to-redirect-stdout-to-both-file-and-console-with-scripting
import sys
class Logger(object):                    #send a copy of the terminal out put to a file
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("w_output.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    
sys.stdout = Logger()

if __name__ == "__main__":
    print("Willem")