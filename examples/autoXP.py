import time
import travelersApi
token = input('token:')
api = travelersApi.travelerApi(token, openBrowser=True)
turn = 'e'
while True:
    if(api.isNewCycle() == True):
        api.move(turn)
        if turn == 'e':
            turn = 'w'
        else:
            turn = 'e'
    time.sleep(.1)
