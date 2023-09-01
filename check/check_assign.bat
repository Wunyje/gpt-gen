:: schtasks /create /tn check_assign /st 0:00 /sc DAILY /tr %~dp0check_assign.bat
:: schtasks /Query /tn check_assign
:: schtasks /delete /tn check_assign
cd /d %~dp0
git pull

:: set /a rand_minute=%RANDOM% %% 50 + 10 
:: set /a rand_sec=%RANDOM% %% 50 + 10 
:: schtasks /create /tn check_test /st 10:00:00 /sc once /tr %~dp0check_test.bat  < Y.txt
:: 11:%rand_minute%:%rand_sec%

set /a check_in_rand_minute=%RANDOM% %% 50 + 10 
set /a check_in_rand_sec=%RANDOM% %% 50 + 10 
schtasks /create /tn check_in_task /st 07:%check_in_rand_minute%:%check_in_rand_sec% /sc DAILY /tr %~dp0check_in.bat  < Y.txt

set /a check_out_rand_minute=%RANDOM% %% 50 + 10  
set /a check_out_rand_sec=%RANDOM% %% 50 + 10 
schtasks /create /tn check_out_task /st 21:%check_out_rand_minute%:%check_out_rand_sec% /sc DAILY /tr %~dp0check_out.bat  < Y.txt

adb connect 192.168.8.191
adb devices
adb -s 192.168.8.191:5555 shell input keyevent 224
adb  -s 192.168.8.191:5555 shell screencap -p /sdcard/check_assign.png
ping /n 2 /w 1000 localhost > nul
adb  -s 192.168.8.191:5555 pull /sdcard/check_assign.png
ping /n 2 /w 1000 localhost > nul
adb  -s 192.168.8.191:5555 shell input keyevent 26

git add --all
git commit -m "07:%check_in_rand_minute%:%check_in_rand_sec%  21:%check_out_rand_minute%:%check_out_rand_sec%"
git push