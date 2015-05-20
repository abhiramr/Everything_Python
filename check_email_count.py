from os import system
import imaplib
import getpass
def speak(stuff):
    system('say You have '+stuff+' unread emails')

def get_unread_count(username,password):
    obj = imaplib.IMAP4_SSL('imap.gmail.com','993')  
    obj.login(username,password) 
    obj.select('Inbox')
    typ, messageIDs = obj.search(None, "UNSEEN")
    listOfSplitStrings = str(messageIDs).split(" ")
    unread=len(listOfSplitStrings) 
    speak(str(unread))
    return unread

if __name__=="__main__":
    names=raw_input("Enter username:")
    password=getpass.getpass()
    unread = get_unread_count(names,password)
    print("You have "+str(unread)+" unread mails.")

     
     
