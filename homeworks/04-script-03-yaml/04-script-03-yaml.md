### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-03-yaml/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис
```
{
	"info": "Sample JSON output from our service\t",
	"elements": [
		{
			"name": "first",
			"type": "server",
			"ip": 7175
		},
		{
			"name": "second",
			"type": "proxy",
			"ip": "71.78.22.43"
		}
	]
}
```

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
#!/bin/python
import socket
import json
import os.path
import yaml
import time


def get_sites(sites):
        for site in sites.keys():
                sites[site] = socket.getaddrinfo(site, 443)[0][4][0]
                print(f'{site}  {sites[site]}')
        print('---')
        return sites


def write_files(sites):
        with open('old_ip.json', 'w') as jfile:
                json.dump(sites, jfile)
        with open('old_ip.yaml', 'w') as yfile:
                yaml.dump(sites, yfile)


sites = {'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}
mismatch = False

while not mismatch:
        sites = get_sites(sites)

        if os.path.exists('old_ip.json'):
                with open('old_ip.json') as file:
                        old_sites = json.load(file)
        else:
                sites = get_sites(sites)
                old_sites = sites
                write_files(sites)


        for site in sites.keys():
                if sites[site] != old_sites[site]:
                        print(f'[ERROR] {site} IP mismatch: {old_sites[site]} {sites[site]}')
                        print('---')
                        write_files(sites)
        time.sleep(1)

```

### Вывод скрипта при запуске при тестировании:
```
drive.google.com  216.58.207.238
mail.google.com  142.250.74.165
google.com  142.250.74.14
---
[ERROR] drive.google.com IP mismatch: 142.250.74.14 216.58.207.238
---
[ERROR] google.com IP mismatch: 142.250.74.174 142.250.74.14
---
drive.google.com  216.58.207.238
mail.google.com  142.250.74.165
google.com  142.250.74.14
---
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
{"drive.google.com": "216.58.207.238", "mail.google.com": "142.250.74.165", "google.com": "142.250.74.14"}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
drive.google.com: 216.58.207.238
google.com: 142.250.74.14
mail.google.com: 142.250.74.165
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

### Ваш скрипт:
```python
???
```

### Пример работы скрипта:
???
