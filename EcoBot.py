import discord
import random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Activa la intención para leer el contenido de los mensajes

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! Soy EcoBot, un bot de Discord que te dara ideas basicas de ecologia.')

@bot.command()
async def ayuda(ctx):
    await ctx.send('Utiliza es simbolo / seguido de alguna de estas palabras para recibir mas informacion: ecologia (te explica que es la ecologia y sus bases), ideas (te da ideas sobre que hacer para aportar en la ecologia), ramas (te explica algunas ramas de la ecologia), org (te dice organizaciones sobre ecologia), meme (te envia memes graciosos sobre la ecologia)')

@bot.command()
async def ecologia(ctx):
    await ctx.send('La ecología es la rama de la biología que estudia las interacciones entre los organismos y su entorno, incluyendo tanto factores bióticos (seres vivos) como abióticos (elementos no vivos, como el clima o el suelo). Su objetivo es entender cómo estas interacciones influyen en la distribución y abundancia de los organismos y el funcionamiento de los ecosistemas.')

@bot.command()
async def ideas(ctx):
    await ctx.send('Reducir, reutilizar y reciclar. \n Ahorrar agua y energía. \n Plantar árboles o cuidar áreas verdes. \n Usar transporte sostenible (bicicleta, caminar, transporte público). \n Evitar plásticos de un solo uso. \n Participar en limpiezas comunitarias. \n Promover la conservación de la biodiversidad.')

@bot.command()
async def ramas(ctx):
    await ctx.send('Autoecología: Estudia la relación de una especie individual con su entorno. \n Sinecología: Analiza las interacciones entre diferentes especies dentro de una comunidad. \n Ecología de poblaciones: Se centra en las dinámicas de población de una sola especie. \n Ecología del paisaje: Examina la organización espacial y las interacciones entre ecosistemas. \n Ecología evolutiva: Estudia cómo las interacciones ecológicas influyen en la evolución. \n Ecología aplicada: Aborda problemas ambientales, como la conservación y la gestión de recursos naturales.')

@bot.command()
async def org(ctx):
    await ctx.send('El Programa de las Naciones Unidas para el Medio Ambiente (PNUMA) es una de las principales organizaciones a nivel mundial que promueve la sostenibilidad ambiental y coordina acciones internacionales en ecología y conservación del medio ambiente.')

@bot.command()
async def meme(ctx):
    # Lista de imágenes en la carpeta 'images'
    img_name = random.choice(os.listdir('images'))  # Selecciona una imagen al azar
    with open(f'images/{img_name}', 'rb') as f:  # Abre la imagen seleccionada en modo lectura binaria
        picture = discord.File(f)  # Crea un archivo de Discord con la imagen
        await ctx.send(file=picture)  # Envía la imagen al canal de Discord

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Ocurrió un error: {error}')

bot.run('TU TOKEN')
