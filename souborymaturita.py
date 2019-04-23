#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:18:34 2019

@author: lov35174
"""

#1-tolower(), cyklus + testovat jednotlive znaky  ord('A')..znak..ord('Z')
#2-replace(), cyklus + test jednotlivych znaku
#3-pomoci slovníkku + pridavat vyskyty
#4-pomocny retezec:"bcd...z" "aeiouy"



def prevod():
    try:
        vstJmeno = input("Zadej jméno vstupního souboru: ")
        vstSoubor = open(vstJmeno, "r")
        vystJmeno = input("Zadej jméno výstupního souboru: ")
        vystSoubor = open(vystJmeno,"w")
        while True:
            radek = vstSoubor.readline()
            if radek == '':
                break
            vystSoubor.write(radek.upper())
            vystSoubor.write(radek.lower())
        vstSoubor.close()
        vystSoubor.close()
        print("\n!!!HOTOVO!!!\n")
    except IOError:
        print("\n ERROR ---> Chyba při zadávání ! ! !")

def nahrad():
    try:
        vstJmeno = input("Zadej jméno vstupního souboru: ")
        vstSoubor = open(vstJmeno, "r")
        vystJmeno = input("Zadej jméno výstupního souboru: ")
        vystSoubor = open(vystJmeno,"w")
        znakStary = input("Zadej znak, který se má nahradit: ")
        znakNovy = input("Zadej znak, kterým se má starý znak nahradit: ")
        while True:
            radek = vstSoubor.readline()
            if radek == '':
                break
            vystSoubor.write(radek.replace(znakStary,znakNovy))
        vstSoubor.close()
        vystSoubor.close()
        print("\n!!!HOTOVO!!!\n")
    except IOError:
        print("\n ERROR ---> Chyba při zadávání ! ! !")
        
def statistika():
    pocetRadku = 0
    pocetZnaku = 0
    pocetSlov = 0
    cetnostZnaku={}
    vstJmeno = input("Zadej jméno vstupního souboru: ")
    vstSoubor = open(vstJmeno, "r")    
    while True:
        radek=vstSoubor.readline()
        if radek == '':  
            break     
        pocetRadku = pocetRadku + 1
        delka=len(radek)
        pocetZnaku += delka         
        pocetSlov += len(radek.split())
        for znak in radek:  
            if znak in (' ','\t', '\n' ):
                continue   
            if znak in cetnostZnaku:
                cetnostZnaku[znak] += 1
            else:
                cetnostZnaku[znak] = 1          
    
    print("----  četnosti znaků    -------------")
    for item in cetnostZnaku.items():print("{}\t{}".format(*item))
    print("-------------------------------------")
    print("počet řádků:", pocetRadku)
    print("počet slov:", pocetSlov)
    print("počet znaků:", pocetZnaku)
    print("-------------------------------------")
        
def nahodny_text(pocet_slov):
    import random
    def slovo():
        SAMOHLASKY = 'aeiouy'
        SOUHLASKY = 'qwrtzpsdfghjklxcvbnm'
        pocet_pismen = random.randint(2, 8)
        zacatek = random.randint(False, True)
        vystup = ''
        for i in range(pocet_pismen):
            if zacatek:
                vystup += random.choice(SOUHLASKY)
            else:
                vystup += random.choice(SAMOHLASKY)
            zacatek = not(zacatek)
        return vystup
            
    vysledek = tuple()
    for i in range(pocet_slov):
        vysledek += (slovo(),)
    return ' '.join(vysledek)
    
        

while True:
    print("1) Převod na malá písmena")
    print("2) Nahrazení znaků")
    print("3) Statistika souboru ")
    print("4) Generování náhodného textu")
    print("5) Konec")
    try:
        volba = int(input("1-5> "))
        if volba == 1:
            prevod()
        elif volba == 2: 
            nahrad()
        elif volba == 3: 
            statistika()
        elif volba == 4:
            pocet_slov=int(input("Zadej počet slov: "))
            print("\n",nahodny_text(pocet_slov),"\n")
        elif volba == 5: 
            exit(0)
        else:
            print("\n>>>> Zadej číslo od 1 do 5\n")
    except ValueError: 
        print("\n>>>> Zadej číslo od 1 do 5\n")
    except EOFError: 
        exit(0)        