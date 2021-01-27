#!/bin/bash 
clear

# This is to install python3 and pip3 or others programs thaht we may use  
aptModules(){
    programUnix=("python3" "pip3")
    for i in "${programUnix[@]}"
    do
        check=$(which $i)
        if [[ -z $check ]]
        then
            echo "Not installed > $i"
            $(apt install -y $i) > /dev/null 2>&1
            echo "$i installed"
        else
            echo "Installed > $i"
        fi
    done
}

pip3Modules(){
    programPython=("pynput" "os-sys")
    for i in "${programPython[@]}"
    do
        check=$(pip3 show $i)
        if [[ -z $check ]]
        then
            echo "Not installed > $i"
            $(pip3 install $i) > /dev/null 2>&1
            echo "$i installed"
            exit 0
        else
            echo "Installed > $i"
        fi
    done
}

aptModules

pip3Modules