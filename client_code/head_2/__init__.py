from ._anvil_designer import head_2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..Portfolio import Portfolio
from ..About import About
from ..Contact import Contact


class head_2(head_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def Main_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Main')
    pass

  def Portfolio_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Portfolio')
    pass

  def About_click(self, **event_args):
    open_form('About')
    """This method is called when the link is clicked"""

  def Contact_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Contact')
    pass




  