USE northwind;

-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells.
SELECT ProductID, ProductName, UnitPrice
FROM products;

-- 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT ProductID, ProductName, UnitPrice
FROM products
WHERE UnitPrice <= 7.50;

-- 3. Products with no units on hand, but 1 or more units on backorder.
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock = 0
  AND UnitsOnOrder >= 1;

-- 4. Category information and seafood items
-- Category is identified using CategoryID in the products table.
-- List all categories:
SELECT *
FROM categories;

-- List all seafood products:
SELECT ProductName, UnitPrice
FROM products
WHERE CategoryID = (
    SELECT CategoryID
    FROM categories
    WHERE CategoryName = 'Seafood'
);

-- 5. Supplier information and Tokyo Traders products
-- Supplier is identified using SupplierID in the products table.
-- Find supplier info:
SELECT *
FROM suppliers;

-- Find SupplierID for Tokyo Traders:
SELECT SupplierID, CompanyName
FROM suppliers
WHERE CompanyName = 'Tokyo Traders';

-- List all products from Tokyo Traders:
SELECT ProductID, ProductName, SupplierID
FROM products
WHERE SupplierID = (
    SELECT SupplierID
    FROM suppliers
    WHERE CompanyName = 'Tokyo Traders'
);

-- 6a. How many employees work at Northwind?
SELECT COUNT(*) AS NumberOfEmployees
FROM employees;

-- 6b. Employees with "manager" in their job title
SELECT EmployeeID, FirstName, LastName, Title
FROM employees
WHERE Title LIKE '%manager%';