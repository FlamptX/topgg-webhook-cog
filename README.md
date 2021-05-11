# Top.gg Webhook Cog
This is for everyone who is struggling with implementing top.gg votes in the bot and handling them.

Webhook.py is a discord.py cog that starts an aiohttp webserver and listens for posts on route `/dbl` and when a user votes for the bot a function runs, but in this example it sends a dm to the user.
## First step
Before using this you have to fill two things in the confix.txt file.

The `auth` value can be whatever you want, it is used to protect the webhook so that only top.gg and you can use it.

The `token` value is your bots token.

## Second step
Go to top.gg and add your bot if you haven't. After that go to its edit page and click on the webhooks section.

The `Webhook URL` field will be the URL of the webhook in Webhook.py Now the webhook URL is: **HTTP(S) + domain + /dbl**.
The domain depends on the bots host. If you were to host it on your machine it would something like to 127.0.0.1:5000

The `Authorization` filed has to be the same as the `auth` value in the config file.

#### That's it
I would appreciate credit if you are using it publicly but it's no big deal.
Tell me if I forgot anything.

Discord: Flampt#4460