import frappe 
def execute():
    flight_passengers =frappe.db.get_all("Flight Passenger",pluck="name")
    for p in flight_passengers:
        flight_passenger=frappe.get_doc("Flight Passenger",p)
        flight_passenger.set_full_name()
        flight_passenger.save()

    frappe.db.commit()