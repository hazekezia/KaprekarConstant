import time

def kaprekar(number):
    number_ite = number
    while(True):
        #make this to list
        digits = [0] * 4
        for i in range(4):
            digits[i] = number_ite % 10;
            number_ite = int(number_ite / 10);
        print(digits)

        #ascending
        asc = sorted(digits)
        asc_i = 0
        for i in range(4):
            asc_i = asc_i * 10 + asc[i]
        print(asc_i)

        #descending
        desc = sorted(digits, reverse=True)
        desc_i = 0
        for i in range(4):
            desc_i = desc_i * 10 + desc[i]

        #make diff
        subs = abs(asc_i - desc_i)
        print("diff:", subs)
        if (subs == 0):
            print("Can't do the same 4 digit number!")
            break
        elif (subs == 6174):
            print("Already 6174!")
            break #delete this line if you wanna see 6147 looping forefer!
        time.sleep(1)
        number_ite = subs

kaprekar(2111)