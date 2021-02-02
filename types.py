from typing import List
class fx():
	pass
class item():
	name:str
class equipItem():
	status_text:str
class skills():
	"""
	skills in json.skills
	"""
	next_level_xp:int
	level:int
	xp:int
# interaction/pvp
class user():
	"""
	the type for a  user in an interaction
	"""
	username:str
	has_constitution:bool
	online:bool
class intMessages():
	"""
	messages that appear during an interaction
	"""
	_from:str
	text:str
class intInteraction():
	"""
	base class for interaction message that popup in the chat
	"""
	victim:str
class killer(intInteraction):
	"""
	a message of who killed who in an interaction
	"""
	killer:str
class looter(intInteraction):
	"""
	a message of who killed who in an interaction
	"""
	looter:str
class defeat():
	"""
	a message of who defeated who in an interaction
	"""
	victor:str
	loser:str
class challenge():
	"""
	a message of who challenged who in an interaction
	"""
	challenger:str
	challenged:str
class pvpStartMsg(intInteraction):
	"""
	a message of who started a fight with who in an interaction
	"""
	attacker:str
	defender:str
class offlineLoot():
	"""
	details for who you are looting offline
	"""
	username:str
	loot:dict
	limit:int
class battleStart():
	against:str
	youAttacked:str
class battleStart():
	against:str
	youAttacked:str
class pvpMidFight():
	opp_sq:int
	opp_hp:int
	you_option:str
	opp_option:str
class pvpNextRound():
	round:int
class pvpEndBattle():
	next_round:int
	youWon:bool
class pvpMessages():
	"""
	messages that appear during the end of a fight
	"""
	_from:str
	message:str
# proximity
class tileObjects():
	char:str
	x:int
	y:int
	is_breakable:bool
	walk_over:bool
class stump():
	x:int
	y:int
class player():
	x:int
	y:int
class proximity():
	"""
	proximity around a player like trees and such
	"""
	stumps:List[stump]
	players:List[player]
	objs:List[tileObjects]
# events
class lootChange():
	takeall:bool
	was_you:bool
	your_new:dict
	your_weight:int
	opp_new:dict
	opp_weight:int
	which:bool
	item_id:str
	amount:int
	item_data:dict	
class lootEvent():
	title:str
	visited:bool
	items:dict
	desc:str
	visitdesc:str
class eventStageData():
	title:str
	desc:str
	visited:str
	btns:dict
class event():
	visited:bool
	stage_data:eventStageData
# other stuff



class gameObject():
	"""
	the information sent to the client from the server
	the only value here guaranteed not to be None is turn
	"""
	turn:int
	steps_taken:int
	seconds_played:int
	deaths:int
	kills:int
	locs_explored:int
	kills_offline:int
	deaths_battle:int
	exe_js:str
	state:str
	effects:fx
	effects_removed:fx
	death_x:int
	death_y:int
	server_stop:bool
	x:int
	y:int
	username:str
	level:int
	craft_items:dict
	craft_queue:str
	supplies:dict
	new_items:dict
	equipped:str
	equip_data:equipItem
	skills:skills
	gained_xp:int
	offline_msgs:List[str]
	int_here:user
	outside_protection:bool
	int_messages:List[intMessages]
	int_gotmsg:str
	int_killer:killer
	int_looted:looter
	int_defeated:defeat
	int_challenge:challenge
	int_pvpstarted:pvpStartMsg
	int_offlineloot:offlineLoot
	battle_start:battleStart
	battle_timer:int
	opp_ready:bool
	battle_ready_weapon:str
	battle_startround:int
	battle_roundview:pvpMidFight
	battle_startnextround:pvpNextRound
	battle_endchatmsg:pvpMessages# they are the same so it is ok
	battle_close:bool
	proximity:proximity
	loot:lootEvent
	item_limit:int
	event_data:event
	new_icon:str
	doors:List[str]
	loot_change:lootChange
	break_time:int
	breaking:bool
	tut:int
	cutscene:int