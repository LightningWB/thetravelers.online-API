class travelerApi():
    """
    The class for a travelers bot.\n
    Correct usage is (accountToken, captchaToken).\n
    I recommend doing openBrowser = true also while testing the bot so you can see what is going on.
    """
    def __init__(self, token:str, captchaToken:str, openBrowser=False, printInitialize=True):# recommened to operate not in headless for testing
        from selenium import webdriver
        from time import sleep
        options=webdriver.FirefoxOptions()
        if(not(openBrowser)):
            options.set_headless(True)
        self.driver=webdriver.Firefox(options=options)
        self.driver.get('https://thetravelers.online')
        self.driver.add_cookie({"name":"T","domain":"thetravelers.online","value":token})# logs in without password
        self.driver.execute_script(f'SOCKET.captcha="{captchaToken}"')
        self.driver.execute_script('SOCKET.autologBtn()')
        sleep(3)# logging in takes about a second but 3 to be safe
        self.prevCycle=self.driver.execute_script('return TIME.turn')
        if printInitialize:
            print('api initiated')
    def __del__(self):
        """
        Close the bot
        """
        self.stop()
    def stop(self):
        """
        Please use this to stop the api otherwise you can end up with a bunch of firefoxes running in the background.
        """
        self.driver.delete_all_cookies()# stops cookies from being stored
        self.driver.close()
    def move(self,dir:str):
        """
		Goes a given direction.
			dir: the direction you wish to move.
		"""
        self.driver.execute_script('SOCKET.send({action:"setDir",dir:"'+dir+'",autowalk:false})')
    def doubleStep(self):
        """
		Doublesteps if the server allows it.
		"""
        self.driver.execute_script('DSTEP.click()')
    def equip(self, itemID:str):
        """
		Equips an item.
			itemID: the item ID of the item to equip.
		"""
        self.driver.execute_script(f'SUPPLIES.open("{itemID}")')
        self.driver.execute_script('EQUIP.open()')
    def unEquip(self):
        """
		Unequips an item if you currently have one equiped.
		"""
        self.driver.execute_script('EQUIP.dequip()')
    def getLastEventInLog(self):
        """
		Returns the most recent message to appear in the event log.
		"""
        return self.driver.execute_script('return ENGINE.logMsgs[ENGINE.logMsgs.length-1].split("</span>")[1]')
    def getFullEventLog(self):
        """
        Returns an array of every message in the event log.
        """
        msgs= self.driver.execute_script('return ENGINE.logMsgs')
        for i in range(len(msgs)):
            msgs[i]=msgs[i].split('</span>')[1]
        return msgs
    def getSuppliesList(self):
        """
        Return your supplies as a list with just which item ids you currently have.
        """
        return list(self.driver.execute_script('return SUPPLIES.current'))
    def getSuppliesData(self):
        """
        Return as a dictionary with all item data.
        """
        return self.driver.execute_script('return SUPPLIES.current')
    def craft(self,ID:str):
        """
        Crafts one item. there is a limit internally of 1 per cycle.
			ID: the item id of what you wish to craft.
        """
        self.driver.execute_script(f'CRAFTING.open("craft-{ID}")')
        self.driver.execute_script('CRAFTING.craft()')
        self.driver.execute_script('CRAFTING.close()')
    def getCurrentCrafting(self):
        """
        Returns a dictionary of every item currently being crafted.
        """
        return self.driver.execute_script('return CRAFTING.queue')
    def pressEventButton(self,text:str):
        """
        Selects an event button based of the value.
			text: The event choice.
        """
        self.driver.execute_script('''
        btns=POPUP.evBtns.children
        for(i=0;i<btns.length;i++){
            if(btns[i].innerHTML="'''+text+'''"){
                btns[i].click()
            }
        }
        ''')
    def getEventName(self):
        """
        Returns the title of an event as html.
        """
        return self.driver.execute_script('return POPUP.evTitle.innerHTML')
    def getLootingName(self):
        """
        Returns the looting title as html.
        """
        return self.driver.execute_script('return LOOT.titleEl.innerHTML')
    def getLootingDescription(self):
        """
        Returns the looting event description as html.
        """
        return self.driver.execute_script('return LOOT.descEl.innerHTML')
    def getLootablesData(self):
        """
        Returns a dictionary of current items to loot. This includes data about the items.
        """
        return self.driver.execute_script('return LOOT.current')
    def getLootablesAsList(self):
        """
        This returns every lootable item as a list for easier handeling.
        """
        return list(self.getLootablesData())
    def takeAll(self):
        """
        This takes all the available items in a looting event.
        """
        self.driver.execute_script('LOOT.takeall()')
    def takeItem(self,itemID:str,amount:int):
        """
        Takes a specific item.
			itemID: The item id of the target id.
			ammount: The ammount to take.
        """
        self.driver.execute_script(f'LOOT.takeItems("{itemID}",{amount})')
    def giveItem(self, itemID:str, amount:int):
        """
        Gives an item to the loot container.
			itemID: The id of the item to give.
			ammount: The ammount to give.
        """
        self.driver.execute_script(f'LOOT.giveItems("{itemID}",{amount})')
    def exitLooting(self):
        """
        Leaves a looting event.
        """
        self.driver.execute_script('SOCKET.send({action: "loot_next"})')
    def openDropping(self):
        """
        Opens a drop item menu which you can give/take items from.
        """
        self.driver.execute_script('''
            SOCKET.send({
                "action": "hands",
                "option": "drop"
            });
        ''')
    def getUsername(self):
        """
        Returns your username
        """
        return self.driver.execute_script('return YOU.username')
    def getLevel(self):
        """
        Returns your current level.
        """
        return self.driver.execute_script('return XP.level+1')
    def getMaxWeight(self):
        """
        Retuens your current max weight.
        """
        return self.driver.execute_script('return XP.max_carry')
    def getMaxHealth(self):
        """
        Returns your current max health.
        """
        return self.driver.execute_script('return XP.max_hp')
    def getMaxStamina(self):
        """
        Returns your current max stamina.
        """
        return self.driver.execute_script('return XP.max_sp')
    def getMinute(self):
        """
        Returns the current minute.
        """
        return self.driver.execute_script('return TIME.minute')
    def getHour(self):
        """
        Returns the current hour.
        """
        return self.driver.execute_script('return TIME.hour')
    def getAmPm(self):
        """
        Returns weather it is am or pm.
        """
        return self.driver.execute_script('return TIME.ampm')
    def getDay(self):
        """
        Returns the current day.
        """
        return self.driver.execute_script('return TIME.day')
    def getSeason(self):
        """
        Returns the current season.
        """
        return self.driver.execute_script('return TIME.season')
    def getYear(self):
        """
        Returns the current year.
        """
        return self.driver.execute_script('return TIME.year')
    def getCycleTime(self):
        """
        Returns the time reaming till the next cycle.
        """
        return self.driver.execute_script('return TIME.countdownEl.innerHTML')
    def getBiome(self):
        """
        Returns your current biome.
        """
        return self.driver.execute_script('return WORLD.getBiome()')
    def getPos(self):
        """
        Returns your coordinates as a list. [x,y].
        """
        return [self.driver.execute_script('return YOU.x'),self.driver.execute_script('return YOU.y')]
    def deriveTile(self,x:int,y:int):
        """
        This uses the actual js function to generatea tile. If i made a mistake generateTileAt in my code this will still work.
        """
        return self.driver.execute_script(f'return WORLD.deriveTile({x},{y})')
    def getTielMap(self):# I am doing this because i made a typo early on and don't want to break anything
        """
        Returns the current viewable area as a list. The first index is the top left going right and then down.
        """
        return self.getTileMap()
    def getTileMap(self):
        """
        Returns the current viewable area as a list. The first index is the top left going right and then down.
        """
        return self.driver.execute_script('''tMap=[]
                                            for(i=0;i<961;i++){
                                                tMap.push(WORLD.tilemap[i].innerHTML);
                                            }
                                            return tMap;
                                            delete Tmap;
                                        ''')# deleteing saves up a little bit of memory
    def getLocalTile(self,screenX:int,screenY:int):# example 1,1 is top left and 31,31 is bottom right
        """
        Gets a tile relative to the top left of the screen. Ex. 1,1 is top left and 31,31 is bottom right.
        """
        if screenX>31 or screenX<1:
            raise ValueError('x must be greater than zero and less than 32')
        if screenY>31 or screenY<1:
            raise ValueError('y must be greater than zero and less than 32')
        return self.driver.execute_script(f'return WORLD.tilemap[({screenY}*31-31)+{screenX}-1].innerText')
    def getRelTile(self,relX:int,relY:int):
        """
        Gets a tile relative to your self. Ex. 1,1 is right and down one from your player.
        """
        return self.getLocalTile(relX+16,relY+16)
    def isNewCycle(self):
        """
        This checks if it is a new cycle. Run it in a while loop.
		while True:
			if api.isNewCycle():
				# do stuff
        """
        self.currnetCycle=self.driver.execute_script('return TIME.turn')
        if self.prevCycle<self.currnetCycle:
            self.prevCycle=self.currnetCycle
            return True
        else:
            return False
    def executeRawJS(self,js:str):# lets you reuse scripts
        """
        Executes js in the browser. This can be used to fill any holes I leave.
        """
        # js should be a string type
        self.driver.execute_script(js)
    def returnJS(self,js:str):# this will give you values of variables in js Ex: returnJS('YOU.x')
        """
        Returns a js variable. Ex: returnJS('YOU.x') to get your x position.
        """
        return self.driver.execute_script('return '+js)
    def sendPacket(self, packet:dict):
        """
        Sends a packet to the server.\n
		Ex: sendPacket({action: 'int_leave'})
        """
        self.executeRawJS(f'SOCKET.send({packet});')