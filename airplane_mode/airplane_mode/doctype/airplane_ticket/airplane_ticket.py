# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from airplane_mode.airplane_mode.doctype.airplane_ticket_add_on_item.airplane_ticket_add_on_item import AirplaneTicketAddonItem
		from frappe.types import DF

		add_ons: DF.Table[AirplaneTicketAddonItem]
		amended_from: DF.Link | None
		departure_date: DF.Date
		departure_time: DF.Time
		destination_airport_code: DF.Data | None
		duration_of_flight: DF.Duration
		flight: DF.Link
		flight_price: DF.Currency
		passenger: DF.Link
		seat: DF.Data | None
		source_airport_code: DF.Data | None
		ticket_status: DF.Literal["Booked", "Checked-In", "Boarded"]
		total_amount: DF.Currency
	# end: auto-generated types


	#Generate ramdom seat for passengers
	def before_save(self):
		alphabet=["A","B","C","D","E","F"]
		self.number=random.randrange(1,100)
		self.letter=random.choice(alphabet)
		self.seat=str(self.number)+self.letter

	#No duplicates add_on allow 
	def validate(self):
		seen=set()
		unique_add_ons=[]
		for row in self.add_ons:
			if row.item not in seen:
				seen.add(row.item)
				unique_add_ons.append(row)      

		self.add_ons = unique_add_ons

	
    # Don't allow submit if status is not boarded
	def on_submit(self):
		if self.ticket_status != "Boarded":
			frappe.throw("You cannot submit the Airplane Ticket document unless the status is 'Boarded'.")
	
	






	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from airplane_mode.airplane_mode.doctype.airplane_ticket_add_on_item.airplane_ticket_add_on_item import AirplaneTicketAddonItem
		from frappe.types import DF

		add_ons: DF.Table[AirplaneTicketAddonItem]
		amended_from: DF.Link | None
		departure_date: DF.Date
		departure_time: DF.Time
		destination_airport: DF.Link
		destination_airport_code: DF.Data
		duration_of_flight: DF.Duration
		flight: DF.Link
		flight_price: DF.Currency
		passenger: DF.Link
		source_airport: DF.Link
		source_airport_code: DF.Data
		ticket_status: DF.Literal["Booked", "Checked-In", "Boarded"]
		total_amount: DF.Currency
	# end: auto-generated types

	_DOCTYPE_NAME = "Airplane Ticket"
