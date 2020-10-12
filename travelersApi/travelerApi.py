class TravelerAPI():
    # Recommended to operate with openBrowser=True for testing(opens browser that you can see)
    def __init__(self, token: str, captchaToken: str, openBrowser=False, printInitialize=True):
        from time import sleep

        from selenium import webdriver

        options = webdriver.FirefoxOptions()
        if(!openBrowser):
            options.set_headless(True)

        self.driver = webdriver.Firefox(options=options)
        self.driver.get('https://thetravelers.online')
        self.driver.add_cookie(
            {
                "name": "T",
                "domain": "thetravelers.online",
                "value": token
            }
        )
        self.driver.execute_script(f'SOCKET.captcha = "{captchaToken}"')
        self.driver.execute_script('SOCKET.autologBtn()')

        sleep(3)  # Logging in takes about a second but 3 to be safe

        self.prevCycle = self.driver.execute_script('return TIME.turn')

        if printInitialize:
            print('api initiated')

    def stop(self):  # Use this to stop the api. Prevents having a bunch of firefoxes running in the background
        self.driver.delete_all_cookies()  # Stops cookies from being stored
        self.driver.close()

    def move(self, dir: str):
        self.driver.execute_script('SOCKET.send({action:"setDir",dir:"' + dir + '",autowalk:false})')

    def doubleStep(self):
        self.driver.execute_script('DSTEP.click()')

    def equip(self, itemID: str):
        self.driver.execute_script(f'SUPPLIES.open("{itemID}")')
        self.driver.execute_script('EQUIP.open()')

    def unEquip(self):
        self.driver.execute_script('EQUIP.dequip()')

    def getLastEventInLog(self):
        return self.driver.execute_script('return ENGINE.logMsgs[ENGINE.logMsgs.length-1].split("</span>")[1]')

    def getFullEventLog(self):
        msgs = self.driver.execute_script('return ENGINE.logMsgs')
        for i in msgs:
            msgs[msgs.index(i)] = i.split('</span>')[1]
        return msgs

    def getSuppliesList(self):  # Returns the data as a list with items you currently have
        return list(self.driver.execute_script('return SUPPLIES.current'))

    def getSuppliesData(self):  # Returns a dictionary with all item data
        return self.driver.execute_script('return SUPPLIES.current')

    def craft(self, ID: str):  # Craft one item. There is a limit internally of 1 per cycle
        self.driver.execute_script(f'CRAFTING.open("craft-{ID}")')
        self.driver.execute_script('CRAFTING.craft()')
        self.driver.execute_script('CRAFTING.close()')

    def getCurrentCrafting(self):
        return self.driver.execute_script('return CRAFTING.queue')

    def pressEventButton(self, text: str):
        self.driver.execute_script(
            """
            btns=POPUP.evBtns.children
            for(i=0;i<btns.length;i++){
                if(btns[i].innerhtml=\"""" + text + """\"){
                    btns[i].click()
                }
            }
            """
        )

    def getEventName(self):  # Returns event title html
        return self.driver.execute_script('return POPUP.evTitle.innerHTML')

    def getLootingName(self):  # Returns as html
        return self.driver.execute_script('return LOOT.titleEl.innerHTML')

    def getLootingDescription(self):
        return self.driver.execute_script('return LOOT.descEl.innerHTML')

    def getLootablesData(self):  # Returns loot as a dictionary with data
        return self.driver.execute_script('return LOOT.current')

    def getLootablesAsList(self):
        return list(self.getLootablesData())

    def takeAll(self):  # Takes all items in looting
        self.driver.execute_script('LOOT.takeall()')

    def takeItem(self, itemID: str, amount: int):
        self.driver.execute_script(f'LOOT.takeItems("{itemID}",{amount})')

    def giveItem(self, itemID: str, amount: int):
        self.driver.execute_script(f'LOOT.giveItems("{itemID}",{amount})')

    def exitLooting(self):
        self.driver.execute_script('SOCKET.send({action: "loot_next"})')

    def openDropping(self):  # Dropping items is the same as looting
        self.driver.execute_script(
            """
            SOCKET.send(
                {
                    \"action\": \"hands\",
                    \"option\": \"drop\"
                }
            );
            """
        )

    def getUsername(self):
        return self.driver.execute_script('return YOU.username')

    def getLevel(self):
        return self.driver.execute_script('return XP.level+1')

    def getMaxWeight(self):
        return self.driver.execute_script('return XP.max_carry')

    def getMaxHealth(self):
        return self.driver.execute_script('return XP.max_hp')

    def getMaxStamina(self):
        return self.driver.execute_script('return XP.max_sp')

    def getMinute(self):
        return self.driver.execute_script('return TIME.minute')

    def getHour(self):
        return self.driver.execute_script('return TIME.hour')

    def getAmPm(self):
        return self.driver.execute_script('return TIME.ampm')

    def getDay(self):
        return self.driver.execute_script('return TIME.day')

    def getSeason(self):
        return self.driver.execute_script('return TIME.season')

    def getYear(self):
        return self.driver.execute_script('return TIME.year')

    def getCycleTime(self):
        return self.driver.execute_script('return TIME.countdownEl.innerHTML')

    def getBiome(self):
        return self.driver.execute_script('return WORLD.getBiome()')

    def getPos(self):  # This will give you coords as an list [x,y]
        return [self.driver.execute_script('return YOU.x'), self.driver.execute_script('return YOU.y')]

    def deriveTile(self, x: int, y: int):
        return self.driver.execute_script(f'return WORLD.deriveTile({x},{y})')

    def getTielMap(self):
        return self.driver.execute_script(
            """
            tMap=[]
            for(i=0;i<961;i++){
                tMap.push(WORLD.tilemap[i].innerHTML);
            }
            return tMap;
            delete Tmap;
            """
        ) # Deleteing saves up a little bit of memory

    def getLocalTile(self, screenX: int, screenY: int):  # Example 1,1 is top left and 31,31 is bottom right
        if screenX > 31 or screenX < 1:
            raise ValueError('x must be greater than zero and less than 32')

        if screenY > 31 or screenY < 1:
            raise ValueError('y must be greater than zero and less than 32')

        return self.driver.execute_script(f'return WORLD.tilemap[({screenY}*31-31)+{screenX}-1].innerText')

    def getRelTile(self, relX: int, relY: int):
        return self.getLocalTile(relX + 16, relY + 16)

    def isNewCycle(self):
        self.currnetCycle = self.driver.execute_script('return TIME.turn')

        if self.prevCycle < self.currnetCycle:
            self.prevCycle = self.currnetCycle
            return True
        else:
            return False

    def executeRawJS(self, js: str):  # Lets you reuse scripts
        # js should be a string type
        self.driver.execute_script(js)

    def returnJS(self, js: str):  # This will give you values of variables in js Ex: returnJS('YOU.x')
        return self.driver.execute_script('return ' + js)
