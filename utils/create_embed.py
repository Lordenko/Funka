import disnake
import asyncio
from disnake.ext import commands
from dataclasses import dataclass, field
import datetime

@dataclass
class Embed_Field:
    name: str = ''
    value: str = ''
    inline: bool = False

@dataclass
class CustomEmbed:
    #channel
    channel: disnake.channel

    #standart embed
    title: str = ''
    description: str = ''
    general_icon_url: str = '' # small img (right)
    color: disnake.Colour = disnake.Colour.purple() # border-left color
    timestamp: datetime.datetime = datetime.datetime.now()

    #addition content
    #author
    author_name: str = ''
    author_url: str = ''
    author_icon_url: str = ''
    
    #footer
    footer_text: str = ''
    footer_icon_url: str = ''

    #big image
    big_image_url: str = ''

    #logo image
    logo_image_url: str = ''

    #Field
    fields: list[Embed_Field] = field(default_factory=list)

    async def create_embed(self):
        embed = disnake.Embed(
            title=self.title,
            description=self.description,
            url=self.general_icon_url,
            color=self.color,
            timestamp=self.timestamp,
        )
        
        if self.author_name:
            embed.set_author(
                name=self.author_name,
                url=self.author_url,
                icon_url=self.author_icon_url,
            )
        
        if self.footer_text:
            embed.set_footer(
                text=self.footer_text,
                icon_url=self.footer_icon_url,
            )

        if self.big_image_url:
            embed.set_image(url=self.big_image_url)

        if self.logo_image_url:
            embed.set_thumbnail(url=self.logo_image_url)

        if self.fields:
            for field in self.fields:
                embed.add_field(name=field.name, value=field.value, inline=field.inline)

        await self.channel.send(embed=embed)