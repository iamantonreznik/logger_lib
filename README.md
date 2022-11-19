# logger_lib

<b>Библиотека для логирования logger_lib
v0.2</b>

<br><a href="https://github.com/iamantonreznik/logger_lib/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/iamantonreznik/logger_lib?style=for-the-badge"></a><br><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/iamantonreznik/logger_lib?style=for-the-badge"><br><br>
# ОПИСАНИЕ

Библиотека для логирования проектов
<br><br>
# ПОДКЛЮЧЕНИЕ

1. Подключить библиотеку к своему проекту с помощью `import logger_lib`
2. Инициализировать библиотеку, передав в параметры **имя папки** для хранения логов и **префикс** для лог файлов, например,  так: `mylogger = logger_lib.Logger('logs', 'log_')`
<br>

# ИСПОЛЬЗОВАНИЕ

<pre>
mylogger.write('Простое событие')
</pre>
<pre>
mylogger.debug('Событие с пометкой DEBUG')
</pre>
<pre>
mylogger.error('Событие с пометкой ERROR')
</pre>
<pre>
mylogger.critical('Событие с пометкой CRITICAL')
</pre>
