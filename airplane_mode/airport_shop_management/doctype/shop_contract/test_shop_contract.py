# Copyright (c) 2026, Ahmed Ansari and Contributors
# See license.txt

# import frappe
from airplane_mode.airport_shop_management.doctype.shop_contract import shop_contract
import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestShopContract(IntegrationTestCase):
	"""
	Integration tests for ShopContract.
	Use this class for testing interactions between multiple components.
	"""

	def test_shop_name_update_on_contract_activation(self):
		shop = frappe.get_doc("Shop", "Shop-003")
		tenant = frappe.get_doc("Shop Tenant", "TEN-FASIAL-AHMED001")
		# Create Shop Contract
		shop_contract = frappe.new_doc("Shop Contract")
		shop_contract.shop = shop.name
		shop_contract.tenant = tenant.name
		shop_contract.contract_start_date = "2024-01-01"
		shop_contract.contract_end_date = "2024-12-31"
		shop_contract.rent_amount = 1000
		shop_contract.security_deposit = 500
		shop_contract.status = "Active"
		shop_contract.shop_display_name = "New Shop Name"
		shop_contract.insert()
		shop = frappe.get_doc("Shop", shop_contract.shop)
		self.assertEqual(shop.shop_name, "New Shop Name")