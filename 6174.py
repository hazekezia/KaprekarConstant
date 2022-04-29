import time

"""
Issue of this code is 2111 because discarding of zero values. See another code in this github to the solution.

The rules is you cannot make 4 digits number, it's always zero anyway.
"""

def kaprekar(number):
    number_ite = number
    while(True):
        print("number now:", number_ite)
        #ascending
        asc = "".join(sorted(str(number_ite)))

        #descending
        desc = "".join(sorted(str(number_ite), reverse=True))

        #make diff
        subs = abs(int(asc)-int(desc))
        print("diff:", subs)
        if (subs == 0):
            print("Can't do the same 4 digit number!")
            break
        elif (subs == 6174):
            print("Already 6174!")
            break #delete this line if you wanna see 6147 looping forefer!
        time.sleep(1)
        number_ite = subs

kaprekar(1111)