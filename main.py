import logging, datetime, time, requests
ip_list = [
    "http://localhost:5000/",
    "http://localhost:5000/404",
    "http://178.218.117.7/",
    "http://localhost:80/"
]
err = ""
now = datetime.datetime.now()
# add filemode="w" to overwrite
logging.basicConfig(filename="log.txt", level=logging.INFO, filemode="w")
logging.info("****NEW LOG****")
logging.info(str(now))
 
#logging.error("An error has happened!")

while(True):
    for i in ip_list:
        try:
            response = requests.get(i)
            #print(i, " - ", response.status_code)
            if response.status_code != 200:
                err = i + " - " + str(response.status_code)
                print(err)
                logging.error(err)
        except Exception as E:
            logging.error(str(i + " - " + str(E)))
        
            
    
    logging.info(datetime.datetime.now())
    time.sleep(5)