# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe.utils import add_to_date


class ShopContract(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		contract_end_date: DF.Date
		contract_start_date: DF.Date
		rent_amount: DF.Currency
		security_deposite: DF.Currency
		shop: DF.Link
		shop_display_name: DF.Data
		status: DF.Literal["Draft", "Active", "Expired", "Cancel"]
		tenant: DF.Link
	# end: auto-generated types

	def on_update_after_submit(self):
		
		shop=frappe.get_doc('Shop',self.shop)
		if self.status=='Active':
			shop.status='Leased'
			shop.shop_name=self.shop_display_name
			shop.current_tenant = self.tenant
			shop.current_contract = self.name
			
		if self.status in ("Expired", "Cancel"):
			shop.status = "Available"
			shop.shop_name = ""
			shop.current_tenant = None
			shop.current_contract = None
		shop.save(ignore_permissions=True)

	def before_insert(self):
		shop=frappe.get_doc('Shop',self.shop)
		if shop.status=="Leased" and shop.current_contract!=self.name:
			frappe.throw(f"Shop {shop.name} is already leased. Cannot create a new contract for this shop.")

	
	#Contract Agreement duration validation
	def validate(self):
		self.contract_end_date=add_to_date(self.contract_start_date,years=2)
		if self.contract_start_date >= self.contract_end_date:
			frappe.throw("Contract start date must be before contract end date")

	_DOCTYPE_NAME = "Shop Contract"
