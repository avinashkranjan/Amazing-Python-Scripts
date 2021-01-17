#!/bin/bash
################################################################################

# Sometimes the port number causes problem and it doesn't restart
while true
do
echo "s to start, q to exit, r to start/ restart."
read key

if [[ "$key" == 'r' ]]
then
    echo "Server Running On port 5562"
    echo
    kill $(lsof -t -i:5562)
    gnome-terminal -e "bash -c \"python3 httpServer.py 5562; exec bash\""       
elif [[ "$key" == 'q' ]]
then
    echo "Shutting Down... zzzz..."
	# program to quit
    # fuser -k 5562/tcp
    kill $(lsof -t -i:5562)
    # killall terminal
    exit;
elif [[ $key == 's' ]]
then
    echo "Starting :D"
    # killall zsh
    kill $(lsof -t -i:5562)
    gnome-terminal -e "bash -c \"python3 httpServer.py 5562; exec bash\""       
    
else
    echo
fi

done
