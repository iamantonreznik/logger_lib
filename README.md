# logger_lib

<b>Библиотека для логирования logger_lib
v0.1</b>

<br><a href="https://github.com/iamantonreznik/logger_lib/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/iamantonreznik/logger_lib?style=for-the-badge"></a><br><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/iamantonreznik/logger_lib?style=for-the-badge"><br><br>
# ОПИСАНИЕ

Библиотека для простого логирования проектов. Написана для обучения языку Python
<br><br>
# ПОДКЛЮЧЕНИЕ

1. Подключить библиотеку к своему проекту с помощью `import logger_lib`
2. Настроить файл конфигурации `logger.cfg`
3. Инициализировать библиотеку, например, так: `mylogger = logger_lib.Logger()`
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
mylogger.crit('Событие с пометкой CRITICAL')
</pre>


# todo:
1. delete config file
2. rewrite initialization
