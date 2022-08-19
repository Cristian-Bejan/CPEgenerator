import pyperclip
import urllib.parse

# use the pyperclip package, copy your input first, then execute the program
"""
    use split() to split the words in your products names if necessary - space is the default one
    depending on your situation you might want to choose a separator like ',' or '/'
"""
products = pyperclip.paste().split(", ")
products = list(dict.fromkeys(products))  # remove duplicates

baseCPE = ""
outputApplication = ""
outputHardware = ""
outputOS = ""
output = ""
CPEvendor = ""
CPEtype = ""
counterCPEtype = 0
counterCPEvendor = 0

# check the vendor name
while len(CPEvendor.split()) != 1:
    CPEvendor = input("Enter just the vendor name\n").lower()
    if len(CPEvendor.split()) != 1:
        print("Use only 1 word for vendor")
        counterCPEvendor += 1
        if counterCPEvendor == 3:
            print("Focus - use only 1 word for vendor, e.g. very_cool_vendor_name or very-cool-vendor-name")
        elif counterCPEvendor == 4:
            exit("Use coffee and try again later")
    else:
        print(CPEvendor)

# check the CPE type
CPEtype = input("Enter the product type (a, o, or h)\n").lower()

while baseCPE == "":
    if CPEtype != "a" and CPEtype != "o" and CPEtype != "h":
        print("Wrong input")
        counterCPEtype += 1
        if counterCPEtype == 3:
            print("Focus - only enter the appropriate character for your product:\n"
                  "a - for application,\no - for firmware/operating system or,\nh - for hardware")
        elif counterCPEtype == 4:
            exit("Dirty Fingers")
        CPEtype = input("Enter the product type (a, o, or h)\n").lower()
    else:
        baseCPE = "cpe:/" + CPEtype + ":" + CPEvendor + ":"
        print("The base CPE is '" + baseCPE + "' which will not appear in your pasted output:")

# urllib.parse.quote() doesn't quote letters, digits, and these chars: '_.-~'
def processSpecialChars(prod):
  dictionary = {'_': '%5f', '.':'%2e', '-': '%2d', '~': '%7e'}
  prod = urllib.parse.quote(prod, safe=' ')
  transTable = prod.maketrans(dictionary)
  prod = prod.translate(transTable)
  return(prod)

if baseCPE[5] == "a":
    for productName in products:
        productName = processSpecialChars(productName)
        i = 0
        CPEs = baseCPE
        productNameWords = productName.split()
        count = len(productNameWords)

        while i < count:
            words = productNameWords[i].lower()
            i += 1
            CPEs = CPEs + words
            if i == count:
                break
            else:
                CPEs = CPEs + "_"
        print(CPEs)
        outputApplication = outputApplication + CPEs + "\n"
    applicationCPEs = outputApplication.split()
    sizeApplication = len(applicationCPEs)

    g = 0
    while g < sizeApplication:
        if g + 1 == sizeApplication:
            output = output + applicationCPEs[g]
            break
        else:
            output = output + applicationCPEs[g] + "\n"
        g += 1

    print("\noutput\n")
    print(output)

    pyperclip.copy(output)
elif baseCPE[5] == "h" or baseCPE[5] == "o":
    if baseCPE[5] == "h":
        CPEsh1 = baseCPE
        CPEso1 = baseCPE[:5] + "o" + baseCPE[6:]
    else:
        CPEso1 = baseCPE
        CPEsh1 = baseCPE[:5] + "h" + baseCPE[6:]
    for productName in products:
        productName = processSpecialChars(productName)
        i = 0
        CPEsh = CPEsh1
        CPEso = CPEso1
        productNameWords = productName.split()
        count = len(productNameWords)

        while i < count:
            words = productNameWords[i].lower()
            i += 1
            CPEsh = CPEsh + words
            CPEso = CPEso + words

            if i == count:
                CPEso = CPEso + "_firmware"
                break
            else:
                CPEsh = CPEsh + "_"
                CPEso = CPEso + "_"
        print(CPEsh)
        print(CPEso)
        outputHardware = outputHardware + CPEsh + "\n"
        outputOS = outputOS + CPEso + "\n"

    print("\nThe output for Harware CPEs is separated from the Firmware/Operating System CPEs output\n")
    print(outputHardware + "\n" + outputOS)  # uncomment/comment to use/not use - hardware CPEs are separated from os CPEs

    hardwareCPEs = outputHardware.split()
    osCPEs = outputOS.split()
    g = 0
    z = 0
    sizeHardware = len(hardwareCPEs)
    sizeOS = len(osCPEs)

    while g < sizeHardware:
        output = output + hardwareCPEs[g] + "\n"
        while z < sizeOS:
            if g + 1 == sizeHardware:
                output = output + osCPEs[z]
            else:
                output = output + osCPEs[z] + "\n"
            z += 1
            break
        g += 1

    print("\nmixed output\n")
    print(output)

    pyperclip.copy(output)
else:
    print("not ok")
