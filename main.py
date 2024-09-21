import yt_dlp


def baixar_audio_mp3(url_video, caminho_salvar):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': caminho_salvar + '/%(title)s.%(ext)s',
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_video])

        print(f"Áudio baixado com sucesso!")
    except Exception as e:
        print("Ocorreu um erro:", e)


pasta = input("DIGITE A PASTA PARA SALVAR OS MP3: ")

while True:
    video_url = input("URL: ")
    output_path = f"mp3/{pasta}"
    baixar_audio_mp3(video_url, output_path)
