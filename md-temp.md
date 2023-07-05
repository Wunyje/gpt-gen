Assuming that you are a master in coding C and using Gstreamer. Convert this to Gstreamer C API :```gst-launch-1.0 v4l2src device=/dev/video41 ! image/jpeg,width=640,height=480,framerate=30/1 ! jpegdec ! autovideosink```
	
There is a re
"
*main function*
1 用Gstreamer实现编码板与解码板之间的音视频数据通信 
2 用Gstreamer提供多通讯协议支持 
2.1 实现RTP、RTSP和RTMP协议传输 
2.2 实现上述协议存储、推拉流和点播功能 
3 用Gstreamer实现多码率视频转换与生成 
4 用Gstreamer在3的基础上实现网络带宽探测与码率选择(QoS)

*other requirement*
1) 客户端，服务器端为命令行形式控制；
2) 视频分辨率为4K向下兼容，编码方式为H 264/H 265；git pull
3) 点播服务软件支持多点访问，支持不少于32个用户同时在线异步回放。
"
How would you do that? Tell your thought step by step.


I noticed that the points in program outline are seperated and isolated
1 can you make outline more intergral about the whole program to form a complete solution, relate the points in the outline, after all, the eventual program is an *intergral application*
2 I need to spot the application's processing logic on the level of Gstreamer API.

Is there any necessity to differentiate the server and the clients program? If so, please list out the outline of corresponding sides.

Take server side as example, make a more intergral outline and give me the possible file structure.

Try to write the pseudo code of all the '.c' files of server side, revealing the dynamic invoking relationship between these files