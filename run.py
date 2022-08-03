from nike.nike import Nike

from configparser import ConfigParser

config = ConfigParser()
config.read("config_.ini")

bot = Nike(config)

bot.land_item_page()
print("logging in...")
bot.login()
bot.purchase()
print("Purchase complete!")
