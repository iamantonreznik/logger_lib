# logger_lib

<b>Библиотека для логирования logger_lib
v.0.0.3</b>

<br><a href="https://github.com/iamantonreznik/logger_lib/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/iamantonreznik/logger_lib?style=for-the-badge"></a><br><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/iamantonreznik/logger_lib?style=for-the-badge"><br><br>
# ОПИСАНИЕ

Библиотека для простого логирования проектов. Написана для обучения языку Python
<br><br><br>
# ИСПОЛЬЗОВАНИЕ

1. Подключить библиотеку к своему проекту с помощью `import logger_lib`
2. Настроить файл конфигурации `logger.cfg`
3. Инициализировать `logger = logger_lib.Logger()`
4. Передать в `logger().write` сообщения для лога

<br><br>
# ПРИМЕР ИСПОЛЬЗОВАНИЯ
<pre>
import logger_lib


logger = logger_lib.Logger()
logger.startLogging()

# [ 027 ]  14:12:50  Простое событие
logger.write('Простое событие')

# [ 035 ]  14:12:52  [ DEBUG ]  Отладочное событие
logger.write('Отладочное событие', "DEBUG")

# [ 038 ]  14:12:54  [ ERROR ]  Событие с ошибкой
logger.write('Событие с ошибкой', "ERROR")

#                    |------------|
# [ 041 ]  14:12:56  |  CRITICAL  |  Критическое событие
#                    |------------|
logger.write('Критическое событие', "CRITICAL")
</pre>
<br><br>
# TODO 

<s>1. Задать уровни логирования</s><br>
<s>2. Возможность оповещения о важных ошибках</s>
