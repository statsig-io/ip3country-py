from country_lookup import CountryLookup

seqExpected = [
    "--",
    "US",
    "FR",
    "US",
    "US",
    "DE",
    "US",
    "US",
    "US",
    "US",
    None,
    "US",
    "US",
    "US",
    "JP",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "GB",
    "US",
    "CN",
    "US",
    "US",
    "US",
    "MD",
    "US",
    "US",
    "US",
    "US",
    "CN",
    "KW",
    "US",
    "PK",
    "US",
    "EG",
    "KR",
    "CN",
    "US",
    "CA",
    "RU",
    "US",
    "US",
    "TH",
    "US",
    "GB",
    "US",
    "DE",
    "US",
    "US",
    "US",
    "US",
    "CN",
    "CN",
    "JP",
    "TW",
    "BE",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "CA",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "IR",
    "SE",
    "GB",
    "NL",
    "IT",
    "DE",
    "NL",
    "NL",
    "ES",
    "NL",
    "GB",
    "NO",
    "FR",
    "FR",
    "FR",
    "FR",
    "RU",
    "IT",
    "PT",
    "US",
    "US",
    "US",
    "US",
    None,
    "TW",
    "MA",
    "BD",
    "US",
    "DZ",
    "TW",
    "US",
    "US",
    "NL",
    "CN",
    "JP",
    "CN",
    "CN",
    "CN",
    "IN",
    "CN",
    "CN",
    "CN",
    "CN",
    "TW",
    "MY",
    "TW",
    "CN",
    "IN",
    "CN",
    "JP",
    None,
    "US",
    "CH",
    "AU",
    "US",
    "US",
    "JP",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "CA",
    "US",
    "US",
    "NL",
    "US",
    "GB",
    "SE",
    "US",
    "KR",
    "US",
    "BE",
    "JP",
    "KE",
    "US",
    "TZ",
    "IS",
    "SG",
    "CA",
    "MA",
    "US",
    "US",
    "BE",
    "IN",
    "ZA",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "CN",
    "FR",
    "BR",
    "RU",
    "BR",
    "TH",
    "VE",
    "PK",
    "JP",
    "US",
    "LV",
    "VE",
    "MX",
    "BE",
    "MX",
    "AR",
    "BR",
    "TW",
    "UA",
    "GB",
    "GB",
    "FI",
    "EG",
    "US",
    "US",
    "BR",
    "CR",
    "CN",
    "TW",
    "US",
    "US",
    "US",
    "US",
    "US",
    "US",
    "KR",
    "KR",
    "GB",
    "BE",
    "US",
    "US",
    "US",
    "ES",
    "JP",
    "CN",
    "JP",
    "CN",
    "CN",
    "SG",
]


def expectedSequenceTest():
    cl = CountryLookup()
    for ii in range(1, len(seqExpected)):
        ipStr = f"{ii}.{ii}.{ii}.{ii}"
        expected = seqExpected[ii]
        actual = cl.lookupStr(ipStr)

        failed = False
        if expected == actual:
            print('.', end="")
        else:
            failed = True
            print(f"F: {expected}/{actual}")

    print("[end]")
    if failed:
        print("TEST FAILED")
    else:
        print("ALL TESTS PASSED")

if __name__ == '__main__':
    expectedSequenceTest()
