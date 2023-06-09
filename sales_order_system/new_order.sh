clear
i="y"
while [ $i = "y" ]; do
clear
line_no=`wc -l orders.txt | cut -d" " -f1`
if [ $line_no = 0 ]
then
  order_no=10001
else
  order_no=`tail -1 orders.txt | cut -d":" -f1`
  order_no=`expr $order_no + 1`
fi
order_date=`date +%D`
echo "Date de commande: $order_date"
echo "New commande number: $order_no"
echo -n "Enter First Name: "
read first_name
echo -n "Enter Last Name: "
read last_name
echo -n "Enter Article: "
read article
echo -n "Enter Quantity: "
read quantity
echo -n "Enter Price: "
read price
echo "$order_no : $first_name $last_name : $article : $quantity : $price : $order_date" >> orders.txt
echo -n "Do you want to add new order(y/n)? "
read i
  if [ $i != "y" ]; then
    exit
  fi
done