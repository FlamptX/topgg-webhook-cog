from aiohttp import web
from discord.ext import commands, tasks
import discord
from configparser import ConfigParser
parser = ConfigParser()
parser.read("conifg.txt")
auth = parser.get('config', 'auth')

app = web.Application()
routes = web.RouteTableDef()

class Webhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.web_server.start()

        @routes.post('/dbl')
        async def dblwebhook(request):
            if request.headers.get('authorization') == auth:
                data = await request.json()
                user = self.bot.get_user(data['user']) or await self.bot.fetch_user(data['user'])
                if user is None:
                    return
                _type = 'testing' if data['type'] == 'test' else 'voting for'
                embed = discord.Embed(title=_type, colour=discord.Color.blurple())
                embed.description = f'Thanks for {_type} the bot!.'
                embed.set_thumbnail(url=user.avatar_url)
                await user.send(embed=embed)
                return web.Response(text='success', status=200)
            else:
                return web.Response(text='Unauthorized', status=400)

        app.add_routes(routes)

    @tasks.loop()
    async def web_server(self):
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host='0.0.0.0', port=2000)
        await site.start()

    @web_server.before_loop
    async def web_server_before_loop(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Webhook(bot))
