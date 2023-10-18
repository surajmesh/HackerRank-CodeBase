# make function for 12 hours time convert into 25 Hours 

def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == '12':        # if time present 12 and AM then print 00 insted 12
        return "00" + s[2:-2]
    elif s[-2:] == 'AM':                        # if time present only AM then print time as it insted of AM
        return s[:-2]
    elif s[-2:] == 'PM' and s[:2] == '12':      # if time present 12 and PM then print as it insted of PM
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:-2]       # otherwise add 12 to start pos 2 


s = '01:30:00AM'
print(timeConversion(s))
