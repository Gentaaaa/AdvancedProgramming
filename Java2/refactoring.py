def filter_by_type(items, item_type):
    """
    Filters a list of items by the given type.

    Parameters:
        items (list): List of dictionaries with a 't' key.
        item_type (str): The type to filter by.

    Returns:
        list: Items where 't' == item_type.
    """
    return [item for item in items if item.get("t") == item_type]

# Example usage
if __name__ == "__main__":
    items = [
        {"id": 1, "t": "book", "price": 20},
        {"id": 2, "t": "food", "price": 10},
        {"id": 3, "t": "book", "price": 15},
        {"id": 4, "t": "food", "price": 5}
    ]

    books = filter_by_type(items, "book")
    print("Filtered items (type='book'):")
    print(books)
