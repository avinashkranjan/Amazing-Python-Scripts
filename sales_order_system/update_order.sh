clear
echo "UPDATE AN ORDER"
echo -n "Enter order number: "
read order_no
chk=`grep -c $order_no orders.txt`
if [ $chk -gt 0 ]
then
  line=`grep -n $order_no orders.txt`
  line_no=`echo $line | cut -d":" -f1`
  old_quantity=`echo $line | cut -d":" -f5`
  echo "The order is: "
  echo $line
else
  echo "Invalide order number"
  exit
fi
echo "Update forms"
echo -n "Enter new quantity : "
read new_quantity
sed "$line_no s/$old_quantity/$new_quantity/" "orders.txt" > file.tmp && mv file.tmp "orders.txt"
echo "Order quantity updated successfully!"
