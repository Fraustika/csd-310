import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'outland_user',
    'password': 'outland_adven',
    'host': 'localhost',
    'port': '3306',
    'database': 'outland_adventures',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:

    db.close()

    # Create a cursor object
    cursor = conn.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS outland_reports")
    cursor.execute("USE outland_reports")

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sales (
        id INT AUTO_INCREMENT PRIMARY KEY,
        item_type VARCHAR(255),
        quantity INT,
        revenue FLOAT,
        date DATE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        region VARCHAR(255),
        bookings INT,
        date DATE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Inventory (
        id INT AUTO_INCREMENT PRIMARY KEY,
        item_id INT,
        acquired_date DATE
    )
    ''')

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

    import datetime

    # Sample data
    sales_data = [
        {"item_type": "buy", "quantity": 10, "revenue": 1000, "date": "2025-01-15"},
        {"item_type": "rent", "quantity": 15, "revenue": 750, "date": "2025-01-20"},
        {"item_type": "buy", "quantity": 5, "revenue": 500, "date": "2025-02-10"},
        {"item_type": "rent", "quantity": 20, "revenue": 1000, "date": "2025-02-15"},
    ]

    booking_data = [
        {"region": "Africa", "bookings": 50, "date": "2025-01-15"},
        {"region": "Asia", "bookings": 70, "date": "2025-01-20"},
        {"region": "Southern Europe", "bookings": 30, "date": "2025-02-10"},
        {"region": "Africa", "bookings": 40, "date": "2025-02-15"},
    ]

    inventory_data = [
        {"item_id": 1, "acquired_date": "2018-01-10"},
        {"item_id": 2, "acquired_date": "2017-05-22"},
        {"item_id": 3, "acquired_date": "2020-07-18"},
        {"item_id": 4, "acquired_date": "2016-11-30"},
    ]


    def sales_report(sales_data):
        total_bought = sum(item["quantity"] for item in sales_data if item["item_type"] == "buy")
        total_rented = sum(item["quantity"] for item in sales_data if item["item_type"] == "rent")
        revenue_bought = sum(item["revenue"] for item in sales_data if item["item_type"] == "buy")
        revenue_rented = sum(item["revenue"] for item in sales_data if item["item_type"] == "rent")

        report = f"Sales Report for Equipment (Buy vs. Rent)\n\n"
        report += f"Total Items Bought: {total_bought}\n"
        report += f"Total Items Rented: {total_rented}\n\n"
        report += f"Revenue from Sales:\n- Total Revenue from Bought Items: ${revenue_bought}\n\n"
        report += f"Revenue from Rentals:\n- Total Revenue from Rented Items: ${revenue_rented}\n\n"
        report += f"Analysis:\n- Comparison of total items bought versus rented.\n"
        report += f"- Assessment of revenue generated from each category.\n"
        report += f"- Insights on whether the purchase option is profitable.\n"
        report += f"- Recommendations on inventory strategy based on the data.\n\n"
        report += f"Conclusion:\nBased on the data, Blythe and Jim can determine if the equipment sales aspect of the business is sustainable or if adjustments are needed.\n"

        return report


    def booking_trends_report(booking_data):
        regions = ["Africa", "Asia", "Southern Europe"]
        report = f"Booking Trends by Location\n\n"

        for region in regions:
            total_bookings = sum(item["bookings"] for item in booking_data if item["region"] == region)
            report += f"{region}:\n- Total Bookings: {total_bookings}\n- Trend Analysis: [Upward/Downward/Stable]\n\n"

        report += f"Analysis:\n- Detailed analysis of booking trends in each region.\n"
        report += f"- Identification of regions experiencing a downward trend.\n"
        report += f"- Insights on which areas are performing poorly.\n\n"
        report += f"Recommendations:\n- Suggestions for changes in marketing strategy for underperforming regions.\n"
        report += f"- Consideration of phasing out less popular destinations in favor of more popular ones.\n\n"
        report += f"Conclusion:\nThis report will help Blythe and Jim identify which regions need attention and how to adjust their strategies to improve bookings.\n"

        return report


    def inventory_age_report(inventory_data):
        current_date = datetime.datetime.now()
        threshold_date = current_date - datetime.timedelta(days=5 * 365)

        old_inventory = [item for item in inventory_data if
                         datetime.datetime.strptime(item["acquired_date"], "%Y-%m-%d") < threshold_date]

        report = f"Inventory Age Report\n\n"
        report += f"Total Inventory Items: {len(inventory_data)}\n"
        report += f"Items Over 5 Years Old: {len(your_list_here)}"