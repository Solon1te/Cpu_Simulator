class CPU:
    def __init__(self):
        self.PC = 0
        self.R7 = 0
        self.registers = [0] * 32
        self.zero_flag = False

    def execute_instruction(self, instruction):
        opcode = instruction[0:6]
        if opcode == '000000': 
            funct = instruction[-6:]
            if funct == '100000':
                self.execute_add(instruction)
        elif opcode == '001000':
            self.execute_addi(instruction)

    def execute_add(self, instruction):
        rd = int(instruction[16:21], 2)
        rs = int(instruction[6:11], 2)
        rt = int(instruction[11:16], 2)
        
    
        result = self.registers[rs] + self.registers[rt]
        self.registers[rd] = result
        self.PC += 4  

    def execute_addi(self, instruction):
    
        rt = int(instruction[11:16], 2)
        rs = int(instruction[6:11], 2)
        immediate = int(instruction[16:], 2)
        
    
        result = self.registers[rs] + immediate
        self.registers[rt] = result
        self.PC += 4

    

    def halt_execution(self):
        print("Execution halted.")
        

    def get_state(self):
        return {
            'PC': self.PC,
            'R7': self.R7,
            'registers': self.registers,
            'zero_flag': self.zero_flag
        }