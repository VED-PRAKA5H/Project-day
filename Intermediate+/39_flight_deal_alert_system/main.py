from datetime import datetime, timedelta
from flight_data_and_search import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

# Define the origin airport IATA code (Varanasi in this case)
ORIGIN_LOCATION = "VNS"

# Create an instance of FlightData to interact with flight search API or data
fd = FlightData()

# Create an instance of DataManager to interact with data source
dm = DataManager()


def update_iata():
    """
    Update the IATA codes for each city in the data sheet.
    For each city, fetch the corresponding IATA code using FlightData API
    and update the data sheet with this code.
    """
    sheet_data = dm.get_sheet_data()  # Fetch current data from the sheet
    # Loop through each row in the "prices" data
    for row in sheet_data["prices"]:
        city = row["city"]  # Extract city name
        row_id = row["id"]  # Extract row identifier for updating
        # Search for IATA code of the city using FlightData API
        iata_code = fd.city_search(city=city)["data"][0]['iataCode']
        # Update the sheet with the found IATA code and print the response
        print(dm.update_cell(row_id=row_id, column="iataCode", value=iata_code))


# Uncomment below line to update IATA codes in the sheet
# update_iata()

def update_price():
    """
    Search for the cheapest flights from the origin location to each destination city
    over the next 6 months, update the sheet with new lowest prices if found,
    and prepare a notification message with the best deal.
    """
    # Generate a list of dates for the next 6 months (approx 183 days)
    next_6month = [(datetime.now() + timedelta(i)) for i in range(1, 183)]

    # Fetch the current price data from the sheet
    sheet_data = dm.get_sheet_data()

    # Dictionary to store new flight price data for each destination
    new_flight_price_data = {}

    # Loop through each destination in the sheet data
    for row in sheet_data["prices"]:
        # Unpack relevant details from each row
        city, destination_iata, current_price, row_id = row.values()
        print(f"Searching price for: {destination_iata}")

        # Use FlightData API to find the cheapest flight within the date range
        lowest_price, outbound_date, inbound_date = fd.find_cheapest_flight(
            date_range=next_6month,
            origin_location_iata=ORIGIN_LOCATION,
            destination_location_iata=destination_iata
        )

        if lowest_price == "N/A":
            # No flight found for this destination in the date range
            print("No flight found")
            # Keep the current price and dates as is
            new_flight_price_data[destination_iata] = {
                "price": current_price,
                "inbound_date": inbound_date,
                "outbound_date": outbound_date
            }
        else:
            # Flight found, check if the price is better or equal to the current stored price
            if lowest_price <= float(current_price):
                # Update with new lowest price and dates
                new_lowest = lowest_price
                new_flight_price_data[destination_iata] = {
                    "price": new_lowest,
                    "inbound_date": inbound_date,
                    "outbound_date": outbound_date
                }
                # Update the sheet with the new lowest price
                dm.update_cell(row_id=row_id, column="lowestPrice", value=f"{new_lowest}")

                # Print details of the best deal found
                print(
                    f"🛫 Found a flight to {destination_iata} "
                    f"(Outbound: {new_flight_price_data[destination_iata]['outbound_date']}, "
                    f"Inbound: {new_flight_price_data[destination_iata]['inbound_date']}) "
                    f"→ Lowest round-trip price: ₹{new_flight_price_data[destination_iata]['price']} "
                    f"(Search window: {next_6month[0].strftime('%Y-%m-%d')} to {next_6month[-1].strftime('%Y-%m-%d')})"
                )

    # After checking all destinations, sort them by price in ascending order
    sorted_offers = sorted(new_flight_price_data.items(), key=lambda item: float(item[1]["price"]))

    # Select the cheapest flight offer
    cheapest_iata, cheapest_data = sorted_offers[0]

    # Prepare a notification message for the lowest price alert
    message = (
        f"📢 Low price alert! Only ₹{cheapest_data['price']} to fly from {ORIGIN_LOCATION} to {cheapest_iata} "
        f"(Outbound: {cheapest_data['outbound_date']}, Inbound: {cheapest_data['inbound_date']}) "
        f"(Search window: {next_6month[0].strftime('%Y-%m-%d')} to {next_6month[-1].strftime('%Y-%m-%d')})"
    )

    return message


# Call update_price to get the notification message
notification = update_price()

# Create an instance of NotificationManager to send notifications
nm = NotificationManager()

print("Sending notification...")
# Send the notification with the lowest price alert message
nm.send_notification(update=notification)
