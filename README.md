# Benchmark-Performance-Analysis-of-Raspberry-Pi-Pico-Boards
This document provides Benchmark and Performance Analysis of Raspberry Pi Pico Boards
## Introduction:
An analysis of experimental results comparing the execution performance of Fibonacci number calculations, as a part of benchmarking across various Raspberry Pi Pico boards is carried out in this work. The resuts focus on ARM Cortex-M0, ARM Cortex-M33 and RISC-V cores, as implemented in the RP2040 (Raspberry Pi Pico and Raspberry Pi Pico W) and RP2350 (Raspberry Pi Pico 2) microcontrollers. Experiments are carried out using the recent MicroPython firmwares loaded in appropriate boards: [Ref](https://micropython.org/download) (screen shots given below). program is developed in MicroPython using Thonny editor. 
<p align="center"><img src="https://github.com/user-attachments/assets/1750ef81-776e-45c7-aa66-76af4cd54c31"width="300"height="450">
   <img src="https://github.com/user-attachments/assets/b57b37a3-8f42-4834-bdcd-c48f5c8e1652"width="300"height="450"></p>

Motivational Website(s):[Ref](https://forums.raspberrypi.com/viewtopic.php?t=377831), and also number of YouTube presentations.
Software developed in the present work, in the form of Python code is given in the repository. Experimental results obtained in the form of tables are given below. Videos corresponding to the experimental work are also given below.
<p align="center"><img src="https://github.com/user-attachments/assets/f5986410-cb63-4328-8ffa-96ab8e03170f"width="350"height="650">
    <img src="https://github.com/user-attachments/assets/f0e3bca3-2b6c-4b49-8c23-911ee7097721"width="350"height="650"></p>


## Analysis and Insights:
> ### Performance of Raspberry Pi Pico RP2040 and Raspberry Pi Pico W RP2040
The Raspberry Pi Pico outperforms the Raspberry Pi Pico W consistently. At 250MHz, Pico RP2040(ARM Cortex-M0) takes an execution time of 0.892816s, while the Pico W takes 1.137592s, making the Pico W approximately 1.27 times slower. This may be due to the additional overhead on the CPU due to the Wireless and BlueTooth interface hardware. At125 MHz, the Pico completes Fibonaccci computation in 1.785616s versus Pico W's 2.27556s, maitaining the same performance gap.
> ### Performance of Raspberry Pi Pico 2 RP2350 (ARM Cortex-M33 and RISC-V Hazard3) 
As for as Fibonacci computation is concerned, the ARM Cortex-M33 mode in Pico 2 is significantly faster than the RISC-V Hazard 3 mode:
At 250MHz, Cortex M-33 executes in 0.561120s, while RISC-V Hazard3 architecture takes 1.286060s, showing that the Cortex M-33 core is 2.29 times faster. At 125MHz, Cortex M-33 core completes the computation in 1.122360s, while RISC-V Hazard3 takes 2.2572735s, maintaining the same performance difference. however, other parameters that may affect include: Compiler optimization/ Code quality and optimization/ Memory heirarchy and access patterns/ Pipeline efficiency/ Specific use case and workload.
ARM Cortex M-33 features DSP Extensions for optimized mathematical calculations.
> ### Clock Speed Scaling
Across all tested boards and modes, execution time scales proportionally with clock speed. Halving the clock frequency results in approximately twice the execution time ( factor/scale ~2). This linear relationship aligns with theoretical expectations for CPU-bound workloads. 


