import pandas as pd
import subprocess
import time
from datetime import datetime
from hashlib import sha256
""" 
m modulo 
a multiplicador
c incremento
X0 valor inicial
X valor
xn+1 = (axn + c) mod m
"""
class prandom():
        def __init__(self,valorInicial = 3, mod = 600 ,incrementador = 10,multiplicador = 7 ,veces=1):    
            self.valorInicial = valorInicial #valor  inicial para ir aumentandolo y disminuyendo
            self.mod = mod # tambien se pude usar como valor maximo
            self.incrementador = incrementador
            self.multiplicador = multiplicador
            self.veces = veces #veces para que salgan numeros "aleatorios" o tamaño del la lista 
            self.array = []
            self.valor=  self.valorInicial 
        def vector(self):
                self.contador = 0
                while self.veces > self.contador :#and self.valor < self.mod :
                    self.valor = (self.multiplicador * self.valor + self.incrementador) % self.mod
                    self.contador += 1
                    self.array.append(int(self.valor))    
                return self.array
        def digito(self):
            self.digito = (self.multiplicador * self.valor + self.incrementador) % self.mod
            return self.digito
        def help(self):
                print("PSEUDORANDOM \n formula \n m modulo \n a multiplicador \n c incremento \n X0 valor inicial \n X valor \n xn+1 = (axn + c) mod m")
                print("\n \n m>0 \n m>a>0 \n m>c>0")
                print("random(valorInicial = 3, mod = 600 ,incrementador = 10,multiplicador = 7 ,veces=1)")        


class gpgforall():
    cols = [[],[],[]]
    collectionschars = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'+-*/._=9876543210<>" 
    rows = {"password":cols[0],"encodepassword":cols[1],"reminder":cols[2]}
    now = int(datetime.now().strftime('%S'))
    if now !=0:
        for i in range(now):
            pr = prandom(valorInicial = now,incrementador=now+now,multiplicador =now*now,veces = int(20191231%now))
    diyrand = pr.vector()
    diyrand = diyrand[len(pr.vector())//2]
    print("\n rembember the key",diyrand,"\n")
    def help(self):
        print("""
                
                *if you don't know no press enter read 
                
                user id looks like '0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F'
                
                columns {"password":self.cols[0],"encodepassword":self.cols[1],"reminder":self.cols[2]}
                
                gpg4a.cols[2].append()reminder
                gpg4a.cols[1].append()encodepassword
                gpg4a.cols[0].append()password
                
                *comand used list 
               
                self.open = "gpg"+" -o "+out+" --decrypt "+self.file
                self.file = "passwords.csv"
                self.createcsv = "touch " + self.file
                self.list = " gpg --list-keys"
                self.genkey = "gpg --full-generate-key"
                self.encript = "gpg -e "+self.file
                self.row1 = {"password":[],"encodepassword":[],"reminder":[]}
                self.delet = "rm "+self.file
                self.start = time.time()
                
                ==combinations==
                
                *create and delete
                
                gpg4a.report(file)
                gpg4a.deletreport(1,file)
                
                *time to open a file
                
                time.sleep(1)
                gpg4a.openreport(file)
                gpg4a.deletreport(15,file)

                """)
    
    def cifrar(self,text,key = diyrand, chares=collectionschars):
        self.chars = str(chares)
        self.key = int(key)
        print("\n rembember the key",self.key,"\n")
        self.cifrar = ""
        self.text = str(text)
        for self.char in self.text:
                self.num = self.chars.find(self.char ) + self.key
                self.mod = int(self.num) % len(self.chars)
                self.cifrar = self.cifrar + (self.chars[self.mod])
        #self.cifrar = self.cifrar
        return  str(self.cifrar),self.key 
    def descifrar(self,text,key = diyrand,chares=collectionschars):#"ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'+-*/._=9876543210<>ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσ/ςΤτΥυΦφΧχΨψΩω'"):
        self.chars = str(chares)
        self.key = int(key)
        print("\n rembember the key",self.key,"\n")
        self.descifrar = ""
        self.text = str(text)
        for self.char in self.text:
                self.num = self.chars.find(self.char ) - self.key
                self.mod = int(self.num) % len(self.chars)
                self.descifrar = self.descifrar + str(self.chars[self.mod])
        return str(self.descifrar),self.key 
    def report(self,file):
        self.file = file
        self.file = self.file+".csv"
        self.createcsv = "touch " + self.file
        self.list = " gpg --list-keys"
        self.genkey = "gpg --full-generate-key"
        self.encript = "gpg -e "+self.file
        self.row  = self.rows

        #subprocess.run(self.createcsv,shell=1)
        f = pd.DataFrame(self.row)
        print(f)
        f.to_csv(self.file)
        try:
            subprocess.run(self.list,shell=1)
            subprocess.run(self.encript,shell=1)
        except:
            print("you dont have installed gpg")
    def deletreport(self,times,file):
        self.file = file
        self.file = self.file+".csv"
        self.times = times
        self.delet = "rm "+self.file
        time.sleep(self.times)
        subprocess.run(self.delet,shell=1)
    def openreport(self,file):
        self.file = file
        self.file = self.file+".csv.gpg"
        self.out = self.file.replace(".gpg","")
        self.open = "gpg"+" -o "+self.out+" --decrypt "+self.file
        subprocess.run(self.open,shell=1)
    def encryption(self,file):
        self.file = file
        self.encript = "gpg -e "+self.file
        self.list = " gpg --list-keys"
        subprocess.run(self.list,shell=1)
        subprocess.run(self.encript,shell=1)
    def decrypt(self,file):
        self.file = file
        self.file = self.file+".gpg"
        self.out = self.file.replace(".gpg","")
        self.decrypt = "gpg"+" -o "+out+" --decrypt "+self.file
        self.list = " gpg --list-keys"
        subprocess.run(self.list,shell=1)
        subprocess.run(self.decrypt,shell=1)
    def sha256aplay(self,password):
        self.password = password
        self.enpassword = str(sha256(self.password.encode('utf-8')).hexdigest())
        return self.enpassword
