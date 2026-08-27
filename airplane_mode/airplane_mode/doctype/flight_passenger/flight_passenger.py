# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		self.full_name= f"{self.first_name} {self.last_name}"
	 

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date_of_birth: DF.Date
		first_name: DF.Data
		full_name: DF.Data | None
		last_name: DF.Data | None
		name: DF.Int | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Flight Passenger"
