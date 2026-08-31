import frappe
import random
def execute():

    seat=frappe.get_all("Airplane Ticket",fields=["name","seat"])
    generate_seat=lambda: str(random.randint(1, 100)) + random.choice(["A", "B", "C", "D", "E", "F"])
    for s in seat:
        if not s.seat:
            frappe.db.set_value("Airplane Ticket",s.name,"seat",generate_seat())