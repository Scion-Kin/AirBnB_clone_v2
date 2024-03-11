#!/usr/bin/bash
# deploys a web static to given servers

set -e # exit if any command returns a none 0 status. i.e command failed

if [ $# != 3 ]; then
    echo "Usage: ./deploy.sh server_name1 server_name2 deployment_file"
    exit 1
fi

servers=("$1" "$2")
file=$3

echo ""
echo "After this operation, the deployed version will be stored in the folder 'versions/'"
echo "Deployment will commence in five seconds. Check if you entered correct information."
echo "Press ctrl c, to cancel if you made a mistake."
echo ""

for ((j=5;j>0;j--)); do
    sleep 1
    echo "$j"
done
clear

echo "The directory $file will be deployed to the following servers: "
echo ""
for i in "${servers[@]}"; do
    printf "        %s\n" "$i" 
done

if [ ! -d versions ]; then
    mkdir "versions/"
fi

tar -czf "versions/$file.tgz" "$file"

for i in "${servers[@]}"; do
    echo ""
    scp -i ~/.ssh/id_rsa "versions/$file.tgz" "ubuntu@$i:/tmp/"
    echo ""
    echo "Copied archive file to server:        $i in directory:        /tmp/"
    echo ""
    echo "Checking and removing an existing web_static directory on the desired location ..."
    echo ""
    ssh ubuntu@"$i" "sudo rm -rf /data/web_static/releases/web_static && ls /tmp/ | grep web_static"
    echo ""
    echo "Extracting archive to:        /data/web_static/releases/ ..."
    ssh ubuntu@"$i" "tar -xzf /tmp/$file.tgz -C /data/web_static/releases/"
    echo ""
    ssh ubuntu@"$i" "sudo rm -rf /data/web_static/current && ln -s /data/web_static/releases/web_static /data/web_static/current"
    echo "Finished making a symbolic link for the new web static on server:        $i"
    echo ""
    ssh ubuntu@"$i" "sudo rm -rf /tmp/$file.tgz && ls -l /data/web_static/ | grep current && sudo service nginx restart"
    echo ""
    echo "Deleted the archive from /tmp/, and restarted the Nginx server."
    echo ""
done

echo "Your /hbnb_static/ is now live! You can visit: "
echo ""       
echo "                                     ${servers[0]}/hbnb_static/100-index.html or"
echo ""
echo "                                     ${servers[1]}/hbnb_static/100-index.html to view your web static"
