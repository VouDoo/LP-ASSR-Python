### Function definition

# Function "formatMillisec"
def formatMillisec(msToFormat) :
    # Milliseconds
    ms = msToFormat % 1000
    # Seconds
    s = int(msToFormat / 1000 % 60)
    # Minutes
    m = int(msToFormat / (1000 * 60) % 60)
    # Hours
    h = int(msToFormat / (1000 * 60 * 60) % 60)
    
    return '{}:{}:{}:{}'.format(h, m, s, ms)


### Main program

msToFormat = int(input())

print(formatMillisec(msToFormat))
