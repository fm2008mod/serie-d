# serie-d
First time fully activated Italy’s Serie D in Football Manager 2008!

If you enjoy this project, you can show your appreciation for my work by buying me a coffee. Thank you very much in advance!
https://ko-fi.com/fm2008mod/

#Polish manual below.

Instructions: applying the Serie D modification to Football Manager 2008

Requirements

Python 3 (no extra libraries needed; the script only uses struct, sys and base64).
An original, unmodified fm.exe from Football Manager 2008, version 8.0.2 (ProductVersion 8.0.2f117931, PE timestamp 0x47B3C3C6). The clean file is 22,245,376 bytes (0x1537000) and has 4 sections. The script also accepts a file that already contains a .mycode section.

Steps

Back up the original fm.exe in a separate folder.
Copy apply_serieD_v14.py and the original fm.exe into one working folder, not into the game folder.
Run this from the command line: python apply_serieD_v14.py fm.exe fm_serieD_v14.exe
The script checks the expected bytes at every patch location and stops with a message if anything doesn't match (e.g. "expected … found …"). It never overwrites the input file, and the output file must have a different name.
If it finishes without errors, fm_serieD_v14.exe will appear in the folder. Rename it to fm.exe and put it in the game folder in place of the original (after making the backup from step 1).
Start a new game and choose Italy. Serie D should be visible in the competition tree, with groups A–I of 18 clubs each.


Instrukcja: nakładanie modyfikacji Serie D na FM 2008

Wymagania

Python 3 (bez dodatkowych bibliotek, skrypt używa tylko struct, sys i base64).
Oryginalny, niemodyfikowany fm.exe z Football Managera 2008 w wersji 8.0.2 (ProductVersion 8.0.2f117931, znacznik czasu PE 0x47B3C3C6). Czysty plik ma 22 245 376 bajtów (0x1537000) i 4 sekcje. Skrypt przyjmuje też plik, który już ma sekcję .mycode.

Kroki

Zrób kopię zapasową oryginalnego fm.exe w osobnym folderze.
Skopiuj apply_serieD_v14.py i oryginalny fm.exe do jednego folderu roboczego, nie do folderu gry.
Uruchom w wierszu poleceń: python apply_serieD_v14.py fm.exe fm_serieD_v14.exe
Skrypt sprawdza oczekiwane bajty w każdym miejscu poprawki i przerywa z komunikatem, jeśli coś się nie zgadza (np. „oczekiwano … jest …”). Nie nadpisuje pliku wejściowego, a plik wyjściowy musi mieć inną nazwę.
Jeśli skończy bez błędu, w folderze pojawi się fm_serieD_v14.exe. Zmień jego nazwę na fm.exe i wstaw do folderu gry w miejsce oryginału (po zrobieniu kopii z kroku 1).
Zacznij nową grę i wybierz Włochy. Serie D powinna być widoczna w drzewie rozgrywek, z grupami A–I po 18 klubów.
