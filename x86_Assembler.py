"""
Program Description: x86 Assembler (Converting Assembly to Machine Language)
Author: AmirHossein Roodaki (Student No. 9935707)
School: Department of Computer Science & Engineering, Shiraz University
Creation Date: 11/24/2021
Revisions: 3            Modifier: AmirHossein Roodaki
"""


# A Function to Check If a registerName Is One of 8-Bit Registers of Assembly Language or Not
def isReg8(registerName):
    allReg8List = ["AH", "AL", "BH", "BL", "CH", "CL", "DH", "DL"]
    return registerName in allReg8List


# A Function to Check If a registerName Is One of 16-Bit Registers of Assembly Language or Not
def isReg16(registerName):
    allReg16List = ["AX", "BX", "CX", "DX", "SP", "BP", "SI", "DI"]
    return registerName in allReg16List


# A Function to Check If a registerName Is One of 32-Bit Registers of Assembly Language or Not
def isReg32(registerName):
    allReg32List = ["EAX", "EBX", "ECX", "EDX", "ESP", "EBP", "ESI", "EDI"]
    return registerName in allReg32List


# A Function to Check If a name Is a Valid Register in Assembly or Not
def isReg(name):
    return isReg8(name) or isReg16(name) or isReg32(name)


# A Function to Count Number of Bits of a Register
def countBits(registerName):
    if isMemory(registerName):
        registerName = registerName[1:][:-1]

    if isReg8(registerName):
        return 8
    elif isReg16(registerName):
        return 16
    elif isReg32(registerName):
        return 32


# A Function to Check If an Name is a Memory (Starts & Ends with Square Bracket) and Has a Valid Register Inside It
def isMemory(name):
    return (name.startswith('[') and name.endswith(']')) and isReg(
        name[1:][:-1])


# A Function to Check If an Name is a Label (Ends with ':') Or Not
def isLabel(name):
    return name.endswith(':')


# A Function to Find Opcode of the Instruction
def findOpcode():
    if instruction == "JMP":
        return r"\xEB"
    else:
        opcodeTable = {  # Source: https://x86.puri.sm/
            "ADD": {
                8: {
                    False: r"\x00",
                    True: r"\x02"
                },
                16: {
                    False: r"\x66\x01",
                    True: r"\x66\x03"
                },
                32: {
                    False: r"\x01",
                    True: r"\x03"
                }
            },
            "SUB": {
                8: {
                    False: r"\x28",
                    True: r"\x2A"
                },
                16: {
                    False: r"\x66\x29",
                    True: r"\x66\x2B"
                },
                32: {
                    False: r"\x29",
                    True: r"\x2B"
                }
            },
            "AND": {
                8: {
                    False: r"\x20",
                    True: r"\x22"
                },
                16: {
                    False: r"\x66\x21",
                    True: r"\x66\x23"
                },
                32: {
                    False: r"\x21",
                    True: r"\x23"
                }
            },
            "OR": {
                8: {
                    False: r"\x08",
                    True: r"\x0A"
                },
                16: {
                    False: r"\x66\x09",
                    True: r":\x66\x0B"
                },
                32: {
                    False: r"\x09",
                    True: r"\x0B"
                }
            }
        }
        return opcodeTable[instruction][countBits(destinationOperand)][
            isMemory(sourceOperand)]


# A Function to find MOD
def findMOD():
    return "00" if isMemory(destinationOperand) or isMemory(
        sourceOperand) else "11"


# A Function to Find REG & R/M Byte (Source: http://www.c-jump.com/CIS77/CPU/x86/lecture.html#X77_0080_mod_reg_r_m_byte_reg)
def find_REG_RM():
    """
    1. If One of the Operands Is a Memory: REG = Register, R/M = Memory
    2. If No Memory Is Involved: REG = sourceOperand, R/M = destinationOperand
    """
    REGvaluesOfRegisters = {  # Source: http://www.c-jump.com/CIS77/images/x86_register_encoding.png
        "AL": "000",
        "AX": "000",
        "EAX": "000",
        "CL": "001",
        "CX": "001",
        "ECX": "001",
        "DL": "010",
        "DX": "010",
        "EDX": "010",
        "BL": "011",
        "BX": "011",
        "EBX": "011",
        "AH": "100",
        "SP": "100",
        "ESP": "100",
        "CH": "101",
        "BP": "101",
        "EBP": "101",
        "DH": "110",
        "SI": "110",
        "ESI": "110",
        "BH": "111",
        "DI": "111",
        "EDI": "111"
    }

    if isMemory(destinationOperand):
        REG = REGvaluesOfRegisters[sourceOperand]
        RM = REGvaluesOfRegisters[destinationOperand[1:][:-1]]
    elif isMemory(sourceOperand):
        REG = REGvaluesOfRegisters[destinationOperand]
        RM = REGvaluesOfRegisters[sourceOperand[1:][:-1]]
    else:
        REG = REGvaluesOfRegisters[sourceOperand]
        RM = REGvaluesOfRegisters[destinationOperand]

    return REG + RM


# A Function to Count Number of Bytes from the Beginning of the Input File Till the Given Label of 'JMP' Instruction
def countBytesTillLabel():
    """
    Add 2 for JMP or 8-Bit & 32-Bit Registers and 3 for 16-Bit Registers to our Counter
    Break the Loop Return the Counter if Reached the Wanted Label of JMP Instruction
    """
    global isBeingTested
    isBeingTested = False

    countBytesTillLabel = 0

    for testCase in testCases:
        testCase = testCase.split()
        if testCase[0][:-1] == destinationOperand:
            break
        else:
            if isValidTestCase() and not isLabel(testCase[0]):
                if testCase[0] == "JMP":
                    countBytesTillLabel += 2
                else:
                    if isReg16(testCase[1][:-1]) or isReg16(testCase[2]):
                        countBytesTillLabel += 3
                    else:
                        countBytesTillLabel += 2

    isBeingTested = True

    return countBytesTillLabel


