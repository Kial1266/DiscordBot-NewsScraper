import discord

def setup_events(client):
    """
    Function to setup events when bot starts
    """

    @client.event
    async def on_ready():
        """Function called when the client is connected."""
        print(f'We have logged in as {client.user}')

    # @client.event
    # async def on_message(message):
    #     """Function called when a message is received."""
    #     if message.author == client.user:
    #         return



