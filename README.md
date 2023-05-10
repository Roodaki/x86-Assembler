<div align="center">
  <h1><strong>x86 Assembler</strong></h1>
  <p><strong>This is a simple x86 Assembler that takes a text file containing x86 assembly instructions as input and converts them into machine code.</strong></p>
</div>

## Requirements
* Python 3.X

## Usage Guide
1. Clone the repository: `git clone https://github.com/Roodaki/x86-Assembler`
2. Edit "inputs.txt" file and enter the x86 assembly instructions that you want to assemble.
4. Run the program: `python3 X86_Assembler.py`

## Example
Assuming you have entered following x86 assembly instructions to the "input.txt" file:
```
OR AL, BL
ADD [AL], BL
LABEL1:
SUB EAX, EBX
JMP LABEL1
```
Running the program will output the machine code instructor-by-instruction to the terminal:
```
x86 Assembly Language Input: OR AL, BL
x86 Machine Code Output: \x08\xD8

x86 Assembly Language Input: ADD [AL], BL
x86 Machine Code Output: \x00\x18

x86 Assembly Language Input: SUB EAX, EBX
x86 Machine Code Output: \x29\xD8

x86 Assembly Language Input: JMP LABEL1
x86 Machine Code Output: \xEB\xFC
```
Please note that you need to enter the x86 assembly instructions in "input.txt" before running the program. 
