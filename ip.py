# Ciena Coding Challenge.

import time

class IPAdress:
    adress = ''
    validLease = True # True means u can connect, false means its in use.
    startTimer =  0.0
    # userID =

    def __init__(self, adress, validLease):
        self.adress = adress
        self.validLease = False
        self.startTimer = time.time()

    def release(self):
        self.validLease = True
        print("IP address released sucessfully.")

    def renew(self):
        self.startTimer = time.time()
    def isValidLease(self):
        if (time.time() - self.startTimer > 60):
            return False
        else:
            return True
    # def leaseTimer(self):