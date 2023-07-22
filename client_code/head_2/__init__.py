from ._anvil_designer import head_2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class head_2(head_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def Portfolio_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def About_click(self, **event_args):
    """This method is called when the link is clicked"""

    pass

  def Main_click(self, **event_args):
    """This method is called when the link is clicked"""
  pass
  def Contact_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
