## 个人语音助手

打算使用百度语音识别API做个简单的个人语音助手，基本方法就是调用百度语音识别API将语音转换成文字，然后根据文字执行不同的命令/脚本来实现自己需要的功能，文字转语音使用了google_speech，可能需要科学上网才可以正常使用。比如：
```
打开vscode   -    subprocess.Popen('code')
打开浏览器    -    subprocess.Popen('google-chrome-stable')
关机         -    os.system('poweroff')
重启         -    os.system('reboot')
```

## 使用方法

### 脚本调用
仅适用于Linux，需要安装 `arecord`，然后执行脚本 `yuan-assistant.sh`　即可调出语音助手，默认接收输入的时间是2s，不合适的话自行修改脚本中 `yuan-assistant.sh` 中 `arecord` 命令的 `-d` 参数即可。

### 快捷调用 
可以为此脚本绑定一个快捷键，即可使用快捷键呼出语音助手。也可以修改 `yuan-assistant.desktop` 中的路径然后将其放到 `～/.local/share/applications/`下，即可添加到启动器。

### 自定义功能
通过 `command_handler.py` 中的 `command_handler` 函数自定义关键词和相应的命令。

### 日志
日志记录在项目下的 `log.txt`，识别不成功时可以查看下日志中的识别结果，可能是语速或者发音偏差导致识别错误。

### 使用自己的账号
现在使用的　`API_KEY`　和　`SECRET_KEY`　是官方demo里的，如果失效的话可以自己申请百度AI平台账号，然后替换成自己的 `API_KEY`　和　`SECRET_KEY`。

## 其他说明

### 天气预报
使用和风天气API做了简单的天气预报，用到了私有APIKEY，因此创建了一个 `config_private.py` 用于存储私有配置，此文件并未上传到github
