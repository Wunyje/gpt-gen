gst-launch-1.0 v4l2src device=/dev/video31 ! video/x-raw,width=640,height=480 ! x264enc pass=qual quantizer=25 tune=zerolatency ! flvmux streamable=true ! rtmpsink location="rtmp://192.168.8.35:1935/test"