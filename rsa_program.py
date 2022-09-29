import hashlib
import rsa  # pobrana biblioteka rsa

(pubkey, privkey) = rsa.newkeys(512)    # Stworzenie klucza prywatnego i publicznego

message = "Text to decode".encode('utf-8')  # Wiadomosc na wejscie

signature = rsa.sign(message, privkey, "SHA-1")     # Podpisanie kluczem prywatnym

hash = rsa.compute_hash(message, 'SHA-1')           # Za hashowanie

signature = rsa.sign_hash(hash, privkey, 'SHA-1')       

print(rsa.verify(message, signature, pubkey))       # Wyswietlenie "SHA-1"

print(message.decode('utf8'))       # Wyswietlenie wiadomosci podanej na wejscie po rozszyfrowaniu