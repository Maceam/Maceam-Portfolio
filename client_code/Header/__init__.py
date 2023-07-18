from ._anvil_designer import HeaderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Header(HeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
    
  def portfolio_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
    
  def about_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
    
  def contact_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

