# thetravelers.online-API
## Description
A python API for the travelers.online.
Read documentation bellow for details on usage.
## Installation
1. Run this in command line:
```bash 
pip install thetravelers.online-Api
```
2. Download install the latest version of Firefox Here:https://www.mozilla.org/en-US/firefox/new/
3. Download Geckodriver from:https://github.com/mozilla/geckodriver/releases
4. Place geckodriver.exe with your python instalation or anywhere else in your path. <br> (Either C:\Users\your_user\AppData\Local\Programs\Python\Python38 or C:\Python38)
## Account Token
1. Go to https://thetravelers.online and login.
2. In firefox press shift+f9 to open up storage.
3. Scroll until you see a cookie named T.
4. The value is your account token.
## Captcha Token
1. To get your captcha token go to the https://thetravelers.online.
2. Complete the captcha and don't log in.
3. Paste this into the browser console.
```js
prompt("Copy the captcha:", SOCKET.captcha);
```
## Examples
Example auto xp program:
```python
token=input('token:')
captchaToken=input('captcha token:')
import travelersApi
api=travelersApi.travelerApi(token, captchaToken, openBrowser=True)
import time
turn='e'
while True:
    if(api.isNewCycle()==True):
        api.move(turn)
        if turn=='e':
            turn='w'
        else:
            turn='e'
    time.sleep(.1)
```
## Documentation
- `generateTileAt(x, y)`
	- This will generate a tile at a specific location.
- `getPerlin(x, y, s=100)`
	- This gets the noise value at a given location.
- `isTileEvent(x, y)`
	- Returns a boolean for if the given tile is an event or not.
- `api=travelerApi(token, captchaToken, openBrowser=False, printInitialize=True)`
  - Token is your acount token.
  - captchaToken is your captcha token.
  - OpenBrowser is defaulted to False but I would recommend setting it to True when testing.
  - PrintInitialize is whether or not to print API initialized when the api is set up.
- `api.stop()`
  - This will close all browsing context from firefox and delete your account token. Always use this to stop your bot.
- `api.move(dir)`
  - dir is the direction you would like to move.
  - Valid directions are n ,ne ,e ,se ,s ,sw ,w ,nw.
- `api.doubleStep()`
  - Will click the double step button once.
- `api.equip(itemID)`
  - itemID is the id of the item you would like to equip.
  - This lets you equip anything.
- `api.unEquip()`
  - Unequips the current item.
- `api.getLastEventInLog()`
  - Returns a string of the most recent event in your log.
- `api.getFullEventLog()`
  - Returns a list of every message in the event log.
- `api.getSuppliesList()`
  - Returns a list of each itemID you currently have.
  - this doesnt give any information about the items other than the ID.
- `api.getSuppliesData`
  - Returns a dictionary of each item you currently have.
  - This does include data such as ammount, equip data, crafting recipee, etc.
-  `api.craft(ID)`
   - This will craft an item from it's ID.
   - You can only craft one item a second due to game limits.
- `api.getCurrentCrafting()`
  - Returns a dictionary of your crafting queue.
- `api.pressEventButton(text)`
  - text is the buttons text you would like to click.
- `api.getEventName()`
  - Returns the current event title as a string.
- `api.getLootingName()`
  - Returns the current looting title as a string.
- `api.getLootingDescription()`
  - Returns the current looting menu description as a string.
- `api.getLootablesAsData()`
  - Returns every item you can loot as a dictionary with data.
- `api.getLootablesAsList()`
  - Returns every item to loot as a list.
- `api.takeAll()`
  - Will take all lootables.
- `api.takeItem(ID, amount)`
  - ID is the itemID you wish to take.
  - Amount is the amount you wish to take.
- `api.giveItem(ID, amount)`
  - ID is the itemID you wish to give.
  - Amount is the amount you wish to give.
- `api.openDropping()`
  - Opens the dropping items menu.
- `api.getUsername()`
  - Returns your username.
- `api.getLevel()`
  - Returns your current level.
- `api.getMaxWeight()`
  - Returns your current max weight.
- `api.getMaxHealth()`
  - Returns your current max health.
- `api.getMaxStamina()`
  - Returns your current max stamina.
- `api.getMinute()`
  - Returns the current minute.
- `api.getHour()`
  - Returns the current hour.
- `api.getAmPm()`
  - Returns if it is a.m. or p.m. as a string.
- `api.getDay()`
  - Returns the current day.
- `api.getSeason()`
  - Returns the current season.
- `api.getYear()`
  - Returns the current year.
- `api.getCycleTime()`
  - Returns the current time till next cycle.
  - Ex. 
  ```python
  >>> print(api.getCycleTime())
  .5
  ```
- `api.getBiome()`
  - Returns your current biome.
- `api.getPos()`
  - Returns you position as a list [x,y].
- `api.deriveTile(x,y)`
  - Returns the tile at the coordinates.
  - Only shows client side generation.
- `api.getTileMap()`
  - Returns a list with each tile in view distance.
- `api.getLocalTile(x,y)`
  - Top left is 1,1 and bottom right is 31,31.
  - Returns a tile within view distance.
  - Can show server side locations.
- `api.getRelTile(x,y)`
  - Returns a tile relative to you.
  - Ex.
  ```python
  >>> api.getRelTile(0,-1)
  (tile above you)
  ```
- `api.isNewCycle()`
  - When run repeaditely it will return true when it is a new cycle.
  - Ex.
  ```python
  from time import sleep
  while True:
    if api.isNewCycle():
      code to be run every cycle
    sleep(.01)
  ```
- `api.executeRawJS(js)`
  - Executes raw java script so if my API missed something you can use javascript.
- `api.returnJS(js)`
  - Same as executeRawJS except it can use return values.
  - Ex. 
  ```python
  >>> print(api.returnJS('YOU.username')
  (your username)
  ```
- `api.sendPacket(packet)`
  - Sends a packet to the server.