# Write Gate Number update function
import frappe


def update_ticket_gate_number(flight, gate_number):

    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={"flight": flight},
        pluck="name"
    )

    for ticket in tickets:
        frappe.db.set_value(
            "Airplane Ticket",
            ticket,
            "gate_number",
            gate_number
        )
