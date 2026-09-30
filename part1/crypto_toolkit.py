import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def sec(t):
    print("\n" + "=" * 45 + f"\n {t} \n" + "=" * 45)

sec("1. MA HOA VA GIAI MA AES-128-CBC")
plain = "Thuc hanh Cryptography - Nhom 6".encode('utf-8')
k, iv = get_random_bytes(16), get_random_bytes(16)
print(f"[*] Ban ro : {plain.decode('utf-8')}")
c_enc = AES.new(k, AES.MODE_CBC, iv)
cipher = c_enc.encrypt(pad(plain, AES.block_size))
print(f"[+] Ban ma : {cipher.hex()}")

c_dec = AES.new(k, AES.MODE_CBC, iv)
dec = unpad(c_dec.decrypt(cipher), AES.block_size)
print(f"[+] Giai ma: {dec.decode('utf-8')}")
assert plain == dec
print("[V] Xac minh: Giai ma khop 100%!")

sec("2. HAM BAM MAT MA (MD5, SHA-1, SHA-256)")
msg = "Lab 5 Cryptography Nhom 6".encode('utf-8')
print(f"Input: {msg.decode('utf-8')}")
print(f"MD5    : {hashlib.md5(msg).hexdigest()}")
print(f"SHA-1  : {hashlib.sha1(msg).hexdigest()}")
print(f"SHA-256: {hashlib.sha256(msg).hexdigest()}")

sec("3. HIEU UNG TUYET LO (AVALANCHE EFFECT)")
m1, m2 = "Nhom 6 Test A".encode('utf-8'), "Nhom 6 Test B".encode('utf-8')
print(f"Input 1: {m1.decode()} -> Hash: {hashlib.sha256(m1).hexdigest()}")
print(f"Input 2: {m2.decode()} -> Hash: {hashlib.sha256(m2).hexdigest()}")
