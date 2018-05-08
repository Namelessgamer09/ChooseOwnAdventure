
start = input("Type 'Start'")
if start == "Start": 

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
						print("You assassinate the king. The end.")
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
				
			elif choicea == "Harad":
				print("You decide to venture into the desert land of Harad.")
				
		elif choice == "Flee":
			print("///////////////////////////////////")
			print("You decide to make a run for it.")
			print("The nearby Mountains of Shadow could provide a refuge, because the Gondorian soldiers would not dare to enter there.")
			print("Sadly, the soldiers are on horseback, and they easily catch up to you.")
			print("'By orders of the King, you are under arrest on crimes of high treason!' ordered the chief guard.")
		elif choice == "Bribe":
			print("///////////////////////////////////")
			print("'Bribery is considered a federal offense, sir.")
			print("*sounds of getting tased*")
		
		
		

