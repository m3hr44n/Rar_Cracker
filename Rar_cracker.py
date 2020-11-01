import rarfile
import os , sys


print("""       
               Rar File Cracker

              Coded By : m3hr44n

            https://github.com/m3hr44n

                   Version 1.1
""")

def test_password(fn,password):
    try:
        rar = rarfile.RarFile(fn)
        try:
           rar.extractall(pwd=password)
           return 1
        except:
            return -1
    except:
        return 0

filename = input("Please Insert Your Rar File ==> :")
pass_list = input("Please Insert Your PasswordList ==> :")
if not os.path.isfile(filename):
    print("Not Found {}".format(filename))
    sys.exit()

if not os.path.isfile(pass_list):
    print("not Found {}".format(pass_list))
    sys.exit()
f = open(pass_list,"r")
for p in f:
    rp=p.strip().replace('\r\n','').replace('\n','')
    st = test_password(filename,rp)
    if st ==1:
        print("[+] Password Found : {}".format(rp))
        sys.exit()
    elif st ==-1:
        print("[-] Not Found {}".format(rp))
    else:
        print("premission Denaig Or Not Found")
        sys.exit()
