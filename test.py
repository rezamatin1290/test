from sys import stdout

from time import sleep
class star:
    BLUE = '{}'.format('\033[94m')
    GREEN = '{}'.format('\033[92m')
    RED = '{}'.format('\033[91m')
    YELLOW = '{}'.format('\033[33m')
    WHITE = "{}".format("\033[0m")

    
    
def show_out(matn, s):
    """show and clear out put"""
    stdout.write(f"{star.BLUE}{str(matn)}")
    stdout.write("\033[?25h")
    stdout.flush()
    sleep(s)
    stdout.write("\b"*len(str(matn)))
    stdout.write("\033[?25h")
    stdout.flush()


show_out("reza", 0.56)

