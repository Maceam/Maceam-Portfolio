from ._anvil_designer import MainTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..Portfolio import Portfolio
from ..About import About
from ..Contact import Contact

about_panel = About()
portfolio_panel = Portfolio()
contact_panel = Contact()



class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def header_main_click(self, **event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    open_form('Main')
    self.header_main.underline = true
  def header_portfolio_click(self, **event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(portfolio_panel)

    
  def header_about_click(self, **event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(about_panel)

  def header_contact_click(self, **event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(contact_panel)
    self.refresh_data_bindings()
    





