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


if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')


def wakeup_yuan_assistant():
    import os
    import sys
    global interrupted

    snowboydecoder.play_audio_file()
    # 目的是暂时禁止检测，不知是否有效
    interrupted = True
    os.system(f'{sys.path[0]}/yuan_assistant/yuan_assistant.sh')
    interrupted = False


# main loop
detector.start(detected_callback=wakeup_yuan_assistant,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
