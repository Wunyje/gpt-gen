cd /d %~dp0

adb connect 192.168.8.191
rem WiFi�����ֻ�

adb devices
rem �鿴adb�����ֻ��豸

adb shell input keyevent 224
rem ������Ļ

adb shell am start -n com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity
rem �ҵ�����Ӧ�ã����򿪡�
ping /n 6 /w 1000 localhost > nul
rem �ȴ�6��%

adb shell input tap 550 2200
rem ���붤���󣬵��:����Դ������
ping /n 20 /w 1000 localhost > nul

adb shell input tap 125 1415
rem ��������ڴ򿨡�
ping /n 21 /w 1000 localhost > nul

adb shell input tap 530 1360
rem ������ϰ�򿨣��°�򿨡�
ping /n 5 /w 1000 localhost > nul

adb shell screencap -p /sdcard/check_out_res.png
ping /n 2 /w 1000 localhost > nul
adb pull /sdcard/check_out_res.png
ping /n 2 /w 1000 localhost > nul
rem ��ͼ�ɹ���ͼƬ������


adb shell am force-stop com.alibaba.android.rimet
rem �رն���
ping /n 2 /w 1000 localhost > nul

adb shell input keyevent 26
rem �ر��ֻ���Ļ��
ping /n 2 /w 1000 localhost > nul

check_out_res.png

git add --all
git commit -m "check out done"
git push


exit
