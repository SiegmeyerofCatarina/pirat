from pyglet.window import key

keyboard = key.KeyStateHandler()


class KeyHandler:
    is_event_handler = True

    def __init__(self):
        super(KeyHandler, self).__init__()
        self.__keysHandlers = dict()

    def on_key_press(self, key_code, modifiers):
        if key_code in self.__keysHandlers and 'press' in self.__keysHandlers[key_code]:
            self.__keysHandlers[key_code]['press']()

    def on_key_release(self, key_code, modifiers):
        if key_code in self.__keysHandlers and 'release' in self.__keysHandlers[key_code]:
            self.__keysHandlers[key_code]['release']()

    def key_handler(self, key_name, press_handler=None, release_handler=None):
        key_number = getattr(key, key_name)
        self.__keysHandlers[key_number] = dict()
        if press_handler:
            self.__keysHandlers[key_number]['press'] = press_handler
        if release_handler:
            self.__keysHandlers[key_number]['release'] = release_handler
