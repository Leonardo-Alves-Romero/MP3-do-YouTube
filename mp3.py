# Primeiro instalar as bibliotecas 'pytube' e 'moviepy' e importar no código
from pytube import YouTube
import moviepy.editor as mp
import re
import os

# Link do video que desejar pegar o áudio  
link = input('Digite o link do video que deseja baixar: ')

# Pasta onde vai salvar o arquivo
path = input('Digite o diretório que deseja salvar o vídeo: ')
yt = YouTube(link)

# Baixando o video
print('Baixando...')
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Dawnload completo!!")

# Convertendo em áudio e salvando na pasta
print('Convertendo arquivo...')
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print('sucesso!')