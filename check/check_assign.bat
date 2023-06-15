cd /d %~dp0

set /a rand_minute=%RANDOM% %% 51 + 10 
schtasks /create /tn check_test /st 11:%rand_minute% /sc once /tr "check_test.bat"  < Y.txt

set /a rand_minute=%RANDOM% %% 51 + 10 
schtasks /create /tn check_in_task /st 07:%rand_minute% /sc once /tr "check_in.bat"  < Y.txt

set /a rand_minute=%RANDOM% %% 51 + 10  
schtasks /create /tn check_out_task /st 21:%rand_minute% /sc once /tr "check_out.bat"  < Y.txt