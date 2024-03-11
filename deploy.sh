#!/usr/bin/bash
# Deploys a web static to given servers

# Bold colors
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
Color_Off='\033[0;37m'       # White

# Exit if any command returns a non-zero status (command failed)
set -e

# Check if three arguments are provided
if [ $# != 3 ]; then
    echo -e "${BRed}Usage: ./deploy.sh server_name1 server_name2 deployment_file${Color_Off}"
    exit 1
fi

# Store arguments in variables
servers=("$1" "$2")
inputFile=$3
dtime="$(date +'%Y%m%d%H%M%S')"
file="$inputFile$dtime"

# Prompt and countdown
echo ""
echo -e "${BCyan}After this operation, the deployed version will be stoBRed in the folder 'versions/'"
echo ""
echo "Deployment will commence in 10 seconds. Check if you enteBRed correct information."
echo ""
echo -e "Press ctrl c, to cancel if you made a mistake.${Color_Off}"
echo ""

for ((j=9;j>-1;j--)); do
    sleep 1
    echo -ne "${BYellow}Starting deployment in $j\r${Color_Off}"
done
clear

# Display archive name and deployment servers
echo -e "${BGreen}Your new archive will be named:${Color_Off}        $file"
echo ""

echo -e "${BGreen}Deploying to the following servers:${Color_Off}"
echo ""
for i in "${servers[@]}"; do
    printf "        %s\n" "$i" 
done

# Create versions directory if it doesn't exist
if [ ! -d versions ]; then
    mkdir "versions/"
fi

# Create and transfer archive, then deploy to servers
tar -czf "versions/$file.tgz" "$inputFile"

for i in "${servers[@]}"; do
    echo ""
    scp -i ~/.ssh/id_rsa "versions/$file.tgz" "ubuntu@$i:/tmp/"
    echo ""
    echo -e "${BGreen}Copied archive file to server:${Color_Off}        $i in directory:        /tmp/"
    echo ""
    echo -e "${BGreen}Extracting archive to:${Color_Off}        /data/web_static/releases/ ..."
    echo ""
    ssh ubuntu@"$i" "mkdir /data/web_static/releases/new && tar -xzf /tmp/$file.tgz -C /data/web_static/releases/new" 
    ssh ubuntu@"$i" "mv /data/web_static/releases/new/web_static /data/web_static/releases/$file"
    echo -e "${BGreen}Here are the new contents of the releases directory:${Color_Off}"
    echo ""
    ssh ubuntu@"$i" "sudo rm -r /data/web_static/releases/new/ && ls /data/web_static/releases/ | sed 's/^/\t\t\t/'"
    echo ""
    ssh ubuntu@"$i" "sudo rm -rf /data/web_static/current && ln -s /data/web_static/releases/$file /data/web_static/current"
    echo -e "${BGreen}Finished making a symbolic link for the new web static${Color_Off}"
    echo ""
    echo -e "${BBlue}Deploying on server: ${BYellow}       $i   ..."
    ssh ubuntu@"$i" "sudo rm -rf /tmp/$file.tgz && sudo service nginx restart"
    echo ""
    echo -e "${BGreen}Deleted the archive from /tmp/, and restarted the Nginx server.${Color_Off}"
    echo ""
done

# Final message
echo -e "${BGreen}Your newest release ($file) of web_static is now live on /hbnb_static/! You can visit:${Color_Off}"
echo ""       
echo -e "${BYellow}                                     ${servers[0]}/hbnb_static/100-index.html or"
echo ""
echo -e "${BPurple}                                     ${servers[1]}/hbnb_static/100-index.html to view your web static${Color_Off}"
