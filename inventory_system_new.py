"""Inventory Management System - Clean Version"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='inventory.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global inventory data
stock_data = {}


def add_item(item: str, qty: int, logs=None):
    """Add an item and its quantity to inventory."""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning(f"Invalid input types for item={item}, qty={qty}")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info(f"Added {qty} of {item}")


def remove_item(item: str, qty: int):
    """Remove a quantity of an item from inventory safely."""
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
                logging.info(f"Removed {item} from inventory")
        else:
            logging.warning(f"Tried to remove non-existent item: {item}")
    except KeyError:
        logging.exception("Item not found in stock_data during removal")


def get_qty(item: str) -> int:
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from JSON file."""
    global stock_data
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Inventory loaded successfully.")
    except FileNotFoundError:
        logging.warning("Inventory file not found. Starting with empty stock.")
        stock_data = {}


def save_data(file_path="inventory.json"):
    """Save inventory data to JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)
    logging.info("Inventory saved successfully.")


def print_data():
    """Print all items in inventory."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return items with quantity below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function for demonstration."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()