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