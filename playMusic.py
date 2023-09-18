# Faz o python executar um arquivo mp3
from pygame import mixer
from pygame import time
import os

def playMusic(songContains):
    musicName = findsSongOnDir(songContains)
    mixer.init()
    music = mixer.Sound(musicName)
    channel = music.play()
    print(f'Playing {songContains}')

    # Não para a musica enquanto não houver terminado a faixa
    while channel.get_busy():
        time.wait(100) 
    print ("Finished.")

# Acha uma musica dentro do diretorio que contenha a palavra enviada
def findsSongOnDir(songContains):

    # Percorre todos os arquivos no diretório
    for nome_arquivo in os.listdir("./songs"):
        if songContains in nome_arquivo:
            songPath = os.path.join('./songs', nome_arquivo)
            if os.path.isfile(songPath):
                songPath = songPath.replace('/','\\')

    if songPath:
        return songPath

playMusic('Batalha')
