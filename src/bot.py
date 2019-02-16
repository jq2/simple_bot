#!/usr/bin/python
import os
import json


isDebugOn = True
BOT_TOKEN = None


class UpdateMessage:

    def __init__(self):
        self.update_id = None

    def getUpdates(self, limit, offset):
        # curl to api and return a list of json objects
        # self.update_id = '{"key" : "value"}'
        # self.update_id = dict()
        # self.update_id = 999999
        # self.update_id = None
        self.update_id = "Hello, world!, new message received!!!"
        return self.update_id



class telegram:

    update_id = None

    def __init__(self, token):
        self.__token = token
        self.__update_id = -1
        self.__updates = []
        self.update_id = 0

    def set_token(self, token):
        if isDebugOn:
            print("[DEBUG] Adding a new TG_BOT_TOKEN: %s" % (self.__token))

    def get_updates(self):
        if isDebugOn:
            print("[DEBUG:22222] call get_updates")

        new_updates = UpdateMessage()
        self.update_id = new_updates.getUpdates(100, 999999999999999)
        # self.__updates.append(self.update_id)
        self.__updates.append(new_updates)
        # return self.__updates
        return self.__updates



def main():

    print("Starting bot.py")
    
    update_id = None

    try:
        BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')

        if isDebugOn:
            print("[DEBUG] KEY: %s" % (os.environ.get('TG_BOT_TOKEN')))
            print("TOKEN: %s" % (BOT_TOKEN))
        if not BOT_TOKEN:
            raise Exception
        if isDebugOn:
            print("Telegram bot token: %s" % BOT_TOKEN)
        print("[SIMPLE_BOT] Running...")
    except:
        print("[ERROR] Please, set your local environment variable: TG_BOT_TOKEN")
        print("USAGE: $ export TG_BOT_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>")
        exit(-1)

    bot = telegram(BOT_TOKEN)

    # dynamically setting the bot token
    bot.set_token(BOT_TOKEN)
 
    # for debugging purposes    
    if isDebugOn:
        print("[DEBUG:11111]: %s" % type(bot.get_updates()[0].update_id))
        print("[DEBUG:11111]: %s" % bot.get_updates()[0].update_id)

    try:
        update_id = bot.get_updates()[0].update_id
        if update_id is None:
            raise Exception
        if isDebugOn:
            print("[DEBUG:33333] update_id: %s" % type(update_id))
            print("[DEBUG:33333] update_id: %s" % update_id)
    except Exception:
        if isDebugOn:
            print("[DEBUG][Error] An exception was thrown: invalid update_id!")
            print("[DEBUG][UPDATE] UpdateMessage: %s" % (update_id))
        update_id = None



if __name__ == '__main__':
    main()


