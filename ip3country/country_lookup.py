import os

class CountryLookup:
    countryCodes = []
    countryTable = []
    ipRanges = []

    def __init__(self):
        datafile = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', 'ip_supalite.table')
        with open(datafile, mode="rb") as file:
            self.ipSupalite = file.read()
        self.processTable()

    def processTable(self):
        index = 0
        for ii in range(256):
            c1 = self.ipSupalite[index]
            c2 = self.ipSupalite[index + 1]
            index += 2
            self.countryTable.append(chr(c1) + chr(c2))
            if chr(c1) == "*":
                break

        lastEndRange = 0
        while index < len(self.ipSupalite):
            count = 0
            n1 = self.ipSupalite[index]
            index += 1
            if n1 < 240:
                count = n1
            elif n1 == 242:
                n2 = self.ipSupalite[index]
                n3 = self.ipSupalite[index + 1]
                index += 2
                count = n2 | (n3 << 8)
            elif n1 == 243:
                n2 = self.ipSupalite[index]
                n3 = self.ipSupalite[index + 1]
                n4 = self.ipSupalite[index + 2]
                index += 3
                count = n2 | (n3 << 8) | (n4 << 16)

            lastEndRange += count * 256
            cc = self.ipSupalite[index]
            index += 1

            self.ipRanges.append(lastEndRange)
            self.countryCodes.append(self.countryTable[cc])

    def lookupStr(self, ipAddrStr):
        components = ipAddrStr.split(".")
        if len(components) != 4:
            return None

        ipNumber = (
            int(components[0]) * pow(256, 3)
            + (int(components[1]) << 16)
            + (int(components[2]) << 8)
            + (int(components[3]))
        )
        return self.lookupNumeric(ipNumber)

    def lookupNumeric(self, ipNumber):
        index = self.binarySearch(ipNumber)
        cc = self.countryCodes[index]
        if cc == "--":
            return None

        return cc

    def binarySearch(self, value):
        min = 0
        max = len(self.ipRanges) - 1

        while min < max:
            mid = (min + max) >> 1
            if self.ipRanges[mid] <= value:
                min = mid + 1
            else:
                max = mid

        return min
