
#command-line Campus Resource Management System

resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}

borrow_records = []
print(f"{'🔹 ' * 40}")
print(f"\n{'  ' * 10}{'Learn2Earn Campus Resource Management System'.upper()}{'  ' * 10}")
print(f"{'🔹 ' * 40}\n")


def add_resources():

    resources_id = input("Enter item ID: ").strip().upper()

    for resource in resources:
        if resource["id"] == resources_id:
            print("❌ ID already exist")
            return

    if resources_id == "":
        print("❌ ID cannot be empty")
        return

    print("continue.....")

    name = input("Enter item name: ").strip()
    category = input("Enter item category: ").strip()

    try:
        total = int(input("Enter Total Quantity: "))
    except ValueError:
        print("Enter an integer value")
        return

    if total <= 0:
        print("❌ Quantity must be greater than 0")
        return

    available = total

    resources.append({
        "id": resources_id,
        "name": name,
        "category": category,
        "total": total,
        "available": available
    })

    print("✅ Resource added successfully")


def list_resources():

    print("\n===== RESOURCE LIST =====")

    for resource in resources:
        print(
            f"{resource['id']} | "
            f"{resource['name']} | "
            f"{resource['category']} | "
            f"Total: {resource['total']} | "
            f"Available: {resource['available']}"
        )


def borrow_resource():

    fellow_id = input("Enter fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("❌ Fellow ID not found")
        return

    resource_id = input("Enter resource ID: ").strip().upper()

    resource = None

    for item in resources:
        if item["id"] == resource_id:
            resource = item
            break

    if resource is None:
        print("❌ Resource ID not found")
        return

    try:
        quantity = int(input("Enter quantity to borrow: "))
    except ValueError:
        print("Enter an integer value")
        return

    if quantity <= 0:
        print("❌ Quantity must be greater than 0")
        return

    if quantity > resource["available"]:
        print("❌ Not enough stock")
        return

    borrow_records.append({
        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": quantity
    })

    resource["available"] -= quantity

    print(
        f"✅ {fellows[fellow_id]} borrowed "
        f"{quantity} {resource['name']}(s)"
    )


def return_resource():

    fellow_id = input("Enter fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("❌ Fellow ID not found")
        return

    resource_id = input("Enter resource ID: ").strip().upper()

    resource = None

    for item in resources:
        if item["id"] == resource_id:
            resource = item
            break

    if resource is None:
        print("❌ Resource ID not found")
        return

    borrow_record = None

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            borrow_record = record
            break

    if borrow_record is None:
        print("❌ No borrowed record found")
        return

    print(
        f"{fellows[fellow_id]} has "
        f"{borrow_record['quantity']} unit(s) on loan"
    )

    try:
        quantity = int(input("Enter quantity to return: "))
    except ValueError:
        print("Enter an integer value")
        return

    if quantity <= 0:
        print("❌ Quantity must be greater than 0")
        return

    if quantity > borrow_record["quantity"]:
        print("❌ You cannot return more than borrowed")
        return

    resource["available"] += quantity
    borrow_record["quantity"] -= quantity

    if borrow_record["quantity"] == 0:
        borrow_records.remove(borrow_record)

    print("✅ Resource returned successfully")


def search_item():

    search_by_name = input(
        "Enter item name to search "
        "(eg Laptop, keyboard or headset): "
    )

    search_query = search_by_name.strip().lower()

    for resource in resources:

        if resource.get("name", "").lower() == search_query:

            print(f"{resource['name']} ✅ Found")
            print(f"ID: {resource['id']}")
            print(f"Category: {resource['category']}")
            print(f"Total: {resource['total']}")
            print(f"Available: {resource['available']}")

            return resource

    print("❌ Item not found.")
    return None


def filter_category():

    category = input("Enter category: ").strip().lower()

    found = False

    for resource in resources:

        if resource["category"].lower() == category:

            print(
                f"{resource['id']} | "
                f"{resource['name']} | "
                f"{resource['category']} | "
                f"Available: {resource['available']}"
            )

            found = True

    if not found:
        print("❌ No resource found")


def report():

    total_units = 0
    available_units = 0

    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    borrowed_units = total_units - available_units

    print("\n===== REPORT =====")

    print(f"Total units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Units currently borrowed: {borrowed_units}")

    print("\nLow stock:")

    for resource in resources:

        if resource["available"] < 3:

            print(
                f"{resource['name']} - "
                f"{resource['available']} available"
            )

    max_borrowed = 0

    for resource in resources:

        borrowed = resource["total"] - resource["available"]

        if borrowed > max_borrowed:
            max_borrowed = borrowed

    print("\nMost borrowed:")

    for resource in resources:

        borrowed = resource["total"] - resource["available"]

        if borrowed == max_borrowed and borrowed > 0:

            print(
                f"{resource['name']} - "
                f"{borrowed} borrowed"
            )


def main():

    while True:

        print("\n===== MENU =====")
        print("1. Add Resource")
        print("2. List Resources")
        print("3. Borrow Resource")
        print("4. Return Resource")
        print("5. Search Resource")
        print("6. Filter Category")
        print("7. Report")
        print("8. Exit")
        print(f"{'🔹 ' * 40}\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_resources()

        elif choice == "2":
            list_resources()

        elif choice == "3":
            borrow_resource()

        elif choice == "4":
            return_resource()

        elif choice == "5":
            search_item()

        elif choice == "6":
            filter_category()

        elif choice == "7":
            report()

        elif choice == "8":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice")


main()
