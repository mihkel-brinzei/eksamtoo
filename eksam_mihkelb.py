# Mihkel Brinzei, IS23

import math # Impordib math mooduli

class cal():      # Pea klass "cal"                      
    def __init__(self, a, b):   #alg meetod, kus a ja b on välja toodud          
        self.a = a  #klassi a võrdub a, kutsutakse a'na
        self.b = b  #klassi b võrdub b, kutsutakse lihtsalt b'na

    def liitmine(self):       # liitmise meetod         
        return self.a + self.b  #tagastab a ja b muutuja väärtused, kui nad on liidetud
    
    def lahutamine(self):     # lahutamise meetod          
        return self.a - self.b  #tagastab a ja b muutuja väärtused, kui nad on lahutatud
    
    def korrutamine(self):       # korrutamise meetod
        return self.a * self.b  # tagastab a ja b muutuja väärtused, kui nad on korrutatud
    
    def jagamine(self):  #jagamise meetod
        if b != 0:  #kui b ei ole null, siis . . .
            return self.a / self.b  #tagasta muutuja a ja b väärtuse, kui nad on jagatud
        else: # muul juhul
            print("Jagatis on null, proovige uuesti!") # Väljastab print käsu kasutajale, et programm ei saa töödata. Lisafunktsioon 1.
    
    def jaak(self):           # jäägi meetod          
        return self.a % self.b  # tagastab a ja b muutuja väärtuse jäägi, mis tekib jagamisel
    
    def ruutjuur(self):       # ruutjuure meetod      
        return math.sqrt(a)  #programm on muudetud, et see võtaks ainult muutuja a väärtuse arvutusse. Lisafunktsioon 2.
    
    def keskmine(self): # keskmise meetod
        return kalk.liitmine() / 2 # programm arvutab kahe arvu keskmist niimodi, et kasutab liitmis meetodi ja jagab kahega, sest on ainult kaks arvu.
    # Lisafunktsioon 3.
        
        
    
a = int(input("Sisesta esimene number: "))  # kasutaja sisestus muutuja a jaoks        
b = int(input("Sisesta teine number: "))  # kasutaja sisestus muutuja b jaoks

kalk = cal(a,b)  # kalk muutuja on klass lühend, kus on veel muutujad a ja b lisatud.

while True:  # seni kuni on tõsi, tee
    def menu():  # menüü meetod (valikud)
        # kommentaar lisatud siia, sest muutuja on pikk. Muutujas on defineeritud stringina valikute jada, kus \n#, teeb uue rea ja lisab järjekorra sinna.
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine.(NB! Võtab aind esimese arvu)\n7. Keskmise arvutamine\n8. Restart ')
        print(x) # Väljastab suure teksti jada.
    menu() #kutsub meetodi, et konsoolis oleks näha seda.
    
    valik = int(input('Sisesta üks valikutest: ')) #küsib kasutajalt kasutaja sisestust.
    if valik == 1: #kui valik on 1 siis
        print("Vastus: ",kalk.liitmine()) #väljasta vastus, ja meetodi return väärtus, igas kehtib kalk muutuja välja kutsumine.
        break #peatab while tsükli.
    
    elif valik == 2: # kui valik on 2 siis
        print("Vastus: ",kalk.lahutamine()) #väljasta vastus, ja meetodi return väärtus
        break # peatab while tsükli
    
    elif valik == 3: # kui valik on 3 siis
        print("Vastus: ",kalk.korrutamine()) #väljasta vastus, ja meetodi return väärtus
        break #peatab while tsükli
    
    elif valik == 4: # kui valik on 4 siis
        print("Vastus: ",kalk.jagamine()) #väljasta vastus, ja meetodi return väärtus
        break #peatab while tsükli
    
    elif valik == 5: # kui valik on 5 siis
        print("Vastus: ",kalk.jaak()) #väljasta vastus, ja meetodi return väärtus
        break #peatab while tsükli
    
    elif valik == 6: # kui valik on 6 siis
        print("Vastus: ",kalk.ruutjuur()) #väljasta vastus, ja meetodi return väärtus
        break #peatab while tsükli
    
    elif valik == 7: # Kui valik on 7 siis
        print("Vastus: ", kalk.keskmine()) # väljasta vastus, ja meetodi return väärtus
        break #peatab while tsükli
    
    else: # muul juhul
        input("Programm sulgeb, vajutage 'Enter', et alustada uuesti") # küsib kasutajalt sisestust, aga käseb vajutada Enter nuppu, et lõpetaks koodi täielikult
        break #peatab while tsükli
        
        



