from controllers import ledController
from controllers import somfyController
import evdev

devicePath = ''
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    if device.name == "gpio_ir_recv":
        devicePath = device.path
        break

ledControllerInstance = ledController.ledController()
somfyControllerInstance = somfyController.somfyController()

inputDevice = evdev.InputDevice(devicePath)
for event in inputDevice.read_loop():
    if (event.type == evdev.ecodes.EV_KEY and
        evdev.categorize(event).keystate == evdev.KeyEvent.key_down):
        ledControllerInstance.postKeyDown(evdev.categorize(event).keycode)
        somfyControllerInstance.postKeyDown(evdev.categorize(event).keycode)