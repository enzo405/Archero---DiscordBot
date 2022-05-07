import discord 
from discord.ext import commands
from bot_auth import TOKENH
import database_handler as Mydb
from discord import User
from typing import Optional
import asyncio

bot = commands.Bot(command_prefix = "?", help_command = None, case_insensitive  =True)
channel_command = [736659714670198794, 948565096366481428, 948681408640073818, 889881030188748810]
db = Mydb.DatabaseHandler()

#--------------------- EVENT ---------------------

@bot.event
async def on_ready():
	print("Ready !")

@bot.event
async def on_message(message):
	if message.channel.id == 504560321772650537:
		await message.add_reaction("😍")
	await bot.process_commands(message)

#--------------------- DATABASE ADMIN /HOST COMMAND ---------------------

@bot.command(name="dbh_cp")
async def dbhost_create_person(ctx, target: User, attaque:int, pv:int):
	chat = bot.get_channel(952673377787711529)
	user = await bot.fetch_user("382930544385851392")
	name = target.display_name.replace("'","").replace('"','')
	if int(pv)/1.8 >= int(attaque) and ctx.author.id == user.id: 
		await ctx.reply(f":white_check_mark: Tu viens d'enregistré les stats de <@{target.id}> (Atk :{attaque}, Pv :{pv})", delete_after = 60, mention_author=True)
		confirm = await chat.send(f":white_check_mark: **{ctx.author}** à utilisé la commande ``{ctx.message.content}`` pour enregistré les stats de {target}")	
		try:
			reaction, user = await bot.wait_for(event = 'reaction_add', timeout = 300)
		except asyncio.TimeoutError:
			await confirm.reply(f"**Temps écoulé !** Fait cette commande : ``?dbh_cp <@!{target.id}> {attaque} {pv}`` !")
			return
		else:
			if str(reaction.emoji) == "\U00002705":
				db.create_person(target.id, name, attaque, pv)
				await confirm.reply(f"Les stats de {target} ont bien été enregistré",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
			if str(reaction.emoji) == "\U0000274c":
				await confirm.reply(f"Les stats de {target} n'ont pas été confirmé",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
	else:
		await ctx.reply(f"Soit tu t'es trompé de valeurs, soit tu n'es pas <@{user.id}>", delete_after = 15, mention_author=True)

@bot.command(name="dbh_ep")
async def dbhost_edit_person(ctx, target: User, attaque:int, pv:int):
	chat = bot.get_channel(952673377787711529)
	user = await bot.fetch_user("382930544385851392")
	name = target.display_name.replace("'","").replace('"','')
	if int(pv)/1.8 >= int(attaque) and ctx.author.id == user.id: 
		await ctx.reply(f":white_check_mark: Tu viens d'enregistré les nouvelles stats de <@{target.id}> (Atk :{attaque}, Pv :{pv})", delete_after = 60, mention_author=True)
		confirm = await chat.send(f"**{user}** à utilisé la commande ``{ctx.message.content}``!",mention_author=True)
		try:
			reaction, user = await bot.wait_for(event = 'reaction_add', timeout = 300)
		except asyncio.TimeoutError:
			await confirm.reply(f"**{user}**, tu n'a surement pas eu le temps d'accepter,\nFait cette commande si tu veux accepter sinon ignore ce message : ``?dbh_ep <@!{target.id}> {attaque} {pv}`` !", mention_author=True)
			return
		else:
			if str(reaction.emoji) == "\U00002705":
				db.change_stats(target.id, name, attaque, pv)
				await confirm.reply(f"Les stats de {name} ont été changé avec succès !",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
			if str(reaction.emoji) == "\U0000274c":
				await confirm.reply(f"Les stats de {name} n'ont pas été confirmé",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
	else:
		await ctx.reply(f"Soit tu t'es trompé de valeurs, soit tu n'es pas <@{user.id}>", delete_after = 15, mention_author=True)

@bot.command(name="dbh_rm")
async def dbhost_remove_user(ctx, target: User):
	chat = bot.get_channel(952673377787711529)
	user = await bot.fetch_user("382930544385851392")
	if ctx.author.id == user.id: 
		await ctx.reply(f"Une attente à la confirmation vient d'être envoyé dans #{chat} pour supprimer les stats de <@{target.id}>", mention_author=True)
		confirm = await chat.send(f":white_check_mark: **{ctx.author}** à utilisé la commande ``{ctx.message.content}`` pour supprimer les stats de {target}")	
		try:
			reaction, user = await bot.wait_for(event = 'reaction_add', timeout = 300)
		except asyncio.TimeoutError:
			await confirm.reply(f"**Temps écoulé !** Fait cette commande : ``?dbh_rm <@!{target.id}>`` !")
			return
		else:
			if str(reaction.emoji) == "\U00002705":
				db.delete_person(target.id)
				await confirm.reply(f"Les stats de {target} ont bien été supprimé",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
			if str(reaction.emoji) == "\U0000274c":
				await confirm.reply(f"Les stats de {target} n'ont pas été supprimé",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
	else:
		await ctx.reply(f"Soit tu t'es trompé de valeurs, soit tu n'es pas <@{user.id}>", delete_after = 15, mention_author=True)

@bot.command(name="dbh_f2p")
async def dbhost_free_to_play(ctx, target: User, response):
	user = await bot.fetch_user("382930544385851392")
	if ctx.author.id == user.id:
		db.free_to_play(target.id, response)
		await ctx.reply(f"{target} a maintenant `{response}` dans F2P",delete_after=15)
		await target.send(f"Vous avez maintenant {response} dans la colonne F2P")
	else:
		await ctx.reply(f"Tu n'a pas accès a cette commande seul <@{user.id}> peut", delete_after = 15, mention_author=True)

@bot.command(name="dbh_help")
async def dbhost_help_command(ctx):
	user = await bot.fetch_user("382930544385851392")
	em1=discord.Embed(
	title="Commande pour Database Host",url="https://www.youtube.com/channel/UCJoV9pAMDRvD70JV7iLwA2g",color=0xFF5733)
	em1.add_field(name="Créer un profil",value="``?dbh_cp <@123456789901> 10000 50000``", inline=False)
	em1.add_field(name="Changer les stats",value="``?dbh_ep <@123456789901> 10001 50001``", inline=False)
	em1.add_field(name="Supprimer les stats",value="``?dbh_rm <@123456789901>``", inline=False)
	em1.add_field(name="Status F2P",value="``?dbh_f2p <@123456789901> ✅/❌``", inline=False)
	em1.add_field(name="Insérer chapitre",value="``?dbh_ch <@123456789901> 21 24``", inline=False)
	await user.send(embed=em1)

@bot.command(name="dbh_ch")
async def dbhost_set_chapter(ctx, target: User, nm:int, hm:int):
	chat = bot.get_channel(952673377787711529)
	user = await bot.fetch_user("382930544385851392")
	if ctx.author.id == user.id:
		await ctx.reply(f"Une attente à la confirmation vient d'être envoyé dans #{chat} pour insérer les chapitres de <@{target.id}>", mention_author=True, delete_after=60)
		confirm = await chat.send(f":white_check_mark: **{ctx.author}** à utilisé la commande ``{ctx.message.content}`` ! {target} aura maintenant Nm:{nm} et Hm:{hm} en chapitre")	
		try:
			reaction, user = await bot.wait_for(event = 'reaction_add', timeout = 300)
		except asyncio.TimeoutError:
			await confirm.reply(f"**Temps écoulé !** Fait cette commande : ``?dbh_ch <@!{target.id}> {nm} {hm}`` !")
			return
		else:
			if str(reaction.emoji) == "\U00002705":
				db.set_chapter(target.id, nm, hm)
				await confirm.reply(f"Les chapitres de {target} ont bien été insérer (nm: {nm} hm: {hm})",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
			if str(reaction.emoji) == "\U0000274c":
				await confirm.reply(f"Les chapitres de {target} ont été refusé",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
	else:
		await ctx.reply(f"Soit tu t'es trompé de valeurs, soit tu n'es pas <@{user.id}>", delete_after = 15, mention_author=True)

#--------------------- USER DATABASE COMMAND ---------------------

@bot.command(name="stats")
async def create_stats(ctx, attaque:int, pv:int):
	chat = bot.get_channel(952673377787711529)
	user = await bot.fetch_user(382930544385851392)
	name = str(ctx.author.display_name).replace("'","")
	if int(pv)/1.8 >= int(attaque) and 1 <= attaque <= 64000 and 1<= pv <= 300000: 
		await ctx.reply(f"✅ Vos stats viennent d'être envoyé à <@{user.id}> et sont maintenant en attente de confirmation !\nVeuillez m'envoyer un screen de vos stats svp (----><@{user.id}>)\nVous pouvez demander à avoir le statuts Free To Play (faites `?rank_help` pour + d'info)", delete_after = 60, mention_author=True)
		confirm = await chat.send(f":white_check_mark: **{name}** à utilisé la commande ``{ctx.message.content}``!")	
		try:
			reaction, user = await bot.wait_for(event = 'reaction_add', timeout = 300)
		except asyncio.TimeoutError:
			await chat.send(f"**{ctx.author}**, tu n'a surement pas eu le temps d'accepter,\nFait cette commande si tu veux accepter sinon ignore ce message : ``?dbh_cp <@{ctx.author.id}> {attaque} {pv}`` !")
			await confirm.delete()
			return
		else:
			if str(reaction.emoji) == "\U00002705":
				db.create_person(ctx.author.id, name, attaque, pv)
				await confirm.reply(f"Vous venez de confirmer les stats de {name}",delete_after=15)
				await ctx.author.send(f"Vos Stats viennent d'être enregistrés !\nVous pouvez consulter votre classement en faisant ``?rank`` ou en alant sur ce site : https://adarmy.herokuapp.com/classement/")
				await asyncio.sleep(5)
				await confirm.delete()
			if str(reaction.emoji) == "\U0000274c":
				await confirm.reply(f"Les stats de {name} n'ont pas été confirmé",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
	else:
		await ctx.reply(f"Veuillez rentrer des valeurs cohérentes", delete_after = 15, mention_author=True)

@bot.command(name="edit")
async def edit_stats(ctx, attaque:int, pv:int):
	chat = bot.get_channel(952673377787711529)
	user = await bot.fetch_user("382930544385851392")
	name = str(ctx.author.display_name).replace("'","")
	if int(pv)/1.8 >= int(attaque) and 1 <= attaque <= 64000 and 1<= pv <= 300000: 
		await ctx.reply(f"✅ Vos stats viennent d'être envoyé à <@{user.id}> et sont maintenant en attente de confirmation !\nVous pouvez demander à avoir le statuts Free To Play (faites `?rank_help` pour + d'info)", delete_after = 60, mention_author=True)
		confirm = await chat.send(f"**{name}** à utilisé la commande ``{ctx.message.content}``!")
		try:
			reaction, user = await bot.wait_for(event = 'reaction_add', timeout = 300)
		except asyncio.TimeoutError:
			await chat.send(f"**{ctx.author}**, tu n'a surement pas eu le temps d'accepter,\nFait cette commande si tu veux accepter sinon ignore ce message : ``?dbh_ep <@{ctx.author.id}> {attaque} {pv}`` !")
			await confirm.delete()
			return
		else:
			if str(reaction.emoji) == "\U00002705":
				db.change_stats(ctx.author.id, name, attaque, pv)
				await confirm.reply(f"Vous venez de confirmer les stats de {name}",delete_after=15)
				await ctx.author.send(f"Vos Stats viennent d'être changé !\nVous pouvez consulter votre classement en faisant ``?rank`` ou en allant sur : https://adarmy.herokuapp.com/classement/")
				await asyncio.sleep(5)
				await confirm.delete()
			if str(reaction.emoji) == "\U0000274c":
				await confirm.reply(f"Les stats de {name} n'ont pas été confirmé",delete_after=15)
				await asyncio.sleep(5)
				await confirm.delete()
	else:
		await ctx.reply(f"Veuillez rentrer des valeurs cohérentes", delete_after = 15, mention_author=True)

@bot.command(name="rank")
async def display_rank(ctx, target: Optional[User]):
	target = target or ctx.author
	place = db.column("SELECT id FROM Stats ORDER BY attaque DESC")
	target_F2P = db.column(f"SELECT F2P FROM Stats WHERE id={target.id}")
	target_atk2 = db.column(f"SELECT attaque FROM Stats WHERE id={target.id}")
	target_pv2 = db.column(f"SELECT pv FROM Stats WHERE id={target.id}")
	target_chapitreHm = db.column(f"SELECT ChapterHm FROM Stats WHERE id={target.id}")
	target_chapitreNm = db.column(f"SELECT ChapterNm FROM Stats WHERE id={target.id}")
	target_atk = str(target_atk2).replace("]","").replace("[","")
	target_pv = str(target_pv2).replace("]","").replace("[","")
	F2P = str(target_F2P).replace("]","").replace("[","").replace("None","❌").replace("'","")
	chapitreNm = str(target_chapitreNm).replace("]","").replace("[","").replace("None","Pas précisé")
	chapitreHm = str(target_chapitreHm).replace("]","").replace("[","").replace("None","Pas précisé")
	try:
		em1=discord.Embed(
		title=f"Voici les Stats de {target.display_name}",url="https://adarmy.herokuapp.com/classement/",color=0xFF5733)
		em1.add_field(name=f"Tu es n°{place.index(target.id)+1} sur {len(place)}",value=f"Avec {target_atk} d'attaque et {target_pv} pv !\nF2P : {F2P}\n__Nm__: {chapitreNm}\n__Hm__: {chapitreHm}", inline=False)
		em1.set_thumbnail(url= target.avatar_url)
		em1.set_footer(text="https://adarmy.herokuapp.com/classement/")
		await ctx.send(embed=em1)
	except ValueError:
		await ctx.send(f"{target.display_name} n'est pas présent dans le classement.", delete_after = 6)

@bot.command(name="top")
async def display_leaderboard(ctx):
	em1=discord.Embed(
	title="Voici le classement du Discord ADA",color=0xFFFF00)
	em1.add_field(name="https://adarmy.herokuapp.com/classement/",value="l'url du site est aussi dans la description du bot", inline=False)
	await ctx.channel.send(embed=em1)

@bot.command()
async def rank_help(ctx):
	user = await bot.fetch_user("382930544385851392")
	em1=discord.Embed(
	title="Comment rentrer dans le classement ?",url="https://adarmy.herokuapp.com/classement/",color=0xFF5733)
	em1.add_field(name="Créer un profil",value="?stats *attaque* *pv* \nVoici un exemple = ``?stats 10000 50000``", inline=False)
	em1.add_field(name="Changer vos stats",value="?edit *attaque* *pv* \nVoici un exemple = ``?edit 10001 50001``", inline=False)
	em1.add_field(name="Connaitre ton rank ",value="``?rank``", inline=False)
	em1.add_field(name="Connaitre le top10",value="``?top`` ou https://adarmy.herokuapp.com/classement/", inline=False)
	em1.add_field(name="Free To Play",value=f"Preuves à envoyer en MP à <@{user.id}> :\n-Un screen du compte (menu d'accueil)\n-Un screen du nombre de tenues que vous possédez\n-Un screen de vos stats", inline=False)
	em1.add_field(name="Chapitre",value=f"Preuves à envoyer en MP à <@{user.id}> :\n-Un screen des chapitres sur lesquels vous êtes bloqués (nm et hm)\n-Un screen de vos stats", inline=False)
	em1.set_footer(text="Cela ne sert à rien de mettre des stats au pif, je vérifierai vos entrés")
	await ctx.channel.send(embed=em1)

#--------------------- EMBED COMMAND ---------------------

@bot.command()
async def help(ctx):
	em0=discord.Embed(
	title="Voici toutes les commandes proposées :",description = "",color=0xFF5733)
	em0.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em0.add_field(name="Commandes",value="?sylvan_command \n?bug \n?abreviation \n?pvp \n?qr \n?formulaire_endless \n?stuff_pve1 \n?stuff_pve2 (mythic) \n?stuff_pvp \n?laby_guide \n?conseil \n?oeufs_level \n?talent \n?doc_oeufs \n?stats_calc", inline= True)
	em0.add_field(name="Commandes",value="?skill_description \n?joyaux_fusion \n?rune_effect \n?offre_item \n?index_archive \n?skin \n?all_tierlist \n?shards_evo \n?tuto_apk \n?archero_red \n?archero_compilation \n?glitch \n?boost_heros \n?rank_help",inline=True)
	em0.add_field(name="Commandes pas dans la liste",value="?discord_archero \n?heros_laby \n?stats_joyaux \n?stuff_fusion \n",inline=True)
	if ctx.channel.id in channel_command: 
		await ctx.channel.send(embed=em0)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def stats_calc(ctx):
	em1=discord.Embed(
	title="Calculateur de Stats Version Updated",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name='Stats Calculator',value="https://docs.google.com/spreadsheets/d/1NIfusyFcHqo-UzhGGpro03AxfXLXZFd1AIsOYGcP9zU/edit?usp=sharing ", inline= True)
	em1.add_field(name=" Petite indication :",value="2 choses importantes : \n-Si vous rencontrer un bug/trop gros écart de valeurs veuillez me Mp \n-Il faut aussi savoir qu'a chaque Mise à jour du jeux il faudra re-remplir les valeurs sauf si vous souhaiter garder la version non-update", inline= True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def bug(ctx):
	em1=discord.Embed(
	title="adaYTgaming",url = "https://www.youtube.com/channel/UCJoV9pAMDRvD70JV7iLwA2g",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="__Bug Mythic__",value="**Stalker Staff** : pas d'amélioration d'attaque speed\n**Bracelet invincible**: le bouclier n'apparait que 1,7sec mais on est protéger pendant 3,,5sec comme indiqué\n**Bracelet tir rapide**: aucune diférence de vitesse de projectile\n**Boomerang**: en pvp le boomerang ne fait pas de retour",inline=False)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def glitch(ctx):
	em1=discord.Embed(
	title="PAS DE GLITCH DANS CE SERVEUR",url="https://www.youtube.com/channel/UCJoV9pAMDRvD70JV7iLwA2g",description = "C'est sujet qui peut aboutir à un ban du serveur",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Définition Glitch :",value="A partir du moment où tu influes sur le jeu de manière anormal par un kill de l'app, ou autre, c'est du glitch, donc pas autorisé ici.", inline=False)
	em1.add_field(name="C'est écrit dans le règlement",value="donc pas d'excuses", inline=False)
	em1.set_footer(text="Si vous voulez en parler c'est en message privé !")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def talent(ctx):
	em1=discord.Embed(
	title="Talent Tree",url="https://docs.google.com/spreadsheets/d/1Wu5yNEMrnoTGimhS5a2qfKHuZvHSRXyxLhkbok3nTX0/edit#gid=0",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Voici le lien qui vous mènera au gsheet",value="https://docs.google.com/spreadsheets/d/1Wu5yNEMrnoTGimhS5a2qfKHuZvHSRXyxLhkbok3nTX0/edit#gid=0", inline=False)
	em1.add_field(name=":warning: ATTENTION LES NOUVEAUX TALENTS SONT VALABLES QUE POUR CEUX QUI AVAIS FINIS LES TALENTS AVANT LA MAJ DES RUNES  ",value="https://docs.google.com/spreadsheets/d/1IHrFHEIuuCGkgt1c39jrtsscZhNcFLCxKzdROl1EktM/edit?usp=sharing", inline=False)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def QR(ctx):
	em1=discord.Embed(
	title="Voici le gsheet qui donne accès au tableau de QuickRaid",url="https://docs.google.com/spreadsheets/d/1gI3lxMxjVT3iLb-71kyNrAGE8a4rhAp_tSo7IDwNm3w/edit#gid=808920507",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="QR (Raid éclair)",value="https://docs.google.com/spreadsheets/d/1gI3lxMxjVT3iLb-71kyNrAGE8a4rhAp_tSo7IDwNm3w/edit#gid=808920507",inline=True)
	em1.set_footer(text="Il est en francais et anglais car je l'ai partagé avec le discord Officiel")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def all_tierlist(ctx):
	em1=discord.Embed(
	title="Voici le gsheet qui donne accès aux TierList",url="https://docs.google.com/spreadsheets/d/1vm2xlsrUYbgXDYP7lmh60I4CBWkTLKA5YBhzrY-t0Tw/edit#gid=380709681",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Tierlist stuff PvP et PvE, et une TierList skill en Endless ",value="https://docs.google.com/spreadsheets/d/1vm2xlsrUYbgXDYP7lmh60I4CBWkTLKA5YBhzrY-t0Tw/edit#gid=380709681",inline=True)
	em1.set_footer(text="Attention !!! Il faut parfois savoir faire preuve de bon sens, donc ne prenez pas cette tierlist aux pieds de la lettre")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def index_archive(ctx):
	em1=discord.Embed(
	title="Voici un gdoc qui recense tout les documents présent dans Archives",url="https://docs.google.com/document/d/1Y8EGuiOL2t6alAgz7_Uyib5hADUNlnTJbMK3hE3Xxtc/edit",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Il a été réalisé par Flora",value="https://docs.google.com/document/d/1Y8EGuiOL2t6alAgz7_Uyib5hADUNlnTJbMK3hE3Xxtc/edit",inline=True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def doc_oeufs(ctx):
	em1=discord.Embed(
	title="Archero info Couveuse", url="https://docs.google.com/spreadsheets/d/1bfq-F1BoT3FO-Nerg7KFn3jE5IMy768uokjLN5b7WCw/edit#gid=1801182798",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Réalisé par LuhCaran & Doodam's1402 vous y trouverez les stats de tout les mob/boss mais aussi rapidement trouver dans quel chapitre il se situe .",value="https://docs.google.com/spreadsheets/d/1bfq-F1BoT3FO-Nerg7KFn3jE5IMy768uokjLN5b7WCw/edit#gid=1801182798",inline=True)
	em1.add_field(name="Très pratique !",value="Vous retrouverez toutes les infos concernant les oeufs de niveau 0 et vous pouvez aussi trouver les stats à chaque niveau dans l'onglet 'Stats Complète'",inline=True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def archero_compilation(ctx):
	em1=discord.Embed(
	title="Voici un gdoc réalisé par LanderZ", url="https://discord.com/channels/504559824617603082/607110270250385418/885938275712381028",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Dans ce gdoc vous retrouverez TOUTES, absolument toutes les info d'Archero",value="https://discord.com/channels/504559824617603082/607110270250385418/885938275712381028",inline=True)
	em1.add_field(name="Il y a :",value="-Hero Evolution and Evolution Stats \n -Daily Events past calendar \n -Jewels \n -Mystery Mine, Hero Buffs and Battle Contracts \n -Ancient Maze Bosses \n -Lucky Spin Events \n -Outfits \n -Avatars and Frames \n -Support Hero Daily Event Affinity Boosts \n -Chapter bonuses [gold per wheels, Quick Raids, etc.]",inline=True)
	em1.set_footer(text="Spoiler : Le document est en anglais !!")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def tuto_apk(ctx):
	em1=discord.Embed(
	title="Voici un tuto réalisé par Flora", url="https://docs.google.com/document/d/1_dMG8fEA5g86V_c4FY_2Kmu3NG9H4at-xUIdd4ueWWA/edit",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Apprenez comment installer une apk pour avoir les dernière MAJ avant les iOs",value="https://docs.google.com/document/d/1_dMG8fEA5g86V_c4FY_2Kmu3NG9H4at-xUIdd4ueWWA/edit",inline=True)
	em1.set_footer(text="Car oui seul les Android peuvent installer une Apk !! ")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def skill_description(ctx):
	em1=discord.Embed(
	title="Voici la description de skill par Flora et Akhé", url="https://docs.google.com/spreadsheets/d/1O_RdljeBNAA9Wi7tgqDMrQJgubZvWMS8xzuV6n1d-cQ/edit#gid=0",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Tout les skill ne sont pas présent dans ce gdoc mais la plupart y sont",value="https://docs.google.com/spreadsheets/d/1O_RdljeBNAA9Wi7tgqDMrQJgubZvWMS8xzuV6n1d-cQ/edit#gid=0",inline=True)
	em1.set_footer(text="Si le skill que vous cherchez n'y est pas vous pouvez demandé dans le channel général-archero")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def rune_effect(ctx):
	em1=discord.Embed(
	title="Voici un gdoc dans lequel vous trouverez chaque ligne de runes disponible", url="https://docs.google.com/spreadsheets/d/1Y2C0yY-Ht5XDEYcA85XSnM51G8bguFIWE8LL7AMCVc0/edit#gid=0",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Réalisé par Chaos (un mec du discord officiel)",value="https://docs.google.com/spreadsheets/d/1Y2C0yY-Ht5XDEYcA85XSnM51G8bguFIWE8LL7AMCVc0/edit#gid=0",inline=True)
	em1.set_footer(text="Il est possible que les nouvelles ligne ne soit pas ajouté dans le gdoc !")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def conseil(ctx):
	em1=discord.Embed(
	title="FAQ archero", url="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Réalisé par Vawaxe ce gdoc est destiné aux débutant qui on besoin de conseil",value="https://docs.google.com/document/d/18ASAbf1qCAAGmrF1LtXOxHaY66n1Rko6Dd4DGrGeoxQ/edit",inline=True)
	em1.set_footer(text="Vous y trouverez une tierlist du meilleur équipement et plein de conseil même utile aux personne plus avancées dans le jeux !")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def skin(ctx):
	em1=discord.Embed(
	title="Voici un document qui vous donnera le prix de tout les skins",url="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Vous y trouverez tous les skins avec leurs prix et leurs boost",value="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",inline=True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def oeufs_level(ctx):
	em1=discord.Embed(
	title="Voici le nombre d'oeufs à avoir pour monter l'étoile d'un mob boss :", url="https://docs.google.com/spreadsheets/d/1EcvyN2NGT3k8hDrIk14CsUmyILzMDOJidKKEDDB2dSU/edit#gid=0",description = "Il en faut 42 en tout pour monter un oeufs lvl10 et 86 pour le monter lvl15!",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="L'oeuf pour débloquer le mob/boss n'est pas pris en compte",value="1 :star: = 1 oeuf \n 2 :star: = 1  oeuf \n 3 :star: = 2 oeufs \n 4 :star: = 2 oeufs \n 5 :star: = 3 oeufs \n 6 :star: = 4 oeufs \n 7 :star: = 5 oeufs \n 8 :star: = 6 oeufs \n 9 :star: = 8 oeufs \n 10 :star: = 10 oeufs\n 11 :star: = 15 oeufs\n 12 :star: = 4 oeufs\n 13 :star: = 6 oeufs\n 14 :star: = 8 oeufs\n 15 :star: = 12 oeufs",inline=True)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def laby_guide(ctx):
	em1=discord.Embed(
	title="Voici comment marche l'event Labyrinthe",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Voici la signification de chaque couleur des portails dans le laby ",value="https://discord.com/channels/504559824617603082/607110270250385418/888317966574313502",inline=False)
	em1.add_field(name="Et là c'est le pattern à suivre pour rendre le laby plus facile car il suffit juste de prendre un maximum de portail orange et violet",value="https://cdn.discordapp.com/attachments/604720918182232074/888154387866853437/IMG_20210916_220814.jpg",inline=False)
	em1.set_footer(text="il est possible que le screen des pattern à suivre soit plus d'actualité ou que quelque salle ne marche pas")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def pvp(ctx):
	em1=discord.Embed(
	title="Si vous cherchez à savoir comment marche le PvP, ce document est fait pour vous !",url = "https://docs.google.com/spreadsheets/d/1gZsuhfJR6LzpLxlC8Kj40aeRKn9LeEPjC63whaj_Cts/edit#gid=0",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Vous y trouverez comment marche le système de groupe",value="https://docs.google.com/spreadsheets/d/1gZsuhfJR6LzpLxlC8Kj40aeRKn9LeEPjC63whaj_Cts/edit#gid=0",inline=False)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def archero_red(ctx):
	em1=discord.Embed(
	title="Voilà le lien qui vous ménera à la page Instagram de Archero_Red",url = "https://www.instagram.com/archerored/",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Sur la page instagram de cette personne (qui ne fais pas partie du staff d'Archero) vous y trouverez beaucoup d'information utile notamment quel est le chapitre qui drop le mieux ...etc",value="https://www.instagram.com/archerored/",inline=False)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def sylvan_command(ctx):
	em1=discord.Embed(
	title="Voici les commandes de Sylvan",url = "", description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Prix Upgrade Item  (de 0 à 120)",value="Sylvan item cost ?? to ??",inline=False)
	em1.add_field(name="Prix Upgrade Héros (de 0 à 110)",value="Sylvan hero cost ?? to ??",inline=False)
	em1.add_field(name="Prix Upgrade talent (de 0 à 193)",value="Sylvan talent cost ?? to ??",inline=False)
	em1.add_field(name="Stats item",value="Sylvan + nom de l'item en anglais",inline=False)
	em1.set_footer(text="Vous pouvez aussi rejoindre ce Serveur :https://discord.gg/eAqZquTF6X \n puis aller dans le channel <#670976125014638593>")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def stuff_pvp(ctx):
	em1=discord.Embed(
	title="",url = "",description = "",color=0xFF5733)
	em1.set_image(url = "https://cdn.discordapp.com/attachments/607110270250385418/889796930023088128/tierlist_pvp.png")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def abreviation(ctx):
	em1=discord.Embed(
	title="Voici toutes les Abréviation que l'on utilise souvent",url = "",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Liste des Abréviations",value="PDS = pierre de sang\nQR = QuickRaid \nRdG = Royaume de Glace \nCdG = Contrat de géant \nDBR= demon blade rain \nAoC = Art du Combat \nALE = Ancient Legendary \nLeg = Legendary \nES = épique splendide \nHm = héroic mode \nNm = Normal mode \nStaff = Bâton du harceleur \ncac = corps à corps\nPVP = player versus player \nPVE = player versus environment",inline=False)
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def boost_heros(ctx):
	em1=discord.Embed(
	title="Voici tout les boost passif que donne les héros",url = "",description = "",color=0xFF5733)
	em1.set_image(url = "https://cdn.discordapp.com/attachments/624522840783192074/899356977422041198/unknown.png")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def offre_item(ctx):
	em1=discord.Embed(
	title="Merci Lovii pour cette astuce :yum:",url = "",description = "",color=0xFF5733)
	em1.set_thumbnail(url="https://pbs.twimg.com/profile_images/1115253379398348800/nd4kxZE9.png")
	em1.add_field(name="Préparez la :credit_card:",value="Faut être sûr que la dernière offre ait plus de 24h. \nMettre son perso à poil avec juste l'item voulu (avoir 2 items de même rareté). \nBien kill le jeu. \nEn ouvrant, aller fusionner. \nSi ça ne marche pas, prendre l'autre item et refusionner \nEt si ça ne fonctionne toujours pas, réinstaller le jeu \nLa première action du jeu définit l'offre que vous allez obtenir (golds, runes...)",inline=False)
	em1.set_footer(text="Spoiler : Oui c'est un glitch mais vu que ça touche à l'argent bah on dit rien xD")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def stuff_pve1(ctx):
	em1=discord.Embed(
	title="Voici une tierlist des items ALE",url = "",description = "",color=0xFF5733)
	em1.set_image(url = "https://cdn.discordapp.com/attachments/889452351587495948/964812094245576744/unknown.png")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def stuff_pve2(ctx):
	em1=discord.Embed(
	title="",url = "",description = "",color=0xFF5733)
	em1.set_image(url = "https://cdn.discordapp.com/attachments/889452351587495948/964811951874117632/unknown.png")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def shards_evo(ctx):
	em1=discord.Embed(
	title="",url = "",description = "",color=0xFF5733)
	em1.set_image(url = "https://cdn.discordapp.com/attachments/607110270250385418/939878194507563048/InShot_20220206_143932779.jpg")
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send(embed=em1)
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def joyaux_fusion(ctx):
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send("https://cdn.discordapp.com/attachments/604720918182232074/892118488175489064/unknown.png")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def heros_laby(ctx):
	if (ctx.channel.id == channel_command): 
		await ctx.channel.send("https://cdn.discordapp.com/attachments/607110270250385418/847431973244108810/image0.png")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def stuff_fusion(ctx):
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send("https://media.discordapp.net/attachments/889452351587495948/927346154289655869/Screenshot_20220103-004121.jpg")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def stats_joyaux(ctx):
	if (ctx.channel.id in channel_command): 
		await ctx.channel.send("https://cdn.discordapp.com/attachments/607110270250385418/918104338289786880/jewles_landerz.png")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

@bot.command()
async def discord_archero(ctx):
	if (ctx.channel.id in channel_command): 
			await ctx.channel.send("Voici le lien qui permet de rejoindre le discord officiel pas très officiel, car l'admin du discord n'est rien d'autre qu'un ancien dévelopeur de HABBY : https://discord.gg/d7w6FxhHjj")
	else:
		await ctx.channel.send("Vous devez envoyer cette commande dans <#736659714670198794>",delete_after = 15)
		await ctx.message.delete()

bot.run(TOKENH)