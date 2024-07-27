
users = [5692000351]
#EL PRIMER USUARIO ES EL ADMIN, LOS USUARIOS VAN SEPARADOS POR , EN FORMA QUE QUEDA [0000000,0000000,0000000]
cloud_space_gb = 10
#ALMACENAMIENTO EN NUBE POR USUARIO
space_control = True
#SI SE VA A CONTROLAR EL ALMACENAMIENTO LOCAL
space_local = 5
#ALMACENAMIENTO LOCAL POR USUARIO EN GB
cola_download = True
bitzero = 1
api_id = 9024532
api_hash = '131b576240be107210aace99a5f5c5b0'
bot_token = "6446287319:AAHCl-e2ShbqlOM90t2pwqI71LHvsjHntzI"
start_msg = ""
key = ""
ghost = "https://revistatelematica.cujae.edu.cu/index.php/tele"
guser = "techdev"
gpass = "@A1a2a3mo"
grepo = 634
zips = 14

import subprocess
try:
    import requests
except:
    subprocess.run(["pip","install","requests"])
    import requests
try:
    from bs4 import BeautifulSoup
except:
    subprocess.run(["pip","install","bs4"])
    from bs4 import BeautifulSoup
import random
try:
    from telethon.sync import TelegramClient, events, Button, types
except:
    subprocess.run(["pip","install","telethon"])
    from telethon.sync import TelegramClient, events, Button, types
from os.path import exists
import os
import asyncio
import urllib
import threading
import time
import json
import urllib3
import shutil
import aiohttp
import base64
import urllib.parse
from pytube import YouTube
import zipfile
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
nube = []
backup_file = "backup.json"
account_file = "account.json"
backup_interval = 3
def save_backup():
    global nubes
    while True:
        with open(backup_file, 'w') as f:
            json.dump(nubes, f)
        time.sleep(backup_interval)
def load_backup():
    with open(backup_file, 'r') as f:
        return json.load(f)
if exists(backup_file):
    nubes = load_backup()
    print("BACKUP IMPORTADO")
else:
    nubes = []
def save_account():
    global ghost
    global guser
    global gpass
    global grepo
    global bitzero
    while True:
        with open(account_file, 'w') as fa:
            fa.write(f"{ghost} {guser} {gpass} {grepo} {bitzero}")
        time.sleep(backup_interval)
def load_account():
    global ghost
    global guser
    global gpass
    global grepo
    global bitzero
    with open(account_file, 'r') as fa:
        sta = fa.read()
        ghost = sta.split(" ")[0]
        guser = sta.split(" ")[1]
        gpass = sta.split(" ")[2]
        grepo = sta.split(" ")[3]
if exists(account_file):
    load_account()
    print("ACCOUNT IMPORTADO")
backup_thread = threading.Thread(target=save_backup)
backup_thread.daemon = True
backup_thread.start()
account_thread = threading.Thread(target=save_account)
account_thread.daemon = True
account_thread.start()
procesos = []
for u in users:
    nubes.append({"user":u,"nube":[]})
cc = 0
cloud_space = cloud_space_gb*1024*1024*1024
timed = time.time()
async def upload_div(ruta_archivo,user_id, msg_id, tamano_parte_mb, cd):
    tamano_parte_bytes = tamano_parte_mb * 1024 * 1024
    lista_archivos_divididos = []
    tamano_archivo = os.path.getsize(cd+"/"+ruta_archivo)
    if tamano_archivo < tamano_parte_bytes:
        open(cd+"/temp/"+ruta_archivo,"wb").write(open(cd+"/"+ruta_archivo,"rb").read())
        lista_archivos_divididos.append(ruta_archivo)
    else:
        with open(cd+"/"+ruta_archivo, 'rb') as archivo_original:
            numero_parte = 1
            while True:
                contenido_parte = archivo_original.read(tamano_parte_bytes)
                if not contenido_parte:
                    break
                nombre_parte = f"{ruta_archivo}_parte_{numero_parte}"
                with open(cd+"/temp/"+nombre_parte, 'wb') as archivo_parte:
                    archivo_parte.write(contenido_parte)
                lista_archivos_divididos.append(nombre_parte)
                numero_parte += 1
    return lista_archivos_divididos
async def ziper(file, user_id, msg_id, zips):
    file_size = os.path.getsize(file)
    zipy = int(zips) * 1024 * 1024
    filed = []
    if file_size > zipy:
    	mult_file = zipfile.MultiFile(file,zipy)
    	zip = zipfile.ZipFile(mult_file,  mode='w', compression=zipfile.ZIP_DEFLATED)
    	zip.write(file)
    	zip.close()
    	mult_file.close()
    	ti = 1
    	te = True
    	await bot.edit_message(user_id, msg_id, "<b>[✓]</b> #seven #local\n\n<code>Dividido</code>", parse_mode='HTML')
    	while te:
    		if exists(file+'.7z.{:03d}'.format(ti)):
    			file_named = file+'.7z.{:03d}'.format(ti)
    			ti += 1
    			filed.append(file_named.split("/")[-1])
    		else:
    			te = False
    else:
    	filed = [file.split("/")[-1]]
    return filed
def new_process(pid):
    global procesos
    procesos.append(pid)
def wait_process(pid):
    global procesos
    if procesos[0] == pid:
        return True
    else:
        for w in range(len(procesos)):
            if procesos[w] == pid:
                return w
def fin_process(pid):
    global procesos
    procesos.remove(pid)
def rm_process():
    global procesos
    procesos = []
def o85ea6(eu6363):
	  texto_desencriptado = base64.b64decode(eu6363.encode()).decode()
	  return texto_desencriptado
