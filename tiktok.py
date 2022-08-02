from moviepy.editor import VideoFileClip
import os

url = 'https://v16-webapp.tiktok.com/41197fd839a099a2aa50cf257a4dd820/62e93bd5/video/tos/useast2a/tos-usea' \
      'st2a-pve-0068/68e17727aec140108911aa33dadef421/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=' \
      '1&br=1886&bt=943&btag=80000&cs=0&ds=3&ft=ar5S8qT2mo0PDV9v_uaQ9me1~ObpkV1PCf&mime_type=video_mp4&qs=0&rc=N2' \
      'ZkaDtlZjQ8NTlkOWY6PEBpanc8NWg6ZnI5ZDMzNzczM0BhYzYxYmItXi8xLS01NWI1YSMybmM0cjRvbWlgLS1kMTZzcw%3D%3D&l=2022080' \
      '2085812010190186038220717B0'


def gif(url):
    clip = VideoFileClip(url)
    clip.write_gif("output.gif", fps=1)

    scr = "output.gif"
    dest = os.path.expanduser("~") + "/Документи/output.gif"

    os.replace(scr, dest)

gif(url)