from urllib.parse import urlparse
from discord_webhook import DiscordEmbed, DiscordWebhook
import random
from modules.logger import Customlogger, Logger_type
from modules.pdf import convert_webpage_to_pdf
from modules.variables import discord_webhook

# List of 20 hex color codes
hex_colors = [
    '03b2f8', 'ff6347', '008080', '7cfc00', '9932cc',
    'ffa500', '00ced1', 'ff4500', '8a2be2', '008000',
    'ff69b4', '4682b4', 'b0c4de', 'f08080', 'dda0dd',
    '00ff00', '800080', '808000', 'ff8c00', '87cefa'
]

def notify(args , writeup):

    
    # Webhook x 
    main_webhook_channel_x = ""

    webhook_main , webhook_x  = DiscordWebhook.create_batch(urls=[discord_webhook , main_webhook_channel_x] , rate_limit_retry=True)
    
    domain = urlparse(writeup['Links'][0]['Link']).netloc
    
    embed = DiscordEmbed()
    embed.set_color(random.choice(hex_colors))
    embed.set_title(f"{writeup['Links'][0]['Title']}")
    embed.set_url(writeup['Links'][0]['Link'])
    embed.add_embed_field(name=f"Programs", value=f"{', '.join(writeup['Programs'])}" , inline=False)
    embed.add_embed_field(name=f"Bugs", value=f"{', '.join(writeup['Bugs'])}" , inline=False)
    
    bounty_value = f"${writeup['Bounty']}" if writeup['Bounty'] != '-' else writeup['Bounty']
    embed.add_embed_field(name=f"Bounty", value=f"{bounty_value}" , inline=False)
    
    embed.add_embed_field(name=f"Publish date", value=f"{writeup['PublicationDate']}" , inline=False)
    embed.add_embed_field(name=f"Write-up source", value=f"https://{domain}" , inline=False)
    embed.set_timestamp()
    embed.set_author(name=f"{', '.join(writeup['Authors'])}")
    embed.set_thumbnail(url=f"https://{domain}")
    
    if args.pdf:
        output_name = f"{writeup['Links'][0]['Title']}.pdf"
        link_to_convert = writeup['Links'][0]['Link']
        output = convert_webpage_to_pdf(link_to_convert , output_name)
        if output:
            with open(output, "rb") as f:
                content = f.read()
                webhook_main.add_file(file=content, filename=output_name)
                # webhook_x.add_file(file=f.read(), filename="example.jpg")
        else:
            Customlogger(True, f"[-] Problem with converting to PDF --> {link_to_convert} ", Logger_type.ERROR)
            
    try:
        # Send to main channel
        webhook_main.add_embed(embed)
        response = webhook_main.execute()
        
        
        # Send to other servers
        # webhook_x.add_embed(embed)
        # response_x = webhook_x.execute()
        
        
        if response.status_code == 204 or 200:
            Customlogger(True, f"[+] Alert successfully sent data to Discord", Logger_type.INFO)
        else:
            Customlogger(True, f"[-] Problem with sending alert to Discord -> status code {response.status_code}", Logger_type.ERROR)
    except Exception as e:
            Customlogger(True, f"[-] Error occured : {e}", Logger_type.ERROR)
    