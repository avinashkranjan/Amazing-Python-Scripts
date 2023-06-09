clear
i="y"
while [ $i = "y" ]; do
  clear
  tput setaf 3
  tput cup 2 20; echo "--------------------------------"
  tput cup 3 20; echo "------  TRANSACTION Menu -------"
  tput cup 4 20; echo "--------------------------------"
  tput cup 5 20; echo "-------  1. NEW ORDER     ------"
  tput cup 6 20; echo "-------  2. UPDATE ORDER  ------"
  tput cup 7 20; echo "-------  3. QUIT          ------"
  tput cup 8 20; echo "--------------------------------"
  tput cup 9 20; echo -n "---- SELECT AN OPTION : "
  read option
  tput cup 10 20; echo "-------------------------------"
  case $option in
  1) sh new_order.sh ;;
  2) sh update_order.sh ;;
  3) exit ;;
  *) tput cup 11 20; echo "Invalid option....Quitting"
    sleep 1
    exit ;;
  esac
  tput cup 12 20; echo -n "Return to transaction menu(y/n)? "
  read i
  if [ $i != "y" ]; then
    echo "Quitting the program..."
    sleep 1
    exit
  fi
done
