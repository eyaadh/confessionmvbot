# confessionmvbot:
A telegram bot intended for confession channels, the users confess to the bot and for approval the bot forwards the confessions to a group which contains admins for the channel - so that they can review the confession and post it to the channel accordingly.

## Cloning and Run:
1. `https://github.com/eyaadh/confessionmvbot.git`, to clone the repository.
2. `cd confessionmvbot`, to enter the directory.
3. `pip3 install -r requirements.txt`, to install rest of the dependencies/requirements.
4. Create a new `config.ini` using the sample available at `config.ini.sample`.
   > - More info on API_ID and API_HASH can be found here: https://docs.pyrogram.org/intro/setup#api-keys
   > - More info on Bot API Key/token can be found here: https://core.telegram.org/bots#6-botfather
5. Run with `python3.8 main.py`, stop with <kbd>CTRL</kbd>+<kbd>C</kbd>.
> It is recommended to use [virtual environments](https://docs.python-guide.org/dev/virtualenvs/) while running the app, this is a good practice you can use at any of your python projects as virtualenv creates an isolated Python environment which is specific to your project.
