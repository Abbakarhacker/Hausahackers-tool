## Hausahackers.py - Hausahackers v4.0
##
import os, sys
import readline
from time import sleep as timeout
from core.lzmcore import *

def main():
	banner()
	print("   [01] Information Gathering")
	print("   [02] Vulnerability Analysis")
	print("   [03] Web Hacking")
	print("   [04] Database Assessment")
	print("   [05] Password Attacks")
	print("   [06] Wireless Attacks")
	print("   [07] Reverse Engineering")
	print("   \033[1;94m[08] Exploitation Tools")
	print("   \033[1;97m[09] Sniffing and Spoofing")
	print("   \033[1;97m[10] Reporting Tools")
	print("   \033[1;97m[11] Forensic Tools")
	print("   \033[1;92m[12] Stress Testing")
	print("   \033[1;92m[13] Install Linux Distro")
	print("   \033[1;92m[14] Termux Utility")
	print("   \033[1;92m[15] Shell Function [.bashrc]")
	print("   \033[1;94m[16] Install CLI Games")
	print("   \033[1;91m[17] Malware Analysis")
	print("   \033[1;94m[18] Compiler/Interpreter")
	print("   \033[1;94m[19] Social Engineering Tools")
	print("\n   [99] Update the Hausahackers-tool ")
	print("   [00] Exit the Hausahackers-tool \n")
	lazymux = input("Hausahackers >>> ")

	# 01 - Information Gathering
	if lazymux.strip() == "1" or lazymux.strip() == "01":
		os.system("clear")
		os.system("figlet information Gathering")
		print("\n    [01] Nmap  ")
		print("     \033[1;93m[02] Red Hawk ")
		print("     \033[1;92m[03] D-TECT   ")
		print("     \033[1;93m[04] sqlmap ")
		print("     \033[1;94m[05] Infoga ")
		print("     \033[1;93m[06] ReconDog ")
		print("     \033[1;95m[07] AndroZenmap")
		print("     \033[1;96m[08] sqlmate ")
		print("     \033[1;97m[09] AstraNmap ")
		print("     \033[1;93m[10] MapEye ")
		print("     \033[1;92m[11] Easymap  ")
		print("     \033[1;96m[12] BlackBox  ")
		print("     \033[1;95m[13] XD3v ")
		print("     \033[1;91m[14] Crips ")
		print("     \033[1;93m[15] SIR ")
		print("     \033[1;97m[16] EvilURL ")
		print("     \033[1;94m[17] Striker ")
		print("     \033[1;92m[18] Xshell  ")
		print("     \033[1;93m[19] OWScan  ")
		print("     \033[1;95m[20] OSIF ")
		print("     \033[1;91m[21] Devploit ")
		print("     \033[1;93m[22] Namechk ")
		print("     \033[1;93m[23] AUXILE ")
		print("     \033[1;95m[24] inther ")
		print("     \033[1;95m[25] GINF  ")
		print("     \033[1;92m[26] GPS Tracking")
		print("     \033[1;92m[27] ASU ")
		print("     \033[1;93m[28] fim  ")
		print("     \033[1;93m[29] MaxSubdoFinder  ")
		print("     \033[1;94m[30] pwnedOrNot  ")
		print("     \033[1;94m[31] Mac-Lookup  ")
		print("     \033[1;95m[32] BillCipher ")
		print("     \033[1;95m[33] dnsrecon  ")
		print("     \033[1;93m[34] zphisher  ")
		print("     \033[1;93m[35] Mr.SIP  ")
		print("     \033[1;91m[36] Sherlock ")
		print("     \033[1;91m[37] userrecon ")
		print("     \033[1;93m[38] PhoneInfoga ")
		print("     \033[1;93m[39] SiteBroker ")
		print("     \033[1;96m[40] maigret ")
		print("     \033[1;96m[41] GatheTOOL ")
		print("     \033[1;93m[42] ADB-ToolKit")
		print("     \033[1;93m[43] TekDefense-Automater ")
		print("     \033[1;97m[44] EagleEye ")
		print("     \033[1;97m[45] EyeWitness ")
		print("     \033[1;93m[46] InSpy ")
		print("     \033[1;93m[47] Leaked ")
		print("     \033[1;93m[48] fierce ")
		print("     \033[1;93m[49] gasmask ")
		print("\n    [00] Back to main menu\n")
		infogathering = input("hausahackers >>>  ")
		if infogathering == "@":
			infogathering = ""
			for x in range(1,201):
				infogathering += f"{x} "
		if len(infogathering.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for infox in infogathering.split():
			if infox.strip() == "01" or infox.strip() == "1": nmap()
			elif infox.strip() == "02" or infox.strip() == "2": red_hawk()
			elif infox.strip() == "03" or infox.strip() == "3": dtect()
			elif infox.strip() == "04" or infox.strip() == "4": sqlmap()
			elif infox.strip() == "05" or infox.strip() == "5": infoga()
			elif infox.strip() == "06" or infox.strip() == "6": reconDog()
			elif infox.strip() == "07" or infox.strip() == "7": androZenmap()
			elif infox.strip() == "08" or infox.strip() == "8": sqlmate()
			elif infox.strip() == "09" or infox.strip() == "9": astraNmap()
			elif infox.strip() == "10": mapeye()
			elif infox.strip() == "11": easyMap()
			elif infox.strip() == "12": blackbox()
			elif infox.strip() == "13": xd3v()
			elif infox.strip() == "14": crips()
			elif infox.strip() == "15": sir()
			elif infox.strip() == "16": evilURL()
			elif infox.strip() == "17": striker()
			elif infox.strip() == "18": xshell()
			elif infox.strip() == "19": owscan()
			elif infox.strip() == "20": osif()
			elif infox.strip() == "21": devploit()
			elif infox.strip() == "22": namechk()
			elif infox.strip() == "23": auxile()
			elif infox.strip() == "24": inther()
			elif infox.strip() == "25": ginf()
			elif infox.strip() == "26": gpstr()
			elif infox.strip() == "27": asu()
			elif infox.strip() == "28": fim()
			elif infox.strip() == "29": maxsubdofinder()
			elif infox.strip() == "30": pwnedOrNot()
			elif infox.strip() == "31": maclook()
			elif infox.strip() == "32": billcypher()
			elif infox.strip() == "33": dnsrecon()
			elif infox.strip() == "34": zphisher()
			elif infox.strip() == "35": mrsip()
			elif infox.strip() == "36": sherlock()
			elif infox.strip() == "37": userrecon()
			elif infox.strip() == "38": phoneinfoga()
			elif infox.strip() == "39": sitebroker()
			elif infox.strip() == "40": maigret()
			elif infox.strip() == "41": gathetool()
			elif infox.strip() == "42": adbtk()
			elif infox.strip() == "43": tekdefense()
			elif infox.strip() == "44": eagleeye()
			elif infox.strip() == "45": eyewitness()
			elif infox.strip() == "46": inspy()
			elif infox.strip() == "47": leaked()
			elif infox.strip() == "48": fierce()
			elif infox.strip() == "49": gasmask()
			elif infox.strip() == "00" or infox.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 02 - Vulnerability Analysis
	elif lazymux.strip() == "2" or lazymux.strip() == "02":
		os.system("clear")
		os.system("figlet  Vulnerability Analysis")
		print("\n    [01] Nmap    ")
		print("   \033[1;93m[02] AndroZenmap")
		print("   \033[1;93m[03] AstraNmap   ")
		print("   \033[1;93m[04] Easymap    ")
		print("   \033[1;92m[05] Red Hawk    ")
		print("   \033[1;92m[06] D-TECT   ")
		print("   \033[1;92m[07] Damn Small SQLi Scanner    ")
		print("   \033[1;93m[08] SQLiv  ")
		print("   \033[1;93m[09] sqlmap   ")
		print("   \033[1;91m[10] sqlscan    ")
		print("   \033[1;91m[11] Wordpresscan   ")
		print("   \033[1;96m[12] WPScan    ")
		print("   \033[1;96m[13] sqlmate     ")
		print("   \033[1;96m[14] termux-wordpresscan")
		print("   \033[1;93m[15] TM-scanner    ")
		print("   \033[1;93m[16] Rang3r    ")
		print("   \033[1;95m[17] Striker ")
		print("   \033[1;95m[18] Routersploit:   ")
		print("   \033[1;95m[19] Xshell   ")
		print("   \033[1;93m[20] SH33LL    ")
		print("   \033[1;93m[21] BlackBox    ")
		print("   \033[1;94m[22] XAttacker     ")
		print("   \033[1;94m[23] OWScan    ")
		print("   \033[1;94m[24] XPL-SEARCH     ")
		print("   \033[1;93m[25] AndroBugs_Framework     ")
		print("   \033[1;93m[26] Clickjacking-Tester    ")
		print("    [27] Sn1per:      ")
		print("\n    [00] Back to main menu\n")
		vulnsys = input("hausahackers >>> ")
		if vulnsys == "@":
			vulnsys = ""
			for x in range(1,201):
				vulnsys += f"{x} "
		if len(vulnsys.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for vulnx in vulnsys.split():
			if vulnsys.strip() == "01" or vulnsys.strip() == "1": nmap()
			elif vulnsys.strip() == "02" or vulnsys.strip() == "2": androZenmap()
			elif vulnsys.strip() == "03" or vulnsys.strip() == "3": astraNmap()
			elif vulnsys.strip() == "04" or vulnsys.strip() == "4": easyMap()
			elif vulnsys.strip() == "05" or vulnsys.strip() == "5": red_hawk()
			elif vulnsys.strip() == "06" or vulnsys.strip() == "6": dtect()
			elif vulnsys.strip() == "07" or vulnsys.strip() == "7": dsss()
			elif vulnsys.strip() == "08" or vulnsys.strip() == "8": sqliv()
			elif vulnsys.strip() == "09" or vulnsys.strip() == "9": sqlmap()
			elif vulnsys.strip() == "10": sqlscan()
			elif vulnsys.strip() == "11": wordpreSScan()
			elif vulnsys.strip() == "12": wpscan()
			elif vulnsys.strip() == "13": sqlmate()
			elif vulnsys.strip() == "14": wordpresscan()
			elif vulnsys.strip() == "15": tmscanner()
			elif vulnsys.strip() == "16": rang3r()
			elif vulnsys.strip() == "17": striker()
			elif vulnsys.strip() == "18": routersploit()
			elif vulnsys.strip() == "19": xshell()
			elif vulnsys.strip() == "20": sh33ll()
			elif vulnsys.strip() == "21": blackbox()
			elif vulnsys.strip() == "22": xattacker()
			elif vulnsys.strip() == "23": owscan()
			elif vulnsys.strip() == "24": xplsearch()
			elif vulnsys.strip() == "25": androbugs()
			elif vulnsys.strip() == "26": clickjacking()
			elif vulnsys.strip() == "27": sn1per()
			elif vulnsys.strip() == "00" or vulnsys.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)

	# 03 - Web Hacking
	elif lazymux.strip() == "3" or lazymux.strip() == "03":
		os.system("clear")
		os.system("figlet  Web Hacking")
		print("\n    [01] sqlmap   ")
		print("    \033[1;93m[02] WebDAV   ")
		print("    \033[1;93m[03] MaxSubdoFinder   ")
		print("    \033[1;92m[04] Webdav   ")
		print("    \033[1;92m[05] Atlas  ")
		print("    \033[1;93m[06] sqldump   ")
		print("    \033[1;94m[07] Websploit  ")
		print("    \033[1;94m[08] sqlmate  ")
		print("    \033[1;92m[09] inther   ")
		print("    \033[1;93m[10] HPB  ")
		print("    \033[1;95m[11] Xshell   ")
		print("    \033[1;95m[12] SH33LL   ")
		print("    \033[1;91m[13] XAttacker   ")
		print("    \033[1;93m[14] XSStrike   ")
		print("    \033[1;96m[15] Breacher   ")
		print("    \033[1;96m[16] OWScan    ")
		print("    \033[1;96m[17] ko-dork   ")
		print("    \033[1;97m[18] ApSca   ")
		print("    \033[1;93m[19] amox   ")
		print("    \033[1;93m[20] FaDe   ")
		print("    \033[1;94m[21] AUXILE    ")
		print("    \033[1;94m[22] xss-payload-list    ")
		print("    \033[1;93m[23] Xadmin   ")
		print("    \033[1;93m[24] CMSeeK  ")
		print("    \033[1;92m[25] CMSmap  ")
		print("    \033[1;92m[26] CrawlBox    ")
		print("    \033[1;91m[27] LFISuite ")
		print("    \033[1;91m[28] Parsero  ")
		print("    \033[1;93m[29] Sn1per    ")
		print("    \033[1;93m[30] Sublist3r     ")
		print("    \033[1;96m[31] WP-plugin-scanner  ")
		print("    \033[1;96m[32] WhatWeb     ")
		print("    \033[1;96m[33] fuxploider    ")
		print("\n    [00] Back to main menu\n")
		webhack = input("hausahackers >>> ")
		if webhack == "@":
			webhack = ""
			for x in range(1,201):
				webhack += f"{x} "
		if len(webhack.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for webhx in webhack.split():
			if webhx.strip() == "01" or webhx.strip() == "1": sqlmap()
			elif webhx.strip() == "02" or webhx.strip() == "2": webdav()
			elif webhx.strip() == "03" or webhx.strip() == "3": maxsubdofinder()
			elif webhx.strip() == "04" or webhx.strip() == "4": webmassploit()
			elif webhx.strip() == "05" or webhx.strip() == "5": atlas()
			elif webhx.strip() == "06" or webhx.strip() == "6": sqldump()
			elif webhx.strip() == "07" or webhx.strip() == "7": websploit()
			elif webhx.strip() == "08" or webhx.strip() == "8": sqlmate()
			elif webhx.strip() == "09" or webhx.strip() == "9": inther()
			elif webhx.strip() == "10": hpb()
			elif webhx.strip() == "11": xshell()
			elif webhx.strip() == "12": sh33ll()
			elif webhx.strip() == "13": xattacker()
			elif webhx.strip() == "14": xsstrike()
			elif webhx.strip() == "15": breacher()
			elif webhx.strip() == "16": owscan()
			elif webhx.strip() == "17": kodork()
			elif webhx.strip() == "18": apsca()
			elif webhx.strip() == "19": amox()
			elif webhx.strip() == "20": fade()
			elif webhx.strip() == "21": auxile()
			elif webhx.strip() == "22": xss_payload_list()
			elif webhx.strip() == "23": xadmin()
			elif webhx.strip() == "24": cmseek()
			elif webhx.strip() == "25": cmsmap()
			elif webhx.strip() == "26": crawlbox()
			elif webhx.strip() == "27": lfisuite()
			elif webhx.strip() == "28": parsero()
			elif webhx.strip() == "29": sn1per()
			elif webhx.strip() == "30": sublist3r()
			elif webhx.strip() == "31": wppluginscanner()
			elif webhx.strip() == "32": whatweb()
			elif webhx.strip() == "33": fuxploider()
			elif webhx.strip() == "00" or webhx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 04 - Database Assessment
	elif lazymux.strip() == "4" or lazymux.strip() == "04":
		os.system("clear")
		os.system("figlet  database Assessment ")
		print("\n \033[1;97m  [01] DbDat   ")
		print("   \033[1;92m[02] sqlmap    ")
		print("   \033[1;93m[03] NoSQLMap   ")
		print("   \033[1;94m[04] audit_couchdb   ")
		print("   \033[1;91m[05] mongoaudit   ")
		print("\n    \033[1;95m[00] Back to main menu\n")
		dbssm = input("hausahackers >>> ")
		if dbssm == "@":
			dbssm = ""
			for x in range(1,201):
				dbssm += f"{x} "
		if len(dbssm.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for dbsx in dbssm.split():
			if dbsx.strip() == "01" or dbsx.strip() == "1": dbdat()
			elif dbsx.strip() == "02" or dbsx.strip() == "2": sqlmap()
			elif dbsx.strip() == "03" or dbsx.strip() == "3": nosqlmap
			elif dbsx.strip() == "04" or dbsx.strip() == "4": audit_couchdb()
			elif dbsx.strip() == "05" or dbsx.strip() == "5": mongoaudit()
			elif dbsx.strip() == "00" or dbsx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 05 - Password Attacks
	elif lazymux.strip() == "5" or lazymux.strip() == "05":
		os.system("clear")
		os.system("figlet  password Attacks ")
		print("\n    [01] Hydra    ")
		print("    \033[1;93m[02] FMBrute  ")
		print("   \033[1;95m[03] HashID    ")
		print("   \033[1;95m[04] Facebook Brute Force ")
		print("   \033[1;95m[05] Black Hydra   ")
		print("   \033[1;93m[06] Hash Buster ")
		print("   \033[1;93m[07] FBBrute   ")
		print("   \033[1;91m[08] Cupp    ")
		print("   \033[1;91m[09] InstaHack   ")
		print("   \033[1;91m[10] Indonesian Wordlist  ")
		print("   \033[1;92m[11] Xshell")
		print("   \033[1;92m[12] Aircrack-ng     ")
		print("   \033[1;92m[13] BlackBox:    ")
		print("   \033[1;93m[14] Katak    ")
		print("   \033[1;96m[15] Hasher  ")
		print("   \033[1;93m[16] Hash-Generator:      ")
		print("   \033[1;93m[17] nk26   ")
		print("   \033[1;97m[18] Hasherdotid:    ")
		print("   \033[1;97m[19] Crunch   ")
		print("   \033[1;97m[20] Hashcat    ")
		print("   \033[1;93m[21] ASU   ")
		print("   \033[1;93m[22] Credmap     ")
		print("   \033[1;93m[23] BruteX     ")
		print("   \033[1;96m[24] Gemail-Hack     ")
		print( "  \033[1;95m[25] GoblinWordGenerator:     ")
		print("   \033[1;94m[26] PyBozoCrack     ")
		print( "  \033[1;93m[27] brutespray    ")
		print("   \033[1;92m[28] crowbar    ")
		print("   \033[1;91m[29] elpscrk   ")
		print("    [30] fbht     ")
		print("\n    [00] Back to main menu\n")
		passtak = input("hausahackers >>> ")
		if passtak == "@":
			passtak = ""
			for x in range(1,201):
				passtak += f"{x} "
		if len(passtak.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for passx in passtak.split():
			if passx.strip() == "01" or passx.strip() == "1": hydra()
			elif passx.strip() == "02" or passx.strip() == "2": fmbrute()
			elif passx.strip() == "03" or passx.strip() == "3": hashid()
			elif passx.strip() == "04" or passx.strip() == "4": fbBrute()
			elif passx.strip() == "05" or passx.strip() == "5": black_hydra()
			elif passx.strip() == "06" or passx.strip() == "6": hash_buster()
			elif passx.strip() == "07" or passx.strip() == "7": fbbrutex()
			elif passx.strip() == "08" or passx.strip() == "8": cupp()
			elif passx.strip() == "09" or passx.strip() == "9": instaHack()
			elif passx.strip() == "10": indonesian_wordlist()
			elif passx.strip() == "11": xshell()
			elif passx.strip() == "12": aircrackng()
			elif passx.strip() == "13": blackbox()
			elif passx.strip() == "14": katak()
			elif passx.strip() == "15": hasher()
			elif passx.strip() == "16": hashgenerator()
			elif passx.strip() == "17": nk26()
			elif passx.strip() == "18": hasherdotid()
			elif passx.strip() == "19": crunch()
			elif passx.strip() == "20": hashcat()
			elif passx.strip() == "21": asu()
			elif passx.strip() == "22": credmap()
			elif passx.strip() == "23": brutex()
			elif passx.strip() == "24": gemailhack()
			elif passx.strip() == "25": goblinwordgenerator()
			elif passx.strip() == "26": pybozocrack()
			elif passx.strip() == "27": brutespray()
			elif passx.strip() == "28": crowbar()
			elif passx.strip() == "29": elpscrk()
			elif passx.strip() == "30": fbht()
			elif passx.strip() == "00" or passx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 06 - Wireless Attacks
	elif lazymux.strip() == "6" or lazymux.strip() == "06":
		os.system("clear")
		os.system("figlet  Wireless Attacks ")
		print("\n    [01] Aircrack-ng:   ")
		print("    \033[1;92m[02] Wifite:    ")
		print("    \033[1;93m[03] Wifiphisher:    ")
		print("    \033[1;94m[04] Routersploit:    ")
		print("    \033[1;95m[05] PwnSTAR:     ")
		print("    \033[1;96m[06] Pyrit:    ")
		print("\n    [00] Back to main menu\n")
		wiretak = input("hausahackers >>> ")
		if wiretak == "@":
			wiretak = ""
			for x in range(1,201):
				wiretak += f"{x} "
		if len(wiretak.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for wirex in wiretak.split():
			if wirex.strip() == "01" or wirex.strip() == "1": aircrackng()
			elif wirex.strip() == "02" or wirex.strip() == "2": wifite()
			elif wirex.strip() == "03" or wirex.strip() == "3": wifiphisher()
			elif wirex.strip() == "04" or wirex.strip() == "4": routersploit()
			elif wirex.strip() == "05" or wirex.strip() == "5": pwnstar()
			elif wirex.strip() == "06" or wirex.strip() == "6": pyrit()
			elif wirex.strip() == "00" or wirex.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 07 - Reverse Engineering
	elif lazymux.strip() == "7" or lazymux.strip() == "07":
		os.system("clear")
		os.system("figlet  Reverse Engineering")
		print("\n    [01] Binary Exploitation")
		print("   \033[1;93m[02] jadx   ")
		print("   \033[1;93m[03] apktool   ")
		print("   \033[1;94m[04] uncompyle6   ")
		print("   \033[1;95m[05] ddcrypt     ")
		print("   \033[1;96m[06] CFR     ")
		print("   \033[1;97m[07] UPX    ")
		print("   \033[1;96m[08] pyinstxtractor    ")
		print("   \033[1;96m[09] innoextract    ")
		print("   \033[1;91m[10] pycdc     ")
		print("   \033[1;91m[11] APKiD       ")
		print("   \033[1;93m[12] DTL-X      ")
		print("   \033[1;93m[13] APKLeaks       ")
		print("   \033[1;94m[14] apk-mitm       ")
		print("   \033[1;94m[15] ssl-pinning-remover      ")
		print("\n    [00] Back to main menu\n")
		reversi = input("Hausahackers >>>  ")
		if reversi == "@":
			reversi = ""
			for x in range(1,201):
				reversi += f"{x} "
		if len(reversi.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for revex in reversi.split():
			if revex.strip() == "01" or revex.strip() == "1": binploit()
			elif revex.strip() == "02" or revex.strip() == "2": jadx()
			elif revex.strip() == "03" or revex.strip() == "3": apktool()
			elif revex.strip() == "04" or revex.strip() == "4": uncompyle()
			elif revex.strip() == "05" or revex.strip() == "5": ddcrypt()
			elif revex.strip() == "06" or revex.strip() == "6": cfr()
			elif revex.strip() == "07" or revex.strip() == "7": upx()
			elif revex.strip() == "08" or revex.strip() == "8": pyinstxtractor()
			elif revex.strip() == "09" or revex.strip() == "9": innoextract()
			elif revex.strip() == "10": pycdc()
			elif revex.strip() == "11": apkid()
			elif revex.strip() == "12": dtlx()
			elif revex.strip() == "13": apkleaks()
			elif revex.strip() == "14": apkmitm()
			elif revex.strip() == "15": ssl_pinning_remover()
			elif revex.strip() == "00" or revex.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 08 - Exploitation Tools
	elif lazymux.strip() == "8" or lazymux.strip() == "08":
		os.system("clear")
		os.system("figlet  Exploitation Tools")
		print("\n    [01] Metasploit  ")
		print("    [02] commix   ")
		print("    [03] BlackBox   ")
		print("    [04] Brutal    ")
		print("    [05] TXTool      ")
		print("    [06] XAttacker     ")  
		print("    [07] Websploit    ")
		print("    [08] Routersploit      ")
		print("    [09] A-Rat     ")
		print("    [10] BAF   ")
		print("    [11] Gloom-Framework   ")
		print("    [12] Zerodoor   ")
		print("\n    [00] Back to main menu\n")
		exploitool = input("hausahackers >>>  ")
		if exploitool == "@":
			exploitool = ""
			for x in range(1,201):
				exploitool += f"{x} "
		if len(exploitool.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for explx in exploitool.split():
			if explx.strip() == "01" or explx.strip() == "1": metasploit()
			elif explx.strip() == "02" or explx.strip() == "2": commix()
			elif explx.strip() == "03" or explx.strip() == "3": blackbox()
			elif explx.strip() == "04" or explx.strip() == "4": brutal()
			elif explx.strip() == "05" or explx.strip() == "5": txtool()
			elif explx.strip() == "06" or explx.strip() == "6": xattacker()
			elif explx.strip() == "07" or explx.strip() == "7": websploit()
			elif explx.strip() == "08" or explx.strip() == "8": routersploit()
			elif explx.strip() == "09" or explx.strip() == "9": arat()
			elif explx.strip() == "10": baf()
			elif explx.strip() == "11": gloomframework()
			elif explx.strip() == "12": zerodoor()
			elif explx.strip() == "00" or explx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 09 - Sniffing and Spoofing
	elif lazymux.strip() == "9" or lazymux.strip() == "09":
		os.system("clear")
		os.system("figlet  Sniffing and Spoofing")
		print("\n    [01] KnockMail    ")
		print("    [02] tcpdump   ")
		print("    [03] Ettercap    ")
		print("    [04] hping3  ")
		print("    [05] tshark    ")
		print("\n    [00] Back to main menu\n")
		sspoof = input("hausahackers >>> ")
		if sspoof == "@":
			sspoof = ""
			for x in range(1,201):
				sspoof += f"{x} "
		if len(sspoof.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for sspx in sspoof.split():
			if sspx.strip() == "01" or sspx.strip() == "1": knockmail()
			elif sspx.strip() == "02" or sspx.strip() == "2": tcpdump()
			elif sspx.strip() == "03" or sspx.strip() == "3": ettercap()
			elif sspx.strip() == "04" or sspx.strip() == "4": hping3()
			elif sspx.strip() == "05" or sspx.strip() == "5": tshark()
			elif sspx.strip() == "00" or sspx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 10 - Reporting Tools
	elif lazymux.strip() == "10":
		os.system("clear")
		os.system("figlet    Reporting Tools")
		print("\n    [01] dos2unix   ")
		print("    [02] exiftool   ")
		print("    [03] iconv    ")
		print("    [04] mediainfo    ")
		print("    [05] pdfinfo   ")
		print("\n    [00] Back to main menu\n")
		reportls = input("hausahackers >>>  ")
		if reportls == "@":
			reportls = ""
			for x in range(1,201):
				reportls += f"{x} "
		if len(reportls.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for reportx in reportls.split():
			if reportx.strip() == "01" or reportx.strip() == "1": dos2unix()
			elif reportx.strip() == "02" or reportx.strip() == "2": exiftool()
			elif reportx.strip() == "03" or reportx.strip() == "3": iconv()
			elif reportx.strip() == "04" or reportx.strip() == "4": mediainfo()
			elif reportx.strip() == "05" or reportx.strip() == "5": pdfinfo()
			elif reportx.strip() == "00" or reportx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 11 - Forensic Tools
	elif lazymux.strip() == "11":
		os.system("clear")
		os.system("figlet Forensic Tools")
		print("\n    [01] steghide   ")
		print("    [02] tesseract   ")
		print("    [03] sleuthkit   ")
		print("    [04] CyberScan  ")
		print("    [05] binwalk  ")
		print("\n    [00] Back to main menu\n")
		forensc = input("hausahackers >>> ")
		if forensc == "@":
			forensc = ""
			for x in range(1,201):
				forensc += f"{x} "
		if len(forensc.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for forenx in forensc.split():
			if forenx.strip() == "01" or forenx.strip() == "1": steghide()
			elif forenx.strip() == "02" or forenx.strip() == "2": tesseract()
			elif forenx.strip() == "03" or forenx.strip() == "3": sleuthkit()
			elif forenx.strip() == "04" or forenx.strip() == "4": cyberscan()
			elif forenx.strip() == "05" or forenx.strip() == "5": binwalk()
			elif forenx.strip() == "00" or forenx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 12 - Stress Testing
	elif lazymux.strip() == "12":
		os.system("clear")
		os.system("figlet Stress Testing")
		print("\n    [01] Torshammer   ")
		print("    [02] Slowloris  ")
		print("    [03] Fl00d &   ")
		print("    [04] GoldenEye   ")
		print("    [05] Xerxes   ")
		print("    [06] Planetwork-DDOS")
		print("    [07] Xshell")
		print("    [08] santet-online   ")
		print("    [09] dost-attack   ")
		print("    [10] DHCPig   ")
		print("\n    [00] Back to main menu\n")
		stresstest = input("hausahackers >>>  ")
		if stresstest == "@":
			stresstest = ""
			for x in range(1,201):
				stresstest += f"{x} "
		if len(stresstest.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for stressx in stresstest.split():
			if stressx.strip() == "01" or stressx.strip() == "1": torshammer()
			elif stressx.strip() == "02" or stressx.strip() == "2": slowloris()
			elif stressx.strip() == "03" or stressx.strip() == "3": fl00d12()
			elif stressx.strip() == "04" or stressx.strip() == "4": goldeneye()
			elif stressx.strip() == "05" or stressx.strip() == "5": xerxes()
			elif stressx.strip() == "06" or stressx.strip() == "6": planetwork_ddos()
			elif stressx.strip() == "07" or stressx.strip() == "7": xshell()
			elif stressx.strip() == "08" or stressx.strip() == "8": sanlen()
			elif stressx.strip() == "09" or stressx.strip() == "9": dostattack()
			elif stressx.strip() == "10": dhcpig()
			elif stressx.strip() == "00" or stressx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 13 - Install Linux Distro
	elif lazymux.strip() == "13":
		os.system("clear")
		os.system("figlet  Install Linux Distro")
		print("\n    [01] Ubuntu  ")
		print("    [02] Fedora")
		print("    [03] Kali Nethunter")
		print("    [04] Parrot")
		print("    [05] Arch Linux")
		print("    [06] Alpine Linux   ")
		print("    [07] Debian    ")
		print("    [08] Manjaro AArch64")
		print("    [09] OpenSUSE    ")
		print("    [10] Void Linux")
		print("\n    [00] Back to main menu\n")
		innudis = input("hausahackers >>>  ")
		if innudis == "@":
			innudis = ""
			for x in range(1,201):
				innudis += f"{x} "
		if len(innudis.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for innux in innudis.split():
			if innux.strip() == "01" or innux.strip() == "1": ubuntu()
			elif innux.strip() == "02" or innux.strip() == "2": fedora()
			elif innux.strip() == "03" or innux.strip() == "3": nethunter()
			elif innux.strip() == "04" or innux.strip() == "4": parrot()
			elif innux.strip() == "05" or innux.strip() == "5": archlinux()
			elif innux.strip() == "06" or innux.strip() == "6": alpine()
			elif innux.strip() == "07" or innux.strip() == "7": debian()
			elif innux.strip() == "08" or innux.strip() == "8": manjaroArm64()
			elif innux.strip() == "09" or innux.strip() == "9": opensuse()
			elif innux.strip() == "10": voidLinux()
			elif innux.strip() == "00" or innux.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 14 - Termux Utility
	elif lazymux.strip() == "14":
		os.system("clear")
		os.system("figlet  Termux Utility")
		print("\n    [01] SpiderBot ")
		print("    [02] Ngrok  ")
		print("    [03] Sudo  ")
		print("    [04] google    ")
		print("    [05] kojawafft")
		print("    [06] ccgen   ")
		print("    [07] VCRT  ")
		print("    [08] E-Code  ")
		print("    [09] Termux-Styling")
		print("    [11] xl-p   ")
		print("    [12] BeanShell   ")
		print("    [13] vbug  ")
		print("    [14] Crunch    ")
		print("    [15] Textr  ")
		print("    [16] heroku   ")
		print("    [17] RShell   ")
		print("    [18] TermPyter   ")
		print("    [19] Numpy    ")
		print("    [20] BTC-to-IDR-checker    ")
		print("    [21] ClickBot ")
		print("\n    [00] Back to main menu\n")
		moretool = input("hausahackers >>> ")
		if moretool == "@":
			moretool = ""
			for x in range(1,201):
				moretool += f"{x} "
		if len(moretool.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for moret in moretool.split():
			if moret.strip() == "01" or moret.strip() == "1": spiderbot()
			elif moret.strip() == "02" or moret.strip() == "2": ngrok()
			elif moret.strip() == "03" or moret.strip() == "3": sudo()
			elif moret.strip() == "04" or moret.strip() == "4": google()
			elif moret.strip() == "05" or moret.strip() == "5": kojawafft()
			elif moret.strip() == "06" or moret.strip() == "6": ccgen()
			elif moret.strip() == "07" or moret.strip() == "7": vcrt()
			elif moret.strip() == "08" or moret.strip() == "8": ecode()
			elif moret.strip() == "09" or moret.strip() == "9": stylemux()
			elif moret.strip() == "10": passgencvar()
			elif moret.strip() == "11": xlPy()
			elif moret.strip() == "12": beanshell()
			elif moret.strip() == "13": vbug()
			elif moret.strip() == "14": crunch()
			elif moret.strip() == "15": textr()
			elif moret.strip() == "16": heroku()
			elif moret.strip() == "17": rshell()
			elif moret.strip() == "18": termpyter()
			elif moret.strip() == "19": numpy()
			elif moret.strip() == "20": btc2idr()
			elif moret.strip() == "21": clickbot()
			elif moret.strip() == "00" or moret.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 15 - Shell Function [.bashrc]
	elif lazymux.strip() == "15":
		os.system("clear")
		os.system("figlet  Shell Function ")
		print("\n    [01] FBVid   ")
		print("    [02] cast2video   ")
		print("    [03] iconset   ")
		print("    [04] readme  ")
		print("    [05] makedeb  ")
		print("    [06] quikfind   ")
		print("    [07] pranayama   ")
		print("    [08] sqlc ")
		print("\n    [00] Back to main menu\n")
		myshf = input("hausahackers >>> ")
		if myshf == "@":
			myshf = ""
			for x in range(1,201):
				myshf += f"{x} "
		if len(myshf.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for mysh in myshf.split():
			if mysh.strip() == "01" or mysh.strip() == "1": fbvid()
			elif mysh.strip() == "02" or mysh.strip() == "2": cast2video()
			elif mysh.strip() == "03" or mysh.strip() == "3": iconset()
			elif mysh.strip() == "04" or mysh.strip() == "4": readme()
			elif mysh.strip() == "05" or mysh.strip() == "5": makedeb()
			elif mysh.strip() == "06" or mysh.strip() == "6": quikfind()
			elif mysh.strip() == "07" or mysh.strip() == "7": pranayama()
			elif mysh.strip() == "08" or mysh.strip() == "8": sqlc()
			elif mysh.strip() == "00" or mysh.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 16 - Install CLI Games
	elif lazymux.strip() == "16":
		os.system("clear")
		os.system("figlet  Install CLI Games")
		print("\n    [01] Flappy Bird")
		print("    [02] Street Car")
		print("    [03] Speed Typing")
		print("    [04] NSnake  ")
		print("    [05] Moon buggy   ")
		print("    [06] Nudoku  ")
		print("    [07] tty-solitaire")
		print("    [08] Pacman4Console")
		print("\n    [00] Back to main menu\n")
		cligam = input("hausahackers >>> ")
		if cligam == "@":
			cligam = ""
			for x in range(1,201):
				cligam += f"{x} "
		if len(cligam.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for clig in cligam.split():
			if clig.strip() == "01" or clig.strip() == "1": flappy_bird()
			elif clig.strip() == "02" or clig.strip() == "2": street_car()
			elif clig.strip() == "03" or clig.strip() == "3": speed_typing()
			elif clig.strip() == "04" or clig.strip() == "4": nsnake()
			elif clig.strip() == "05" or clig.strip() == "5": moon_buggy()
			elif clig.strip() == "06" or clig.strip() == "6": nudoku()
			elif clig.strip() == "07" or clig.strip() == "7": ttysolitaire()
			elif clig.strip() == "08" or clig.strip() == "8": pacman4console()
			elif clig.strip() == "00" or clig.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 17 - Malware Analysis
	elif lazymux.strip() == "17":
		os.system("clear")
		os.system("figlet  Malware Analysis")
		print("\n    [01] Lynis  ")
		print("    [02] Chkrootkit    ")
		print("    [03] ClamAV    ")
		print("    [04] Yara    ")
		print("    [05] VirusTotal-CLI     ")
		print("    [06] H-Virus   ")
		print("    [07] avpass    ")
		print("    [08] DKMC    ")
		print("\n    [00] Back to main menu\n")
		malsys = input("hausahackers >>>  ")
		if malsys == "@":
			malsys = ""
			for x in range(1,201):
				malsys += f"{x} "
		if len(malsys.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for malx in malsys.split():
			if malx.strip() == "01" or malx.strip() == "1": lynis()
			elif malx.strip() == "02" or malx.strip() == "2": chkrootkit()
			elif malx.strip() == "03" or malx.strip() == "3": clamav()
			elif malx.strip() == "04" or malx.strip() == "4": yara()
			elif malx.strip() == "05" or malx.strip() == "5": virustotal()
			elif malx.strip() == "06" or malx.strip() == "6": hvirus()
			elif malx.strip() == "07" or malx.strip() == "7": avpass()
			elif malx.strip() == "08" or malx.strip() == "8": dkmc()
			elif malx.strip() == "00" or malx.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 18 - Compiler/Interpreter
	elif lazymux.strip() == "18":
		os.system("clear")
		os.system("figlet  Compiler/Interpreter ")
		print("\n    [01] Python2 ")
		print("    [02] ecj   ")
		print("    [03] Golang   ")
		print("    [04] ldc ")
		print("    [05] Nim    ")
		print("    [06] shc   ")
		print("    [07] TCC  ")
		print("    [08] PHP   ")
		print("    [09] Ruby    ")
		print("    [10] Perl     ")
		print("    [11] Vlang     ")
		print("    [12] BeanShell     ")
		print("    [13] fp-compiler    ")
		print("    [14] Octave    ")
		print("    [15] BlogC  ")
		print("    [16] Dart   ")
		print("    [17] Yasm   ")
		print("    [18] Nasm   ")
		print("\n    [00] Back to main menu\n")
		compter = input("hausahackers >>> ")
		if compter == "@":
			compter = ""
			for x in range(1,201):
				compter += f"{x} "
		if len(compter.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for compt in compter.split():
			if compt.strip() == "01" or compt.strip() == "1": python2()
			elif compt.strip() == "02" or compt.strip() == "2": ecj()
			elif compt.strip() == "03" or compt.strip() == "3": golang()
			elif compt.strip() == "04" or compt.strip() == "4": ldc()
			elif compt.strip() == "05" or compt.strip() == "5": nim()
			elif compt.strip() == "06" or compt.strip() == "6": shc()
			elif compt.strip() == "07" or compt.strip() == "7": tcc()
			elif compt.strip() == "08" or compt.strip() == "8": php()
			elif compt.strip() == "09" or compt.strip() == "9": ruby()
			elif compt.strip() == "10": perl()
			elif compt.strip() == "11": vlang()
			elif compt.strip() == "12": beanshell()
			elif compt.strip() == "13": fpcompiler()
			elif compt.strip() == "14": octave()
			elif compt.strip() == "15": blogc()
			elif compt.strip() == "16": dart()
			elif compt.strip() == "17": yasm()
			elif compt.strip() == "18": nasm()
			elif compt.strip() == "00" or compt.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	
	# 19 - Social Engineering Tools
	elif lazymux.strip() == "19":
		os.system("clear")
		os.system("figlet  Social Engineering Tools")
		print("\n    [01] weeman     ")
		print("    [02] SocialFish   ")
		print("    [03] santet-online   ")
		print("    [04] SpazSMS  ")
		print("    [05] LiteOTP   ")
		print("    [06] F4K3    ")
		print("    [07] Hac")
		print("    [08] Cookie-stealer     ")
		print("    [09] zphisher     ")
		print("    [10] Evilginx     ")
		print("    [11] ghost-phisher     ")
		print("\n    [00] Back to main menu\n")
		soceng = input("hausahackers >>> ")
		if soceng == "@":
			soceng = ""
			for x in range(1,201):
				soceng += f"{x} "
		if len(soceng.split()) > 1:
			writeStatus(1)
		else:
			writeStatus(0)
		for socng in soceng.split():
			if socng.strip() == "01" or socng.strip() == "1": weeman()
			elif socng.strip() == "02" or socng.strip() == "2": socfish()
			elif socng.strip() == "03" or socng.strip() == "3": sanlen()
			elif socng.strip() == "04" or socng.strip() == "4": spazsms()
			elif socng.strip() == "05" or socng.strip() == "5": liteotp()
			elif socng.strip() == "06" or socng.strip() == "6": f4k3()
			elif socng.strip() == "07" or socng.strip() == "7": hac()
			elif socng.strip() == "08" or socng.strip() == "8": cookiestealer()
			elif socng.strip() == "09" or socng.strip() == "9": zphisher()
			elif socng.strip() == "10": evilginx()
			elif socng.strip() == "11": ghostphisher()
			elif socng.strip() == "00" or socng.strip() == "0": restart_program()
			else: print("\nERROR: Wrong Input");timeout(1);restart_program()
		if readStatus():
			writeStatus(0)
	elif lazymux.strip() == "99":
		os.system("git pull")
	elif lazymux.strip() == "0" or lazymux.strip() == "00":
		sys.exit()
	
	else:
		print("\nERROR: Wrong Input")
		timeout(1)
		restart_program()

if __name__ == "__main__":
	os.system("clear")
	main()
