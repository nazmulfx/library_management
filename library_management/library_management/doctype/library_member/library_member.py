# Copyright (c) 2024, Nazmul Hossain and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    
    #this method will run every time a document is saved
    def before_save(self):
        self.get_full_name()
    
    def get_full_name(self):
        self.full_name = (self.first_name + " " + self.last_name) if self.last_name else self.first_name




#####################  Controllers  #####################

def before_insert(self):
    description         = 'This is called before a document is prepared for insertion.'
    Insert              = 'X'
    Save                = ' '
    Submit              = ' '
    Cancel              = ' '
    Update_after_submit = ' '
    
    """In Frappe, the before_insert hook is triggered server-side before a new document is saved for the first time in the database. This means it runs before the document gets a database record (before its name is generated for new documents).
        This is particularly useful for:
            1. Setting or overriding default values: You can modify or set field values before the document is inserted into the database.
            2. Validations: Ensure certain conditions are met or data integrity is maintained.
            3. Custom logic: Implement any logic you want to run before a document is created."""

def before_naming(self):
    description         = 'This is called before the "name" property of the document is set.'
    Insert              = 'X'
    Save                = ' '
    Submit              = ' '
    Cancel              = ' '
    Update_after_submit = ' '
    
    """In Frappe, the before_naming hook works before a document's name (ID) is generated or set. 
        This hook is particularly useful when:
            1. The document is using a custom naming series.
            2. You want to programmatically set or modify the document's name before it is saved.
        When before_naming is Triggered:
            1. It is executed before the document's autoname logic runs.
            2. This happens only if the document does not already have a name set manually.
            3. The hook is triggered in the document lifecycle, usually during: Insert operations: when a new document is being saved for the first time."""

def autoname(self):
    description         = 'If defined in the controller, this method is used to set name property of the document.'
    Insert              = 'X'
    Save                = ' '
    Submit              = ' '
    Cancel              = ' '
    Update_after_submit = ' '
    
    """In Frappe, the autoname method in a controller hook is used to define how the name (or primary key) of a document is automatically generated when the document is created. It works during the insert phase, which occurs before a new document is saved to the database.
        When Does autoname Work?
            1. It is triggered only when a document is being created for the first time.
            2. It runs before the before_insert event.
            3. If the autoname logic is not explicitly defined in the controller, Frappe will fall back to the naming logic defined in the Options field of the DocType's Naming settings."""

def before_validate(self):
    description         = 'This hook is called before validation, use this for auto setting missing values.'
    Insert              = 'X'
    Save                = 'X'
    Submit              = 'X'
    Cancel              = ' '
    Update_after_submit = ' '
    
def validate(self):
    description         = 'Use this method to throw any validation errors and prevent the document from saving.'
    Insert              = 'X'
    Save                = 'X'
    Submit              = 'X'
    Cancel              = ' '
    Update_after_submit = ' '
       
def before_save(self):
    description         = 'This method is called before the document is saved.'
    Insert              = 'X'
    Save                = 'X'
    Submit              = ' '
    Cancel              = ' '
    Update_after_submit = ' ' 
    
def before_submit(self):
    description         = 'This method is called before the document is submitted.'
    Insert              = 'X'
    Save                = ' '
    Submit              = 'X'
    Cancel              = ' '
    Update_after_submit = ' ' 
    
def before_cancel(self):
    description         = 'This method is called before the document is cancelled.'
    Insert              = ' '
    Save                = ' '
    Submit              = ' '
    Cancel              = 'X'
    Update_after_submit = ' ' 
    
def before_update_after_submit(self):
    description         = 'This method is called when doc fields are updated on submitted document.'
    Insert              = ' '
    Save                = ' '
    Submit              = ' '
    Cancel              = ' '
    Update_after_submit = 'X'     
    
def db_insert(self):
    description         = 'This method inserts document in database, do not override this unless you are working on virtual DocType.'
    Insert              = 'X'
    Save                = ' '
    Submit              = ' '
    Cancel              = ' '
    Update_after_submit = ' '        
    
def after_insert(self):
    description         = 'This is called after the document is inserted into the database.'
    Insert              = 'X'
    Save                = ' '
    Submit              = ' '
    Cancel              = ' '
    Update_after_submit = ' '  
    
def db_update(self):
    description         = 'This method updates document in database, do not override this unless you are working on virtual DocType.'
    Insert              = ' '
    Save                = 'X'
    Submit              = 'X'
    Cancel              = 'X'
    Update_after_submit = 'X'   
    
def on_update(self):
    description         = 'This is called when values of an existing document is updated.'
    Insert              = ' '
    Save                = 'X'
    Submit              = 'X'
    Cancel              = ' '
    Update_after_submit = ' '    
    
def on_submit(self):
    description         = 'This is called when a document is submitted.'
    Insert              = ' '
    Save                = ' '
    Submit              = 'X'
    Cancel              = ' '
    Update_after_submit = ' '    
    
def on_cancel(self):
    description         = 'This is called when a submitted document is cancelled.'
    Insert              = ' '
    Save                = ' '
    Submit              = ' '
    Cancel              = 'X'
    Update_after_submit = ' '    
    
def on_update_after_submit(self):
    description         = 'This is called when a submitted document values are updated.'
    Insert              = ' '
    Save                = ' '
    Submit              = ' '
    Cancel              = ' '
    Update_after_submit = 'X'  
    
def on_change(self):
    description         = "This is called when a document's values has been changed. This method is also called when db_set is performed, so operation performed in this method should be idempotent."
    Insert              = ' '
    Save                = ' '
    Submit              = ' '
    Cancel              = ' '
    Update_after_submit = 'X'  
    
def before_rename(self):
    description         = 'This is called before a document is renamed.'
    
def after_rename(self):
    description         = 'This is called after a document is renamed.'
    
def on_trash(self):
    description         = 'This is called when a document is being deleted.'

def after_delete(self):
    description         = 'This is called after a document has been deleted.'