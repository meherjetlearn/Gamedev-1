
import hashlib

print("the availabe algos")
print(hashlib.algorithms_available)
from hashlib import sha256
text='Jetlearn'
hash_result=hashlib.sha256(text.encode())

print("hexadecima equivalent of sha256")
print(hash_result.hexdigest())


#ask learners to import diiferent kind of hashalgo





