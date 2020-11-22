"""
The world generation
"""
from .noise import simplex2
import math as Math
edgeDist = 500000
TILES={
	'traveler': "&",
	'sand': " ",
	'grass': ",",
	'tree': "t",
	'water': "w",
	'swamp': "~",
	'mountain': "M",
	'forest': "T",
	'house': "H",
	'city': "C",
	'startbox': "u",
	'monument': "\u258B",
	'island': ".",
	'worldedge': "\u2591"
}
invalidPlace=''
def setInvalids():
	"""
	used to set locations that can't have structures
	"""
	global invalidPlace, TILES
	invalidPlace+=TILES['worldedge']+TILES['monument']+TILES['mountain']+TILES['water']+TILES['island']+TILES['tree']+TILES['forest']# big line

setInvalids()

def getPerlin(x:int, y:int, s:int=100):
	"""
	Low level perlin generation
		x: the x value of the target location
		y: the y value of the target location
		s: 100: the other modifer to change stuff
	"""
	return simplex2(x/s, y/s)

def deriveTile(x:int, y:int):
	"""
	Uses client side world gen to generate a tile at a given location.
		x: the x value of the target tile
		y: the y value of the target tile
	"""
	global invalidPlace, TILES, edgeDist
	if x==0 and y==0:
		return TILES['monument']
	bottomTile = TILES['sand']
	giganticPerl = getPerlin(x, y + 5500, s=10000)
	# ground
	if giganticPerl > 0.57:
		if giganticPerl < 0.578:
			pass# in the original it sets it back to sand which is a waste because nomatter what it is sand
		else:
			if giganticPerl > 0.99788:
				if getPerlin(x, y, s=11) < -0.85:
					bottomTile = TILES['tree']
				else:
					bottomTile = TILES['island']
			else:
				bottomTile = TILES['water']
	else:
		hugePerl = getPerlin(x, y, s=5001)
		if hugePerl < -0.84:
			if hugePerl < 0.85:
				if abs(giganticPerl) > getPerlin(x, y, s=27):
					bottomTile = TILES['forest']
				else:
					bottomTile = TILES['grass']
			else:
				bottomTile = TILES['grass']
		else:
			bigPerl = getPerlin(x,y)
			if bigPerl > 0.7:
				bottomTile = TILES['swamp']
			elif bigPerl < -0.5 and abs(giganticPerl) > getPerlin(x, y, s=25):
				bottomTile = TILES['mountain']
			else:
				smallPerl = getPerlin(x, y, s=10)
				if smallPerl > 0.3:
					bottomTile = TILES['grass']
				elif getPerlin(y, x, s=11) < -0.85:
					bottomTile = TILES['tree']

	# places
	if bottomTile not in invalidPlace:
		perlRand = getPerlin(x, y, s=2.501)
		if Math.floor(perlRand * 3400) == 421:
			bottomTile = TILES['house']
		elif Math.floor(perlRand * 9000) == 4203:
			bottomTile = TILES['city']

	# edge
	if edgeDist - abs(x) < 10:
		if edgeDist - abs(x)<1:
			bottomTile = TILES['worldedge']
		else:
			perlEdge = getPerlin(x, y, s=0.005)
			if 1/ (edgeDist - abs(x) + perlEdge) > 0.16:
				bottomTile = TILES['worldedge']
	if edgeDist - abs(y) < 10:
		if edgeDist - abs(y)<1:
			bottomTile = TILES['worldedge']
		else:
			perlEdge = getPerlin(x, y, s=0.005)
			if 1/ (edgeDist - abs(y) + perlEdge) > 0.16:
				bottomTile = TILES['worldedge']
		
	return bottomTile

def isTileEvent(x:int, y:int):
	"""
	checks if a given tile is an event or not quicker than generateTileAt
		x: the x value of the target tile
		y: the y value of the target tile
	"""
	perlRand = getPerlin(x, y, s=2.501)
	if Math.floor(perlRand * 3400) == 421 and deriveTile(x, y)=='H':
		return True
	elif Math.floor(perlRand * 9000) == 4203 and deriveTile(x, y)=='C':
		return True
	return False