1. Какие значения переменным c,d,e будут присвоены? Почему?

    | Переменная  | Значение | Обоснование |
    | ------------- | ------------- | ------------- |
    | `c`  | a+b  | В команде нет $ перед переменными, bash понимаем что мы хотим присвоить строку "a+b" |
    | `d`  | 1+2  | Мы разрешили названия переменных в значения, однако для bash это всё ещё строка |
    | `e`  | 3  | Знаки (()) говорят bash, что мы хотим провести арифметическую операцию |

2.  ```bash
    while ((1==1)
    do
        curl https://localhost:4757
        if (($? != 0))
        then
            date >> curl.log
        else
            break
        fi
    done
    ```

3.  ```bash
    #!/bin/bash

    i=0
    ip=("192.168.3.1" "173.194.222.113" "87.250.250.242")

    while (( $i < 5 ))
    do
        i=$(( $i + 1 ))
        for elem in ${ip[@]}
        do
            echo > /dev/tcp/$elem/80
            if (( $? == 0 ))
            then
                echo "$elem на порту 80 доступен" >> log
            else
                echo "$elem на порту 80 недоступен" >> log
            fi
        done
    done
    ```

4.  ```bash
    #!/bin/bash

    i=0
    ip=("192.168.3.1" "173.194.222.113" "87.250.250.242")
    while (( $i < 5 ))
    do
        i=$(( $i + 1 ))
        for elem in ${ip[@]}
        do
            echo > /dev/tcp/$elem/80
            if (( $? == 0 ))
            then
                echo "$elem на порту 80 доступен" >> log
            else
                echo "$elem на порту 80 недоступен" >> error
                breaking=yes
                break
            fi
        done
        if [ "$breaking" == "yes" ]
        then
            break
        fi
    done
    ```