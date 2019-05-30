class SMS_store():
    
    def __init__(self):
        self.store = []

    def __str__(self):
        return ("{0}".format(self))

    def add_new_arrival(self, number, time, text ):
        self.store.append(("Read: False", "From: "+number, "Recieved: "+time, "Msg: "+text))

    def message_count(self):
        return (len(self.store))

    def get_unread_indexes(self):
        result = []
        for (i, v) in  enumerate(self.store):
            if v[0] == "Read: False":
                result.append(i)
        return (result)

    def get_message(self, i):
        msg = self.store[i]
        msg = ("Read: True",) + msg[1:]
        self.store[i] = (msg)
        return (self.store[i][1:])

    def delete(self, i):
        del self.store[i]

    def clear(self):
        self.store = []

"""
import time
class SMS_store:
    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, text_of_sms,read_status = False):
        number = str(from_number)
        time_received = time.strftime("%D %T")
        self.inbox.append([time_received, number, text_of_sms, read_status])

    def message_count(self):
        return "There are {0} messages in your Inbox".format(len(self.inbox))

    def get_unread_indexes(self):
        unread = []
        for index, message in enumerate(self.inbox):
            if False in message:
                unread.append(index)
        return "Unread Messages in:", unread

    def get_message(self, index):
        message = self.inbox[index]
        message[3] = "Read"
        return message[ : 3]

    def delete(self, index):
        del self.inbox[index]
        return "Deleted Message", index

    def clear(self):
        self.inbox = []
        return "Empty Inbox"
"""    

    