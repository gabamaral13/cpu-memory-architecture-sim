import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

#memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
#memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')


def buscarEDecodificarInstrucao():
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    instrucao = memoria.getValorMemoria(registrador_cp)

    if CPU_DEBUG:
        if instrucao == 0x00:
            print('buscarEDecodificarInstrucao: instrução ADD Reg, Byte')
        elif instrucao == 0x01:
            print('buscarEDecodificarInstrucao: instrução ADD Reg, Reg')
        elif instrucao == 0x10:
            print('buscarEDecodificarInstrucao: instrução INC Reg')
        elif instrucao == 0x20:
            print('buscarEDecodificarInstrucao: instrução DEC Reg')
        elif instrucao == 0x40:
            print('buscarEDecodificarInstrucao: instrução MOV Reg, Byte')
        elif instrucao == 0x41:
            print('buscarEDecodificarInstrucao: instrução MOV Reg, Reg')
        elif instrucao == 0x50:
            print('buscarEDecodificarInstrucao: instrução JMP Byte')
        elif instrucao == 0x60:
            print('buscarEDecodificarInstrucao: instrução CMP Reg, Byte')
        elif instrucao == 0x79:
            print('buscarEDecodificarInstrucao: instrução JZ Byte')

    if instrucao in [0x00, 0x01, 0x10, 0x20, 0x40, 0x41, 0x50, 0x60, 0x79]:
        return instrucao

    return -1


def lerOperadoresExecutarInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    if idInstrucao == 0x00:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            registrador_ax += operador2
            if CPU_DEBUG: print(f'lerOperadoresExecutarInstrucao: somando {operador2:02X} em AX')
        elif operador1 == 0x03:
            registrador_bx += operador2
            if CPU_DEBUG: print(f'lerOperadoresExecutarInstrucao: somando {operador2:02X} em BX')
        elif operador1 == 0x04:
            registrador_cx += operador2
            if CPU_DEBUG: print(f'lerOperadoresExecutarInstrucao: somando {operador2:02X} em CX')
        elif operador1 == 0x05:
            registrador_dx += operador2
            if CPU_DEBUG: print(f'lerOperadoresExecutarInstrucao: somando {operador2:02X} em DX')

    elif idInstrucao == 0x01:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02 and operador2 == 0x02:
            registrador_ax = registrador_ax + registrador_ax
        elif operador1 == 0x02 and operador2 == 0x03:
            registrador_ax = registrador_ax + registrador_bx
        elif operador1 == 0x02 and operador2 == 0x04:
            registrador_ax = registrador_ax + registrador_cx
        elif operador1 == 0x02 and operador2 == 0x05:
            registrador_ax = registrador_ax + registrador_dx
        elif operador1 == 0x03 and operador2 == 0x03:
            registrador_bx = registrador_bx + registrador_bx
        elif operador1 == 0x03 and operador2 == 0x04:
            registrador_bx = registrador_bx + registrador_cx
        elif operador1 == 0x03 and operador2 == 0x05:
            registrador_bx = registrador_bx + registrador_dx
        elif operador1 == 0x04 and operador2 == 0x04:
            registrador_cx = registrador_cx + registrador_cx
        elif operador1 == 0x04 and operador2 == 0x05:
            registrador_cx = registrador_cx + registrador_dx
        elif operador1 == 0x05 and operador2 == 0x05:
            registrador_dx = registrador_dx + registrador_dx
        elif operador1 == 0x05 and operador2 == 0x04:
            registrador_dx = registrador_dx + registrador_cx
        elif operador1 == 0x05 and operador2 == 0x03:
            registrador_dx = registrador_dx + registrador_bx
        elif operador1 == 0x05 and operador2 == 0x02:
            registrador_dx = registrador_dx + registrador_ax
        elif operador1 == 0x04 and operador2 == 0x03:
            registrador_cx = registrador_cx + registrador_bx
        elif operador1 == 0x04 and operador2 == 0x02:
            registrador_cx = registrador_cx + registrador_ax
        elif operador1 == 0x03 and operador2 == 0x02:
            registrador_bx = registrador_bx + registrador_ax

        if CPU_DEBUG: print('lerOperadoresExecutarInstrucao: executando ADD Reg, Reg')

    elif idInstrucao == 0x10:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:
            registrador_ax += 1
        elif operador1 == 0x03:
            registrador_bx += 1
        elif operador1 == 0x04:
            registrador_cx += 1
        elif operador1 == 0x05:
            registrador_dx += 1
        if CPU_DEBUG: print('lerOperadoresExecutarInstrucao: executando INC Reg')

    elif idInstrucao == 0x20:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:
            registrador_ax -= 1
        elif operador1 == 0x03:
            registrador_bx -= 1
        elif operador1 == 0x04:
            registrador_cx -= 1
        elif operador1 == 0x05:
            registrador_dx -= 1
        if CPU_DEBUG: print('lerOperadoresExecutarInstrucao: executando DEC Reg')

    elif idInstrucao == 0x40:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            registrador_ax = operador2
        elif operador1 == 0x03:
            registrador_bx = operador2
        elif operador1 == 0x04:
            registrador_cx = operador2
        elif operador1 == 0x05:
            registrador_dx = operador2
        if CPU_DEBUG: print(f'lerOperadoresExecutarInstrucao: atribuindo {operador2:02X}')

    elif idInstrucao == 0x41:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        valor_op2 = 0

        if operador2 == 0x02:
            valor_op2 = registrador_ax
        elif operador2 == 0x03:
            valor_op2 = registrador_bx
        elif operador2 == 0x04:
            valor_op2 = registrador_cx
        elif operador2 == 0x05:
            valor_op2 = registrador_dx

        if operador1 == 0x02:
            registrador_ax = valor_op2
        elif operador1 == 0x03:
            registrador_bx = valor_op2
        elif operador1 == 0x04:
            registrador_cx = valor_op2
        elif operador1 == 0x05:
            registrador_dx = valor_op2
        if CPU_DEBUG: print('lerOperadoresExecutarInstrucao: executando MOV Reg, Reg')

    elif idInstrucao == 0x60:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        valor_op1 = 0

        if operador1 == 0x02:
            valor_op1 = registrador_ax
        elif operador1 == 0x03:
            valor_op1 = registrador_bx
        elif operador1 == 0x04:
            valor_op1 = registrador_cx
        elif operador1 == 0x05:
            valor_op1 = registrador_dx

        if valor_op1 == operador2:
            flag_zero = True
        else:
            flag_zero = False
        if CPU_DEBUG: print(f'lerOperadoresExecutarInstrucao: comparando. ZF={flag_zero}')

    elif idInstrucao == 0x50:
        pass

    elif idInstrucao == 0x79:
        pass


def calcularProximaInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    if idInstrucao == 0x00 or idInstrucao == 0x01 or idInstrucao == 0x40 or idInstrucao == 0x41 or idInstrucao == 0x60:
        registrador_cp = registrador_cp + 3
        if CPU_DEBUG: print(f'calcularProximaInstrucao: mudando CP para {registrador_cp}')

    elif idInstrucao == 0x10 or idInstrucao == 0x20:
        registrador_cp = registrador_cp + 2
        if CPU_DEBUG: print(f'calcularProximaInstrucao: mudando CP para {registrador_cp}')

    elif idInstrucao == 0x50:
        registrador_cp = memoria.getValorMemoria(registrador_cp + 1)
        if CPU_DEBUG: print(f'calcularProximaInstrucao: mudando CP para {registrador_cp}')

    elif idInstrucao == 0x79:
        if flag_zero:
            registrador_cp = memoria.getValorMemoria(registrador_cp + 1)
        else:
            registrador_cp = registrador_cp + 2
        if CPU_DEBUG: print(f'calcularProximaInstrucao: mudando CP para {registrador_cp}')


def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] \
            AX[{registrador_ax:02X}]  \
            BX[{registrador_bx:02X}]  \
            CX[{registrador_cx:02X}]  \
            DX[{registrador_dx:02X}]  \
            ZF[{flag_zero}] ')


if __name__ == '__main__':
    while (True):
        idInstrucao = buscarEDecodificarInstrucao()

        if idInstrucao == -1:
            break

        lerOperadoresExecutarInstrucao(idInstrucao)

        dumpRegistradores()

        calcularProximaInstrucao(idInstrucao)

        sys.stdin.read(1)