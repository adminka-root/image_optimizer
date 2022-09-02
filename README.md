

# Оптимизатор изображений

Image Optimizer for GNU/Linux (далее — ОИ) преставляет собой приложение, предоставляющее простой интерфейс для консольных утилит  jpegoptim, optipng и advdef. Они в основном предназначены для оптимизации jpg и png изображений.

> <u>*Примечание*</u>: Под оптимизацией (в отличии от «сжатия») понимается уменьшение размера входных изображений без ухудшения качества.

Также поддерживает mat/mat2 для удаления метаданных.

## Содержание:

> 1. [Установка](https://github.com/adminka-root/image_optimizer#1-установка)
>    1. [Pyinstaller](https://github.com/adminka-root/image_optimizer#pyinstaller)
>    2. [Conda](https://github.com/adminka-root/image_optimizer#conda)
> 2. [Использование](https://github.com/adminka-root/image_optimizer#2-использование)
> 3. [Явные недостатки программы](https://github.com/adminka-root/image_optimizer#3-явные-недостатки-программы)

---
## 1. Установка

Первым делом установите git:

```bash
sudo apt update; sudo apt install git
```

Затем **клонируйте** этот репозиторий:

```bash
cd "$HOME/.local/share" && git clone https://github.com/adminka-root/image_optimizer.git
```

Установите системные зависимости:

```bash
sudo apt install jpegoptim optipng advancecomp mat2
```

ОИ написан на python3 с использованием дополнительных библиотек, что вносит ряд потенциальных проблем при поставке конечному пользователю. Заранее неизвестна конфигурация этих компонентов, предоставляемая  конкретной операционной системой. Следовательно, неисключены ошибки. Я вижу два выхода из этой ситуации:

1. Использование pyinstaller для предоставления скомпилированного файла, включающего все используемые библиотеки;

2. Предоставление файла конфигурации для создания виртуального conda-окружения, включающего все необходимые зависимости и соответствующий запуск внутри «бутылки».

Рекомендую сначала испытать первый способ, поскольку он быстрее.

### Pyinstaller

1. Просто выполните:

```bash
cd "$HOME/.local/share/image_optimizer/supply/pyinstaller"
link='https://github.com/adminka-root/image_optimizer/releases/download/pyinstaller/image_optimizer_v0.1'
wget "$link" -O image_optimizer && chmod +x image_optimizer
./image_optimizer
```

2. Проверьте работоспособность программы.
> <u>*Примечание*</u>: В идеале программа должна запуститься без «киллометровых» сообщений об ошибках... Если сразу не запустилась, подождите минуту.

3. Коли все хорошо, добавьте значок запуска программы в меню:
```bash
cd "$HOME/.local/share/" && mkdir -p icons
ln "./image_optimizer/source/icons/window_icon.svg" "./icons/image_optimizer.svg"
cd "$HOME/.local/share/image_optimizer/supply/pyinstaller"
desktop-file-install --dir=$HOME/.local/share/applications --rebuild-mime-info-cache image_optimizer.desktop
```

### Conda

1. Установите [miniconda](https://docs.conda.io/en/latest/miniconda.html). Что-то вроде:

```bash
link="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
file_name="$(basename "$link")"
cd /tmp && wget "$link" && chmod +x "$file_name"

./"$file_name"
```

> <u>*Примечание*</u>: в процессе установки
> ```txt
> # Please, press ENTER to continue
> # 	>>> зажимаем enter
> 
> # Do you accept the license terms? [yes|no]
> # 	[no] >>> 
> # 	Please answer 'yes' or 'no':'
> # 	>>> yes
> 
> # Miniconda3 will now be installed into this location:
> #  ~/miniconda3
> #  - Press ENTER to confirm the location
> # 	>>> нажимаем enter
> 
> # by running conda init? [yes|no]
> #    [no] >>> yes
> ```

После установки:

```bash
source ~/.bashrc  # обновить переменные окружения

# отображать в терминале только название "бутылки"
conda config --set env_prompt '({name})'

# не запускать conda автоматически
conda config --set auto_activate_base false

# обновить корневую ветку conda
conda update -n base -c defaults conda
```

2. Создайте «бутылку» из конфига:

```bash
conda env update -n image_optimizer -f ~/.local/share/image_optimizer/supply/conda/conda.yml
```

3. Проверьте программу, открыв файл запуска:
```bash
# это требуется для работы скрипта запуска окружения!
mkdir -p ~/.local/bin/
ln -s "$(which conda)" ~/.local/bin/

# запуск программы
~/.local/share/image_optimizer/supply/conda/image_optimizer.run
```

4. Коли все хорошо, добавьте значок запуска программы в меню:
```bash
cd "$HOME/.local/share/" && mkdir -p icons
ln "./image_optimizer/source/icons/window_icon.svg" "./icons/image_optimizer.svg"
cd "$HOME/.local/share/image_optimizer/supply/conda"
desktop-file-install --dir=$HOME/.local/share/applications --rebuild-mime-info-cache image_optimizer.desktop
```

## 2. Использование

Использовать программу легко: просто откройте её из контекстного меню «открыть с помощью», предварительно выделив нужные изображения, или из меню запуска. 

![](https://i.imgur.com/m27L3T8.png)

<u>**При наведении на каждый элемент программы можно получить всплывающую подсказку о том, что он делает!**</u> 

![](https://i.imgur.com/9BlQzEu.png)

Слева (1) — область настроек программы, которые применяются перед каждым нажатием кнопки «Запустить» (4). Эти настройки можно запомнить в меню «Настройки» (3) --> «Сохранить текущие настройки», чтобы они автоматически загружались при запуске программы.

Справа (2) — «Drop» зона, куда можно перетащить изображения из файлового менеджера для последующих преобразований. Принимаются только файлы в формате jpeg, jpg, png, к которым у текущего пользователя есть доступ (т.е. он может переписать их от своего имени). Нажатие на кнопку «Запустить» блокирует возможность изменения левой области (1), но оставляет возможность пользователю добавлять новые файлы непосредственно во время процесса оптимизации.

Кнопки внизу (4) — управляющие. «Пауза» — передает сигнал остановки. Это останавливает оптимизацию после завершения работы с файлом, с которым программа работала в момент нажатия. Также эта кнопка разблокирует область настроек (1), позволяя пользователю переопределить применяемые действия к имеющимся в списке (2) файлам. «Убрать» и «Убрать все» — удаляют выделенные и все файлы из списка (2) соотвественно. 

## 3. Явные недостатки программы

Программа тестировалась лишь в LM 19.3 и 21.0, была написана в качестве хобби. Не уверен, что она получит обновления функционала в будущем, но пару слов о недостатках. Не хватает реализации:

1. Логов и интерактивности;
2. Приема в качестве аргумента папок с последующим рекурсивным поиском и добавлением изображений + настроек глубины такого вхождения;
3. Явно заданных шрифтов;
4. Меню «Открыть» через файловый менеджер;
5. Функции вывода сэкономленного пространства.

Известные ошибки:

- При попытке оптимизации на носителях, имеющих группу plugdev с владельцем root (как правило, вcякие ntfs-ки, монтирующиеся при старте), mat2 (v.0.12.2) багует, в результате чего он НЕ перезаписывает изображения (как ожидалось), а создает копию (типа <имя>.cleaned.<расширение>). Т.к. mat2 в некоторых случаях увеличивает размер изображений (почему - тайна, покрытая мраком), его приходится вызывать самым первым. В общем это комбо приводит к мысли, что необходимо будет написать специальную обработку для подобных ситуаций... когда-нибудь :)

