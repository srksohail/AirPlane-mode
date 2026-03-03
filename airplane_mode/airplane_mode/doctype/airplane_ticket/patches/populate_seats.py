import frappe
def execute():
    airplane_tickets = frappe.db.get_all(
        "Airplane Ticket")
    for i in airplane_tickets:
        ticket = frappe.get_doc("Airplane Ticket",i)
        ticket.set_seat()
        ticket.save()

    frappe.db.commit()