import re
import dns.resolver
import socket
import smtplib

def ve(enm):
    # checks syntax of email address
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', enm)
    if match == None: #checks if email address is none
        pass
    else: #checks if email address is not none
        try:
            l = enm.split("@")[1]
            print(l) #print domain of email address
            records = dns.resolver.query(l, 'MX')
            mxRecord = records[0].exchange
            mxRecord = str(mxRecord)

            host = socket.gethostname()
          
            server = smtplib.SMTP()
            server.set_debuglevel(0)

            server.connect(mxRecord)
            server.helo(host)
            server.mail('iserver.tech01@gmail.com')
            code, message = server.rcpt(str(enm))
            server.quit()
            if code == 250: #if email address is valid
                #write email on valid.txt file
                file1 = open("valid.txt", "a") 
                file1.write(enm+ "\n") 
                file1.close() 
                print('Success')
            else: #if email address is not valid
                 #write email on invalid.txt file
                 file2 = open("invalid.txt", "a")
                 file2.write(enm + "\n")
                 file2.close()
                 print('Bad')
        except:
             #write email on invalid.txt file
            file2 = open("invalid.txt", "a")
            file2.write(enm + "\n")
            file2.close()
            print('Bad')

li = []
if __name__ == "__main__":
    with open('email.txt') as f: #open txt file in which all emails to be verified are written 
        lines = f.readlines()
    for x in range(len(lines)):
        lis = lines[x].split('\n')[0]
        li.append(lis)
    for x in range(len(li)):
        ve(li[x])
