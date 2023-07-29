## 1 Find the mic

In order to find the microphone on your system, you can use the `aplay` and `arecord` commands. These commands will list the available playback and capture hardware devices, respectively.

### 1.1 Check `PLAYBACK Hardware Devices`

The `aplay --list-devices` command will list the available playback hardware devices on your system. In the example output provided, there are four playback hardware devices available:
```
root@ubuntu2004:/# aplay --list-devices 
**** List of PLAYBACK Hardware Devices **** 
card 0: rockchiphdmi0 [rockchip-hdmi0], device 0: rockchip-hdmi0 i2s-hifi-0 [rockchip-hdmi0 i2s-hifi-0] 
  Subdevices: 1/1 
  Subdevice #0: subdevice #0 
card 1: rockchiphdmi1 [rockchip-hdmi1], device 0: rockchip-hdmi1 i2s-hifi-0 [rockchip-hdmi1 i2s-hifi-0] 
  Subdevices: 1/1 
  Subdevice #0: subdevice #0 
card 2: rockchipdp0 [rockchip,dp0], device 0: rockchip,dp0 spdif-hifi-0 [rockchip,dp0 spdif-hifi-0] 
  Subdevices: 1/1 
  Subdevice #0: subdevice #0 
card 3: rockchiprt5640c [rockchip,rt5640-codec], device 0: fe470000.i2s-rt5640-aif1 rt5640-aif1-0 [fe470000.i2s-rt5640-aif1 rt5640-aif1-0] 
  Subdevices: 1/1 
  Subdevice #0: subdevice #0 

root@ubuntu2004:/#
```
### 1.2 Check `CAPTURE Hardware Devices`

The `arecord -l` command will list the available capture hardware devices on your system. In the example output provided, there are three capture hardware devices available:
```
root@ubuntu2004:/# arecord -l         
**** List of CAPTURE Hardware Devices **** 
card 3: rockchiprt5640c [rockchip,rt5640-codec], device 0: fe470000.i2s-rt5640-aif1 rt5640-aif1-0 [fe470000.i2s-rt5640-aif1 rt5640-aif1-0] 
  Subdevices: 1/1 
  Subdevice #0: subdevice #0 
card 4: rockchiphdmiin [rockchip,hdmiin], device 0: fddf8000.i2s-dummy_codec hdmiin-dc-0 [fddf8000.i2s-dummy_codec hdmiin-dc-0] 
  Subdevices: 1/1 
  Subdevice #0: subdevice #0 
card 5: Camera [USB2.0 Camera], device 0: USB Audio [USB Audio] 
  Subdevices: 1/1 
  Subdevice #0: subdevice #0 

root@ubuntu2004:/#
```
## 2 Use the mic with _Gstreamer_

Once you have identified the microphone on your system, you can use it in Gstreamer to record audio.

### 2.1 By _Gst command_

To use the microphone in Gstreamer using the Gst command line tool, you can specify the audio source element and set its properties to use the desired microphone. 
You can set the recording duration in a GStreamer pipeline by using the `num-buffers` property of the `alsasrc` element in combination with the `blocksize` property. The num-buffers property specifies the number of buffers to record, while the blocksize property specifies the size of each buffer in bytes. The recording duration can be calculated as `(num-buffers * blocksize) / (sample rate * channels * bytes per sample)`. Here is an example command that records audio from the `rockchip,rt5640-codec` device for 10 seconds using a sample rate of 44100 Hz, 2 channels, and 16 bits per sample: 

```
gst-launch-1.0 alsasrc device=hw:3,0 num-buffers=441 blocksize=88200 ! audioconvert ! wavenc ! filesink location=/tmp/test.wav 
```


### 2.2 By _Gstreamer C API_

To use the microphone in Gstreamer using the C API, you can create an audio source element and set its properties to use the desired microphone. Here is an example of how this could be done:

```c
#include <gst/gst.h>

int main(int argc, char *argv[]) {
    GstElement *pipeline, *source, *convert, *resample, *sink;
    GstBus *bus;
    GstMessage *msg;
    GstStateChangeReturn ret;

    /* Initialize GStreamer */
    gst_init (&argc, &argv);

    /* Create the elements */
    source = gst_element_factory_make ("alsasrc", "source");
    convert = gst_element_factory_make ("audioconvert", "convert");
    resample = gst_element_factory_make ("audioresample", "resample");
    sink = gst_element_factory_make ("autoaudiosink", "sink");

    /* Create the empty pipeline */
    pipeline = gst_pipeline_new ("test-pipeline");

    if (!pipeline || !source || !convert || !resample || !sink) {
        g_printerr ("Not all elements could be created.\n");
        return -1;
    }

    /* Build the pipeline */
    gst_bin_add_many (GST_BIN (pipeline), source, convert, resample, sink, NULL);
    if (gst_element_link_many (source, convert, resample, sink, NULL) != TRUE) {
        g_printerr ("Elements could not be linked.\n");
        gst_object_unref (pipeline);
        return -1;
    }

    /* Set the source properties */
    g_object_set (source, "device", "hw:5", NULL);

    /* Start playing */
    ret = gst_element_set_state (pipeline, GST_STATE_PLAYING);
    if (ret == GST_STATE_CHANGE_FAILURE) {
        g_printerr ("Unable to set the pipeline to the playing state.\n");
        gst_object_unref (pipeline);
        return -1;
    }

    /* Wait until error or EOS */
    bus = gst_element_get_bus (pipeline);
    msg = gst_bus_timed_pop_filtered (bus, GST_CLOCK_TIME_NONE,
        GST_MESSAGE_ERROR | GST_MESSAGE_EOS);

    /* Parse message */
    if (msg != NULL) {
        GError *err;
        gchar *debug_info;

        switch (GST_MESSAGE_TYPE (msg)) {
            case GST_MESSAGE_ERROR:
                gst_message_parse_error (msg, &err, &debug_info);
                g_printerr ("Error received from element %s: %s\n",
                    GST_OBJECT_NAME (msg->src), err->message);
                g_printerr ("Debugging information: %s\n",
                    debug_info ? debug_info : "none");
                g_clear_error (&err);
                g_free (debug_info);
                break;
            case GST_MESSAGE_EOS:
                g_print ("End-Of-Stream reached.\n");
                break;
            default:
                /* We should not reach here because we only asked for ERRORs and EOS */
                g_printerr ("Unexpected message received.\n");
                break;
        }
        gst_message_unref (msg);
    }

    /* Free resources */
    gst_object_unref (bus);
    gst_element_set_state (pipeline, GST_STATE_NULL);
    gst_object_unref (pipeline);
    return 0;
}
```

This code creates a Gstreamer pipeline that uses the `alsasrc` element to capture audio from the `hw:5` device, which corresponds to the `USB Audio` microphone from the example above. The audio is then converted and resampled before being played back using the `autoaudiosink` element.
