import discord,logging,re,subprocess,magic,sys,os,mci,anna

def main():
    help_text = r"""
                    The following commands and features are available:

                    Echo command will echo back what you typed, example !echo hello Anna
                    Help command will display this help message example !help
                    Reboot command will cause me to attempt a reboot, example !reboot
                    Exit command will cause me to become very turned off, example !exit (admins only)
                    Add command will add an admin, example !add <name> (admins only)
                    Rm command will remove an admin example !rm <name> (admins only)
                    ------------------------------------------------------------------
                    You can also type the name of a magic card withing square brackets 
                    and have me fetch an image of that card, example [forest]
                    You can also use double square brackets for a search using magiccards.info syntax,
                    example [[o:flashback]],this method of searching is considerately faster.
                    See website for more info regarding syntax. 
                    -------------------------------------------------------------------
                    My source code and licence is available on github.com/Oliv95/Anna"""
    client = discord.Client()
    bot = anna.Anna(client,help_text)

    @client.event
    def on_ready():
        print("admins are: " + str(bot.admins))
        print("head admins are: " + str(bot.head_admins))
        print("logged in as")
        print(client.user.name)
        print("id is ")
        print(client.user.id)
        print("servers connected to: " + str(client.servers))
        print('--------')

    @client.event
    def on_message(message):
        bot.log_msg(message)
        if message.author.name == 'Anna':
            return
        elif '[' in message.content:
            bot.fetch_card_cmd(message)
        elif message.content.startswith('!echo'):
            bot.echo_msg(message)
        elif message.content.startswith('!help'):
            bot.help_msg(message)
        elif message.content.startswith('!add'):
            bot.add_admins(message)
        elif message.content.startswith('!rm'):
            bot.rm_admins(message)
        elif message.content.startswith('!reboot'):
            bot.reboot_cmd(message)
        elif message.content.startswith('!exit'):
            bot.exit_cmd(message)

    client.run()

if __name__ == "__main__":
    main()
