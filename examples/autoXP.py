token=input('token:')
import travelersApi
api=travelersApi.travelerApi(token, openBrowser=True)
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