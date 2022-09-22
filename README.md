<h1 align="center">x86 Assembler</h1>

* An x86 Assembler that Takes a .txt File of [x86 Assembly](https://en.wikipedia.org/wiki/X86_assembly_language) Instructions as Input and Converts Them into [Machine Code](https://en.wikipedia.org/wiki/Machine_code).

## [Assembler's Encoding Proccess](http://www.c-jump.com/CIS77/CPU/x86/lecture.html):
  1. Check Validity of Inputted Instructions and Their Operands:
  
      - Invalidity Scenarios:
        1. Entered Instruction is NOT Supported (Supported Instructions: JMP, ADD, SUB, AND, OR)
        2. Incorrect Number of Operands for The Instruction
        3. Invalid Type for Destination/Source Operand
        4. Size Mismatch of Destination Operand & Source Operand
  2. Encoding Formulas:
      - ADD, SUB, AND, OR -> [Opcode](https://c9x.me/x86/) + [MOD + REG R/M](http://www.c-jump.com/CIS77/CPU/x86/lecture.html#X77_0060_mod_reg_r_m_byte)
        1. Opcode
          
            ![ADD Opcode](https://user-images.githubusercontent.com/89901590/191819419-032f3131-740d-419d-b335-eef0595893bc.png)
            ![SUB Opcode](https://user-images.githubusercontent.com/89901590/191819530-41b7651c-f2af-4d54-82bb-7ebf0bf2bb3e.png)
            ![AND Opcode](https://user-images.githubusercontent.com/89901590/191819659-a8c35e1e-2804-46d2-ae0b-9081fd9599d4.png)
            ![OR Opcode](https://user-images.githubusercontent.com/89901590/191819771-c464c110-0995-4d2f-a65a-db7bdedfe200.png)

        2. MOD:
            
            ![MOD](http://www.c-jump.com/CIS77/images/mod_meaning.png)
        3. REG R/M:
        
            ![REG R/M](http://www.c-jump.com/CIS77/images/x86_register_encoding.png)
            - If One of the Operands Is a Memory: 
            
              REG = Register
              
              R/M = Memory
            - If Both of the Operands are Register:
            
              REG = sourceOperand
              
              R/M = destinationOperand
      - JMP -> Opcode + Bytes Between JMP Instruction & It's Label
      
        1. Opcode:
        
            ![JMP Opcode](https://user-images.githubusercontent.com/89901590/191822225-e4e2b727-6507-451f-a8c9-958c29692d84.png)
