from subprocess import check_output, call
import sys

class Curl():
    username = "reza1290"
    password = "1290123reza@"

    def __init__(self, subject, text):
        self.text = text
        self.subject = subject

    def throw_to_db(self):
        a = """curl --data "name={}&password={}&text={}&subject={}" http://rezamatin.pythonanywhere.com/ -X POST"""\
        .format(Curl.username, Curl.password, self.text, self.subject)
        
        if call(a, shell=True):
            return "succefully sended :)"
        else:
            return "Error"


wmsg = "\033[0;32;40m"
rmsg = '\033[0;37;40m'

subject = input(wmsg+"subject: "+rmsg+" ")

text = input(wmsg+"text: "+rmsg+" ")


confirmation = input("\nsubject: {}\nmatn:{}\nAya Mayel Hastid Sabt Shavad[Y/n]? ".format(subject, text))

if confirmation.casefold() == "y" or confirmation.casefold() == "yes" or confirmation == "":
    l = Curl(subject, text)
    l.throw_to_db()

else:
    print("Canceld!")
    sys.exit()

