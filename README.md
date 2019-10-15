# Twopassassembler

A program in python (assembler) to convert assembly language program into machine language object code.

This project attempts to emulate the working of an assembler by converting the assembler code to binary opcode.

## Usage

python3 assem.py

## Logic & Working
The two pass assembler performs two passes over the source program.

In the first pass, it reads the entire source program, looking only for label definitions. All the labels are collected, assigned address, and placed in the symbol table in this pass, no instructions as assembled and at the end the symbol table should contain all the labels defined in the program. To assign address to labels, the assembles maintains a Location Counter (LC).

In the second pass the instructions are again read and are assembled using the symbol table. Basically, the assembler goes through the program one line at a time, and generates machine code for that instruction. Then the assembler proceeds to the next instruction. In this way, the entire machine code program is created. For most instructions this process works fine, for example for instructions that only reference registers, the assembler can compute the machine code easily, since the assembler knows where the registers are.

## Assmbler Opcodes

| Opcode | Meaning |	Assembly Opcode |
| ---- | ----------------- | --- |
| 0000 | Clear accumulator |	CLA |
| 0001 | Load into accumulator from address | LAC |
| 0010 | Store accumulator contents into address |	SAC |
| 0011 | Add address contents to accumulator contents | ADD |
| 0100 | Subtract address contents from accumulator contents	| SUB |
| 0101 | Branch to address if accumulator contains zero | BRZ |
| 0110 | Branch to address if accumulator contains negative value | BRN |
| 0111 | Branch to address if accumulator contains positive value | BRP |
| 1000 | Read from terminal and put in address | INP |
| 1000 | Display value in address on terminal | DSP |
| 1010 | Multiply accumulator and address contents | MUL |
| 1011 | Divide accumulator contents by address content. Quotient in R1 and remainder in R2 | DIV |
| 1100 | Stop execution | STP |



## Errors Handled

The error handling in the assembler is done by sending out error codes

| CODE | ERROR |
| ---- | --- |
| 01 | A symbol has been used but not defined |
| 02 | A symbol has been defined more than once |
| 03 | The name in the opcode field is not a legal opcode |
| 04 | An opcode is not supplied with enough operands |
| 05 |  An opcode is supplied with too many operands |
| 06 | The END statement is missing |

