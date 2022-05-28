#!/bin/bash
# WELCOME TO GITHUB #
#OPEN THE NEXT PROFILE#
url="https://api.github.com/users/octocat"
echo "CONSULTA 1"
curl -s $url"/repos"| grep "url" | head -n 10
echo "CONSULTA 2"
curl -s $url"/followers"	#Basada de la 1ra consulta
echo "CONSULTA 3"
curl -s $url"/subscriptions"	#Basada de la 1ra consulta

#API_RESURCE#
echo "CONSULTA 4"
key="5a08e0fe38642aa1532a7690d647dbad"
curl -s "api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=$key"
echo -e "\n"
echo "CONSULTA 5"
url="https://api.nasa.gov"
curl -s $url"/DONKI/CMEAnalysis?startDate=2016-09-01&endDate=2016-09-30&mostAccurateOnly=true&speed=500&halfAngle=30&catalog=ALL&api_key=DEMO_KEY"
echo -e "\n"

