# MCDA5550_Python_REST_Assignment

application link: http://djangorestassignment-env.eba-vapkmrvy.us-west-2.elasticbeanstalk.com/

server_port: 8000

database: hotel.cyhdgor7dxwe.us-west-2.rds.amazonaws.com

db_port: 3306

Functionalities:

1. Get the list of hotels present. url suffix: /hotel_list/
![Screenshot (1173)](https://user-images.githubusercontent.com/90723999/156293696-82dcf6dc-d7a8-4b3e-a722-2a43ed676032.png)
![Screenshot (1174)](https://user-images.githubusercontent.com/90723999/156293734-413f7439-e732-4d38-9ead-21a20f22c8ed.png)

2. Get a particular hotel according to id value entered. url suffix: /hotel_list/<id>
![Screenshot (1175)](https://user-images.githubusercontent.com/90723999/156293757-d638db74-67bb-44b6-a488-623ad73dfc93.png)


3. POST a particular hotel's details. url suffix: (i)  /hotel_list/<id>   (ii)  /hotel_list/
![Screenshot (1176)](https://user-images.githubusercontent.com/90723999/156293790-b7931ddb-4775-4e58-bc39-c87c648fdc46.png)
![Screenshot (1177)](https://user-images.githubusercontent.com/90723999/156293823-fd3ea818-33b0-40fb-aefb-f1a1d81da9b9.png)

4. Unique functionality: as shown above you can post from either of the two links and also a check for same hotel name is done to avoid adding the same hotel:
![Screenshot (1208)](https://user-images.githubusercontent.com/90723999/156299652-3fc44661-bf0b-4b33-bc61-1da67d8be8b9.png)
![Screenshot (1209)](https://user-images.githubusercontent.com/90723999/156299610-f012bd1c-b7e1-4d4b-a7d7-d0d731ecfd53.png)


Database:
![image](https://user-images.githubusercontent.com/90723999/156294467-c2080c22-77e9-4502-b68e-268c609dba0c.png)

