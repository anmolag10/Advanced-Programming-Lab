import re

regex = r'^[a-z]$|^([a-z]).*\1$'


def check(string):
    if(re.match(regex, string)):
        return(True)
    else:
        return(False)


if check("anmol"):
    print("Same Start End")
else:
        print("Different Start End")

