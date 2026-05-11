# CPU Architecture & Memory Simulator

## 📌 Overview
This project is a low-level computer architecture simulator built entirely in Python. It simulates the core execution cycle of a Central Processing Unit (CPU) including a Control Unit, an Arithmetic Logic Unit (ALU), and Cache Memory. Additionally, it includes algorithms for Virtual Memory Mapping (Direct and Associative mapping). 

## 🚀 Key Features

* **Custom Instruction Set Architecture (ISA):** Simulates opcodes for basic assembly-like instructions such as `ADD`, `SUB`, `MOV`, `JMP`, `CMP`, and `JZ`.
* **Register Management:** Implements general-purpose and control registers including `CP` (Program Counter), `AX`, `BX`, `CX`, and `DX`.
* **Instruction Execution Cycle:** Full implementation of the classic Fetch-Decode-Execute cycle (`buscarEDecodificarInstrucao`, `calcularProximaInstrucao`, `lerOperadoresExecutarInstrucao`).
* **Virtual Memory Algorithms:** Contains distinct modules demonstrating how Direct Mapping (`MapeamentoDireto.py`) and Associative Mapping (`MapeamentoAssociativo.py`) handle memory addresses and cache hits/misses.

## 🛠️ Technologies
* **Language:** Python 3.x
* **Core Concepts:** Computer Architecture, Virtual Memory Management, CPU Execution Cycles.

## ⚙️ How to Run

1. Clone this repository:
```bash
git clone https://github.com/gabamaral13/cpu-memory-architecture-sim.git
```

2. Navigate to the project directory:
```bash
cd cpu-memory-architecture-sim
```

3. Run the desired simulation (example for the CPU module):
```bash
python main.py
```
