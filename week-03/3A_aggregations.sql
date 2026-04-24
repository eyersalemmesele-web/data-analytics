USE northwind;

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price.

-- This finds the cheapest price in the products table. (2.5000)

SELECT MIN(UnitPrice) AS cheap_item
FROM products;

--  This finds the product(s) that match the cheapest price. 

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);
-- Geitost, 2.5000

-- 2. Write a query to find the average price of all items that Northwind sells. (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help using the ROUND function to round the average price to the nearest cent.)

SELECT ROUND(AVG(UnitPrice), 2) AS avg_price
FROM products;

-- 28.87

-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then write a second query to find the name of the product with that price, plus the name of the supplier for that product.

SELECT MAX(UnitPrice) AS max_price
FROM products;

-- This finds the highest price in the products table.

SELECT ProductName, CompanyName, UnitPrice
FROM products 
JOIN suppliers ON products.SupplierID = suppliers.SupplierID
ORDER BY UnitPrice DESC
-- 263.5000
-- This shows the product and supplier that match the highest price.

-- 4.  Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).

SELECT SUM(Salary) AS monthly_payroll
FROM employees;

-- 20362.929931640625

-- 5. Write a query to identify the highest salary and the lowest salary amounts which any employee makes. (Just the amounts, not the specific employees!).

SELECT MAX(Salary) AS max_salary,
       MIN(Salary) AS min_salary
FROM employees;

-- MAX"3119.15" and MIN"1744.21"

-- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply. Hint: Join is your friend here.

SELECT suppliers.CompanyName,
       suppliers.SupplierID,
       COUNT(products.ProductID) AS item_number
FROM suppliers, products
WHERE suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.CompanyName, suppliers.SupplierID
ORDER BY item_number;


-- 7. Write a query to find the list of all category names and the average price for items in each category.

SELECT categories.CategoryName,
       AVG(products.UnitPrice) AS avg_price
FROM categories, products
WHERE categories.CategoryID = products.CategoryID
GROUP BY categories.CategoryName
ORDER BY avg_price;
-- Grains/Cereals, 20.25000000

-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, the name of each supplier and the number of items they supply.

SELECT suppliers.CompanyName,
       COUNT(products.ProductID) AS item_number
FROM suppliers, products
WHERE suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.CompanyName, suppliers.SupplierID
HAVING COUNT(products.ProductID) >= 5
ORDER BY item_number;

-- -- Pavlova, Ltd & Plutzer Lebensmittelgromrkte AG each supply 5

-- 9. Write a query to list products currently in inventory by product id, product name, and inventory value (calculated by multiplying unit price by the number of units on hand). Sort the results in descending order by value. If two or more have the same value, order by product name. If a product is not in stock, leave it off the list.

SELECT ProductID,
       ProductName,
       (UnitPrice * UnitsInStock) AS inventory_value
FROM products
WHERE UnitsInStock > 0
ORDER BY inventory_value DESC,
         ProductName ASC;