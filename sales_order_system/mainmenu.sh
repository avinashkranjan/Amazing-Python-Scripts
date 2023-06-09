clear
i="y"
while [ $i = "y" ]; do
  clear
  tput setaf 3
  tput cup 2 20; echo "--------------------------------"
  tput cup 3 20; echo "--------  Main Menu  -----------"
  tput cup 4 20; echo "--------------------------------"
  tput cup 5 20; echo "-------  1. TRANSACTION   ------"
  tput cup 6 20; echo "-------  2. SEARCH        ------"
  tput cup 7 20; echo "-------  3. REPORT        ------"
  tput cup 8 20; echo "-------  4. QUIT          ------"
  tput cup 9 20; echo "--------------------------------"
  tput cup 10 20; echo -n "     SELECT AN OPTION : "
  read option
  tput cup 11 20; echo "--------------------------------"
  case $option in
  1) sh transaction.sh ;;
  2) sh search_order.sh ;;
  3) sh report.sh ;;
  4) exit ;;
  *) tput cup 12 20; echo "Invalid option....Quitting"
     sleep 1
     exit ;;
  esac
  tput cup 13 20; echo -n "Do you want to continue(y/n)? "
  read i
  if [ $i != "y" ]; then
    tput cup 14 20; echo "Quitting the program..."
    sleep 1
    exit
  fi
done
