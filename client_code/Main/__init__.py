from ._anvil_designer import MainTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..Portfolio import Portfolio
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
    #self.header_panel.role = "FlowPanelSticky"
    
  def header_main_click(self, **event_args):
    """This method is called when the link is clicked"""
   
    """Clears the page and adds the requested panel"""
    landing_panel = Landing()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(landing_panel)
    
    """changes which header shows as selected"""
    self.header_about.role = "HeaderDefault"
    self.header_contact.role = "HeaderDefault"
    self.header_main.role = "HeaderSelected"
    self.header_portfolio.role = "HeaderDefault"
    
  def header_portfolio_click(self, **event_args):
    """This method is called when the link is clicked"""

    """Clears the page and adds the requested panel"""
    portfolio_panel = Portfolio()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(portfolio_panel)

    """changes which header shows as selected"""
    self.header_about.role = "HeaderDefault"
    self.header_contact.role = "HeaderDefault"
    self.header_main.role = "HeaderDefault"
    self.header_portfolio.role = "HeaderSelected"
    
  def header_about_click(self, **event_args):
    """This method is called when the link is clicked"""
    """Clears the page and adds the requested panel"""
    about_panel = About()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(about_panel)

    """changes which header shows as selected"""
    self.header_about.role = "HeaderSelected"
    self.header_contact.role = "HeaderDefault"
    self.header_main.role = "HeaderDefault"
    self.header_portfolio.role = "HeaderDefault"
    
  def header_contact_click(self, **event_args):
    """This method is called when the link is clicked"""
    """Clears the page and adds the requested panel"""
    contact_panel = Contact()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(contact_panel)

    """changes which header shows as selected"""
    self.header_about.role = "HeaderDefault"
    self.header_contact.role = "HeaderSelected"
    self.header_main.role = "HeaderDefault"
    self.header_portfolio.role = "HeaderDefault"

  def LandingImg_show(self, **event_args):
    landing_panel = Landing()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(landing_panel)

  def form_show(self, **event_args):
    landing_panel = Landing()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(landing_panel)




