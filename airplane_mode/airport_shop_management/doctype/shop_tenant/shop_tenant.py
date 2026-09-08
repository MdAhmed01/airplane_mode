# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries


class ShopTenant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.SmallText | None
		company_name: DF.Data | None
		email: DF.Data | None
		id_proof: DF.Attach | None
		is_organization: DF.Check
		phone_number: DF.Data
		tax_id: DF.Data | None
		tenant_name: DF.Data | None
	# end: auto-generated types
	def autoname(self):
		base=self.company_name if self.is_organization else self.tenant_name
		prefix='TEN-'
		series=getseries(base,3)
		self.name=f'{prefix}{base.replace(" ","-").upper()}-{series}' if base else self.name

	_DOCTYPE_NAME = "Shop Tenent"
