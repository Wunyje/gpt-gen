cd /d %~dp0

adb connect 192.168.8.191
rem WiFi连接手机

adb devices
rem 查看adb连接手机设备

adb shell input keyevent 224
rem 点亮屏幕

adb shell am start -n com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity
rem 找到钉钉应用，并打开。
ping /n 6 /w 1000 localhost > nul
rem 等待6秒%

adb shell input tap 550 2200
rem 进入钉钉后，点击:【开源网安】
ping /n 20 /w 1000 localhost > nul

adb shell input tap 125 1415
rem 点击【考勤打卡】
ping /n 21 /w 1000 localhost > nul


adb shell screencap -p /sdcard/check_in_res.png
ping /n 2 /w 1000 localhost > nul
adb pull /sdcard/check_in_res.png
ping /n 2 /w 1000 localhost > nul
rem 截图成功打卡图片到电脑


adb shell am force-stop com.alibaba.android.rimet
rem 关闭钉钉
ping /n 2 /w 1000 localhost > nul

adb shell input keyevent 26
rem 关闭手机屏幕。
ping /n 2 /w 1000 localhost > nul

git pull
git add --all
git commit -m "check in done"
git push

exit

