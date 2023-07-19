from ._anvil_designer import head_2Template
from anvil import *
import anvil.server

class head_2(head_2Template):
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

  def Main_click(self, **event_args):
    """This method is called when the link is clicked"""

  def Contact_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
