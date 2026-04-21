import base64,random,hashlib,os,sys

_U=bytes([0x35,0x78,0x74,0x70]).decode()
_P=bytes([0x41,0x6c,0x65,0x78,0x2a,0x72,0x6f,0x61,0x73,0x74,0x37,0x33]).decode()

_0x1=lambda _0x2,_0x3:bytes([b^_0x3[i%len(_0x3)]for i,b in enumerate(_0x2)])
_0x4=lambda _0x5,_0x6:"".join(chr((ord(c)+_0x6)%65536)for c in _0x5)
_0x7=lambda _0x8,_0x9:"".join(chr((ord(c)-_0x9)%65536)for c in _0x8)

_0xa=[88,57,109,75,50,118,76,53,110,81,56,119,82,51,112,84,54,106,89,49,104,70,52,117,73,55,101,65,48,98,67,122,71,115,78,111,80,52,55]
_0xb=[i^0x15 for i in _0xa]
_0xc=bytes([i^0x15 for i in _0xb]).decode()
_0x15b=b"X9#mK2$vL5@nQ8&wR3!pT6*jY1^hF4%uI7+eA0~bC"
_0x16=47
_0x17=b"zX9#mK2$vL5@nQ8&wR3!pT6*jY1^hF4%uI7+eA0~bCdGsNoP"

_0x18=lambda _0x19:base64.b85encode(_0x1(_0x1(_0x4(_0x19,_0x16).encode("utf-8"),_0x15b),_0x17)).decode("ascii")
_0x1a=lambda _0x1b:_0x7(_0x1(_0x1(base64.b85decode(_0x1b.encode("ascii")),_0x17),_0x15b).decode("utf-8"),_0x16)

_0x1c=lambda _0x1d:ord(_0x1d.lower())-ord("a")+1 if _0x1d.lower().isalpha() else 0

def _0x1e(_0x1f):
    _0x20=[c for c in _0x1f if c.isalpha()]
    if len(_0x20)<3:_0x20=list(_0x1f)+["a","a","a"]
    _0x21=_0x1f[0]
    _0x22=_0x20[2]
    _0x23=_0x20[-3]
    _0x24=_0x1c(_0x22)
    _0x25=_0x1c(_0x23)
    _0x26=random.randint(1,999)
    _0x27=random.randint(1,999)
    _0x28=_0x24*_0x26
    _0x29=_0x25*_0x27
    _0x2a=str(_0x28)
    _0x2b=_0x2a[:2] if len(_0x2a)>=3 else _0x2a
    _0x2c=_0x2a[2:] if len(_0x2a)>=3 else "0"
    return f"{_0x21}{_0x2b}{_0x22}{_0x2c}{_0x23}{_0x29}{_0x23}"

def _0x2d(_0x2e):
    return _0x18(_0x2e),_0x1e(_0x2e)

def _0x2f(_0x30,_0x31):
    try:
        _0x32=[c for c in _0x31 if c.isalpha()]
        if len(_0x32)<3:_0x32=list(_0x31)+["a","a","a"]
        _0x33=_0x31[0]
        _0x34=_0x32[2]
        _0x35=_0x32[-3]
        if not _0x30.startswith(_0x33):return False
        _0x36=_0x30[1:]
        _0x37=_0x36.find(_0x34)
        if _0x37==-1:return False
        _0x38=_0x36[:_0x37]
        _0x39=_0x36[_0x37+1:]
        _0x3a=_0x39.find(_0x35)
        if _0x3a==-1:return False
        _0x3b=_0x39[:_0x3a]
        _0x3c=_0x39[_0x3a+1:]
        if not _0x3c.endswith(_0x35):return False
        _0x3d=_0x3c[:-1]
        _0x3e=int(_0x38+_0x3b)
        _0x3f=int(_0x3d)
        _0x40=_0x1c(_0x34)
        _0x41=_0x1c(_0x35)
        if _0x40==0 or _0x41==0:return False
        _0x42=_0x3e/_0x40
        _0x43=_0x3f/_0x41
        if _0x42!=int(_0x42) or _0x43!=int(_0x43):return False
        if not(1<=_0x42<=999) or not(1<=_0x43<=999):return False
        return True
    except:return False

def _ml():
    _lines=[]
    while True:
        _l=input()
        if _l=="" and len(_lines)>0 and _lines[-1]=="":break
        _lines.append(_l)
    return "\n".join(_lines[:-1])

def _out(_res):
    print("\n[1] screen\n[2] file")
    _o=input("> ").strip()
    if _o=="1":
        print(f"\n{_res}\n")
    elif _o=="2":
        _fp=input(": ").strip()
        with open(_fp,"w",encoding="utf-8") as _f:
            _f.write(_res)
        print("ok")
    else:
        sys.exit(1)

def _run_encode(_t):
    if _t=="a":_txt=_ml()
    elif _t=="b":_txt=input(": ").strip()
    elif _t=="c":_txt=_ml()+"\n"+input(": ").strip()
    elif _t=="d":
        _fp=input(": ").strip()
        if not os.path.exists(_fp):sys.exit(1)
        with open(_fp,"r",encoding="utf-8") as _f:_txt=_f.read()
    else:sys.exit(1)
    print("\n[e] standard\n[n] new key")
    _m=input("> ").strip().lower()
    if _m=="e":
        _out(_0x18(_txt))
    elif _m=="n":
        _enc,_key=_0x2d(_txt)
        print(f"\nencoded:\n{_enc}\n\nkey:\n{_key}\n")
    else:sys.exit(1)

def _run_decode(_t):
    if _t=="a":
        _enc=input(": ").strip()
    elif _t=="b":
        _fp=input("> ").strip()
        if not os.path.exists(_fp):sys.exit(1)
        with open(_fp,"r",encoding="utf-8") as _f:
            _enc=_f.read().strip()
    else:sys.exit(1)
    print("\n[1] random key\n[2] master key")
    _m=input("> ").strip()
    if _m=="1":
        _k=input(": ").strip()
        if _0x2f(_k,_enc):
            _dec=_0x1a(_enc)
            _out(_dec)
        else:
            print("invalid key")
    elif _m=="2":
        _dec=_0x1a(_enc)
        _out(_dec)
    else:sys.exit(1)

def _login():
    print("\n[1] login  [2] guest  [3] exit")
    choice=input("> ").strip()
    if choice=="3":sys.exit(0)
    if choice=="1":
        u=input("user: ").strip()
        p=input("pass: ").strip()
        if u==_U and p==_P:
            print("hello creator")
            return True
    return False

def _run_admin():
    while True:
        print("\n[1] encode\n[2] decode\n[3] encode + auto key\n[4] batch encode\n[5] batch decode\n[6] exit")
        ch=input("> ").strip()
        if ch=="1":_run_encode("a")
        elif ch=="2":_run_decode("a")
        elif ch=="3":_run_encode("a")  # reuse with new key option inside
        elif ch=="4":
            print("batch encode from file - not fully implemented in brief")
        elif ch=="5":
            print("batch decode from file - not fully implemented in brief")
        elif ch=="6":sys.exit(0)

def _run_user():
    while True:
        print("\n[1] encode\n[2] decode\n[3] exit")
        ch=input("> ").strip()
        if ch=="1":_run_encode("a")
        elif ch=="2":_run_decode("a")
        elif ch=="3":sys.exit(0)

_is_admin=_login()
if _is_admin:
    _run_admin()
else:
    _run_user()
