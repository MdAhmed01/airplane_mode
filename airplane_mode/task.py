import frappe

def send_payment_reminders():

    payments = frappe.get_all("Shop Rent Payment",
            filters={ "status": ["in", ["Pending", "Unpaid"]]},
            fields=['shop','lease_contract','tenant','due_date']
            )

    for payment in payments:
        tenant_email=frappe.db.get_value(
            'Shop Tenant',
            payment.tenant,
            'email'
        )
        
        if tenant_email:
            frappe.sendmail(
                recipients=[tenant_email],
                subject='Rent Payment Reminder!',
                message=f"""
                Dear {payment.tenant},
                Your rent payment for lease contract
                {payment.lease_contract} is pending.
                Due Date: {payment.due_date}
                Kindly pay the rent before the due date.
                """,
                reference_doctype='Shop Rent Payment'
            )
    frappe.db.commit()
    print('\nFunction is execute properly\n')




# def check():
#     frappe.log_error(
#         "Scheduler is working!",
#         "Scheduler Test"
#     )
