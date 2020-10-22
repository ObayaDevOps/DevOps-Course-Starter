from flask import session

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return session.get('items', _DEFAULT_ITEMS) 


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """

    items = get_items()
    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0
    new_item = { 'id': id, 'title': title, 'status': 'Not Started' }

    if(items != None):
        # Add the item to the list
        items.append(new_item)
    else:
        # Or create a list with the new items
        items = [new_item]

    session['items'] = items
    return new_item



def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


def mark_item_complete(id):
    """
    Changes the status of the item to complete.

    Args:
        title: The title of the item.

    """
    items = get_items()
    item = next((item for item in items if item['id'] == int(id)), None)

    if item != None:
        item['status'] = 'Completed'

    new_items = items.ap



def remove_item(id):
    """
    Removes item with the specified title from the session.

    Args:
        title: The title of the item.

    Returns:
        item: A Boolean representing if the removal was successful or not.
    """
    items = get_items()

    item = next((item for item in items if item['id'] == int(id)), None)

    if item != None:
        new_items = items.remove(item)
        session['items'] = new_items
        return True
    else:
        return False


def clear_all_items():
    """
    Removes all items from the session.

    """
    session['items'] = []


    
    