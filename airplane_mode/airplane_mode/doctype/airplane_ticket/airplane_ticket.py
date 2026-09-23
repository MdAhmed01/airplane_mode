# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

# import frappe
import frappe
import random
from frappe.model.docstatus import DocStatus
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
		destination_airport_code: DF.Data
		duration_of_flight: DF.Duration
		flight: DF.Link
		flight_price: DF.Currency
		gate_number: DF.Data | None
		passenger: DF.Link
		seat: DF.Data
		source_airport_code: DF.Data
		status: DF.Literal["Booked", "Checked-In", "Boarded"]
		total_amount: DF.Currency
	# end: auto-generated types

	# Calculate total amount
	def before_save(self):
			amount=0
			for item in self.add_ons:
				amount+=item.amount
			self.total_amount=self.flight_price+amount

# 	#No duplicates add_on allow 
	def validate(self):
		seen=set()
		unique_add_ons=[]
		for row in self.add_ons:
			if row.item not in seen:
				seen.add(row.item)
				unique_add_ons.append(row)      

		self.add_ons = unique_add_ons
		self.validate_max_seats()
	
#     # Don't allow submit if status is not boarded
	def on_submit(self):
		if self.status != "Boarded":
			frappe.throw("You cannot submit the Airplane Ticket document unless the status is 'Boarded'.")
	
	
	#Generate ramdom seat for passengers
	# def before_insert(self):
	# 	alphabet=["A","B","C","D","E"]
	# 	self.number=random.randrange(1,100)
	# 	self.letter=random.choice(alphabet)
	# 	self.seat=str(self.number)+self.letter

	#check the number of booked tickets exceed the capacity of the airplane
	def validate_max_seats(self):
		
		flight=frappe.get_doc('Airplane Flight', self.flight)
		capacity=frappe.db.get_value('Airplane',flight.airplane,'capacity')
		booked_tickets=frappe.db.count('Airplane Ticket',{'flight':self.flight})
		if booked_tickets>=capacity:
			frappe.throw("No more seats available for this flight.")

	

_DOCTYPE_NAME = "Airplane Ticket"
