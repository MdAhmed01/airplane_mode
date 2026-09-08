# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShopContract(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		contract_end_date: DF.Date
		contract_start_data: DF.Date
		rent_amount: DF.Currency
		security_deposite: DF.Currency
		shop: DF.Link
		status: DF.Literal["Draft", "Active", "Expired", "Cancel"]
		tenant: DF.Link
	# end: auto-generated types

	_DOCTYPE_NAME = "Shop Contract"
