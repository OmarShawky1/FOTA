
# Transmission registers
TXB0CTRL = 0x30
TXB1CTRL = 0x40
TXB2CTRL = 0x50

TXRTSCTRL = 0x0D

TXB0SIDH = 0x31
TXB1SIDH = 0x41
TXB2SIDH = 0x51

TXB0SIDL = 0x32
TXB1SIDL = 0x42
TXB2SIDL = 0x52

TXB0EID8 = 0x33
TXB1EID8 = 0x43
TXB0EID8 = 0x53

TXB0EID0 = 0x34
TXB1EID0 = 0x44
TXB2EID0 = 0x54

TXB0DLC = 0x35
TXB1DLC = 0x45
TXB2DLC = 0x55

TXB0D = 0x36
TXB1D = 0x46
TXB2D = 0x56

# receive registers

RXB0CTRL = 0x60

RXB1CTRL = 0x70

BFPCTRL = 0x0C

RXB0SIDH = 0x61
RXB1SIDH = 0x71

RXB0SIDL = 0x62
RXB1SIDL = 0x72

RXB0EID8 = 0x63
RXB1EID8 = 0x73

RXB0EID0 = 0x64
RXB1EID0 = 0x74

RXB0DLC = 0x65
RXB1DLC = 0x75

RXB0D0 = 0x66
RXB0D1 = 0x67
RXB0D2 = 0x68
RXB0D3 = 0x69
RXB0D4 = 0x6A
RXB0D5 = 0x6B
RXB0D6 = 0x6C
RXB0D7 = 0x6D

RXB1D = 0x76

# Filter Registers

RXF0SIDH = 0x00
RXF1SIDH = 0x04
RXF2SIDH = 0x08
RXF3SIDH = 0x10
RXF4SIDH = 0x14
RXF5SIDH = 0x18

RXF0SIDL = 0x01
RXF1SIDL = 0x05
RXF2SIDL = 0x09
RXF3SIDL = 0x11
RXF4SIDL = 0x15
RXF5SIDL = 0x19

RXF0EID8 = 0x02
RXF1EID8 = 0x06
RXF2EID8 = 0x0A
RXF3EID8 = 0x12
RXF4EID8 = 0x16
RXF5EID8 = 0x1A

RXF0EID0 = 0x03
RXF1EID0 = 0x07
RXF2EID0 = 0x0B
RXF3EID0 = 0x13
RXF4EID0 = 0x17
RXF5EID0 = 0x1B

#Mask Registers

RXM0SIDH = 0x20
RXM1SIDH = 0x24

RXM0SIDL = 0x21
RXM1SIDL = 0x25

RXM0EID8 = 0x22
RXM1EID8 = 0x26

RXM0EID0 = 0x23
RXM1EID0 = 0x27

# Configuration Registers

CNF1 = 0x2A
CNF2 = 0x29
CNF3 = 0x28

TEC = 0x1C
REC = 0x1D
EFLG = 0x2D
CANINTE = 0x2B
CANINTF = 0x2C
CANCTRL = 0x0F
CANSTAT = 0x0E
