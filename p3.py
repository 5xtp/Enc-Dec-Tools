import base64
import random
import os
import sys

# Master keys
_key42 = b"X9#mK2$vL5@nQ8&wR3!pT6*jY1^hF4%uI7+eA0~bC"
_key49 = b"zX9#mK2$vL5@nQ8&wR3!pT6*jY1^hF4%uI7+eA0~bCdGsNoP"
_shift = 47

def _xor(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def _caesar(s, shift):
    return "".join(chr((ord(c) + shift) % 65536) for c in s)

def _uncaesar(s, shift):
    return "".join(chr((ord(c) - shift) % 65536) for c in s)

def encode(text):
    s1 = _caesar(text, _shift).encode("utf-8")
    s2 = _xor(s1, _key42)
    s3 = _xor(s2, _key49)
    return base64.b85encode(s3).decode("ascii")

def decode(encoded):
    s1 = base64.b85decode(encoded.encode("ascii"))
    s2 = _xor(s1, _key49)
    s3 = _xor(s2, _key42)
    return _uncaesar(s3.decode("utf-8"), _shift)

def _login():
    print("\n[1] login  [2] guest  [3] exit")
    choice = input("> ").strip()
    if choice == "3":
        sys.exit(0)
    if choice == "1":
        u = input("user: ").strip()
        p = input("pass: ").strip()
        if u == "5xtp" and p == "Alex*roast73":
            print("hello creator")
            return True
    return False

def run_encode():
    print("\na = multiline text (double Enter to finish)")
    print("b = single line")
    typ = input("> ").strip().lower()

    if typ == "a":
        print("Type text. Press Enter twice when done:")
        lines = []
        while True:
            line = input()
            if line == "" and len(lines) > 0 and lines[-1] == "":
                break
            lines.append(line)
        text = "\n".join(lines[:-1]) if len(lines) > 1 else ""
    elif typ == "b":
        text = input("text: ").strip()
    else:
        print("Invalid option")
        return

    if not text:
        print("No text entered")
        return

    print("\n[e] standard encode")
    print("[n] encode with new key")
    mode = input("> ").strip().lower()

    result = encode(text)
    print("\n=== Encoded ===")
    print(result)
    print("================\n")

    if mode == "n":
        print("Random key system not fully implemented yet - use master key to decode")

def run_decode():
    print("\na = paste encoded text")
    print("b = from file")
    typ = input("> ").strip().lower()

    if typ == "a":
        encoded = input("paste encoded text: ").strip()
    elif typ == "b":
        fp = input("filename: ").strip()
        if not os.path.exists(fp):
            print("File not found")
            return
        with open(fp, "r", encoding="utf-8") as f:
            encoded = f.read().strip()
    else:
        print("Invalid option")
        return

    if not encoded:
        print("No encoded text")
        return

    result = decode(encoded)
    print("\n=== Decoded ===")
    print(result)
    print("================\n")

# Main flow
is_admin = _login()

while True:
    if is_admin:
        print("\n[1] encode  [2] decode  [3] exit")
    else:
        print("\n[1] encode  [2] decode  [3] exit")
    choice = input("> ").strip()

    if choice == "1":
        run_encode()
    elif choice == "2":
        run_decode()
    elif choice == "3":
        sys.exit(0)
    else:
        print("Invalid choice")
