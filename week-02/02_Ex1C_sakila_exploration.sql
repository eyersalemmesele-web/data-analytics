/*
a) The actor table have information that describes each actor, mainly their name and an ID number to adentify them, plus a last update time.
b) The film table has information that describes each movies, like the title, short description, release year, and other details about the film.
c) The film_actor table links actors and movies toghter by showing which film using their IDs.
d) The rental table has information about movie rentals, like when a move a was rented, which copy was rented, who rented it, and when it was reurned. it is hard to understand because it uses ID numbers instead of names.
e) The inventory table has information about each physical copy of a movie in the store and connects each copy to a specific film.
f) To find the names of films rented on a specific data, i would use the rental, inventory, and film tables. They are connected through IDs, so rental links to iventory, and inventory links to film, which lets me find the movie titles from rental records.
*/

SELECT rental_id, rental_data, inventory_id
FROM rental

;

SELECT inventory_id, film_id
FROM iventory
;

SELECT title, film_id
FROM film

