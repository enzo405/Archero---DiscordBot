import discord

class Select(discord.ui.Select):
		def __init__(self):
				options=[
						discord.SelectOption(value="Option 0",label="Help Command",description="?help"),
						discord.SelectOption(value="Option 1",label="Calculateur de Stats",description="?stats_calc"),
						discord.SelectOption(value="Option 2",label="Bugs du jeux",description="?bug"),
						discord.SelectOption(value="Option 3",label="Le Glitch...",description="?glitch"),
						discord.SelectOption(value="Option 4",label="Arbre de Talents",description="?talent_tree"),
						discord.SelectOption(value="Option 5",label="Tableau des QuickRaid",description="?QR"),
						discord.SelectOption(value="Option 6",label="Toutes les TierLists",description="?all_tierlist"),
						discord.SelectOption(value="Option 7",label="Document des oeufs",description="?doc_oeufs"),
						discord.SelectOption(value="Option 8",label="Tuto installer une apk",description="?tuto_apk"),
						discord.SelectOption(value="Option 9",label="Description des Skills",description="?skill_description"),
						discord.SelectOption(value="Option 10",label="Toutes les runes",description="?runes_effect"),
						discord.SelectOption(value="Option 11",label="Conseil pour tout le monde",description="?conseil"),
						discord.SelectOption(value="Option 12",label="Rentabilit√©/Prix des skin",description="?skin"),
						discord.SelectOption(value="Option 13",label="Nombre d'oeufs pour les levels",description="?oeufs_level"),
						discord.SelectOption(value="Option 14",label="Guide pour le laby",description="?laby_guide"),
						discord.SelectOption(value="Option 15",label="Fonctionnement du PvP",description="?pvp"),
						discord.SelectOption(value="Option 16",label="Commande pour classement discord",description="?classement_help"),
						discord.SelectOption(value="Option 17",label="Commandes du bot Sylvan",description="?sylvan_command"),
						discord.SelectOption(value="Option 18",label="TierList stuff PvP",description="stuff_pvp"),
						discord.SelectOption(value="Option 19",label="Toutes les abr√©viations ",description="?abreviation"),
						discord.SelectOption(value="Option 20",label="Tous les boosts des H√©ros",description="?boost_heros"),
						discord.SelectOption(value="Option 21",label="Tuto pour d√©penser ton argent",description="?offre_item"),
						discord.SelectOption(value="Option 22",label="TierList Stuff",description="?stuff_pve1"),
						discord.SelectOption(value="Option 23",label="TierList Stuff (Mythique)",description="?stuff_pve2"),
						discord.SelectOption(value="Option 24",label="C√īut de l'am√©lioration d'un h√©ros",description="?shards_evo"),
						]
				super().__init__(placeholder="Clique ici pour choisir une autre commande ",max_values=1,min_values=1,options=options)
		async def callback(self, interaction: discord.Interaction):
			#0#########ERROR / HELP#######################
			help=discord.Embed(
			title="Voici toutes les commandes propos√©es :",description = "",color=0xFF5733)
			help.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			help.add_field(name="Commandes",value="?sylvan_command \n?bug \n?abreviation \n?pvp \n?qr \n?formulaire_endless \n?stuff_pve1 \n?stuff_pve2 (mythic) \n?stuff_pvp \n?laby_guide \n?conseil \n?oeufs_level \n?talent_tree \n?doc_oeufs \n?stats_joyaux \n?stuff_fusion \n?stats_calc", inline= True)
			help.add_field(name="Commandes",value="?skill_description \n?joyaux_fusion \n?heros_laby \n?rune_effect \n?offre_item \n?index_archive \n?skin \n?all_tierlist \n?discord_archero \n?shards_evo \n?tuto_apk \n?archero_red \n?archero_compilation \n?glitch \n?boost_heros \n?classement_help ",inline=True)
			#1#########STATS CALC#######################
			statscalc=discord.Embed(
			title="Calculateur de Stats Version Updated",description = "",color=0xFF5733)
			statscalc.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			statscalc.add_field(name='Stats Calculator',value="https://docs.google.com/spreadsheets/d/1NIfusyFcHqo-UzhGGpro03AxfXLXZFd1AIsOYGcP9zU/edit?usp=sharing ", inline= True)
			statscalc.add_field(name=" Petite indication :",value="2 choses importantes : \n-Si vous rencontrer un bug/trop gros √©cart de valeurs veuillez me Mp \n-Il faut aussi savoir qu'a chaque Mise √† jour du jeux il faudra re-remplir les valeurs sauf si vous souhaiter garder la version non-update", inline= True)
			#2##########BUGG############################
			bug=discord.Embed(
			title="adaYTgaming",url = "https://www.youtube.com/channel/UCJoV9pAMDRvD70JV7iLwA2g",description = "",color=0xFF5733)
			bug.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			bug.add_field(name="__Bug Mythic__",value="**Stalker Staff** : pas d'am√©lioration d'attaque speed\n**Bracelet invincible**: le bouclier n'apparait que 1,7sec mais on est prot√©ger pendant 3,,5sec comme indiqu√©\n**Bracelet tir rapide**: aucune dif√©rence de vitesse de projectile\n**Boomerang**: en pvp le boomerang ne fait pas de retour",inline=False)
			#3##########GLITCH##########################
			glitch=discord.Embed(
			title="PAS DE GLITCH DANS CE SERVEUR",url="https://www.youtube.com/channel/UCJoV9pAMDRvD70JV7iLwA2g",description = "C'est sujet qui peut aboutir √† un ban du serveur",color=0xFF5733)
			glitch.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			glitch.add_field(name="D√©finition Glitch :",value="A partir du moment o√Ļ tu influes sur le jeu de mani√®re anormal par un kill de l'app, ou autre, c'est du glitch, donc pas autoris√© ici.", inline=False)
			glitch.add_field(name="C'est √©crit dans le r√®glement",value="donc pas d'excuses", inline=False)
			glitch.set_footer(text="Si vous voulez en parler c'est en message priv√© !")
			#4##########TALENT TREE#####################
			talenttree=discord.Embed(
			title="Talent Tree",url="https://docs.google.com/spreadsheets/d/1Wu5yNEMrnoTGimhS5a2qfKHuZvHSRXyxLhkbok3nTX0/edit#gid=0",description = "",color=0xFF5733)
			talenttree.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			talenttree.add_field(name="Voici le lien qui vous m√®nera au gsheet",value="https://docs.google.com/spreadsheets/d/1Wu5yNEMrnoTGimhS5a2qfKHuZvHSRXyxLhkbok3nTX0/edit#gid=0", inline=False)
			talenttree.add_field(name=":warning: ATTENTION LES NOUVEAUX TALENTS SONT VALABLES QUE POUR CEUX QUI AVAIS FINIS LES TALENTS AVANT LA MAJ DES RUNES  ",value="https://docs.google.com/spreadsheets/d/1IHrFHEIuuCGkgt1c39jrtsscZhNcFLCxKzdROl1EktM/edit?usp=sharing", inline=False)
			#5##########QR##############################
			qr=discord.Embed(
			title="Voici le gsheet qui donne acc√®s au tableau de QuickRaid",url="https://docs.google.com/spreadsheets/d/1gI3lxMxjVT3iLb-71kyNrAGE8a4rhAp_tSo7IDwNm3w/edit#gid=808920507",description = "",color=0xFF5733)
			qr.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			qr.add_field(name="QR (Raid √©clair)",value="https://docs.google.com/spreadsheets/d/1gI3lxMxjVT3iLb-71kyNrAGE8a4rhAp_tSo7IDwNm3w/edit#gid=808920507",inline=True)
			qr.set_footer(text="Il est en francais et anglais car je l'ai partag√© avec le discord Officiel")
			#6##########ALL-TIERLIST####################
			alltierlist=discord.Embed(
			title="Voici le gsheet qui donne acc√®s aux TierList",url="https://docs.google.com/spreadsheets/d/1vm2xlsrUYbgXDYP7lmh60I4CBWkTLKA5YBhzrY-t0Tw/edit#gid=380709681",description = "",color=0xFF5733)
			alltierlist.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			alltierlist.add_field(name="Tierlist stuff PvP et PvE, et une TierList skill en Endless ",value="https://docs.google.com/spreadsheets/d/1vm2xlsrUYbgXDYP7lmh60I4CBWkTLKA5YBhzrY-t0Tw/edit#gid=380709681",inline=True)
			alltierlist.set_footer(text="Attention !!! Il faut parfois savoir faire preuve de bon sens, donc ne prenez pas cette tierlist aux pieds de la lettre")
			#7##########DOC-OEUFS######################
			docoeufs=discord.Embed(
			title="Archero info Couveuse", url="https://docs.google.com/spreadsheets/d/1bfq-F1BoT3FO-Nerg7KFn3jE5IMy768uokjLN5b7WCw/edit#gid=1801182798",description = "",color=0xFF5733)
			docoeufs.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			docoeufs.add_field(name="R√©alis√© par LuhCaran & Doodam's1402 vous y trouverez les stats de tout les mob/boss mais aussi rapidement trouver dans quel chapitre il se situe .",value="https://docs.google.com/spreadsheets/d/1bfq-F1BoT3FO-Nerg7KFn3jE5IMy768uokjLN5b7WCw/edit#gid=1801182798",inline=True)
			docoeufs.add_field(name="Tr√®s pratique !",value="Vous retrouverez toutes les infos concernant les oeufs de niveau 0 et vous pouvez aussi trouver les stats √† chaque niveau dans l'onglet 'Stats Compl√®te'",inline=True)
			#8##########TUTO-APK########################
			tutoapk=discord.Embed(
			title="Voici un tuto r√©alis√© par Flora", url="https://docs.google.com/document/d/1_dMG8fEA5g86V_c4FY_2Kmu3NG9H4at-xUIdd4ueWWA/edit",description = "",color=0xFF5733)
			tutoapk.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			tutoapk.add_field(name="Apprenez comment installer une apk pour avoir les derni√®re MAJ avant les iOs",value="https://docs.google.com/document/d/1_dMG8fEA5g86V_c4FY_2Kmu3NG9H4at-xUIdd4ueWWA/edit",inline=True)
			tutoapk.set_footer(text="Car oui seul les Android peuvent installer une Apk !! ")
			#9##########SKILL-DESC######################
			skilldesc=discord.Embed(
			title="Voici la description de skill par Flora et Akh√©", url="https://docs.google.com/spreadsheets/d/1O_RdljeBNAA9Wi7tgqDMrQJgubZvWMS8xzuV6n1d-cQ/edit#gid=0",description = "",color=0xFF5733)
			skilldesc.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			skilldesc.add_field(name="Tout les skill ne sont pas pr√©sent dans ce gdoc mais la plupart y sont",value="https://docs.google.com/spreadsheets/d/1O_RdljeBNAA9Wi7tgqDMrQJgubZvWMS8xzuV6n1d-cQ/edit#gid=0",inline=True)
			skilldesc.set_footer(text="Si le skill que vous cherchez n'y est pas vous pouvez demand√© dans le channel g√©n√©ral-archero")
			#10##########RUNES-EFFECT###################
			runeseffect=discord.Embed(
			title="Voici un gdoc dans lequel vous trouverez chaque ligne de runes disponible", url="https://docs.google.com/spreadsheets/d/1Y2C0yY-Ht5XDEYcA85XSnM51G8bguFIWE8LL7AMCVc0/edit#gid=0",description = "",color=0xFF5733)
			runeseffect.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			runeseffect.add_field(name="R√©alis√© par Chaos (un mec du discord officiel)",value="https://docs.google.com/spreadsheets/d/1Y2C0yY-Ht5XDEYcA85XSnM51G8bguFIWE8LL7AMCVc0/edit#gid=0",inline=True)
			runeseffect.set_footer(text="Il est possible que les nouvelles lignes ne soit pas ajout√© dans le gdoc !")
			#11##########CONSEIL########################
			conseil=discord.Embed(
			title="FAQ archero", url="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",description = "",color=0xFF5733)
			conseil.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			conseil.add_field(name="R√©alis√© par Vawaxe ce gdoc est destin√© aux d√©butant qui on besoin de conseil",value="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",inline=True)
			conseil.set_footer(text="Vous y trouverez une tierlist du meilleur √©quipement et plein de conseil m√™me utile aux personne plus avanc√©es dans le jeux !")
			#12##########SKIN###########################
			skin=discord.Embed(
			title="Voici un document qui vous donnera le prix de tout les skins",url="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",description = "",color=0xFF5733)
			skin.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			skin.add_field(name="Vous y trouverez tous les skins avec leurs prix et leurs boost",value="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",inline=True)
			#13##########OEUFS-LEVEL####################
			oeufslvl=discord.Embed(
			title="Voici le nombre d'oeufs √† avoir pour monter l'√©toile d'un mob boss :", url="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",description = "Il en faut 42 en tout pour monter un oeufs lvl10 !",color=0xFF5733)
			oeufslvl.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			oeufslvl.add_field(name="L'oeuf pour d√©bloquer le mob/boss n'est pas pris en compte",value="1 :star: = 1 oeuf \n 2 :star: = 1  oeuf \n 3 :star: = 2 oeufs \n 4 :star: = 2 oeufs \n 5 :star: = 3 oeufs \n 6 :star: = 4 oeufs \n 7 :star: = 5 oeufs \n 8 :star: = 6 oeufs \n 9 :star: = 8 oeufs \n 10 :star: = 10 oeufs",inline=True)
			#14##########LABY-GUIDES###################
			labyguide=discord.Embed(
			title="Voici comment marche l'event Labyrinthe",description = "",color=0xFF5733)
			labyguide.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			labyguide.add_field(name="Voici la signification de chaque couleur des portails dans le laby ",value="https://discord.com/channels/504559824617603082/607110270250385418/888317966574313502",inline=False)
			labyguide.add_field(name="Et l√† c'est le pattern √† suivre pour rendre le laby plus facile car il suffit juste de prendre un maximum de portail orange et violet",value="https://cdn.discordapp.com/attachments/604720918182232074/888154387866853437/IMG_20210916_220814.jpg",inline=False)
			labyguide.set_footer(text="il est possible que le screen des pattern √† suivre soit plus d'actualit√© ou que quelque salle ne marche pas")
			#15#########PVP#############################
			pvp=discord.Embed(
			title="Si vous cherchez √† savoir comment marche le PvP, ce document est fait pour vous !",url = "https://docs.google.com/spreadsheets/d/1gZsuhfJR6LzpLxlC8Kj40aeRKn9LeEPjC63whaj_Cts/edit#gid=0",description = "",color=0xFF5733)
			pvp.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			pvp.add_field(name="Vous y trouverez comment marche le syst√®me de groupe",value="https://docs.google.com/spreadsheets/d/1gZsuhfJR6LzpLxlC8Kj40aeRKn9LeEPjC63whaj_Cts/edit#gid=0",inline=False)
			#16##########RANK HELP##############
			rankhelp=discord.Embed(
			title="Comment rentrer dans le classement ?",url="https://www.youtube.com/channel/UCJoV9pAMDRvD70JV7iLwA2g",color=0xFF5733)
			rankhelp.add_field(name="Cr√©er un profil",value="?stats `ton attaque` `tes pv` voici le r√©sultat = ``?stats 10000 50000``", inline=False)
			rankhelp.add_field(name="Changer vos stats",value="?edit `ton attaque` `tes pv` voici le r√©sultat = ``?edit 10001 50001``", inline=False)
			rankhelp.add_field(name="Connaitre notre rank ",value="``?rank``", inline=False)
			rankhelp.add_field(name="Connaitre le top10",value="``?top``", inline=False)
			rankhelp.set_footer(text="Cela ne sert √† rien de mettre des stats au pif, je v√©rifierai vos entr√©s")
			#17##########SYLVAN COMMAND#################
			sylvancommand=discord.Embed(
			title="Voici les commandes de Sylvan",url = "", description = "",color=0xFF5733)
			sylvancommand.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			sylvancommand.add_field(name="Prix Upgrade Item  (de 0 √† 120)",value="Sylvan item cost ?? to ??",inline=False)
			sylvancommand.add_field(name="Prix Upgrade H√©ros (de 0 √† 110)",value="Sylvan hero cost ?? to ??",inline=False)
			sylvancommand.add_field(name="Prix Upgrade talent (de 0 √† 193)",value="Sylvan talent cost ?? to ??",inline=False)
			sylvancommand.add_field(name="Stats item",value="Sylvan + nom de l'item en anglais",inline=False)
			sylvancommand.set_footer(text="Vous pouvez aussi rejoindre ce Serveur :https://discord.gg/eAqZquTF6X \n puis aller dans le channel <#670976125014638593>")
			#18##########STUFF PVP######################
			stuffpvp=discord.Embed(
			title="",url = "",description = "",color=0xFF5733)
			stuffpvp.set_image(url = "https://cdn.discordapp.com/attachments/607110270250385418/889796930023088128/tierlist_pvp.png")
			#19##########ABBREVIATION###################
			abbreviation=discord.Embed(
			title="Voici toutes les Abr√©viation que l'on utilise souvent",url = "",description = "",color=0xFF5733)
			abbreviation.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			abbreviation.add_field(name="Liste des Abr√©viations",value="PDS = pierre de sang\nQR = QuickRaid \nRdG = Royaume de Glace \nCdG = Contrat de g√©ant \nDBR= demon blade rain \nAoC = Art du Combat \nALE = Ancient Legendary \nLeg = Legendary \nES = √©pique splendide \nHm = h√©roic mode \nNm = Normal mode \nStaff = B√Ęton du harceleur \ncac = corps √† corps\nPVP = player versus player \nPVE = player versus environment",inline=False)
			#20##########BOOST HEROS####################
			boostheros=discord.Embed(
			title="Voici tout les boost passif que donne les h√©ros",url = "",description = "",color=0xFF5733)
			boostheros.set_image(url = "https://cdn.discordapp.com/attachments/624522840783192074/899356977422041198/unknown.png")
			#21##########OFFRE ITEM#####################
			offreitem=discord.Embed(
			title="Merci Lovii pour cette astuce :yum:",url = "",description = "",color=0xFF5733)
			offreitem.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
			offreitem.add_field(name="Pr√©parez la :credit_card:",value="Faut √™tre s√Ľr que la derni√®re offre ait plus de 24h. \nMettre son perso √† poil avec juste l'item voulu (avoir 2 items de m√™me raret√©). \nBien kill le jeu. \nEn ouvrant, aller fusionner. \nSi √ßa ne marche pas, prendre l'autre item et refusionner \nEt si √ßa ne fonctionne toujours pas, r√©installer le jeu \nLa premi√®re action du jeu d√©finit l'offre que vous allez obtenir (golds, runes...)",inline=False)
			offreitem.set_footer(text="Spoiler : Oui c'est un glitch mais vu que √ßa touche √† l'argent bah on dit rien xD")
			#22##########STUFF PVE 1####################
			stuffpve1=discord.Embed(
			title="",url = "",description = "",color=0xFF5733)
			stuffpve1.set_image(url = "https://cdn.discordapp.com/attachments/889881030188748810/932427299381469255/tierlist_stuff_ale.png")
			#23##########STUFF PVE 2####################
			stuffpve2=discord.Embed(
			title="",url = "",description = "",color=0xFF5733)
			stuffpve2.set_image(url = "https://cdn.discordapp.com/attachments/889881030188748810/932427299813466202/tierlist_stuff_mythic.png")
			#24##########SHARDS EVO#####################
			shardevo=discord.Embed(
			title="",url = "",description = "",color=0xFF5733)
			shardevo.set_image(url = "https://cdn.discordapp.com/attachments/607110270250385418/939878194507563048/InShot_20220206_143932779.jpg")
			

			if self.values[0] == "Option 1":
				await interaction.response.edit_message(embed=statscalc)
			elif self.values[0] == "Option 2":
				await interaction.response.edit_message(embed=bug)
			elif self.values[0] == "Option 3":
				await interaction.response.edit_message(embed=glitch)
			elif self.values[0] == "Option 4":
				await interaction.response.edit_message(embed=talenttree)
			elif self.values[0] == "Option 5":
				await interaction.response.edit_message(embed=qr)
			elif self.values[0] == "Option 6":
				await interaction.response.edit_message(embed=alltierlist)
			elif self.values[0] == "Option 7":
				await interaction.response.edit_message(embed=docoeufs)
			elif self.values[0] == "Option 8":
				await interaction.response.edit_message(embed=tutoapk)
			elif self.values[0] == "Option 9":
				await interaction.response.edit_message(embed=skilldesc)
			elif self.values[0] == "Option 10":
				await interaction.response.edit_message(embed=runeseffect)
			elif self.values[0] == "Option 11":
				await interaction.response.edit_message(embed=conseil)
			elif self.values[0] == "Option 12":
				await interaction.response.edit_message(embed=skin)
			elif self.values[0] == "Option 13":
				await interaction.response.edit_message(embed=oeufslvl)
			elif self.values[0] == "Option 14":
				await interaction.response.edit_message(embed=labyguide)
			elif self.values[0] == "Option 15":
				await interaction.response.edit_message(embed=pvp)
			elif self.values[0] == "Option 16":
				await interaction.response.edit_message(embed=rankhelp)
			elif self.values[0] == "Option 17":
				await interaction.response.edit_message(embed=sylvancommand)
			elif self.values[0] == "Option 18":
				await interaction.response.edit_message(embed=stuffpvp)
			elif self.values[0] == "Option 19":
				await interaction.response.edit_message(embed=abbreviation)
			elif self.values[0] == "Option 20":
				await interaction.response.edit_message(embed=boostheros)
			elif self.values[0] == "Option 21":
				await interaction.response.edit_message(embed=offreitem)
			elif self.values[0] == "Option 22":
				await interaction.response.edit_message(embed=stuffpve1)
			elif self.values[0] == "Option 23":
				await interaction.response.edit_message(embed=stuffpve2)
			elif self.values[0] == "Option 24":
				await interaction.response.edit_message(embed=shardevo)
			else:
				await interaction.response.edit_message(embed=help)
				
class SelectView(discord.ui.View):
		def __init__(self, *, timeout = None):
				super().__init__(timeout=timeout)
				self.add_item(Select())