def gptd(value):
	nonce = requests.get("https://chatgpt.ch/")
	wpnonce = nonce.text.split('data-nonce="')[1].split('"')[0]
	a73664 = "aHR0cHM6Ly9jaGF0Z3B0LmNoL3dwLWFkbWluL2FkbWluLWFqYXgucGhw"
	e657674 = "X3dwbm9uY2U="
	u636e64 = "aHR0cHM6Ly9jaGF0Z3B0LmNoL2Vz"
	d633e64 = "dXJs"
	chatGPT = requests.post(o85ea6(a73664), data={
  o85ea6(e657674): wpnonce,
  o85ea6(d633e64): o85ea6(e657674),
  o85ea6("bWVzc2FnZQ=="): value,
  o85ea6("cG9zdF9pZA=="):106,
  o85ea6("YWN0aW9u"):o85ea6("d3BhaWNnX2NoYXRfc2hvcnRjb2RlX21lc3NhZ2U="),
  o85ea6("Ym90X2lk"):0
  })
	data_bytes = bytes(chatGPT.text, "utf-8")
	data = data_bytes.decode('utf-8')
	data_dict = json.loads(data)
	response = data_dict['data']
	return response
async def download_file(url, bot, user, msg, cd):
    size=0
    timed = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                file_size = response.headers.get('Content-Length')  # Tamaño del archivo
                try:
                    file_name = response.headers.get('Content-Disposition').split('"')[1]  # Nombre original del archivo
                except:
                    file_name = url.split('/')[-1]
                if not file_name == '':
        			                rename = 2
        			                filename_o = file_name
        			                while True:
        			                          if os.path.exists(cd+"/"+file_name):
        			                              file_name = f"c{rename}_"+filename_o
        			                              rename += 1
        			                          else:
        			                              break
                with open(cd+"/"+file_name, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        size+=1024
                        if time.time() - timed > 1.0:
                            timed = time.time()
                            porcentaje = (size/int(file_size))*100
                            barra = "<code>[</code>"+"<b>•</b>"*round(porcentaje/3.33333)+"<i> </i>"*round((100-porcentaje)/3.33333)+"<code>]</code>"
                            await bot.edit_message(user, msg, f"[•] #wget #local #enproceso\n\n<code>{file_name}</code>\n\n<i>{round(porcentaje, 1)}%</i>  <b>{sizeof_fmt(size)}|{sizeof_fmt(int(file_size))}</b>\n{barra}", parse_mode="HTML")
                        if not chunk:
                            break
                        f.write(chunk)
def comprimir_carpeta(nombre_carpeta, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for raiz, directorios, archivos in os.walk(nombre_carpeta):
            for archivo in archivos:
                ruta_archivo = os.path.join(raiz, archivo)
                zipf.write(ruta_archivo, os.path.relpath(ruta_archivo, nombre_carpeta))
def getsize_path(ruta):
    return sum(os.path.getsize(os.path.join(carpeta_actual, archivo))
               for carpeta_actual, subcarpetas, archivos in os.walk(ruta)
               for archivo in archivos)
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Yi', suffix)
def unlink(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
def isuser(u):
    global users
    for user in users:
        if user == u:
            return True
    return False
async def upload(path, host, username, password, repo, session, chat_id, user_id):
    global bitzero
    global ghost
    global guser
    global gpass
    global grepo
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
    if bitzero == 1:
        spypng = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xf6\x178U\x00\x00\x00\x00IEND\xaeB`\x82'
        open(path+f"_#{user_id}@bitzero.png","wb").write(spypng+open(path,"rb").read())
        os.unlink(path)
        path = path+f"_#{user_id}@bitzero.png"
    elif bitzero == 2:
        spypng = '<!DOCTYPE html>\n<html lang="es">\n<bytes>'
        spypng2 = '</bytes></html>'
        with open(path, 'rb') as file:
            bytes_data = file.read()
        base64_data = base64.b64encode(bytes_data).decode('utf-8')
        open(path+f"_#{user_id}@bitzero.html","w").write(spypng+base64_data+spypng2)
        os.unlink(path)
        path = path+f"_#{user_id}@bitzero.html"
    else:
        None
    with session as upload:
            submission_page = upload.get(f"{ghost}/submission/wizard/2?submissionId={grepo}#step-2", headers=headers,verify=False)
            token = submission_page.text.split('"csrfToken":"')[1].split('"')[0]
            # Realizar la carga del archivo
            files_data = {
                "fileStage": "2",
                "name[es_ES]": path,
                "name[en_US]": path
            }
            files = {
                "file": open(path, "rb")
            }
            headers["X-Csrf-Token"] = token
            file_upload = upload.post(f"{ghost}/api/v1/submissions/{grepo}/files", data=files_data, files=files, headers=headers,verify=False)
            # Obtener el ID del archivo subido
            print(file_upload.text)
            file_id = file_upload.text.split('_href":"')[1].split('"')[0].replace("\/", "/").split("/")[-1]
            # Generar el enlace de descarga del archivo
            link = file_id
            return link
async def delete_cloud(fileId, up):
    global bitzero
    global ghost
    global guser
    global gpass
    global grepo
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
    csrfToken = up.get(f"{ghost}/submission/wizard/2?submissionId={grepo}", headers=headers).text.split('csrfToken":"')[1].split('",')[0]
    t = up.post(f"{ghost}/api/v1/submissions/{grepo}/files/{fileId}?stageId=1",headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36","x-http-method-override": "DELETE","x-requested-with":"XMLHttpRequest","x-csrf-token":csrfToken})
bot = TelegramClient(f'BitZerOT', api_id, api_hash).start(bot_token=bot_token)
if not os.path.exists("./database"):
    os.mkdir("./database")
@bot.on(events.NewMessage)
async def techdev_bot(event):
	global users
	global nubes
	global cola_download
	global bitzero
	global ghost
	global guser
	global gpass
	global grepo
	global zips
	global start_msg
	text = event.raw_text
	user_id = event.message.chat.id
	msg_id = event.message.id
	username = event.message.chat.username
	current = 0
	for n in nubes:
	    if n["user"] == user_id:
	        user_nube = current
	        break
	    else:
	        current += 1
	nube = nubes[user_nube]
	if not os.path.exists("./database/"+str(user_id)):
	    os.mkdir("./database/"+str(user_id))
	    os.mkdir("./database/"+str(user_id)+"/files")
	    open("./database/"+str(user_id)+"/log","w").write("[!] USUARIO CREADO\n")
	    open("./database/"+str(user_id)+"/cd","w").write("./database/"+str(user_id)+"/files")
	open("./database/"+str(user_id)+"/log","w").write(f"[!] {msg_id} | {text}\n")
	cd = os.path.normpath(open("./database/"+str(user_id)+"/cd", "r").read())
	size_local = getsize_path(cd)
	if size_local >= space_local*1024*1024*1024 and space_control:
	    sobrepaso = True
	else:
	    sobrepaso = False
	if '/start' == text and isuser(user_id):
	    local_files = sorted(os.listdir(cd))
	    local_files_text = ""
	    listar = 0
	    cloud_size = 0
	    for nub in nubes[user_nube]["nube"]:
	        cloud_size += nub["size"]
	    for dir in local_files:
	        if os.path.isfile(cd+"/"+dir):
	            local_files_text += str(listar)+" 📄 "+dir+"\n"
	        else:
	            local_files_text += "<b><i>"+str(listar)+"</i></b> 📂 <code>"+dir+"</code>\n"
	        listar += 1
	    if len(local_files) == 0:
	        local_files_text += "🤷🏻‍♂️<i>Sin Archivos</i>\n"
	    if start_msg == "":
	        await bot.send_message(user_id, f"<b><-- BitZero [PkP] --></b>\n\n<b>☁️ Nube:</b> <code>{ghost}</code>\n<b>👤 Usuario:</b> <code>{guser}</code>\n<b>🔐 Contraseña:</b> <i>********</i>\n<b>📂 Repo:</b> <code>{grepo}</code>\n<b>🔼 BitZero:</b> <code>{bitzero}</code>\n📚 <b>Zips:</b> <code>{zips}</code>\n\n<i>Acerca de:</i> /about\n<i>Creado por:</i> @l_tech_dev_l", parse_mode="HTML")
	    else:
	        await bot.send_message(user_id, f"<b><-- BitZero [PkP] --></b>\n\n{start_msg}\n\n<i>Acerca de:</i> /about\n<i>Creado por:</i> @l_tech_dev_l", parse_mode="HTML")
	elif (sobrepaso and isuser(user_id)) and not ("/ls" == text or "/rm " in text or "/up " in text):
	    await bot.send_message(user_id, f"<b>⚠️Almacenamiento lleno:</b><code>{sizeof_fmt(size_local)} / {sizeof_fmt(space_local*1024*1024*1024)}</code>\n<i>Use el comando /rm para eliminar.</i>", parse_mode="HTML")
	elif "/ls" == text and isuser(user_id):
	    size_files = sizeof_fmt(getsize_path(cd))
	    local_files = sorted(os.listdir(cd))
	    local_files_text = f"<b>Usado: </b><code>{size_files} / {sizeof_fmt(space_local*1024*1024*1024)}</code>\n\n"
	    listar = 0
	    for dir in local_files:
	        if os.path.isfile(cd+"/"+dir):
	            size = os.path.getsize(cd+"/"+dir)
	            local_files_text += str(listar)+" 📄 <code>"+dir+f"</code> | {sizeof_fmt(size)}\n"
	        else:
	            local_files_text += "<b><i>"+str(listar)+"</i></b> 📂 <code>"+dir+"</code>\n"
	        listar += 1
	    if len(local_files) == 0:
	        local_files_text += "🤷🏻‍♂️<i>Sin Archivos</i>\n"
	    await bot.send_message(user_id,f"[✓] #ls #local\n\n{local_files_text}", parse_mode="HTML")
	elif "/set_cloud " in text and user_id == users[0]:
	    ghost = text.split(" ")[1]
	    guser = text.split(" ")[2]
	    gpass = text.split(" ")[3]
	    grepo = text.split(" ")[4]
	    await bot.send_message(user_id,f"[✓] #cloud_change #local #creado\n\n<code>Editado!!</code>", parse_mode="HTML")
	elif "/mkdir" in text and isuser(user_id):
	    path = text.replace("/mkdir ","")
	    os.mkdir(cd+"/"+path)
	    await bot.send_message(user_id,f"[✓] #mkdir #local\n\n<code>Directorio generado</code>", parse_mode="HTML")
	elif "/rm " in text and isuser(user_id):
	       local_files = sorted(os.listdir(cd))
	       if "-" in text:
	        lisc = list(range(int(text.split("-")[0].split(" ")[1]),int(text.split("-")[1].split(" ")[0])+1))
	        text =  "/rm "+' '.join(map(str,lisc))
	       elif "all" in text:
	           text = "/rm "+' '.join(map(str,list(range(0,len(local_files)))))
	       rm_text = ""
	       rm = text.replace("/rm ","")
	       rm = rm.split(" ")
	       cdir = os.path.dirname(os.path.abspath(__file__))
	       for r in rm:
	           try:
	               unlink(cd+"/"+local_files[int(r)])
	           except:
	               await bot.send_message(user_id,f"[×] #rm #local\n\n<code>Directorio {r} inexistente</code>", parse_mode="HTML")
	       await bot.send_message(user_id,f"[✓] #rm #local\n\n<code>Directorio/s eliminado/s</code>", parse_mode="HTML")
	elif "/cwd" == text:
	    await bot.send_message(user_id,"[✓] #cwd #local\n\n<code>"+cd.replace('database/'+str(user_id)+'/files','$'+str(user_id)+':')+"</code>",parse_mode="HTML")
	elif "/zips " in text:
	    zips = int(text.replace("/zips ",""))
	    await bot.send_message(user_id,"[✓] #zips #local\n\n<code>Tamaño de zips cambiado!!</code>",parse_mode="HTML")
	elif "/cd " in text and isuser(user_id):
	    local_files = sorted(os.listdir(cd))
	    cdc = text.split(" ")[1]
	    if cdc == "..":
	        if not f"database/{user_id}/files" == cd:
	            cd = os.path.dirname(cd)
	            open("./database/"+str(user_id)+"/cd","w").write(cd)
	            await bot.send_message(user_id,f"[✓] #cd #local\n\n<code>Directorio cambiado</code>", parse_mode="HTML")
	        else:
	            await bot.send_message(user_id,f"[✓] #cd #local\n\n<code>Ya está en root!</code>", parse_mode="HTML")
	    else:
	        try:
	            cd = cd+"/"+local_files[int(cdc)]
	            local_files = sorted(os.listdir(cd))
	            open("./database/"+str(user_id)+"/cd","w").write(cd)
	            await bot.send_message(user_id,f"[✓] #cd #local\n\n<code>Directorio cambiado</code>", parse_mode="HTML")
	        except:
	            await bot.send_message(user_id,f"[×] #cd #local\n\n<code>No existe el directorio!</code>", parse_mode="HTML")
	elif ("http://" in text or "https://" in text) and not (" https://" in text or " http://" in text) and isuser(user_id):
	    url = text
	    pid = random.randint(10000,99999)
	    new_process(pid)
	    msg_id_o = msg_id
	    msg = await event.reply(f"[•] #wget #local\n\n<code>Generando solicitud</code>", parse_mode="HTML")
	    c = 0
	    msg_id = msg.id
	    while True:
	        w = wait_process(pid)
	        if procesos[0] == pid:
	            await bot.edit_message(user_id,msg_id,f"[•] #wget #local\n\n<code>Iniciando solicitud</code>", parse_mode="HTML")
	            try:
	                await download_file(url, bot, user_id, msg_id, cd)
	                await bot.edit_message(user_id,msg_id,f"[✓] #wget #local #finalizado\n\n<code>Espere 3 segundos...</code>", parse_mode="HTML")
	                await asyncio.sleep(3)
	                await bot.edit_message(user_id,msg_id,f"[✓] #wget #local #finalizado\n\n<code>Descargado!</code>", parse_mode="HTML")
	                fin_process(pid)
	            except:
	                fin_process(pid)
	                await bot.edit_message(user_id, msg_id, f"[•] #wget #local #error\n\n<code>Error desconocido</code>", parse_mode="HTML")
	            break
	        else:
	            if not w == c:
	                c = w
	                await bot.edit_message(user_id,msg_id,f"[•] #wget #local\n\n<code>Esperando por {w} procesos</code>", parse_mode="HTML")
	                await asyncio.sleep(1)
	            else:
	                None
	                await asyncio.sleep(1)
	elif "/yt " in text and isuser(user_id):
	    url = text.split(" ")[1]
	    pid = random.randint(10000,99999)
	    new_process(pid)
	    msg = await event.reply(f"[•] #yt #local\n\n<code>Generando solicitud</code>", parse_mode="HTML")
	    msg_id = msg.id
	    c = 0
	    while True:
	        w = wait_process(pid)
	        if procesos[0] == pid:
	            try:
	                await bot.edit_message(user_id,msg_id,f"[•] #yt #local\n\n<code>Iniciando solicitud</code>", parse_mode="HTML")
	                async def progress_func(vid, chunk, bytes_remaining):
	                    size = vid.filesize
	                    title = vid.title
	                    p = ((size-(bytes_remaining))/size)*100
	                    p = str(round(p,1))+'%'
	                    await bot.edit_message(user_id,msg_id,f"[•] #yt #local #enproceso\n\n<code>{title}</code><code>{p} | {sizeof_fmt(size-bytes_remaining)}/{sizeof_fmt(size)}</code>", parse_mode="HTML")
	                await bot.edit_message(user_id,msg_id,f"[•] #yt #local #enproceso\n\n<code>Descargando</code>", parse_mode="HTML")
	                yt = YouTube(url,on_progress_callback=progress_func)
	                filename = yt.title+".mp4"
	                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
	                os.rename(filename, cd+"/"+filename)
	                await bot.edit_message(user_id,msg_id,f"[✓] #yt #local #finalizado\n\n<code>{yt.title}</code><code>Finalizado!!</code>", parse_mode="HTML")
	                fin_process(pid)
	            except:
	                fin_process(pid)
	                await bot.edit_message(user_id, msg_id, f"[×] #yt #local #error\n\n<code>Error desconocido</code>", parse_mode="HTML")
	            break
	        else:
	            if not w == c:
	                c = w
	                await bot.edit_message(user_id,msg_id+1,f"[•] #yt #local\n\n<code>Esperando por {w} procesos</code>", parse_mode="HTML")
	                await asyncio.sleep(1)
	            else:
	                None
	                await asyncio.sleep(1)
	elif event.media and isuser(user_id):
	    pid = random.randint(10000,99999)
	    new_process(pid)
	    msg_id_o = msg_id
	    msg = await event.reply(f"[•] #file #local\n\n<code>Generando solicitud</code>", parse_mode="HTML")
	    msg_id = msg.id
	    c = 0
	    while True:
	        w = wait_process(pid)
	        if not cola_download or procesos[0] == pid:
	            try:
	                await bot.edit_message(user_id,msg_id,f"[•] #file #local\n\n<code>Iniciando solicitud</code>", parse_mode="HTML")
	                if event.file:
        			        file_path = cd+"/"
        			        filename = ''
        			        if True:
        			            attributes = event.media.document.attributes
        			            for attr in attributes:
        			              if isinstance(attr, types.DocumentAttributeFilename):
        			                  filename = attr.file_name
        			            async def downprog(c,t):
        			                global timed
        			                global cc
        			                if not c == cc and (time.time()-timed)>3.0:
        			                    timed = time.time()
        			                    cc = c
        			                    porcentaje = (c/int(t))*100
        			                    barra = "<code>[</code>"+"<b>•</b>"*round(porcentaje/3.33333)+"<i> </i>"*round((100-porcentaje)/3.33333)+"<code>]</code>"
        			                    if filename == '':
        			                        await bot.edit_message(user_id, msg_id, f"[•] #file #local #enproceso\n\n<code>Nombre indefinido</code>\n\n<i>{round((c/t)*100, 1)}%</i>  <b>{sizeof_fmt(c)}|{sizeof_fmt(int(t))}</b>\n{barra}", parse_mode="HTML")
        			                    else:
        			                        await bot.edit_message(user_id, msg_id, f"[•] #file #local #enproceso\n\n<code>{filename}</code>\n\n<i>{round((c/t)*100, 1)}%</i>  <b>{sizeof_fmt(c)}|{sizeof_fmt(int(t))}</b>\n{barra}", parse_mode="HTML")
        			            if not filename == '':
        			                rename = 2
        			                filename_o = filename
        			                while True:
        			                          if os.path.exists(cd+"/"+filename):
        			                              filename = f"c{rename}_"+filename_o
        			                              rename += 1
        			                          else:
        			                              break
        			            file_path = os.path.join(file_path, filename)
        			            download = await bot.download_media(event.media, file=file_path, progress_callback=downprog)
	                await bot.edit_message(user_id,msg_id,f"[✓] #file #local #finalizado\n\n<code>Espere 3 segundos</code>", parse_mode="HTML")
	                await asyncio.sleep(3)
	                await bot.edit_message(user_id,msg_id,f"[✓] #file #local #finalizado\n\n<code>Descargado!</code>", parse_mode="HTML")
	                await asyncio.sleep(3)
	                fin_process(pid)
	            except:
	                fin_process(pid)
	                await bot.edit_message(user_id, msg_id, f"[•] #file #local #error\n\n<code>Error desconocido</code>", parse_mode="HTML")
	            break
	        else:
	            if not w == c:
	                c = w
	                await bot.edit_message(user_id,msg_id,f"[•] #file #local\n\n<code>Esperando por {w} procesos</code>", parse_mode="HTML")
	                await asyncio.sleep(1)
	            else:
	                None
	                await asyncio.sleep(1)
	elif "/split " in text and isuser(user_id):
	    local_files = sorted(os.listdir(cd))
	    file = local_files[int(text.split(" ")[1])]
	    size = int(text.split(" ")[2])
	    pid = random.randint(10000,99999)
	    new_process(pid)
	    msg = await event.reply(f"[•] #split #local\n\n<code>Generando solicitud</code>", parse_mode="HTML")
	    msg_id = msg.id
	    c = 0
	    while True:
	        w = wait_process(pid)
	        if procesos[0] == pid:
	            try:
	                await bot.edit_message(user_id,msg_id,f"[•] #split #local #enproceso #allpower\n\n<code>Dividiendo su archivo...</code>", parse_mode="HTML")
	                await ziper(cd+"/"+file, user_id, msg_id, size)
	                fin_process(pid)
	            except:
	                fin_process(pid)
	                await bot.edit_message(user_id, msg_id, f"[•] #split #local #error\n\n<code>Error desconocido</code>", parse_mode="HTML")
	            break
	        else:
	            if not w == c:
	                c = w
	                await bot.edit_message(user_id,msg_id,f"[•] #split #local\n\n<code>Esperando por {w} procesos</code>", parse_mode="HTML")
	                await asyncio.sleep(1)
	            else:
	                None
	                await asyncio.sleep(1)
	elif "/mv " in text and isuser(user_id):
	    local_files = sorted(os.listdir(cd))
	    try:
	        file = text.split(" ")[1]
	        if "-" in file:
	            files = list(range(int(file.split("-")[0]), int(file.split("-")[1])))+([int(file.split("-")[1])])
	        else:
	            files = [file]
	        try:
	            if text.split(" ")[2] == "..":
	                carpeta = str(os.path.normpath(cd+"/.."))+"/{file_name}"
	            else:
	                carpeta = cd+"/"+local_files[int(text.split(" ")[2])]+"/{file_name}"
	        except:
	            carpeta = cd+"/"+text.split(" ")[2]
	        number = 1
	        for f in files:
	            file = local_files[int(f)]
	            os.rename(cd+"/"+file, carpeta.replace("{file_name}", file).replace("##","{:03d}".format(number)))
	            number += 1
	        await bot.send_message(user_id,f"[✓] #mv #local\n\n<code>Movido satisfactoriamente!</code>", parse_mode="HTML")
	    except:
	        await bot.send_message(user_id,f"[×] #mv #local #error\n\n<code>Algún directorio no existe!</code>", parse_mode="HTML")
	elif "/savec" in text and isuser(user_id):
	    open("./database/"+str(user_id)+"/cloud_state","w").write(str(nube))
	    await bot.send_message(user_id,f"[✓] #save #cloud\n\n<code>Base de datos guardada!</code>", parse_mode="HTML")
	elif "/url " in text and isuser(user_id):
	    if "-" in text:
	        lisc = list(range(int(text.split("-")[0].split(" ")[1]),int(text.split("-")[1].split(" ")[0])+1))
	        text =  "/url "+' '.join(map(str,lisc))
	    elif "all" in text:
	           text = "/url "+' '.join(map(str,list(range(0,len(nubes[user_nube]['nube'])))))
	    try:
	        indexs = text.replace("/url ", "").split(" ")
	    except:
	        indexs = [text.replace("/url ", "")]
	    try:
	        if not bitzero == "0":
	            msg = ""
	            key = base64.b64encode(ghost.encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")+"-"+base64.b64encode(guser.encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")+"-"+base64.b64encode(gpass.encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")+"-"+base64.b64encode(str(grepo).encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")
	            for index in indexs:
	                url = f"bitzero https://bitzero.techdev.cu/{nubes[user_nube]['nube'][int(index)]['size']}-{grepo}/{nubes[user_nube]['nube'][int(index)]['token']}/{bitzero}/{key}/{urllib.parse.quote(nubes[user_nube]['nube'][int(index)]['filename'].replace(' ','_'))}"
	                msg += url+" && "
	            msg += "/"
	            msg = msg.replace(" && /", "")
	            await event.reply(f"[✓] #token #cloud\n\n<code>{msg}</code>", parse_mode="HTML")
	        else:
	            msg = ""
	            for index in indexs:
	                tokens = nubes[user_nube]['nube'][int(index)]['token'].split("-")
	                for fileID in tokens:
	                    url = f"{ghost}/$$$call$$$/api/file/file-api/download-file?submissionFileId={fileID}&submissionId={grepo}&stageId=1"
	                    msg += url+"\n"
	            msg += "/"
	            msg = msg.replace("\n/", "")
	            name = nubes[user_nube]['nube'][int(index)]["filename"]
	            name = name.replace("."+name.split(".")[-1], ".txt")
	            open(name,"w").write(msg)
	            await bot.send_file(user_id, name)
	            os.unlink(name)
	    except:
	        await bot.send_message(user_id,f"[×] #token #cloud #error\n\n<code>Archivo inexistente!</code>", parse_mode="HTML")
	elif "/ziper " in text and isuser(user_id):
	    if "-" in text:
	        lisc = list(range(int(text.split("-")[0].split(" ")[1]),int(text.split("-")[1].split(" ")[0])+1))
	        text =  "/ziper "+' '.join(map(str,lisc))
	    elif "all" in text:
	           text = "/ziper "+' '.join(map(str,list(range(0,len(local_files)))))
	    index = int(text.replace("/ziper ",""))
	    local_files = sorted(os.listdir(cd))
	    pid = random.randint(10000,99999)
	    new_process(pid)
	    msg = await event.reply("[•] #zip #local\n\n<code>Generando solicitud</code>", parse_mode="HTML")
	    msg_id = msg.id
	    c = 0
	    while True:
	        w = wait_process(pid)
	        if procesos[0] == pid:
	            await bot.edit_message(user_id,msg_id,f"[•] #zip #local\n\n<code>Iniciando solicitud</code>", parse_mode="HTML")
	            try:
	                await bot.edit_message(user_id,msg_id,f"[•] #zip #local\n\n<code>COMPRIMIENDO....</code>", parse_mode="HTML")
	                comprimir_carpeta(cd+"/"+local_files[int(index)], cd+"/"+local_files[int(index)]+".zip")
	                fin_process(pid)
	                await bot.edit_message(user_id,msg_id,f"[✓] #zip #local\n\n<code>{local_files[int(index)]+'.zip'}\n\nComprimido</code>", parse_mode="HTML")
	            except:
	                fin_process(pid)
	                await bot.edit_message(user_id, msg_id, f"[•] #zip #local #error\n\n<code>Error desconocido</code>", parse_mode="HTML")
	            break
	        else:
	            if not w == c:
	                c = w
	                await bot.edit_message(user_id,msg_id,f"[•] #zip #local\n\n<code>Esperando por {w} procesos</code>", parse_mode="HTML")
	                await asyncio.sleep(1)
	            else:
	                None
	                await asyncio.sleep(1)
	elif "/lsc" in text and isuser(user_id):
	    files_cloud = ""
	    current = 0
	    for nub in nubes[user_nube]["nube"]:
	        files_cloud += "<code>"+str(current)+"</code> 📄 <b>"+nub["filename"]+"</b>\n"
	        current += 1
	    if len(nube) == 0:
	        files_cloud += "🤷🏻‍♂️Sin archivos"
	    await bot.send_message(user_id,f"[✓] #ls #cloud\n\n{files_cloud}", parse_mode="HTML")
	elif "/up " in text and isuser(user_id):
	    total_size = 0
	    for nub in nubes[user_nube]["nube"]:
	        total_size += nub["size"]
	    if total_size >= cloud_space:
	        await bot.send_message(user_id,f"[×] #upload #local #error\n\n<code>Nube llena! Borre!</code>", parse_mode="HTML")
	        return
	    local_files = sorted(os.listdir(cd))
	    if "-" in text:
	        lisc = list(range(int(text.split("-")[0].split(" ")[1]),int(text.split("-")[1].split(" ")[0])+1))
	        text =  "/up "+' '.join(map(str,lisc))
	    elif "all" in text:
	           text = "/up "+' '.join(map(str,list(range(0,len(local_files)))))
	    files = text.replace("/up ","").split(" ")
	    pid = random.randint(10000,99999)
	    new_process(pid)
	    msg = await event.reply(f"[•] #upload #local #enproceso\n\n<code>Generando solicitud</code>", parse_mode="HTML")
	    msg_id = msg.id
	    c = 0
	    while True:
	        w = wait_process(pid)
	        if procesos[0] == pid:
	            try:
	                if not os.path.exists(cd+"/temp"):
	                    os.mkdir(cd+"/temp")
	                await bot.edit_message(user_id,msg_id,f"[•] #upload #local #enproceso\n\n<code>Iniciando solicitud</code>", parse_mode="HTML")
	                for file in files:
	                    file = local_files[int(file)]
	                    size = os.path.getsize(cd+"/"+file)
	                    await bot.edit_message(user_id,msg_id,f"[•] #upload #local #enproceso\n\n<code>Dividiendo archivo...</code>", parse_mode="HTML")
	                    if not bitzero == 0:
	                        div = await upload_div(file, user_id, msg_id, zips, cd)
	                    else:
	                        shutil.copy(cd+"/"+file, cd+"/temp/"+file)
	                        div = await ziper(cd+"/temp/"+file, user_id, msg_id, zips)
	                    fileids = ""
	                    total = len(div)
	                    current = 0
	                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
	                    up = requests.Session()
	                    getToken = up.get(ghost+"/login",headers=headers,verify=False)
	                    token = BeautifulSoup(getToken.text,"html.parser").find('input',{'name':'csrfToken'})
	                    login_data = {"password": gpass,"remember": 1,"source": "","username": guser,"csrfToken":token}
	                    login_response = up.post(f"{ghost}/login/signIn", params=login_data, headers=headers,verify=False)
	                    token = ""
	                    for d in div:
	                        porcentaje = round((current/total)*100,1)
	                        current += 1
	                        await bot.edit_message(user_id,msg_id,f"[✓] #upload #local #enproceso #allpower\n\n<i>{d}</i>\n\n<code>Subiendo {current}/{total} {porcentaje}%</code>", parse_mode="HTML")
	                        upid = await upload(cd+"/temp/"+d, ghost, guser,gpass,grepo,up, msg_id, user_id)
	                        token += str(upid)+"-"
	                    token += "/"
	                    token = token.replace("-/","")
	                    nubes[user_nube]["nube"].append({"filename":file,"token":token, "size":size})
	                    key = base64.b64encode(ghost.encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")+"-"+base64.b64encode(guser.encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")+"-"+base64.b64encode(gpass.encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")+"-"+base64.b64encode(str(grepo).encode("utf-8")).decode("utf-8").replace("==","@").replace("=","#")
	                    if not bitzero == 0:
	                        await event.reply(f"[✓] #upload #local #finalizado\n\n<code>Subido a la nube!\n\n{file}</code>\n\n<b>Comando: </b><code>bitzero https://bitzero.techdev.cu/{size}-{grepo}/{token}/{bitzero}/{key}/{urllib.parse.quote(file.replace(' ','_'))}</code>", parse_mode="HTML")
	                    else:
	                        await event.reply(f"[✓] #upload #local #finalizado\n\n<code>Subido a la nube!\n\n{file}</code>", parse_mode="HTML")
	                        msg = ""
	                        tokens = token.split("-")
	                        for fileID in tokens:
	                            url = f"{ghost}/$$$call$$$/api/file/file-api/download-file?submissionFileId={fileID}&submissionId={grepo}&stageId=1"
	                            msg += url+"\n"
	                        msg += "/"
	                        msg = msg.replace("\n/", "")
	                        name = file
	                        name = name.replace("."+name.split(".")[-1], ".txt")
	                        open(name,"w").write(msg)
	                        await bot.send_file(user_id, name)
	                        os.unlink(name)
	                await bot.delete_messages(user_id, msg_id)
	                unlink(cd+"/temp")
	                fin_process(pid)
	            except:
	                fin_process(pid)
	                await bot.edit_message(user_id, msg_id, f"[•] #upload #local #error\n\n<code>Compruebe el estado de la nube o si el modo de subida a sido correctamente seleccionado</code>", parse_mode="HTML")
	            break
	        else:
	            if not w == c:
	                c = w
	                await bot.edit_message(user_id,msg_id,f"[•] #upload #local\n\n<code>Esperando por {w} procesos</code>", parse_mode="HTML")
	                await asyncio.sleep(2)
	            else:
	                None
	                await asyncio.sleep(2)
	elif "/rmc " in text and isuser(user_id):
	    msg = await event.reply(f"[•] #rm #cloud #enproceso\n\n<code>Conectando nube...</code>", parse_mode="HTML")
	    msg_id = msg.id
	    if "-" in text:
	        lisc = list(range(int(text.split("-")[0].split(" ")[1]),int(text.split("-")[1].split(" ")[0])+1))
	        text =  "/rmc "+' '.join(map(str,lisc))
	    elif "all" in text:
	           text = "/rmc "+' '.join(map(str,list(range(0,len(nubes[user_nube]['nube'])))))
	    files = text.replace("/rmc ","").split(" ")
	    menos = 0
	    for f in files:
	        try:
	            fids_split = nubes[user_nube]['nube'][int(f)-menos]['token'].split("-")
	            total = len(fids_split)
	            current = 0
	            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
	            up = requests.Session()
	            getToken = up.get(ghost+"/login",headers=headers,verify=False)
	            token = BeautifulSoup(getToken.text,"html.parser").find('input',{'name':'csrfToken'})
	            login_data = {"password": gpass,"remember": 1,"source": "","username": guser,"csrfToken":token}
	            login_response = up.post(f"{ghost}/login/signIn", params=login_data, headers=headers,verify=False)
	            for t in fids_split:
	                await bot.edit_message(user_id,msg_id,f"[•] #rm #cloud #enproceso\n\n<code>Eliminando {round((current/total)*100,1)}%</code>", parse_mode="HTML")
	                await delete_cloud(t, up)
	                current += 1
	            nubes[user_nube]["nube"].pop(int(f)-menos)
	            menos += 1
	            await bot.edit_message(user_id,msg_id,f"[✓] #rm #cloud #finalizado\n\n<code>Eliminado</code>", parse_mode="HTML")
	        except:
	            await bot.edit_message(user_id,msg_id,f"[✓] #rm #cloud #error\n\n<code>Error desconocido</code>", parse_mode="HTML")
	elif "/adduser " in text and user_id == users[0]:
	    users.append(int(text.split(" ")[1]))
	    nubes.append({"user":int(text.split(" ")[1]),"nube":[]})
	    ust = []
	    for u in users:
	        ust.append(str(u))
	    us = '\n'.join(ust)
	    await bot.send_message(user_id,f"[✓] #adduser #local\n\n<code>Usuario añadido</code>\n\n"+us, parse_mode="HTML")
	elif "/rmuser " in text and user_id == users[0]:
	    users.remove(int(text.split(" ")[1]))
	    for nube in nubes:
	        if nube["user"] == user_id:
	            nubes.remove(nube)
	    ust = []
	    for u in users:
	        ust.append(str(u))
	    us = '\n'.join(ust)
	    await bot.send_message(user_id,f"[✓] #adduser #local\n\n<code>Usuario añadido</code>\n\n"+us, parse_mode="HTML")
	elif not isuser(user_id):
	    await bot.send_message(user_id,f"[×] #nouser #local #error\n\n<code>Usted no es un usuario de este bot.</code>", parse_mode="HTML")
	elif "/rmp" in text and user_id == users[0]:
	    rm_process()
	    await bot.send_message(user_id,f"[✓] #rmp #local #eliminado\n\n<code>Eliminados</code>", parse_mode="HTML")
	elif "/off_cola" == text and user_id == users[0]:
	    cola_download = False
	    await bot.send_message(user_id,f"[✓] #off_cola #local #eliminado\n\n<code>Cola de descarga apagada</code>", parse_mode="HTML")
	elif "/on_cola" == text and user_id == users[0]:
	    cola_download = True
	    await bot.send_message(user_id,f"[✓] #on_cola #local #creado\n\n<code>Cola de descarga encendida</code>", parse_mode="HTML")
	elif "/bitzero " in text and user_id == users[0]:
	    bitzero = int(text.replace("/bitzero ",""))
	    await bot.send_message(user_id,f"[✓] #on_bitzero #local #creado\n\n<code>BitZero {bitzero}</code>", parse_mode="HTML")
	elif "/start_edit " in text and user_id == users[0]:
	    msg = text.replace("/start_edit ","")
	    start_msg = msg
	    await bot.send_message(user_id,f"[✓] #start_edit #local #creado\n\n<code>Editado!!</code>", parse_mode="HTML")
	elif "/rmc_token " in text and user_id == users[0]:
	       token1 = text.split(" ")[1]
	       try:
	           token2 = text.split(" ")[2]
	           tokens = list(range(int(token1),int(token2)))
	       except:
	           tokens = [token1]
	       total = len(tokens)
	       current = 0
	       headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
	       up = requests.Session()
	       getToken = up.get(ghost+"/login",headers=headers,verify=False)
	       token = BeautifulSoup(getToken.text,"html.parser").find('input',{'name':'csrfToken'})
	       login_data = {"password": gpass,"remember": 1,"source": "","username": guser,"csrfToken":token}
	       login_response = up.post(f"{ghost}/login/signIn", params=login_data, headers=headers,verify=False)
	       await bot.send_message(user_id,f"[•] #rmc_token #cloud #eliminando\n\n<code>Iniciando...</code>", parse_mode="HTML")
	       addnum = 0
	       for token in tokens:
	           current += 1
	           if (current-addnum)>100:
	               addnum += 100
	               await asyncio.sleep(3)
	           await bot.edit_message(user_id, msg_id+1,f"[•] #rmc_token #cloud #eliminando\n\n<code>Eliminando {round((current/total)*100,3)}%</code>", parse_mode="HTML")
	           await delete_cloud(token, up)
	       for nube in nubes:
	           nube["nube"] = []
	       await bot.edit_message(user_id, msg_id+1,f"[✓] #rmc_token #cloud #finalizado\n\n<code>Eliminado</code>", parse_mode="HTML")
	elif "/about" == text and isuser(user_id):
	    await bot.send_message(user_id,f"[✓] #about #local\n\n<b>Comandos:</b>\n\n<code>ls - Ver archivos\nlsc - Ver archivos [Nube]\nrm - Eliminar archivo\nrmc - Eliminar archivo [Nube]\nup - Subir a la nube\nurl - Obtener comando o txt de descarga\nmv - Mover archivo a carpeta\nmkdir - Crear carpeta\nzip - Comprimir carpeta\nsplit - Dividir archivo en partes\nadduser - Añadir usuario [Admin]\nrmuser - Eliminar usuario [Admin]\noff_bitzero - Subida normal\non_bitzero - Subida bitzero\nstart_edit - Editar mensaje de inicio [Admin]\nrmc_token - Eliminar por token [Nube][Admin]\nset_cloud - Cambiar nube [Admin]\nsend - Enviar mensaje a los usuarios [Admin]\nget_code - Obtener código python de descarga\nreport - Reportar error al administrador</code>", parse_mode="HTML")
	elif "/send " in text and user_id == users[0]:
	    for user in users:
	        await bot.send_message(user, text.replace("/send ",""), parse_mode="HTML")
	elif "/report " in text:
	    msg = text.replace("/report ","")
	    await bot.send_message(users[0],"<b>Nuevo reporte</b>\n<i>Usuario: </i>@"+username+"\n<i>ID: </i>"+str(user_id)+"\n\n"+msg, parse_mode="HTML")
#INICIANDO EL CÓDIGO
print("BOT INICIADO")
bot.run_until_disconnected()