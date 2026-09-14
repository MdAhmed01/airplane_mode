import frappe


#Schedule Payment Reminders for pending or unpaid Records
def send_payment_reminders():
    settings = frappe.get_single("Airport Shop Settings")

    if not settings.rent_reminders:
        return

    payments = frappe.get_all("Shop Rent Payment",
            filters={ "status": ["in", ["Pending", "Unpaid"]]},
            fields=['shop','lease_contract','tenant','due_date','rent_amount']
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
                Amount: {payment.rent_amount}
                Kindly pay the rent before the due date.
                """,
                reference_doctype='Shop Rent Payment'
            )
   
    print('\nFunction is execute properly\n')



 #Schedule monthly payment records   
from frappe.utils import get_first_day, getdate, today


def create_monthly_rent_payments():

    today_date = getdate(today())
    current_month = get_first_day(today_date)

    contracts = frappe.get_all(
        "Shop Contract",
        filters={
            "status": "Active"
        },
        fields=[
            "name",
            "tenant",
            "shop",
            "contract_start_date",
            "contract_end_date",
            "rent_amount"
        ]
    )

    for contract in contracts:

        if not contract.contract_start_date or not contract.contract_end_date:
            continue

        start_date = getdate(contract.contract_start_date)
        end_date = getdate(contract.contract_end_date)

        # Convert contract dates to their respective months
        start_month = get_first_day(start_date)
        end_month = get_first_day(end_date)

        # Current month must be inside contract period
        if current_month < start_month or current_month > end_month:
            continue

        # Check if payment already exists for this contract and month
        existing_payment = frappe.db.exists(
            "Shop Rent Payment",
            {
                "lease_contract": contract.name,
                "payment_month": current_month
            }
        )

        if existing_payment:
            continue

        # Create this month's payment
        payment = frappe.new_doc("Shop Rent Payment")

        payment.lease_contract = contract.name
        payment.payment_month = current_month
        payment.due_date = current_month.replace(day=5)
        payment.rent_amount = contract.rent_amount
        payment.status = "Pending"

        payment.insert(ignore_permissions=True)