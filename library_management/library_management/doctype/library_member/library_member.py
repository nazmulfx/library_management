# Copyright (c) 2024, Nazmul Hossain and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    
    #this method will run every time a document is saved
	def before_save(self):
		self.full_name = (self.first_name + " " + self.last_name) if self.last_name else self.first_name