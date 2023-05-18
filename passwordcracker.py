import hashlib



def conversion(type_of_hash,file_path,hash_to_decrypt):
    with open(file_path,'r') as file:
        for line in file.readlines():
            if type_of_hash == 'md5':
                hash_obj = hashlib.md5(line.strip().encode())
                hashed_word = hash_obj.hexdigest()
                if hashed_word == hash_to_decrypt:
                    print('Found MD5 Password : '+ line.strip())
                    exit(0)

            if type_of_hash == 'sha1':
                hash_obj = hashlib.sha1(line.strip().encode())
                hashed_word = hash_obj.hexdigest()
                if hashed_word == hash_to_decrypt:
                    print('Found sha1 Password : '+ line.strip())
                    exit(0)

        print('Password not in list')