# First program using cryptography lets fking go!

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify

#Now let's create a secret message to encrypt. 
message = b'I love cryptography!'

#Before we can encrypt we'll need a key pair. We'll first generate a private key, and then derive the public key from the private key. There are a number of different options for key generation here, but we'll go with a key length of 1024 bits.


private_key = RSA.generate(1024)
public_key = private_key.publickey()


#We can also print these objects out at this point to be sure they are what we are expecting, which is "class 'Crypto.PublicKey.RSA.RsaKey'". 

print(type(private_key), type(public_key))


#Now we'll convert our keys to strings, save them in.pem files and take a look at them. 
private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()


#Be sure that they are now strings. 
print(type(private_pem), type(public_pem))


#And save the strings to.pem files
with open('private.pem', 'w') as pr:
	pr.write(private_pem)
with open('public.pem', 'w') as pu:
	pu.write(public_pem)


#And print it out. 
print('private.pem:')
with open('private.pem', 'r') as f:
	print(f.read())

print('public.pem:')
with open('public.pem', 'r') as f:
        print(f.read())


#Now let's convert these key files back into RSA key objects, and do some encrypting. a

pr_key = RSA.import_key(open('private.pem', 'r').read())
pu_key = RSA.import_key(open('public.pem', 'r').read())


#And again, let's check on it. 

print(type(pr_key), type(pu_key))


#And now, the encryption! Remember data is encrypted with a public key and decrypted with the corresponding private key. 
cipher = PKCS1_OAEP.new(key=pu_key)
cipher_text = cipher.encrypt(message)


#And have a look.

print(cipher_text)


#We'll now use our private key to decrypt the message back to its original form. 

decrypt = PKCS1_OAEP.new(key=pr_key)
decrypted_message = decrypt.decrypt(cipher_text)

#And check if it worked!

print(decrypted_message)

#If you see your original message, congrats, you completed the first exercise. You're done!

print('Done')

