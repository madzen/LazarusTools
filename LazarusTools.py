##################################################################
# LazarusTools.py
# Copyright (c) 2009 Lazarus
# Some Rights Reserved.
##################################################################

import __main__
Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

from __main__ import Character

###############################################################################
# Utility Functions
###############################################################################

def lazHelp():
	print "          -= Lazarus Tools =-"
	print ""
	print "lazMoney(amount): Gives <amount> of money"
	print "lazBlood(): Get 5x Elder Vitae"
	print "lazKeyring(): Gives all keys"
	print ""
	print "lazMaxStats(): Maxes out all stats"
	print "lazMaxDisciplines(): Maxes out all disciplines"
	print ""
	print "lazOpen(): Unlocks nearest locked door or container"
	print "lazClose(): Tried to Lock nearest door or container"
	print "lazHack(): Lists passwords for nearest hackable computer"
	print "lazEasyHack(): Reset difficulty of nearest computer to 1"
	print "lazEasyLock(): Reset difficulty of nearest lock to 1"
	print ""
	print "lazKill(): Kills nearest NPC"
	print "lazWipe(): Erases nearest NPC (not the same as killing them!)"
	print "lazFeed(): Seduces nearest NPC and feeds (no masquerade violation)"
	print ""
	print "lazSparkle(entity): Makes entity sparkle"
	print "lazHint(prefix): Makes all entities of class sparkle"


def lazDist(p1, p2):
    xDistance = (p1[0] - p2[0]) * (p1[0] - p2[0])
    yDistance = (p1[1] - p2[1]) * (p1[1] - p2[1])
    zDistance = (p1[2] - p2[2]) * (p1[2] - p2[2])
    return (xDistance + yDistance + zDistance)

def lazNearest(itemList):
	lazPlayerLoc = __main__.FindPlayer().GetOrigin()
	closeDist = 99999
	closeName = ""
	closeItem = ""
	for item in itemList:
		if (item.classname == "item_container_lock"):
			itemParent = Find(item.parentname)
			itemLoc = itemParent.GetOrigin()
		else:
			itemLoc = item.GetOrigin()
		itemDist = lazDist(lazPlayerLoc, itemLoc)
		try: 
			print "Item ", item.GetName()
			print "Dist ", itemDist
		except: print "Error"
		if (itemDist < closeDist):
			try: cName = item.GetName()
			except: cName = "dummy"
			if (cName != "dummy"):
				if (len(cName) > 0):
					closeName = cName
					closeDist = itemDist
					closeItem = item
	print "Closest named is ", closeName
	return closeItem

def lazFindLocks():
	locks = FindClass("item_container_lock")
	doors = FindClass("func_door")
	for lock in doors:
		locks.append(lock)
	rdoors = FindClass("func_door_rotating")
	for lock in rdoors:
		locks.append(lock)
	doorknobs = FindClass("prop_doorknob*")
	for lock in doorknobs:
		locks.append(lock)
	padlocks = FindClass("prop_padlock")
	for lock in padlocks:
		locks.append(lock)
	switches = FindClass("prop_switch")
	for lock in switches:
		locks.append(lock)
	buttons = FindClass("func_button")
	for lock in buttons:
		locks.append(lock)
	elevators = FindClass("func_elevator")
	for lock in elevators:
		locks.append(lock)
	return locks
	
def lazShowInst(prefix="npc_V"):                                  
	entities = __main__.FindEntitiesByClass(prefix+"*")             
	print "Class                                  Name"             
	print "--------------------------------------------------------"
	for ent in entities:                                            
		name=""                                                     
		try: name=ent.GetName()                                     
		except: pass                                                
		if name != "":                                              
			print "%s %s" % (ent.classname.ljust(35),ent.GetName())

				
###############################################################################
# NPC Related Functions
###############################################################################

def lazWipe():
	wipeList = FindClass("npc_V*")
	victim = lazNearest(wipeList)
	if (victim.GetName() != "Caine"):
		try: victim.Kill()
		except: print "Unable to remove victim"
		
def lazKill():
	killList = FindClass("npc_V*")
	victim = lazNearest(killList)
	if (victim.GetName() != "Caine"):
		vHealth = victim.health
		try: 
			victim.Faint()
			victim.TakeDamage(vHealth)
		except: 
			print "Unable to kill victim"
		
def lazFeed():
	feedList = FindClass("npc_V*")
	victim = lazNearest(feedList)
	pc = __main__.FindPlayer()
	if (victim.GetName() != "Caine"):
		try: pc.SeductiveFeed(victim)
		except: print "Unable to feed on victim"


###############################################################################
# Player Item Related Functions
###############################################################################

def lazMoney(amount=1000):
	pc = __main__.FindPlayer()
	pc.MoneyAdd(amount)

def lazBlood():
	pc = __main__.FindPlayer()
	pc.GiveItem("item_g_eldervitaepack")
	pc.GiveAmmo("item_g_eldervitaepack",4)

