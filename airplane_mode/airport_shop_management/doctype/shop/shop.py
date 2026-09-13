# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Shop(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airport: DF.Link
		area: DF.Data
		current_contract: DF.Link | None
		current_tenant: DF.Link | None
		is_published: DF.Check
		location: DF.Data | None
		route: DF.Data | None
		shop_category: DF.Link | None
		shop_name: DF.Data | None
		shop_number: DF.Data
		shop_type: DF.Link | None
		status: DF.Literal["Available", "Leased", "Under Construction"]
	# end: auto-generated types

	#Shop Number Naming convention
def before_save(self):
	if self.status=='Available':
		self.is_published=1
	else:
		self.is_published=0


		
	

	_DOCTYPE_NAME = "Shop"
