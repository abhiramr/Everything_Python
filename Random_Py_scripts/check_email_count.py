""" Script to Return the number of unread mails """

import os
from os import system
import imaplib
import getpass

def speak(stuff):
    """ Use the system say function to speak out the message below """
    system('say You have '+stuff+' unread emails')

def get_unread_count(username, password):
    """ Return the number of unread mails """
    obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
    obj.login(username, password)
    obj.select('Inbox')
    message_ids = obj.search(None, "UNSEEN")[1]
    list_of_split_strings = str(message_ids).split(" ")
    unread = len(list_of_split_strings)
    # speak(str(unread))
    return unread

if __name__ == "__main__":
    if "EMAIL_USERNAME" in os.environ and "DUMMY_PASSWORD" in os.environ:
        NAME = os.environ["EMAIL_USERNAME"]
        PASSWORD = os.environ["DUMMY_PASSWORD"]
    else:
        NAME = input("Enter username:")
        PASSWORD = getpass.getpass()
    UNREAD = get_unread_count(NAME, PASSWORD)
    print("You have "+str(UNREAD)+" unread mails.")
