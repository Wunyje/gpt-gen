adb connect 192.168.8.191
rem WiFi连接手机

adb devices
rem 查看adb连接手机设备

adb shell input keyevent 224
rem 点亮屏幕

adb shell am start -n com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity
rem 找到钉钉应用，并打开。
ping 127.0.0.1 -n 6
rem 等待2秒%

adb shell input tap 550 2200
rem 进入钉钉后，点击:【开源网安】
ping 127.0.0.1 -n 6

adb shell input tap 330 1000
rem 点击【考勤打卡】
ping 127.0.0.1 -n 6

adb shell input tap 530 1360
rem 点击【上班打卡，下班打卡】
ping 127.0.0.1 -n 2

adb shell screencap -p /sdcard/check_res.png
ping 127.0.0.1 -n 2
adb pull /sdcard/check_res.png
ping 127.0.0.1 -n 2
rem 截图成功打卡图片到电脑


adb shell am force-stop com.alibaba.android.rimet
rem 关闭钉钉
ping 127.0.0.1 -n 2

adb shell input keyevent 26
rem 关闭手机屏幕。
ping 127.0.0.1 -n 2

check_res.png

git add --all
git commit -m "update"
git push

exit
