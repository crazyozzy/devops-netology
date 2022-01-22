# Домашнее задание к занятию "3.4. Операционные системы, лекция 2"

1. На лекции мы познакомились с [node_exporter](https://github.com/prometheus/node_exporter/releases). В демонстрации его исполняемый файл запускался в background. Этого достаточно для демо, но не для настоящей production-системы, где процессы должны находиться под внешним управлением. Используя знания из лекции по systemd, создайте самостоятельно простой [unit-файл](https://www.freedesktop.org/software/systemd/man/systemd.service.html) для node_exporter:

    * поместите его в автозагрузку,
    * предусмотрите возможность добавления опций к запускаемому процессу через внешний файл (посмотрите, например, на `systemctl cat cron`),
    * удостоверьтесь, что с помощью systemctl процесс корректно стартует, завершается, а после перезагрузки автоматически поднимается.
        - У меня получился следующий unti файл:
            ```
            vagrant@vagrant:~$ cat /etc/systemd/system/node_exporter.service
            [Unit]
            Description=Prometheus metrics collector
            After=network.target

            [Service]
            EnvironmentFile=/etc/default/node_exporter
            ExecStart=/usr/sbin/node_exporter
            ExecStop=/bin/kill -15 $MAINPID
            Restart=on-failure

            [Install]
            WantedBy=multi-user.target
            ```
1. Ознакомьтесь с опциями node_exporter и выводом `/metrics` по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.
    - Я бы выбрал следующие опции:
        ```
        --collector.cpu            Enable the cpu collector (default: enabled).
        --collector.diskstats      Enable the diskstats collector
        --collector.meminfo        Enable the meminfo collector
        --collector.netstat        Enable the netstat collector
        ```
    - Следующие метрики выглядят наиболее интересными:
        ```
        node_cpu_seconds_total{cpu="0",mode="idle"} 447.14
        node_cpu_seconds_total{cpu="0",mode="iowait"} 0.69
        node_cpu_seconds_total{cpu="0",mode="irq"} 0
        node_cpu_seconds_total{cpu="0",mode="nice"} 0
        node_cpu_seconds_total{cpu="0",mode="softirq"} 0.5
        node_cpu_seconds_total{cpu="0",mode="steal"} 0
        node_cpu_seconds_total{cpu="0",mode="system"} 9.4
        node_cpu_seconds_total{cpu="0",mode="user"} 1.57

        node_memory_MemAvailable_bytes 1.783279616e+09
        node_memory_MemFree_bytes 1.576460288e+09
        node_memory_MemTotal_bytes 2.084077568e+09

        node_disk_io_now{device="sda"} 0
        node_disk_read_bytes_total{device="sda"} 2.45336064e+08
        node_disk_written_bytes_total{device="sda"} 1.2959744e+07

        node_network_receive_bytes_total{device="eth0"} 122499
        node_network_receive_errs_total{device="eth0"} 0
        node_network_transmit_bytes_total{device="eth0"} 102459
        node_network_transmit_errs_total{device="eth0"} 0
        ```
1. Установите в свою виртуальную машину [Netdata](https://github.com/netdata/netdata). Воспользуйтесь [готовыми пакетами](https://packagecloud.io/netdata/netdata/install) для установки (`sudo apt install -y netdata`). После успешной установки:
    * в конфигурационном файле `/etc/netdata/netdata.conf` в секции [web] замените значение с localhost на `bind to = 0.0.0.0`,
    * добавьте в Vagrantfile проброс порта Netdata на свой локальный компьютер и сделайте `vagrant reload`:

    ```bash
    config.vm.network "forwarded_port", guest: 19999, host: 19999
    ```

    После успешной перезагрузки в браузере *на своем ПК* (не в виртуальной машине) вы должны суметь зайти на `localhost:19999`. Ознакомьтесь с метриками, которые по умолчанию собираются Netdata и с комментариями, которые даны к этим метрикам.
    - NetData установил, доступ с хостовой машины настроил, метрики посмотрел/почитал.

1. Можно ли по выводу `dmesg` понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?
    - Да, можно. В выоде `dmesg` есть следующие строки:
        ```
        [    0.000000] Hypervisor detected: KVM
        [    0.043158] Booting paravirtualized kernel on KVM
        [   10.674906] systemd[1]: Detected virtualization oracle.
        ```
1. Как настроен sysctl `fs.nr_open` на системе по-умолчанию? Узнайте, что означает этот параметр. Какой другой существующий лимит не позволит достичь такого числа (`ulimit --help`)?
    - `fs.nr_open` - максимальное кол-во открытых файловых дескрипторов. Настройка по умолчанию:
        ```
        vagrant@vagrant:~$ sysctl fs.nr_open
        fs.nr_open = 1048576
        ```
    - Существует другой лимит, который не позволит достичь значения `fs.nr_open`:
        ```
        vagrant@vagrant:~$ ulimit -n
        1024
        ```
1. Запустите любой долгоживущий процесс (не `ls`, который отработает мгновенно, а, например, `sleep 1h`) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через `nsenter`. Для простоты работайте в данном задании под root (`sudo -i`). Под обычным пользователем требуются дополнительные опции (`--map-root-user`) и т.д.
    ```
    root@vagrant:/home/vagrant# nsenter --target 1970 --pid --mount
    root@vagrant:/# ps au
    USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root           1  0.0  0.0   5476   520 pts/0    S    19:22   0:00 sleep 1h
    root           2  0.0  0.1   7236  4056 pts/0    S    19:26   0:00 -bash
    root          13  0.0  0.1   8892  3408 pts/0    R+   19:26   0:00 ps au
    ```
1. Найдите информацию о том, что такое `:(){ :|:& };:`. Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (**это важно, поведение в других ОС не проверялось**). Некоторое время все будет "плохо", после чего (минуты) – ОС должна стабилизироваться. Вызов `dmesg` расскажет, какой механизм помог автоматической стабилизации. Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?
    - Как я понял, этот однострочный скрипт порождает две своих копии, каждая из которых порождает ещё две и так далее. В выводе `dmesg` нашел следующую строку:
    ```
    [ 2678.408745] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-3.scope
    ```
 