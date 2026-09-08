import frappe
import random
def execute():

    seat=frappe.get_all("Airplane Ticket",fields=["name","seat"])
    alphabet=["A","B","C","D","E"]      
    
    for s in seat:
        if not s.seat:
            number=random.randrange(1,100)
            letter=random.choice(alphabet)
            generate_seat=str(number)+letter
            frappe.db.set_value("Airplane Ticket",s.name,"seat",generate_seat)