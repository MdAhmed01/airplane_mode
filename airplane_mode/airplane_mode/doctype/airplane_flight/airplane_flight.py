# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):

    def on_submit(self):
        self.status = "Completed"

    def validate(self):
        pilot_count = 0
        co_pilot_count = 0
        attendant_count = 0

        for row in self.flight_crew:

            if row.role == "Pilot":
                pilot_count += 1

            elif row.role == "Co-Pilot":
                co_pilot_count += 1

            elif row.role == "Flight Attendant":
                attendant_count += 1

        if pilot_count > 1:
            frappe.throw("A flight can have only one Pilot.")

        if co_pilot_count >3 :
            frappe.throw("A flight can have two to three Co-Pilot.")

        if attendant_count > 6:
            frappe.throw("A flight cannot have more than 6 Flight Attendants.")

    def on_update(self):
        frappe.msgprint("ON_UPDATE IS RUNNING")

        old_doc = self.get_doc_before_save()

        if old_doc and old_doc.gate_number != self.gate_number:

            frappe.enqueue(
                method="airplane_mode.job.update_ticket_gate_number",
                flight=self.name,
                gate_number=self.gate_number,
                queue="default",
                enqueue_after_commit=True
            )

    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from airplane_mode.airplane_mode.doctype.flight_crew_member.flight_crew_member import FlightCrewMember
        from frappe.types import DF

        airplane: DF.Link
        amended_from: DF.Link | None
        date_of_departure: DF.Date
        destination_airport: DF.Link
        destination_airport_code: DF.Data | None
        duration: DF.Duration
        flight_crew: DF.Table[FlightCrewMember]
        gate_number: DF.Data
        is_published: DF.Check
        route: DF.Data | None
        source_airport: DF.Link
        source_airport_code: DF.Data | None
        status: DF.Literal["Scheduled", "Completed", "Cancelled"]
        time_of_departure: DF.Time
        # end: auto-generated types

    _DOCTYPE_NAME = "Airplane Flight"