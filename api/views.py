from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


food_items = [
    {
        "id": 1,
        "name": "Spaghetti Carbonara",
        "description": "Classic Italian pasta with creamy sauce and pancetta.",
        "price": "$12",
        "image": "https://eze-bucket.s3.amazonaws.com/Spaghetti_Carbonara.jpg",
            "more_details": "Ingredients: Spaghetti, eggs, pancetta, parmesan cheese, black pepper. Calories: 650. Chef's note: Best served hot."
    },
    {
        "id": 2,
        "name": "Margherita Pizza",
        "description": "Tomato, mozzarella, and fresh basil.",
        "price": "$10",
        "image": "https://eze-bucket.s3.amazonaws.com/Margherita_Pizza.jpg",
        "more_details": "Ingredients: Pizza dough, tomato sauce, mozzarella cheese, fresh basil. Calories: 300 per slice. Chef's note: A classic Neapolitan-style pizza."
    },
    {
        "id": 3,
        "name": "Caesar Salad",
        "description": "Crispy romaine lettuce with parmesan and croutons.",
        "price": "$8",
        "image": "https://eze-bucket.s3.amazonaws.com/Caesar_Salad.jpg",
        "more_details": "Ingredients: Romaine lettuce, Caesar dressing, croutons, parmesan cheese. Calories: 200. Chef's note: Add grilled chicken for extra protein."
    },
    {
        "id": 4,
        "name": "Tiramisu",
        "description": "Traditional Italian coffee-flavored dessert.",
        "price": "$7",
        "image": "https://eze-bucket.s3.amazonaws.com/Tiramisu.jpg",
        "more_details": "Ingredients: Mascarpone cheese, coffee, cocoa powder, ladyfingers. Calories: 450. Chef's note: Pairs perfectly with espresso."

    },
    {
        "id": 5,
        "name": "Grilled Chicken Sandwich",
        "description": "Juicy grilled chicken with lettuce, tomato, and mayo.",
        "price": "$9",
        "image": "https://eze-bucket.s3.amazonaws.com/Grilled_Chicken_Sandwich.jpg",
        "more_details": "Ingredients: Grilled chicken breast, lettuce, tomato, mayonnaise, whole wheat bun. Calories: 400. Chef's note: Perfect for a quick lunch."
    },
    {
        "id": 6,
        "name": "Spicy Tuna Roll",
        "description": "A sushi roll filled with spicy tuna, avocado, and cucumber, topped with sesame seeds.",
        "price": "10.99",
        "image": "https://eze-bucket.s3.amazonaws.com/Spicy_Tuna_Roll.jpg",
        "more_details": "Ingredients: Ground beef, lasagna noodles, marinara sauce, ricotta cheese, mozzarella. Calories: 700. Chef's note: A hearty dish for dinner."
    }
]

class FoodItemList(APIView):
    def get(self, request):
        return Response(food_items, status=status.HTTP_200_OK)

class FoodItemDetail(APIView):
    def get(self, request, pk):
        # Retrieve specific food item by its ID
        food_item = next((item for item in food_items if item["id"] == pk), None)
        if food_item:
            return Response(food_item, status=status.HTTP_200_OK)
        return Response({"error": "Food item not found"}, status=status.HTTP_404_NOT_FOUND)
