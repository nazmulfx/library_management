# Copyright (c) 2024, Nazmul Hossain and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryMembership(Document):
            
    def before_submit(doc):
        
        # task: before creating a new membership checking that this person already have membership or not? if not then allow to create membership
        exists = frappe.db.exists(
            "Library Membership",
            {
                'library_member': doc.library_member,
                'docstatus': DocStatus.submitted(),
                'to_date': (">", doc.from_date),
            }
        )
        if exists:
            frappe.throw("There is an active membership for this member.")
