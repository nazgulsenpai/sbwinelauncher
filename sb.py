import os
code = ""
sbcmd = '/connetip:178.33.228.149 /connetport:10001 /clientauthcode:^ /clientauthid:25c883fec75407f3de4fa05330ac302c'
loggedIn = False

def login(username,password,code):
    cmd = 'curl -s -d "username='+ username + '&password=' + password + '&submit=login" --dump-header headers http://oauth.vendettagn.com/auth_login.php > response.txt'
    os.system(cmd)
    f = open('response.txt')
    contents = f.read()
    f.close()
    f = None
    if contents.find("ERROR:") == -1:
        temp1 = contents.split("&code=")[1]
        code = temp1.split("&state")[0]
        print("Login Success")
        return True, code
    else:
        print("Login Failed")
        return False, code

def launch(sbcmd,code):        
    print("Patching XignCode loader...")
    os.system('wget https://github.com/nazgulsenpai/sbxigncode/blob/master/Debug/x3.xem?raw=true')
    os.system('mv x3.xem?raw=true ./xigncode/x3.xem -f')
    f = open('sblaunch.sh','w')
    f.write('wine sb.exe ' + sbcmd.replace("^",code))
    f.close()
    f = None
    os.system("chmod +x sblaunch.sh")
    os.system("sblaunch.sh")
print("\nScarlet Blade Vendetta Linux Launcher\n")
print("---------------------------------------\n")
while loggedIn == False:
    try:
        loggedIn, code = login(sys.argv[1],sys.argv[2], code)
    except:
        loggedIn, code = login(input("Username: "), input("Password: "),code)
launch(sbcmd,code)
exit(0)