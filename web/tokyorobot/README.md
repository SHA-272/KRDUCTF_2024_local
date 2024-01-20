# Tokyo Robot

## Описание

Нальный этап пентеста, узнаем кто такие роботы

## Публикация
Чтобы запустить задание, клонируйте репозиторий и смонтируйте Docker контейнеры с помощью следующих команд:

```
bash
git clone <url-репозитория>
cd <имя-репозитория>
docker-compose up --build
```
## Решение

проверить robots.txt

проверить dissalow

import requests

response = requests.get('http://<your-website>/secretpage')
print(response.text)

## Ответ

krdu{R0b0t5_53cr3T_Fl4G}