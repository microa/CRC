## CRC
There are many CRC codes available online that can be found. <br>
However, there are instances where they cannot be used or encounter compatibility issues with the hardware. <br>
Here, I'm providing my version for serial communication, specifically MODBUS with 485 physical links.<br>
A simple use case as follows:<br>
<br>
def main(): <br>
&nbsp;&nbsp;CRC(0x01, 0x05, 0x00, 0x01, 0xFF, 0x00)  # these 6 hex number is your protocal command
