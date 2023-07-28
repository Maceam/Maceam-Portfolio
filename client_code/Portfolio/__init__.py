from ._anvil_designer import PortfolioTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil_extras import *
from ..Portfolio.Entry1 import Entry1
from ..Portfolio.Entry2 import Entry2

class Portfolio(PortfolioTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.newtest()

  #todo pick bodies of work so you can name shit correctly 
  def newtest(self, **event_args):
    new_panel = Entry1()
    new_panel2 = Entry2()
    c= FlowPanel()
    self.add_component(c)
    c.add_component(new_panel)
    c.add_component(new_panel2)


    