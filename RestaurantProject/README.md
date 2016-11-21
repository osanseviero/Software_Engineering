Schema

	- Users: There are different types of users (admin, chef, waiter, bartender, warehouse, warehouse admin, etc)
	- Menu: Has three times with different products and a special price.
		- Has an array of ids to recipes
	- Recipes: Can be dishes or drinks
	- Ingredients
	- StoredIngredients: An ingredient with a quantity and an expiration date
		- Holds the id of the Ingredient to which it makes reference
	- Tables
	- Order