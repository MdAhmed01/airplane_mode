# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Shop(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link
		area: DF.Data | None
		location: DF.Data | None
		shop_category: DF.Link | None
		shop_name: DF.Data | None
		shop_number: DF.Data
		status: DF.Literal["Available", "Lease", "Under Construction"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Shop"
