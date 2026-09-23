import frappe

def get_context(context):
	shop_number = frappe.form_dict.get("Shop")
	context.Shop = shop_number
	pass
