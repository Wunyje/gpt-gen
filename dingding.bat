adb connect 192.168.8.191
rem WiFi�����ֻ�

adb devices
rem �鿴adb�����ֻ��豸

adb shell input keyevent 224
rem ������Ļ

adb shell am start -n com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity
rem �ҵ�����Ӧ�ã����򿪡�
ping 127.0.0.1 -n 6
rem �ȴ�2��%

adb shell input tap 550 2200
rem ���붤���󣬵��:����Դ������
ping 127.0.0.1 -n 6

adb shell input tap 330 1000
rem ��������ڴ򿨡�
ping 127.0.0.1 -n 6

adb shell input tap 530 1360
rem ������ϰ�򿨣��°�򿨡�
ping 127.0.0.1 -n 2

adb shell screencap -p /sdcard/check_res.png
ping 127.0.0.1 -n 2
adb pull /sdcard/check_res.png
ping 127.0.0.1 -n 2
rem ��ͼ�ɹ���ͼƬ������


adb shell am force-stop com.alibaba.android.rimet
rem �رն���
ping 127.0.0.1 -n 2

adb shell input keyevent 26
rem �ر��ֻ���Ļ��
ping 127.0.0.1 -n 2

check_res.png

git add --all
git commit -m "update"
git push

exit
