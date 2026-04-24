USE northwind;

-- 1. Most expensive product(s)of the most expensive products?
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

-- Cte de Blaye 263.500

-- 2. Least expensive product(s) category of the least expensive products?

SELECT Products.ProductName, Categories.CategoryName, Products.UnitPrice
FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID
WHERE Products.UnitPrice = (SELECT MIN(UnitPrice) FROM Products);


-- Geitost Dairy Products 2.5000

-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?

SELECT Orders.OrderID, Orders.ShipName, Orders.ShipAddress
FROM Orders
JOIN Shippers ON Orders.ShipVia = Shippers.ShipperID
WHERE Shippers.CompanyName = 'Federal Shipping';
-- 255 rows returuned 

-- 4. What are the order ids of the orders that included "Sasquatch Ale"?

SELECT `Order Details`.OrderID
FROM `Order Details`
JOIN Products ON `Order Details`.ProductID = Products.ProductID
WHERE Products.ProductName = 'Sasquatch Ale';

-- Diffrent way but same answer

SELECT OrderID
FROM `Order Details`
WHERE ProductID = (
    SELECT Products.ProductID
    FROM Products
    WHERE Products.ProductName = 'Sasquatch Ale'
);


-- 19 rows returned

-- 5. Employee for order 10266
SELECT Employees.FirstName, Employees.LastName
FROM Employees
WHERE Employees.EmployeeID = (
    SELECT Orders.EmployeeID
    FROM Orders
    WHERE Orders.OrderID = 10266
);
-- Janet Leverling

-- 6. What is the name of the customer that bought order 10266?

SELECT Customers.CompanyName, Customers.ContactName
FROM Customers
WHERE Customers.CustomerID = (
    SELECT Orders.CustomerID
    FROM Orders
    WHERE Orders.OrderID = 10266
);
-- Wartian Herkku, Pirkko Koskitalo