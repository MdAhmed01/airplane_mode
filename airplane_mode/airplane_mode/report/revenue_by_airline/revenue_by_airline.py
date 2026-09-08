# Copyright (c) 2026, Ahmed Ansari and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.query_builder import DocType
from frappe.query_builder.functions import Sum


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()
	chart = {
        "data": {
            "labels": [row["airline"] for row in data],
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [row["total_revenue"] or 0 for row in data],
                }
            ],
			
        },
        "type": "donut",
    }
	report_summary = [{
 		"value": sum(row["total_revenue"] or 0 for row in data),
 		"indicator": "Green",
 		"label": _("Total Revenue"),
 		"datatype": "Currency",
 		"currency": "INR"
	}]

	return columns, data, None, chart, report_summary



def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Airline"),
			"fieldname": "airline",
			"fieldtype": "Link",
			"options": "Airline"
		},
		{
			"label": _("Revenue"),
			"fieldname": "total_revenue",
			"fieldtype": "Currency",
		},
	]


def get_data() -> list[list]:

	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	airline=frappe.qb.DocType('Airline')
	airplane=frappe.qb.DocType('Airplane')
	airplane_flight=frappe.qb.DocType('Airplane Flight')
	airplane_ticket=frappe.qb.DocType('Airplane Ticket')

	query = (
		
		frappe.qb.from_(airline)
		.left_join(airplane).on(airline.name == airplane.airline)
		.left_join(airplane_flight).on(airplane.name == airplane_flight.airplane)
		.left_join(airplane_ticket).on((airplane_flight.name == airplane_ticket.flight) & (airplane_ticket.docstatus == 1))
		.select(
			airline.name.as_("airline"),
			Sum(airplane_ticket.total_amount).as_("total_revenue")
		)
		.groupby(airline.name).orderby(Sum(airplane_ticket.total_amount),order=frappe.qb.desc)
	)
	return query.run(as_dict=True)





