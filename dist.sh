#!/usr/bin/bash
# deploys a web static to given servers

set -e # exit if any command returns a none 0 status. i.e command failed

if [ $# != 3 ]; then
    echo "Usage: ./dist.sh server_name1 server_name2 deployment_file"
    exit 1
fi

servers=("$1" "$2")
file=$3

echo "The directory $file will be deployed to the following servers: "
echo ""
for i in "${servers[@]}"; do
    printf "        %s\n" "$i" 
done

echo ""
echo "After this operation, the deployed version will be stored in the folder 'versions/'"
echo "Deployment will commence in five seconds. Check if you entered correct information."
echo "Press ctrl c, to cancel if you made a mistake."
echo ""

for ((j=5;j>0;j--)); do
    sleep 1
    echo "$j"
done

if [ ! -d versions ]; then
    mkdir "versions/"
fi

tar -czf "versions/$file.tgz" "$file"

for i in "${servers[@]}"; do
    scp -i ~/.ssh/id_rsa "versions/$file.tgz" "ubuntu@$i:/tmp/"
    echo "Copied file to server:        $i in directory:        /tmp/"
    echo ""
    echo "Checking and removing an existing web_static file on the desired location"
    echo ""
    ssh ubuntu@"$i" "sudo rm -rf /data/web_static/releases/web_static"
    echo ""
    ssh ubuntu@"$i" "tar -xzf /tmp/$file.tgz -C /data/web_static/releases/ && ls -l /tmp/ | grep web_static"
    echo "File extracted to:        /data/web_static/releases/"
    echo ""
    ssh ubuntu@"$i" "sudo rm -rf /data/web_static/current && ln -s /data/web_static/releases/web_static /data/web_static/current"
    echo "Finished making a symbolic link on server:        $i"
    echo ""
    ssh ubuntu@"$i" "sudo rm -rf /tmp/$file.tgz && ls -l /data/web_static/ && sudo service nginx restart"
    echo "Restarted Nginx server."
    echo ""
done

echo "Your /hbnb_static/ is now live! You can visit: "       
echo "                                     ${servers[0]}/hbnb_static/100-index.html or"
echo "                                     ${servers[1]}/hbnb_static/100-index.html to view your web static"
