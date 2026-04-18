/* 
a) The table that holds the items Northwind sells is the Products table.
b) The table that holds the types or categories of the items Northwind sells is the Categories table.
*/

USE northwind;

/* 5. Retrieve all columns from employees */
SELECT *
FROM employees;

/* The Northwind employee whose name looks like a bird is Margaret Peacock. */


/* 6. Retrieve all columns from products */
SELECT *
FROM products;

/* This query returns 77 records.
To retrieve only 10 rows using the toolbar, select the Limit to 10 Rows option.
BONUS: You can also write the query as:
SELECT * FROM products LIMIT 10;
Source used: MySQL LIMIT clause documentation.
*/


/* 7. Retrieve all columns from categories */
SELECT *
FROM categories;

/* The category ID of Seafood is 8. */


/* 8. Retrieve top 50 records from orders */
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;