def lazKeyring():
	itemList = ("item_k_ash_cell_key", "item_k_carson_apartment_key", "item_k_chinese_theatre_key", "item_k_clinic_cs_key",
				"item_k_clinic_maintenance_key", "item_k_clinic_stairs_key", "item_k_edane_key", "item_k_empire_jezebel_key",
				"item_k_empire_mafia_key", "item_k_fu_cell_key", "item_k_fu_office_key", "item_k_gallery_noir_key",
				"item_k_gimble_key", "item_k_hannahs_safe_key", "item_k_kiki_key", "item_k_leopold_int_key", "item_k_lilly_key",
				"item_k_lucky_star_murder_key", "item_k_malcolm_office_key", "item_k_malkavian_refrigerator_key", "item_k_murietta_key",
				"item_k_museum_basement_key", "item_k_museum_office_key", "item_k_museum_storage_key", "item_k_museum_storeroom_key",
				"item_k_netcafe_office_key", "item_k_oceanhouse_basement_key", "item_k_oceanhouse_sewer_key", 
				"item_k_oceanhouse_upstairs_key", "item_k_oh_front_key", "item_k_shrekhub_four_key", "item_k_shrekhub_one_key",
				"item_k_shrekhub_three_key", "item_k_skyline_haven_key", "item_k_tatoo_parlor_key", "item_k_tawni_apartment_key",
				"item_k_tutorial_chopshop_stairs_key")
	pc = __main__.FindPlayer()
	for item in itemList:
		pc.GiveItem(item)


###############################################################################
# Player Stats Related Functions
###############################################################################

def lazMaxStats():
	statList = ("strength", "dexterity", "stamina", "charisma", "manipulation", "appearance", "perception", "intelligence", "wits",
				"brawl", "dodge", "intimidation", "subterfuge", "firearms", "melee", "security", "stealth", "computer", "finance",
				"investigation", "academics")
	pc = __main__.FindPlayer()
	for stat in statList:
		pc.BumpStat(stat, 10)
		
def lazMaxDisciplines():
	discList = ("animalism", "auspex", "celerity", "dementation", "dominate", "fortitude", "obfuscate", "potence", "presence",
				"protean", "thaumaturgy")
	pc = __main__.FindPlayer()
	for disc in discList:
		if getattr(pc, disc) != -1:
			pc.BumpStat(disc, 10)

def lazBuff():
	#Blood Buff only MASSIVE buff
	print "WIP"
	

###############################################################################
# Lock / Hacking Related Functions
###############################################################################

def lazOpen():
	locks = lazFindLocks()
	lock = lazNearest(locks)
	try: 
		lock.Unlock()
		lock.Open()
		lock.Close()
	except: pass
	
def lazClose(): 
	locks = lazFindLocks()
	lock = lazNearest(locks)
	try: 
		lock.Close()
		lock.Lock()
	except: pass

def lazEasyHack():
	computers = FindClass("prop_hack*")
	comp = lazNearest(computers)
	try:
		comp.ResetDifficulty(1)
		print "Hacking difficulty reset to ", comp.GetName()
	except:
		print "Unable to reset hacking difficulty"
		
def lazEasyLock():
	locks = lazFindLocks()
	lock = lazNearest(locks)
	try:
		lock.ResetDifficulty(1)
		print "Lock difficulty reset to ", lock.GetName()
	except:
		print "Unable to reset lock difficulty"	

def lazHack():
	uname = ""
	upass = ""
	computers = FindClass("prop_hack*")
	comp = lazNearest(computers)
	try: 
		hackvar = comp.hack_file
		hackdata = "%s%s" % ("Vampire/",hackvar)
		hackfile = open(hackdata,"r")
		print " "
		print "Passwords for ", comp.GetName()
		print "============================"
		print "Section".ljust(25),"Password"
		print "============================"
		while hackfile:
			line = hackfile.readline()
			if not line:
				break
			if line.find("email_password")  >= 0:
				epass = line.split("\"")[3]
				print "Email".ljust(25), epass
			if line.find("\"name\"") >= 0:
				uname = line.split("\"")[3]
			if line.find("\"password\"") >= 0:
				upass = line.split("\"")[3]
			if uname != "" and upass != "":
				print uname.ljust(25), " ", upass
				uname = ""
				upass = ""
		hackfile.close()
	except: 
		print "Unable to open data file"
	

###############################################################################
# World Related Functions
###############################################################################

def lazHint(prefix="item_"):
	sList = FindClass(prefix+"*")
	for item in sList:
		try: lazSparkle(item)
		except: pass
		
def lazSparkle(item):
	lazPlayerLoc = __main__.FindPlayer().GetOrigin()
	point = item.GetOrigin()
	name = item.GetName()
	itemDist = lazDist(lazPlayerLoc, itemLoc)
	if (itemDist > 0):
		try: 
			lazLook = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0))
			lazLook.SetParent(item)
			__main__.CallEntitySpawn(lazLook)
		except: 
			print "Unable to spawn entity"