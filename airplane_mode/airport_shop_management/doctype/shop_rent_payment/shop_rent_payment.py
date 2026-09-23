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
		amount: DF.Currency
		due_date: DF.Date
		lease_contract: DF.Link
		naming_series: DF.Literal["RCPT-.YYYY.-.##"]
		payment_date: DF.Date | None
		payment_mode: DF.Literal["Cash", "UPI", "Credit Card", "Cheque"]
		payment_month: DF.Date
		rent_amount: DF.Currency
		shop: DF.Link
		status: DF.Literal["Pending", "Paid", "Unpaid"]
		tenant: DF.Link
	# end: auto-generated types

	# def before_save(self):
	# 	if self.status=='Paid':
	# 		self.amount_paid=self.amount_due
		

	def on_submit(self):
		if self.status in ('Pending','Unpaid'):
			frappe.throw('You cannot submit the Payment Reciept until the status is Paid')

	def validate(self):
		amount=self.amount or 0
		if amount>self.rent_amount:
			frappe.throw("Amount paid cannot be greater than the rent amount.")
		if amount == self.rent_amount:
			frappe.msgprint("Amount Paid Success ✅")
			self.status = "Paid"
		else:
			self.status = "Unpaid"

			
			


	_DOCTYPE_NAME = "Shop Rent Payment"
