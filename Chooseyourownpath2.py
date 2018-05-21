
start = input("Type 'Start'")
if start == "Start" or "start": 

		name = input("Make the name for your character.")
		print("//////////////////////////////////////")
		print("After a successful heist in Minas Tirith, you have gone to hide in the ruins of Osgiliath.")
		print("The prize was nothing more than King Aragorn\'s crown.")
		print("Upon the realization his prized crown was gone, he sent out a search party in order to find the heirloom, and punish the thief.")
		print("After a quick overlook of Pelennor Fields, you see the search party drawing closer.")
		print("What will you choose to do? Stay in Osgiliath and hide, flee to the Mountains of Shadow, or attempt to bribe the soldiers for your life?")
		print("Type 'Hide' for option one, 'Flee' for option two, and the 'Bribe' for option three.")
		choice = input("The time to decide is now.")
		if choice == "Hide":
			print ("You have chosen to hide within the city ruins.")
			print("////////////////////////////////////////")
			print ("The search party diligently roamed the decrepit capital, and after no luck of finding you they leave.")
			print ("After the soldiers do not return, you have some ideas as to where you could cash in your prize.")
			print("Two choices come to mind, either travel to the distant land of Harad, or try your luck with the enraged orcs.")
			print("Both suffered greatly during the war, and would love to take a stab at Gondor.")
			print("Now, do you wish to bargain with the orcs, or risk your life to get to Harad and bargain with their people?")
			print("Type 'Harad' to go to Harad, or type 'Orcs' to go to Cirith Ungol.")
			choicea = input("Where will you go for the gold?")
			if choicea == "Orcs": #This choice leads to Cirith Ungol
				print("The quest for Cirith Ungol has been decided.")
				print("////////////////////////////////////")
				print("You make your way to the edge of Mordor, which is surrounded by ominous mountains.")
				print("A large boulder begins to tumble down the mountain path you started to climb.")
				print("You press yourself against the side of the mountain to evade the massive rock, and manage to glimpse the person who threw the boulder.")
				print("The uruk addresses you, but you can not understand the rough dark language he speaks to you.")
				print("The language is black speech, a tongue that all of Sauron\'s followers speak.")
				print("Upon seeing the 30 shades of stupid on your face, he begins to speak in common tongue for you to understand.")
				print("He then spoke more clearly, saying 'I will tear off your arms you filthy shrakh if you don\'t tell me what you\'re doing in my mountain!'")
				print(" You then say to uruk 'Who do you think you are to threaten me so violently?'")
				print("The uruk responded as such, 'I am Khrash, Flesh Ripper they call me! I am the warchief of this land!'")
				print("'Be that as it may,' you retort, 'I am %s, the master thief, and I have come to bargain.'" %(name))
				print("Intrigued by your boldness, Khrash restrains you and leads to Cirith Ungol.")
				print("'What have you to offer us that we should trade with man-swine?' asked Khrash.")
				print("With an arrogant smirk, you reveal the crown to the horde of uruks.")
				print("'I will take nothing short of gold for such a prize!' you barter.")
				print("The uruks erupted in laughter.")
				print("'We have no gold fool! We have a poison dagger and a cloak of darkness. Choose one and we will trade,' said Khrash.")
				print("Type 'Poison' for the dagger, or 'Darkness' for the cloak.")
				choiceb = input("What piece of equipment will you choose?")
				if choiceb == "Darkness":  #You receive the Cloak of Darkness
					print("////////////////////////////////////")
					print("'Give me the cloak, and then I will give you the crown,' you negotiate.")
					print("In the end, you both decide to trade at the same time.")
					print("With the cloak, revenge upon the king will be easier.")
					print("In order to get to Minas Tirith, will you pass through Pelennor Fields, or go around the fields and try to enter the city from the side?")
					print("Type 'Fields' for Pelennor Fields, or 'Side' to travel around Pelennor Fields.")
					choicec = input("What course of action will you take?")
			
					if choicec == "Fields":
						print("You travel through the fields and encounter an earth troll.")
						print("Its primordial language is impossible to decipher, but its intentions are clear.")
						print("You evade the troll and make it to the gates of Minas Tirith. It is night time.")
						
					elif choicec == "Side":
						print("///////////////////////////////")
						print("You decide to travel around the fields and try to climp the side of the city's walls.")
						print("No one noticed your shadow-like body heave itself over the wall.")
						print("The magic cloak made you seem like an apparition.")
						print("Your new ability allows you to sneak into the King's chamber's.")
						print("You stab him.")
						print("The End.")
				elif choiceb == "Poison":
					print("Khrash trades you a poisonous dagger for the crown.")
					print("'Tis a fair trade,' said Khrash, 'now get out of my site!'")
					print("You raise the dagger in triumph, and then bring it down into Khrash's abdomen.")
					
			elif choicea == "Harad":
				print("///////////////////////////////////////")
				print("You decide to venture into the desert land of Harad.")
				print("The scorched dunes ravaged your face as the grains of sand burned your skin.")
				print("A journey such as this has never been so arduous.")
				print("The quest for Harad lasted for a daunting five minutes.")
				
		elif choice == "Flee":
			print("///////////////////////////////////")
			print("You decide to make a run for it.")
			print("The nearby Mountains of Shadow could provide a refuge, because the Gondorian soldiers would not dare to enter there.")
			print("Sadly, the soldiers are on horseback, and they easily catch up to you.")
			print("'By orders of the King, you are under arrest on crimes of high treason!' ordered the chief guard.")
		elif choice == "Bribe":
			print("///////////////////////////////////")
			print("They mercilessly beat you for having the gall to bribe them, and you go unconscious")
			print("You are now at the royal prison in Minas Tirith, and have been stripped of everything you own, and have been given tattered, and rough prison robes.")
			print("You hear the guard in front of your cell speak when you begin to get up")
			print("'Don\'t get too comfy scum, you\'re punishment will be at hand'")
			print("Your body still aches from the smackdown you were so kindly handed earlier, so you decide to move to the bed and continue to rest.")
			print("You awake during the night and look around your cell for something.... and you notice some things on the floor...")
			print("A file? Impossible, but yet there it was,l along with... a buzzsaw? Those shouldn't even exist! (Don\'t ask how your character knows modern tools)")
			print("What will you take? Type 'File' to select the file or type 'Bzzzz' for the super fun buzzsaw")
			choicerid = input("Choose now baby!")
			if choicerid == "Bzzzz":
				print("/////////////////////////////////")
				print("You pick up the buzzsaw and begin to cut the bars away with sparks flying around")
				print("A guard hears the ridiculously loud sounds you are creating and runs to your cell.")
				print("He then exclaims in fear,'What is that?!', to which you reply by removing the last bar you need to free yourself and punch the man right in the jaw for a knockout.")
				print("You run with the buzzsaw in hnad, revving it up to scare other guards away from wretched screech of the saw"	)
				print("After running through the keep, you find a glowing white sword in the midst of the armory. 'Nobody took it already?' You say to yourself")
				print("You hold the sword in your hands and the mighty powers of Exaclibur onfolds!... into a small white creure with large eyes, a top hat, and a cane.")
				print("'Fool!' you hear from the creature that formed from the sword.")
				print("What will you choose to do? Try to grab him by the foot and use him as a sword (Type 'Foot'? or will you punt the weird creature away?'Punt'")
				choicewhy = input ("What will you do?")
				if choicewhy == "Punt":
					print("You punt the little thing across the room, but with the amount of time it took to make your decision, a guard came up behind you and stabbed you through the chest, killing you instantly.")
					print("You win the sweet and warm embrace of Lady Death herself")
				elif choicewhy == "Foot":
					print("You force Excaliber back into becoming the holy blade, and you slay everyone in the keep for your freedom.")
					print(" You then escape into the Kings quarters in Minas Tirith to obtain your vengance")
					print("You burst through the door into the King's room with the mighty blade in hand")
					print("He begs, pleading for his life 'please, please don\'t kill me! I\'ll do anything!'")
					print("What shall you do you murderous manic?! Kill the poor man (Type 'End') or will you toture him in front of his kingdom? (Type 'Suffer')")
					choicefin =("Decide the fate of this fool")
					if choicefin = "End":
						print("You hold the sword high into the air and the force of the gods, lightning and fire, begin to engulf the mighty blade")
						print("'No, no!', exclaimed the king, but before anything else could slip out of his mouth, the single swift strike of the sword silenced him for good")
						print("Not only have you slain the King, but now the entire kingdom of Minas Tirith bows before you and your undying might")
						print("You take the seat at the throne room with confidence and arrogance surging through you")
						print("The new king %s is here to stay" %(name))
					elif choicefin = "Suffer":
						print("The mighty blade excalibur morphs back into the little white creature")
						print("The little thing points to the king, and exclaims 'Fool!'")
						print("You leave to take your new place at the throne, while the small excalibur proceeds to torture the past king with all of his rules of being wielded, all 9,999,999,991 of them")
						print("The now deposed king sits in the king's quarters for the rest of your forced ruling of the kingdom, and had been driven to complete insanity only two days in.")
						print("Your rule is even more empowering than you had expected, going on military campaigns, slaying insurrections against your rule, and the filth who tried to capture")
						print("Victory in life is yours")
			
		
		
		

