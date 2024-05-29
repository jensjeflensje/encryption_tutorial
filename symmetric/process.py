from cryptography.fernet import Fernet

KEY = b"6Zd4bw9wEqnUAg5d2xHthq5yvdaUyY-dz_MNgRYrybc="

f = Fernet(KEY)
encrypted = f.encrypt(b"Mijn geheime wachtwoord")
print("Encrypted:", encrypted)
print("Decrypted:", f.decrypt(encrypted))
