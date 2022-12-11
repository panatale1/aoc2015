from hashlib import md5

secret_key = 'bgvyzdsv'
five = False
six = False
i = 1
while i >= 1:
    hash_input = bytes(secret_key, 'utf-8') + bytes(str(i), 'utf-8')
    myhash = md5(hash_input)
    if not five and myhash.hexdigest().startswith('00000'):
        five = True
        print(i)
    if not six and myhash.hexdigest().startswith('000000'):
        print(i)
        break
    i += 1
