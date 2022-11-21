# logger_lib
<img src="https://user-images.githubusercontent.com/112612414/203007923-089b7b0c-dab7-4648-8938-2de1daffd52d.png" width=50% height=50%>

Simple logger library for small projects

## Usage/Examples

```python
import logger_lib

# 'logs' for logfiles folder
# 'log_' for logfiles prefix
mylogger = logger_lib.Logger('logs', 'log_')


mylogger.write('Simple message')
mylogger.debug('Message with DEBUG tag')
mylogger.error('Message with ERROR tag')
mylogger.critical('Message with CRITICAL tag')
```

## Current version
v0.2

<a href="https://github.com/iamantonreznik/logger_lib/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/iamantonreznik/logger_lib?style=for-the-badge"></a><br>
