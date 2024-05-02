from ._anvil_designer import MainTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..Portfolio import *
from ..About import About
from ..Contact import Contact
from ..Landing import Landing
from anvil_extras import *
from anvil_extras import popover
from anvil_extras import augment
from processing import *
import random
from anvil.js import window

class Main(MainTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.header_panel.role = "FlowPanelSticky"

  '''Header events'''
  def header_main_click(self, **event_args):
    self.content_panel.open_form('Landing')

  def header_portfolio_click(self, **event_args):
    open_form('Portfolio')

  def header_about_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('About')

  def header_contact_click(self, **event_args):
    open_form('Contact')

    
