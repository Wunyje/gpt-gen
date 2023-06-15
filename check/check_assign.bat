:: schtasks /create /tn check_assign /st 0:00 /sc DAILY /tr %~dp0check_assign.bat
:: schtasks /Query /tn check_assign
:: schtasks /delete /tn check_assign
cd /d %~dp0

set /a rand_minute=%RANDOM% %% 50 + 10 
set /a rand_sec=%RANDOM% %% 50 + 10 
schtasks /create /tn check_test /st 11:%rand_minute%:%rand_sec% /sc once /tr %~dp0check_test.bat  < Y.txt

set /a rand_minute=%RANDOM% %% 50 + 10 
set /a rand_sec=%RANDOM% %% 50 + 10 
schtasks /create /tn check_in_task /st 07:%rand_minute%:%rand_sec% /sc once /tr %~dp0check_in.bat  < Y.txt

set /a rand_minute=%RANDOM% %% 50 + 10  
set /a rand_sec=%RANDOM% %% 50 + 10 
schtasks /create /tn check_out_task /st 21:%rand_minute%:%rand_sec% /sc once /tr %~dp0check_out.bat  < Y.txt