from services import somfyService

class somfyController:
    def __init__(self):
        print("somfyController: init")
        self.somfyService = somfyService.somfyService()

    def postKeyDown(self, keycode):
        if (keycode == 'KEY_CHANNELUP'):
            self.somfyService.moveUp()
        elif (keycode == 'KEY_CHANNELDOWN'):
            self.somfyService.moveDown()
