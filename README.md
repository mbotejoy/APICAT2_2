***  Admission Number ***
        ***  168051 ***

I have built a REST API using Flask to manage products with the functionality of adding and retrieving all products.

*** Setting up the environment. ***

1) I cloned the repository in order to be able to upload to github using the following line of code,
"git clone https://github.com/mbotejoy/APICAT2_2.git
 
2) To setup the rest_api folder "cd rest_api"
3) Installed the dependencies eg
     pip install flask

*** Running the API server ***
1) Started the server using "python.py"
Until it is able to run on http://127.0.0.1:5000/.

*** Testing the API endpoints manually or with the provided Python script. ***

Tested the API endpoints manually using cURL
  eg for adding a new product "curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{"name": "Laptop", "description": "A high-performance laptop", "price": 999.99}' "
  
  to retrieve all products
     curl http://127.0.0.1:5000/products

*** Provided Python Script ***
    That script being client_interaction.py to interact with API.
The script is able to add sample produsts and retrieve and display all the products by running it using 
 "python client_intercation.py"
  

