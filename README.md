## This is a test project
| Product code  | Name  |  Price |
|---|---|---|
|  001 |  Lavender heart | £9.25  |
|  002 |  Personalised cufflinks | £45.00  |
|  003 |  Kids T-shirt | £19.95 |


Project contains two restful  api resources.

Task - This caters to 

* GET /products - A list of products, names, and prices in JSON.
* POST /product - Create a new product from a JSON body.

TaskByID - This caters to

* GET /product/{product_id} - Return a single product by id in JSON.
* PUT /product/{product_id} - Update a product's name or price by id.
* DELETE /product/{product_id} - Delete a product by id.

## The test excercise is meant for a very basic api call test. Does not include modularised code for database creation/
## initialisation/closing etc. Also the API Calls are not modularized. Just a very basic one with tests from Postman.

Testing the request calls and containerization is left to some other day this week.