#!/usr/bin/python
import os


update_id = None
isDebugOn = True
BOT_TOKEN = None


class telegram:

    def __init__(self, token):
        self.__token = token
        self.__update_id = -1
        self.__updates = []

    def set_token(self, token):
        if isDebugOn:
            print("[DEBUG] Adding a new TG_BOT_TOKEN: %s" % (self.__token))

    def get_updates(self):
        if isDebugOn:
            print("[DEBUG] call get_updates")
        return self.__updates



def main():

    print("Starting bot.py")
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

    try:
        update_id = bot.get_updates()[0].update_id
        if isDebugOn:
            print("[DEBUG] update_id: %d" % (update_id))
    except Exception:
        update_id = None

if __name__ == '__main__':
    main()


