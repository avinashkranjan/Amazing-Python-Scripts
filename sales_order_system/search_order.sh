clear
echo "SEARCH AN ORDER"
echo -n "Enter order number: "
read order_no
line=`grep -n $order_no orders.txt | wc -l`
if [ $line -gt 0 ]
then
  line=`grep -n $order_no orders.txt`
  echo "--------------------------------"
  echo "Order No : `echo $line | cut -d":" -f2` "
  echo "Client : `echo $line | cut -d":" -f3` "
  echo "Article : `echo $line | cut -d":" -f4` "
  echo "Quantity : `echo $line | cut -d":" -f5` "
  echo "Price : `echo $line | cut -d":" -f6` "
  echo "Order Date : `echo $line | cut -d":" -f7` "
  echo "--------------------------------"
else
  echo "Invalid option...."
fi
