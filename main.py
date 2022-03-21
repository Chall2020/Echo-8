from email.errors import ObsoleteHeaderDefect
import os
import sys
from time import sleep
from turtle import clear

global O_Reg
global A_Reg
global B_Reg
global C_Reg
global PC_Reg
global clear_string

A_Reg = 0
B_Reg = 0
C_Reg = 0
O_Reg = 0
SP_Reg = 0
PC_Reg = 0
Flag_Reg = -1

if sys.platform.startswith("linux"):
    clear_string = "clear"
else:
    clear_string = "cls"

def main(target_file):
    global O_Reg
    global A_Reg
    global B_Reg
    global C_Reg
    global PC_Reg
    global clear_string

    try:
        file = open(target_file, "r")
    except FileNotFoundError:
        print(f"Error! File {target_file} does not exist!")
        return -1

    lines = file.read().splitlines()
    instructions = " ".join(lines)

    instructions = instructions.split(" ")

    i = 0
    while i < len(instructions):
        PC_Reg = i
        if instructions[i] == "000":
            while True: continue
        elif instructions[i].startswith("1"):
            src = instructions[i][1:]
            src = int(src, 16)
            A_Reg = src
        elif instructions[i].startswith("2"):
            src = instructions[i][1:]
            src = int(src, 16)
            B_Reg = src
        elif instructions[i].startswith("3"):
            A_Reg = B_Reg
        elif instructions[i].startswith("4"):
            B_Reg = A_Reg
        elif instructions[i].startswith("5"):
            C_Reg = A_Reg + B_Reg
        elif instructions[i].startswith("6"):
            C_Reg = A_Reg - B_Reg
        elif instructions[i].startswith("7"):
            Flag_Reg = A_Reg and B_Reg
        elif instructions[i].startswith("8"):
            Flag_Reg = A_Reg or B_Reg
        elif instructions[i].startswith("9"):
            Flag_Reg = not A_Reg
        elif instructions[i].lower().startswith("a"):
            dest = int(instructions[i][1:])
            i = dest-1
        elif instructions[i].lower().startswith("b"):
            A_Reg = C_Reg
        elif instructions[i].lower().startswith("c"):
            B_Reg = C_Reg
        elif instructions[i].lower().startswith("d"):
            O_Reg = A_Reg
        elif instructions[i].lower().startswith("e"):
            O_Reg = B_Reg
        elif instructions[i].lower().startswith("f"):
            O_Reg = C_Reg

        if A_Reg > 0xff:
            A_Reg = 0

        if B_Reg > 0xff:
            A_Reg = 0

        if C_Reg > 0xff:
            C_Reg = 0

        O_Bin = bin(O_Reg)[2:].rjust(8, "0")
        A_Bin = bin(A_Reg)[2:].rjust(8, "0")
        B_Bin = bin(B_Reg)[2:].rjust(8, "0")
        C_Bin = bin(C_Reg)[2:].rjust(8, "0")
        PC_Bin = bin(PC_Reg)[2:].rjust(8, "0")

        O_Hex = "0x" + hex(O_Reg)[2:].rjust(2, "0").upper()
        A_Hex = "0x" + hex(A_Reg)[2:].rjust(2, "0").upper()
        B_Hex = "0x" + hex(B_Reg)[2:].rjust(2, "0").upper()
        C_Hex = "0x" + hex(C_Reg)[2:].rjust(2, "0").upper()
        PC_Hex = "0x" + hex(PC_Reg)[2:].rjust(2, "0").upper()

        O_Bin = O_Bin.replace("0", "⚫").replace("1", "⚪")
        A_Bin = A_Bin.replace("0", "⚫").replace("1", "⚪")
        B_Bin = B_Bin.replace("0", "⚫").replace("1", "⚪")
        C_Bin = C_Bin.replace("0", "⚫").replace("1", "⚪")
        PC_Bin = PC_Bin.replace("0", "⚫").replace("1", "⚪")

        os.system(clear_string)
        print(f"Output:                 {O_Bin}  {O_Hex}\n")
        print(f"A Register:             {A_Bin}  {A_Hex}\n")
        print(f"B Register:             {B_Bin}  {B_Hex}\n")
        print(f"C Register:             {C_Bin}  {C_Hex}\n")
        print(f"Program Counter:        {PC_Bin}  {PC_Hex}\n")

        sleep(0.0625)
        i += 1

while True:
    os.system(clear_string)
    main(input("File to Open: "))