# A Function to Convert Signed Decimal into Hexadecimal (Supporting 2's Complement)
def signedDecimal2hexadecimalConvertor(signedDecimal):
    convertedNumber = str(hex((signedDecimal) & (2**8 - 1)))[2:].upper()
    return r"\x0" + convertedNumber if len(
        convertedNumber) == 1 else r"\x" + convertedNumber


# A Function to Convert Binary Number to HexaDecimal
def binary2hexadecimalConvertor(binaryNumber):
    convertedNumber = str(hex(int(binaryNumber, 2)))[2:].upper()
    return r"\x0" + convertedNumber if len(
        convertedNumber) == 1 else r"\x" + convertedNumber


# The Main Function of the Program That Calculate the Machine Code
def assembly2machineConvertor():
    """
    # JMP -> Opcode + Bytes Between JMP Instruction & It's Label
    # Add, SUB, AND, OR -> Opcode + MOD + R/M
    """

    if instruction == "JMP":
        opcode = findOpcode()
        countBetweenBytes = countBytesTillLabel() - countPassedBytes

        machineCode = opcode + \
            signedDecimal2hexadecimalConvertor(countBetweenBytes)
    else:
        opcode = findOpcode()
        MOD = findMOD()
        REG_RM = find_REG_RM()

        machineCode = opcode + binary2hexadecimalConvertor(MOD + REG_RM)

    return machineCode


# A Function to Check If a Name Is Valid Instruction or Not
def isValidInstruction(name):
    supportedInstructions = ["ADD", "SUB", "AND", "OR", "JMP"]
    return name in supportedInstructions


# A Function to Check If an Inputted TestCase is Valid or Not
def isValidTestCase():
    """
    Invalidity Scenarios:
        1. Entered Instruction is NOT Supported (1. It's Not Available in Assembly 2. Not Supported in This Version of Program)!
        2. Not Correct Number of Operands for The Instruction!
        3. Invalid Type for Destination/Source Operand!
        4. Size Mismatch of Destination Operand & Source Operand!
    """

    if not isValidInstruction(testCase[0]):
        print("Entered Instruction is NOT Valid!\n") if isBeingTested else None
        return False

    twoOperandInstructions = ["JMP"]
    threeOperandInstructions = ["ADD", "SUB", "AND", "OR"]
    if testCase[0] in twoOperandInstructions:
        if len(testCase) != 2:
            print(
                f"Incorrect Number of Operands for {testCase[0]}'s Instruction!\n"
            ) if isBeingTested else None
            return False

    elif testCase[0] in threeOperandInstructions:
        if len(testCase) != 3:
            print(
                f"Incorrect Number of Operands for {testCase[0]}'s Instruction!\n"
            ) if isBeingTested else None
            return False

        if not ((isReg(testCase[1][:-1]) or isMemory(testCase[1][:-1])) and
                ((isReg(testCase[2]) or isMemory(testCase[2])))):
            print(
                "Invalid Type for Destination/Source Operand!\nMust Be a Valid Register or Memory.\n"
            ) if isBeingTested else None
            return False

        if not isMemory(testCase[2]) and countBits(
                testCase[1][:-1]) != countBits(testCase[2]):
            print(
                "Invalid Type for Destination/Source Operand!\nMust Be a Same Size.\n"
            ) if isBeingTested else None
            return False

    return True


# Opening File 'Inputs.txt' Which Contains All of the testCases(The File Must be in the Same Directory as the PythonCode!)
inputFile = open('Inputs.txt', 'r')
# Store Each Line (= 1 testCase) from The Opened File into a List & Remove the Possible "\n" in the Ending
testCases = [
    testCase[:-1].upper() if testCase.endswith("\n") else testCase.upper()
    for testCase in inputFile.readlines()
]
inputFile.close()  # Closing the Opened File

# A Counter to Count Passed Bytes of the Instructions, Used in Calculating Machine Code of 'JMP' Instruction
countPassedBytes = 0

# A Loop to Traverse All testCases
for testCaseIndex in range(len(testCases)):
    testCase = testCases[testCaseIndex].split(' ')

    # 1. Checking the Validity of the testCases Using Function 'isValidTestCase()' Before Assembling It
    # 2. Adding Passed Byte to 'countPassedBytes'
    if not isLabel(testCase[0]) and isValidTestCase():
        isBeingTested = True

        if testCase[0] == "JMP":
            countPassedBytes += 2
        else:
            if isReg16(testCase[1][:-1]) or isReg16(testCase[2]):
                countPassedBytes += 3
            else:
                countPassedBytes += 2

        # If the testCase Was Valid, split the testCase
        instruction = testCase[0].upper()
        if instruction == "JMP":  # JMP -> destinationOperand = JMP's Label
            destinationOperand = testCase[1]
        else:  # Other -> 1. destinationOperand, sourceOperand = First & Second Operands After Instruction
            destinationOperand = testCase[1][:-1].upper()
            sourceOperand = testCase[2].upper()

        print("x86 Assembly Language Input:", testCases[testCaseIndex])
        if assembly2machineConvertor() != None:
            print("x86 Machine Code Output:",
                  assembly2machineConvertor(),
                  end="\n\n")