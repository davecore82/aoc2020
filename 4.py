#!env python
import re

#separate file in blocks 
with open("4.data") as f:
    lines = f.read()
passports = lines.split("\n\n")

passportdict = {}
goodpassports = 0

for passport in passports:
    # replace any \n with spaces
    passportdict = {}   # reset the dict
    passport = passport.replace('\n',' ')
    #print(passport)
    fields = passport.split()
    #print(fields)
    # fields look like ['eyr:2023', 'hgt:188cm', 'iyr:2014', 'pid:945115479', 'byr:1979', 'ecl:blu', 'hcl:#b6652a']
    for field in fields:
        temp = field.split(":")
        passportdict[temp[0]] = temp[1]

    ecl = False
    pid = False
    eyr = False
    hcl = False
    byr = False
    iyr = False
    hgt = False

    # byr (Birth Year) - four digits; at least 1920 and at most 2002
    if "byr" in passportdict:
        if int(passportdict["byr"])  >= 1920 and int(passportdict["byr"]) <= 2002:
            byr = True

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020
    if "iyr" in passportdict:
        if int(passportdict["iyr"])  >= 2010 and int(passportdict["iyr"]) <= 2020:
            iyr = True

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030
    if "eyr" in passportdict:
        if int(passportdict["eyr"])  >= 2020 and int(passportdict["eyr"]) <= 2030:
            eyr = True

    # hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76
    if "hgt" in passportdict:
        matched = re.match("^[-+]?[0-9]+(cm|in)$", passportdict["hgt"])
        is_match = bool(matched)
        if is_match:
            if "cm" in passportdict["hgt"]:
                heightincm = re.findall(r'\d+', passportdict["hgt"])[0]
                if int(heightincm) >= 150 and int(heightincm) <= 193:
                    hgt = True
            else:
                heightininches = re.findall(r'\d+', passportdict["hgt"])[0]
                if int(heightininches) >= 59 and int(heightininches) <= 76:
                    hgt = True

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
    if "hcl" in passportdict:
        matched = re.match("^#([0-9]|[a-f]){6}$", passportdict["hcl"])
        is_match = bool(matched)
        if is_match:
            hcl = True

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
    if "ecl" in passportdict:
        acceptableeyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if passportdict["ecl"] in acceptableeyecolors:
            ecl = True

    # pid (Passport ID) - a nine-digit number, including leading zeroes
    if "pid" in passportdict:
        matched = re.match("^[0-9]{9}$", passportdict["pid"])
        is_match = bool(matched)
        if is_match:
            pid = True

    # print(passportdict)
    # print("ecl: ", ecl)
    # print("pid: ", pid)
    # print("eyr: ", eyr)
    # print("hcl: ", hcl)
    # print("byr: ", byr)
    # print("iyr: ", iyr)
    # print("hgt: ", hgt)

    if ecl and pid and eyr and hcl and byr and iyr and hgt:
        goodpassports += 1

print(goodpassports)
#print(passportlist)[0]

