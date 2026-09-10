# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ShopRentPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		amount_due: DF.Currency
		amount_paid: DF.Currency
		due_date: DF.Int
		lease_contract: DF.Link
		naming_series: DF.Literal["RCPT-.YYYY.-.##"]
		payment_date: DF.Date
		payment_mode: DF.Literal["Cash", "UPI", "Credit Card", "Cheque"]
		payment_month: DF.Literal["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
		shop: DF.Link
		status: DF.Literal["Pending", "Paid", "Unpaid"]
		tenant: DF.Link
	# end: auto-generated types

	def on_submit(self):
		if self.status in ('Pending','Overdue','Partially Paid'):
			frappe.throw('You cannot submit the Payment Reciept until the status is Paid')

	_DOCTYPE_NAME = "Shop Rent Payment"
