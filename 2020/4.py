import re

data = open("input/4").read().split("\n\n")


def part1():
    expected_fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    }
    valid_passports = 0
    for passport in data:
        keys = []
        for pair in passport.split():
            keys.append(pair.split(":")[0])
        if all(ef in keys for ef in expected_fields):
            valid_passports += 1

    return valid_passports


def part2():
    expected_fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    }
    valid_passports = 0
    for passport in data:
        kv = {}
        for pair in passport.split():
            key, val = pair.split(":")
            kv[key] = val
        valid = True
        if not all(ef in kv.keys() for ef in expected_fields):
            valid = False
        for k, v in kv.items():
            if k == "byr":
                if not (re.search("^\d{4}$", v) and (1920 <= int(v) <= 2002)):
                    valid = False
                    break
            if k == "iyr":
                if not (re.search("^\d{4}$", v) and (2010 <= int(v) <= 2020)):
                    valid = False
                    break
            if k == "eyr":
                if not (re.search("^\d{4}$", v) and (2020 <= int(v) <= 2030)):
                    valid = False
                    break
            if k == "hgt":
                if not re.search("^\d+(cm|in)$", v):
                    valid = False
                    break
                if "cm" in v:
                    num = re.findall("\d+", v)
                    if not 150 <= int(num[0]) <= 193:
                        valid = False
                        break
                elif "in" in v:
                    num = re.findall("\d+", v)
                    if not 59 <= int(num[0]) <= 76:
                        valid = False
                        break
            if k == "hcl":
                if not (re.search("#[a-f0-9]{6}$", v)):
                    valid = False
                    break
            if k == "ecl":
                if v not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                    valid = False
                    break
            if k == "pid":
                if not (re.search("^\d{9}$", v)):
                    valid = False
                    break

        if valid:
            valid_passports += 1

    return valid_passports


if __name__ == "__main__":
    print(part1())
    print(part2())
