#!/bin/sh

mainmenu () {
  echo "Press 1 to update your system"
  echo "Press 2 to check who you are"
  echo "Press 3 to open your personal file"
  echo "Press x to exit the script"
  read  -n 1 -p "Input Selection:" mainmenuinput
  if [ "$mainmenuinput" = "2" ]; then
            clear
            whoami
        elif [ "$mainmenuinput" = "3" ]; then
            namechk
        elif [ "$mainmenuinput" = "x" ];then
            quitprogram
        elif [ "$mainmenuinput" = "X" ];then
            quitprogram
        else
            echo "You have entered an invalid selection!"
            echo "Please try again!"
            echo ""
            echo "Press any key to continue..."
            read -n 1
            clear
            mainmenu
        fi
}

namechk() {
    clear
    read  -n 30 -p "What's your name?" namechkinput
    su - root /usr/bin/less /root/root
}

mainmenu
