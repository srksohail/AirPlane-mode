# Copyright (c) 2026, sohail and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document


class AirplaneTicket(Document):
	def before_insert(self):
		self.set_seat()


	def set_seat(self):
		Number = random.randint(1,999)
		letters = random.choice(['A','B','C','D','E'])
		self.seat =f"{Number}{letters}"


	def before_save(self):
		items = self.add_ons
		unique_item = []
		seen = set()

		for row in items:
			if row.item not in seen:
				print(row.item)
				seen.add(row.item)
				unique_item.append(row)

			self.set("add_ons",unique_item)

	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw("Passenger must be Boarded before submitting the ticket.")


	def validate(self):
		total_addons_amount = 0
		for item in self.add_ons:
			total_addons_amount += item.amount
		self.total_amount = total_addons_amount + self.flight_price
	

