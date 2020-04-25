import sys

def response(text, speed="1.14"):
    import tts
    import config
    if config.speech_on:

        # 由于我树莓派声音蓝牙音箱播放语音时前几个字声音特别小，听不见，所以使用延迟修正声音
        try:
            import config_private
            if config_private.speech_delay:
                text = '啊啊，' + text
        except ImportError:
            pass
        tts.say(text, speed=speed)


def command_handler(command):
    import subprocess
    import os

    if '打开播放器' in command:
        # 使用os.system的话，若终端被杀死，则vlc也会被杀死
        subprocess.Popen('vlc')
        response('正在打开vlc')
    
    elif '播放音乐' in command:
        subprocess.Popen(['vlc', '/home/lpy/Music/'])
        response('即将播放')

    elif '打开浏览器' in command:
        subprocess.Popen('google-chrome-stable')
        response('正在打开chrome')

    elif '打开QQ' in command:
        subprocess.Popen('google-chrome-stable')
        response('正在打开chrome')
    
    elif '网易云音乐' in command:
        subprocess.Popen('netease-cloud-music')
        response('正在打开网易云音乐')

    elif '管理路由器' in command:
        subprocess.Popen('google-chrome-stable --new-window  192.168.2.1'.split())
        response('正在打开luci')

    elif '管理小飞机' in command:
        subprocess.Popen('google-chrome-stable --new-window  192.168.2.1/cgi-bin/luci///admin/services/shadowsocksr'.split())
        response('正在打开ssr plus')

    elif '打开vscode' in command:
        subprocess.Popen('code')
        response('正在打开vscode')
    
    elif '连接树莓派' in command:
        # 参数中有空格了，不能再简单的split一个字符串了
        subprocess.Popen(['gnome-terminal', '-e', 'ssh pi@192.168.2.4'])
        response('正在连接树莓派')

    elif '现在几点' in command:
        import time
        response(time.strftime('%m月%d日 %H:%M', time.localtime()))

    # 依赖于和风天气API KEY
    elif '明天天气' in command:
        import requests
        import config
        try:
            import config_private
        except ImportError:
            response('未找到私有配置文件，请添加和风天气api key')
            return
        resp = requests.get(config.heweather_url, 
            {'location' : config_private.heweather_location, 'key' : config_private.heweather_key})
        tomorrow_weather = resp.json()['HeWeather6'][0]['daily_forecast'][0]
        msg = f"白天 {tomorrow_weather['cond_txt_d']}，晚上 {tomorrow_weather['cond_txt_n']}，{tomorrow_weather['tmp_min']}度到{tomorrow_weather['tmp_max']}度"
        response(msg)

    elif '你是谁' in command:
        response('我叫小源，是你专属的人工智障呀')

    elif '智障' in command:
        response('你才是智障')

    # commit 并 push 本项目
    elif '推送' in command:
        subprocess.Popen(f"gnome-terminal -e  '{sys.path[0]}/push.sh'".split())
        response('正在启动推送')
    
    elif command.startswith('搜索'):
        subprocess.Popen(f"google-chrome-stable --new-window  www.google.com/search?q={command[2:]}".split())
        response('正在启动搜索')

    elif '唱歌' in command or '唱首歌' in command:
        response('twinkle, twinkle, little star, how i wonder what you are')

    elif '讲个笑话' in command:
        response('不讲')

    elif '你会干什么' in command or '你会做什么' in command:
        # subprocess.Popen(f"gedit {sys.path[0]}/command_handler.py".split())
        response('小源只是个人工智障，你自己看一下源代码中定义的功能吧')

    elif '开启复读机模式' in command:
        response('已开启复读机模式')
        os.system(f'touch {sys.path[0]}/.repeater')
    
    elif '关闭复读机模式' in command:
        response('已关闭复读机模式')
        os.system(f'rm -rf {sys.path[0]}/.repeater')

    elif '重启' in command:
        response('正在重启')
        os.system('systemctl reboot -i')

    elif '关机' in command:
        response('正在关机')
        os.system('systemctl poweroff -i')

    elif '休眠' in command:
        response('正在休眠')
        os.system('systemctl hibernate -i')

    else:
        if os.path.exists(f'{sys.path[0]}/.repeater'):
            response(command)
        else:
            response('小源还没有学会此命令 ' + command)


def command_filter(command):
    command = command.strip('。')
    if command.startswith('帮我'):
        command = command[2:]
    if command.startswith('请帮我'):
        command = command[3:]

    return command
