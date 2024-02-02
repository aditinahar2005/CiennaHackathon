import sys

from ip import IPAdress
from Testing import generate_IP

IPaddressarray = []


def find(IP):
    for i in range(0, len(IPaddressarray)):
        if (IPaddressarray[i].adress == IP):
            if (IPaddressarray[i].isValidLease()):
                assign()

running = True


def assign():
    IP = generate_IP()
    find(IP)
    IPaddr = IPAdress(IP, False)
    IPaddressarray.append(IPaddr)
    print("Offered:" + IPaddr.adress)
def releaser(IP):
    addressOfIP = findRel(IP)
    if ( addressOfIP == -1):
        print("IP address not found.")
    else:
        if (len(IPaddressarray) > 0):

            IPaddressarray[addressOfIP].release()
            print("Released: " + IPaddressarray[addressOfIP].adress)
            IPaddressarray.pop(addressOfIP)
        else:
            print("No addresses.")

def findRel(IP):
    for i in range(0, len(IPaddressarray)):
        if (IPaddressarray[i].adress == IP):
            return i
    print("Not found in the List")
    return -1

def renewer(IP):
    addressOfIP = findRel(IP)
    if (addressOfIP == -1):
        print("IP address not found.")
    else:
        IPaddressarray[addressOfIP].renew()
        print("Renewed: " + IPaddressarray[addressOfIP].adress)
while running:
    print("What would you like to do:")
    print("1. Ask")
    print("2. Release")
    print("3. Renew")
    print("0. Exit")

    choice = str(input("Enter your choice: "))

    if choice.lower() == 'ask':
        assign()
    elif choice.split(" ")[0].lower() == 'release':
        print("reached")
        releaser(choice.split(" ")[1])
    elif choice.split(" ")[0].lower() == 'renew':
        renewer(choice.split(" ")[1])
        print("Renewed:")
    elif choice.split(" ")[0].lower() == 'status':
        index = findRel(choice.split(' ')[1])
        if(index == -1 ):
            IPaddressarray[index].status(False)
        else:
            IPaddressarray[index].status(True)
    elif choice.lower() == 'quit':
        sys.exit(0)



