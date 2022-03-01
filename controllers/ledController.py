from services import ledService

class ledController:
    def __init__(self):
        print("LedController: init")
        self.ledService = ledService.ledService()
        self.ledService.clear()

    def postKeyDown(self, keycode):
        print(keycode)
        if (keycode == 'KEY_CHANNELUP' or keycode == 'KEY_CHANNELDOWN'):
            self.ledService.flashGreen()
        else:
            self.ledService.flashOrange()
