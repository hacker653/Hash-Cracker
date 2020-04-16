import hashlib

print("""  _    _           _                 _____                _             
 | |  | |         | |               / ____|              | |            
 | |__| | __ _ ___| |__    ______  | |     _ __ __ _  ___| | _____ _ __ 
 |  __  |/ _` / __| '_ \  |______| | |    | '__/ _` |/ __| |/ / _ \ '__|
 | |  | | (_| \__ \ | | |          | |____| | | (_| | (__|   <  __/ |   
 |_|  |_|\__,_|___/_| |_|           \_____|_|  \__,_|\___|_|\_\___|_|   
                                                                        
                                                                        """)                           

flag = 0

pass_hashes  = input ("Enter Hash: ")
wordlist = input ("Enter The Path of Password File: ")
print("."*50)

try:
    pass_file = open (wordlist, "r")
except:
    print("password file not found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()


    print(word)
    print(digest)
    print(pass_hashes)
    print("."*50)
    

    if digest == pass_hashes:

        

             print("[+]password found")
             print("[+]password is >>> " + word)
             flag = 1
             break

if flag == 0:
             print("password is not in the list:")
