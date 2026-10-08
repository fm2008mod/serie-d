# serie-d
First time fully activated Italy’s Serie D in Football Manager 2008!

If you enjoy this project, you can show your appreciation for my work by buying me a coffee. Thank you very much in advance!  
https://ko-fi.com/fm2008mod/


#Polish, Espanol and Italian manual below.  

  
**Instructions: applying the Serie D modification to Football Manager 2008**

Requirements:  
a) Python 3 (no extra libraries needed; the script only uses struct, sys and base64).  
b) An original, unmodified fm.exe from Football Manager 2008, version 8.0.2 (ProductVersion 8.0.2f117931, PE timestamp 0x47B3C3C6). The clean file is 22,245,376 bytes (0x1537000) and has 4 sections. The script also accepts a file that already contains a .mycode section.

**Steps:** 
a) Back up the original fm.exe in a separate folder.  
b) Copy apply_serieD_v14.py and the original fm.exe into one working folder, not into the game folder.  
c) Run this from the command line:   
python apply_serieD_v14.py fm.exe fm_serieD_v14.exe  
d) The script checks the expected bytes at every patch location and stops with a message if anything doesn't match (e.g. "expected … found …"). It never overwrites the input file, and the output file must have a different name.  
e) If it finishes without errors, fm_serieD_v14.exe will appear in the folder. Rename it to fm.exe and put it in the game folder in place of the original (after making the backup from step 1).  
f) Start a new game and choose Italy. Serie D should be visible in the competition tree, with groups A–I of 18 clubs each.  
  
  
**Instrukcja: nakładanie modyfikacji Serie D na FM 2008**

Wymagania:  
a) Python 3 (bez dodatkowych bibliotek, skrypt używa tylko struct, sys i base64).  
b) Oryginalny, niemodyfikowany fm.exe z Football Managera 2008 w wersji 8.0.2 (ProductVersion 8.0.2f117931, znacznik czasu PE 0x47B3C3C6). Czysty plik ma 22 245 376 bajtów (0x1537000) i 4 sekcje. Skrypt przyjmuje też plik, który już ma sekcję .mycode.  

**Kroki:**  
a) Zrób kopię zapasową oryginalnego fm.exe w osobnym folderze.  
b) Skopiuj apply_serieD_v14.py i oryginalny fm.exe do jednego folderu roboczego, nie do folderu gry.  
c) Uruchom w wierszu poleceń:  
python apply_serieD_v14.py fm.exe fm_serieD_v14.exe  
d) Skrypt sprawdza oczekiwane bajty w każdym miejscu poprawki i przerywa z komunikatem, jeśli coś się nie zgadza (np. „oczekiwano … jest …”). Nie nadpisuje pliku wejściowego, a plik wyjściowy musi mieć inną nazwę.  
e) Jeśli skończy bez błędu, w folderze pojawi się fm_serieD_v14.exe. Zmień jego nazwę na fm.exe i wstaw do folderu gry w miejsce oryginału (po zrobieniu kopii z kroku 1).  
f) Zacznij nową grę i wybierz Włochy. Serie D powinna być widoczna w drzewie rozgrywek, z grupami A–I po 18 klubów.  
  
  
**Instrucciones: aplicar la modificación de Serie D a Football Manager 2008**

Requisitos:  
a) Python 3 (no se necesitan bibliotecas adicionales; el script solo utiliza struct, sys y base64).   
b) Un fm.exe original, sin modificar, de Football Manager 2008, versión 8.0.2 (ProductVersion 8.0.2f117931, PE timestamp 0x47B3C3C6). El archivo limpio tiene un tamaño de 22,245,376 bytes (0x1537000) y contiene 4 secciones. El script también acepta un archivo que ya contenga una sección .mycode.   

**Pasos:**   
a) Haz una copia de seguridad del fm.exe original en una carpeta separada.    
b) Copia apply_serieD_v14.py y el fm.exe original en una misma carpeta de trabajo, no en la carpeta del juego.   
c) Ejecuta lo siguiente desde la línea de comandos:  
python apply_serieD_v14.py fm.exe fm_serieD_v14.exe    
d) El script comprueba los bytes esperados en cada ubicación de parche y se detiene mostrando un mensaje si algo no coincide (por ejemplo, "expected … found …"). Nunca sobrescribe el archivo de entrada, y el archivo de salida debe tener un nombre diferente.    
e) Si termina sin errores, fm_serieD_v14.exe aparecerá en la carpeta. Cámbiale el nombre a fm.exe y colócalo en la carpeta del juego en lugar del original (después de haber realizado la copia de seguridad del paso 1).  
f) Inicia una partida nueva y elige Italia. La Serie D debería aparecer en el árbol de competiciones, con los grupos A–I, cada uno con 18 clubes.  
  
  
**Istruzioni: applicare la modifica della Serie D a Football Manager 2008**

Requisiti:  
a) Python 3 (non sono necessarie librerie aggiuntive; lo script utilizza solamente struct, sys e base64).  
b) Un fm.exe originale e non modificato di Football Manager 2008, versione 8.0.2 (ProductVersion 8.0.2f117931, PE timestamp 0x47B3C3C6). Il file originale ha una dimensione di 22.245.376 byte (0x1537000) e contiene 4 sezioni. Lo script accetta anche un file che contiene già una sezione .mycode.  

**Procedura:**  
a) Esegui una copia di sicurezza dell'fm.exe originale in una cartella separata.  
b) Copia apply_serieD_v14.py e l'fm.exe originale nella stessa cartella di lavoro, non nella cartella del gioco.  
c) Esegui questo comando dalla riga di comando:  
python apply_serieD_v14.py fm.exe fm_serieD_v14.exe  
d) Lo script verifica i byte previsti in ogni posizione della patch e si interrompe mostrando un messaggio se qualcosa non corrisponde (ad esempio, "expected … found …"). Non sovrascrive mai il file di input e il file di output deve avere un nome diverso.  
e) Se termina senza errori, nella cartella apparirà fm_serieD_v14.exe. Rinominalo in fm.exe e inseriscilo nella cartella del gioco al posto dell'originale (dopo aver effettuato il backup indicato al punto 1).  
f) Avvia una nuova partita e scegli l'Italia. La Serie D dovrebbe essere visibile nell'albero delle competizioni, con i gironi A–I, ciascuno composto da 18 club.  
