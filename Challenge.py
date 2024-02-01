def assign(){
    IP = generate()
    for i in range(0,list.length):
        if(list[i].adress == IP):
            if(isValidLease()):
                assign()
    IPaddr = IPAdress(IP,False)
    Ipaddr.time()
    list.append(IP)
    return Iaddr
}