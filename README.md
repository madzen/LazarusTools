LazarusTools Cheat Toolkit
==========================

This is an initial release of a collection of handy little cheat commands I
came up with many aeons ago for the game Vampire The Masquerade: Bloodlines. I
threw them together around 2009 with a first few tenative steps into Python and
they have been gathering digital dust ever since.

The commands include:

Inventory tools
---------------
* __lazMoney(amount)__: Gives <amount> of money
* __lazBlood()__: Get 5x Elder Vitae"
* __lazKeyring()__: Gives all keys"

Character Stat tools
--------------------
* __lazMaxStats()__: Maxes out all stats"
* __lazMaxDisciplines()__: Maxes out all disciplines"

Lock and Hack tools
-------------------
* __lazOpen()__: Unlocks nearest locked door or container"
* __lazClose()__: Tried to Lock nearest door or container"
* __lazHack()__: Lists passwords for nearest hackable computer"
* __lazEasyHack()__: Reset difficulty of nearest computer to 1"
* __lazEasyLock()__: Reset difficulty of nearest lock to 1"

NPC tools
---------
* __lazKill()__: Kills nearest NPC"
* __lazWipe()__: Erases nearest NPC (not the same as killing them!)"
* __lazFeed()__: Seduces nearest NPC and feeds (no masquerade violation)"

Misc tools
----------
* __lazSparkle(entity)__: Makes entity sparkle
* __lazHint(prefix)__: Makes all entities of class sparkle

The files can be added to the requisite directory in the Bloodlines directory
and the commands will become available in the console.

I am intending to reinstall VTM: Bloodlines in the near future and give these
tools a well-deserved rewrite, as I'm sure they can be improved with a few
Python best practices scattered around. At the time of last checking they were
fully functional however, so can be used by whoever is interested.