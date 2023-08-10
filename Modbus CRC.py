def crc16(data: str, poly: hex = 0xA001) -> str:
    '''
        CRC-16 MODBUS HASHING ALGORITHM
    '''
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = ((crc >> 1) ^ poly
                   if (crc & 0x0001)
                   else crc >> 1)

    hv = hex(crc).upper()[2:]
    blueprint = '0000'
    return (blueprint if len(hv) == 0 else blueprint[:-len(hv)] + hv)

def makeBytes(DID,FID,RIDH,RIDL,RVH,RVL):
    a = DID
    b = FID
    c = RIDH
    d = RIDL
    e = RVH
    f = RVL

    return bytes([a,b,c,d,e,f])

def CRC(DeviceID,FunctionID,RegIDH,RegIDL,RegValH,RegValL):
    CMDBytes = makeBytes(DeviceID,FunctionID,RegIDH,RegIDL,RegValH,RegValL)
    CRCResult = crc16(CMDBytes)

    print("CRC:",CRCResult)

    ts = int(CRCResult,16)
    L = ts & 0x00FF  # Low 8bit
    H = (ts & 0xFF00) >>8
    print (L)
    print (H)

    STR = bytearray(CMDBytes)

    STR.append(L)
    STR.append(H)

    return STR