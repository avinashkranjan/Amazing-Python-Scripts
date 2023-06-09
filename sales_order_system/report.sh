clear
echo "| ---------------------------------------------------------------------------- |"
echo "|                                 SALES ORDER SYSTEM                           |"
echo "| ---------------------------------------------------------------------------- |"
echo "| ORDER_NO |    CLIENT     |    ARTICLE   | QUANTITE | PRIX | DATE DE COMMANDE |"
n=6
while read line;
do
  sleep 1
  tput cup $n; echo "| `echo $line | cut -d":" -f1` "
  tput cup $n 11; echo "| `echo $line | cut -d":" -f2` "
  tput cup $n 30; echo "| `echo $line | cut -d":" -f3` "
  tput cup $n 47; echo "| `echo $line | cut -d":" -f4` "
  tput cup $n 55; echo "| `echo $line | cut -d":" -f5` "
  tput cup $n 67; echo "| `echo $line | cut -d":" -f6` "
  tput cup $n 78; echo " | "
  n=`expr $n + 1`
done < orders.txt
# `sort -t ":" -k3 orders.txt`
echo "| ---------------------------------------------------------------------------- |"