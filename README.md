# TemperatureServe-withRealtimeDatabase

I have made this small IoT project using nodemcu as microcontroller.

Nodemcu collects temperature and humidity using dht11 and then display it to a webpage.

Now python scrapper gets that data from a web page and stores that into a sqlite3 databas.

I have also made a flask webserver to view the data or download the data.


#### How to use the script.

After uploading '.ino' code to your device [make sure to change wifi credentials and pin number as per your device]
1] To run the webserver run 'app.py'. [You will be able to see the web page displaying current room temp]
To download data, Go to the navbar and follow the user-interface.

2] To collect data and store it to the database run  'scraper.py' [Default time interval is 120 sec you can change it]
