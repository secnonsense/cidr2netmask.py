#!/usr/bin/python

#basic cidr to subnetmask conertor 

import sys

def cidr_to_mask(value):
    
    def convert(binary):
        binmask=int('11111111',2) - int(binary,2)
        return binmask
   
    def bitcalc(base):
        binary=''
        bits = base - int(cidr)
        if bits > 0:
            for x in range (0,bits):
                binary = binary + '1'
        else:
            binary='0'
        return binary
    
    net, cidr = value.split('/')
    
    if int(cidr)/4 < 2:
        oct2 = oct3 = oct4 = 0
        x=8
        bi=bitcalc(x)
        oct1 = convert(bi)
    elif int(cidr)/4 < 4:
        oct1 = 255 
        oct3 = oct4 = 0
        x=16
        bi=bitcalc(x)
        oct2 = convert(bi) 
    elif int(cidr)/4 < 6:
        oct2 = oct1 = 255 
        oct4 = 0
        x=24
        bi=bitcalc(x)
        oct3 = convert(bi)
    elif int(cidr)/4 <= 8:
        oct2 = oct3 = oct1 = 255
        x=32
        bi=bitcalc(x)
        oct4 = convert(bi)  
    
    smask=str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.' + str(oct4)
    return net, smask

net, mask = cidr_to_mask(sys.argv[1])

print(net + " mask " + str(mask))