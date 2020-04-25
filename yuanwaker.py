#! /usr/bin/python3

import snowboydecoder
import sys
import signal

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


model = f'{sys.path[0]}/resources/models/小源小源.pmdl'
if len(sys.argv) == 2:
    model = sys.argv[1]


# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')


def wakeup_yuan_assistant():
    import os
    import sys
    import subprocess
    global interrupted

    snowboydecoder.play_audio_file()
    # 目的是暂时禁止检测，不知是否有效
    interrupted = True
    ex = subprocess.Popen(f'{sys.path[0]}/yuan_assistant/yuan_assistant.sh', preexec_fn = os.setsid)
    out, err = ex.communicate()
    status = ex.wait()

    print(f'status is {status}, out is {out}, err is {err}')
    interrupted = False


# main loop
detector.start(detected_callback=wakeup_yuan_assistant,
               interrupt_check=interrupt_callback,
               sleep_time=2)

detector.terminate()
