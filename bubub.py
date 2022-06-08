import datetime
import math

def dynamic_date_in_string(strwithdate:str):
    startpoint = -1
    to_format = []
    offset = 0
    if strwithdate.find("|") != -1: offset = int(strwithdate.split("|")[1])
    target_date = date_offset(offset)
    for x in range(len(strwithdate)):
        if strwithdate[x] == "#":
            if startpoint < 0:
                startpoint = x
            else:
                to_format.append(strwithdate[startpoint:x+1])

    for text in to_format:
        string = text.upper().replace("#","")
        string = string.replace("YYYY","%Y")
        string = string.replace("YY","%y")
        string = string.replace("SS","%S")
        string = string.replace("S","%S")
        string = string.replace("DDDD","%A")
        string = string.replace("DDD","%a")
        string = string.replace("DD","%d")
        string = string.replace("D","%d")
        string = string.replace("MMMM","%B")
        string = string.replace("MMM","%b")
        if string.find("H") == -1:
            string = string.replace("MM","%m")
            string = string.replace("M","%m")
        else:
            alphastring = ''.join(x for x in string if x.isalpha())
            while alphastring.find("MM") != -1:
                if alphastring[alphastring.find("MM")-1] == "H":
                    alphastring = alphastring.replace("MM","%M",1)
                    string = string.replace("MM","%M",1)
                else:
                    alphastring = alphastring.replace("MM","%m",1)
                    string = string.replace("MM","%m",1)
            while alphastring.find("MM") != -1:
                if alphastring[alphastring.find("M")-1] == "H":
                    alphastring.replace("M","%M",1)
                    string.replace("M","%M",1)
                else:
                    alphastring.replace("M","%m",1)
                    string.replace("M","%m",1)
        string = string.replace("HH","%H")
        string = string.replace("H","%H")
        strwithdate = strwithdate.replace(text,target_date.strftime(string))
    return strwithdate

def date_offset(offset:int = 0):
    today = datetime.datetime.now()
    if offset == 0:
        return today
    if offset < 0:
        real_offset = abs(offset) + (math.ceil((abs(offset)-today.weekday()) / 7)*2)
        return datetime.datetime.now() + datetime.timedelta(days=-real_offset)
    if offset > 0:
        real_offset = offset + (math.ceil((abs(offset)-(4-today.weekday())) / 7)*2)
        return datetime.datetime.now() + datetime.timedelta(days=real_offset)

print(dynamic_date_in_string("moja data to #yyyy/mm/dd h:mm# i koniec|5"))

