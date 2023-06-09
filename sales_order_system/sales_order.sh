clear
tput cup setaf 3
tput cup 5 20; echo "--------------------------------"
tput cup 6 20; echo "--  Sales order system  --"
tput cup 7 20; echo "--------------------------------"
tput cup 8 20; echo "--------------------------------"
tput cup 9 20; echo -n "Username : "
read usrnm
tput cup 10 20; echo -n "Password : "
read psswd
if test $usrnm = "admin" -a $psswd = "diopdiop"; then
  tput cup 11 20; echo "REGISTRATION SUCCESSFUL..."
  sleep 1
  sh mainmenu.sh
else
  tput cup 12 20; echo "REGISTRATION FAILED, Try again..."
  sleep 1
  sh sales_order.sh
fi
