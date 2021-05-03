from tkinter.constants import END
from pytube import YouTube

datas = {}

def startOrder(link, lstbxParam, labelParam):
    # Listbox Clear
    lstbxParam.delete(0, END)

    vd = YouTube(link)
    vdStream = vd.streams
    datas['vdStream'] = vdStream

    if len(vdStream) != 0:
        for i in vdStream:
            list = str(i).split('"')

            itag = list[1]
            type = vdStream.get_by_itag(itag).mime_type
            if type == 'video/mp4' or type == 'video/webm':
                quality = vdStream.get_by_itag(itag).resolution
                sound = vdStream.get_by_itag(itag).is_progressive
                data = f"order: '{itag}', type: {type}, quality: {quality}, sound = {sound}"
            else:
                quality = vdStream.get_by_itag(itag).abr
                data = f"order: '{itag}', type: {type}, quality: {quality}"

            lstbxParam.insert(0, data)
            labelParam.configure(text=vd.title)
    else:
        labelParam.configure(text='Video veya ses indirilebilir değil :(')


def download(lstbxParam, path):
    if path == '':
        path = 'media'
    selection = lstbxParam.selection_get().split("'")
    vd = datas['vdStream']
    vd.get_by_itag(selection[1]).download(path)


def downloadAudio(ent1Param, ent2Param, labelParam):
    path = ent2Param
    if path == '':
        path = 'media'

    vd = YouTube(ent1Param).streams
    if len(vd) == 0:
        labelParam.configure(text='Ses indirilebilir değil :(')
        return 0
    vd.get_by_itag('140').download(path)
    
