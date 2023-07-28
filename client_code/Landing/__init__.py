from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Landing(LandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    table_row= app_tables.showcase.get(Name=q.like('LandingGirl'))
    LandImg = Image(display_mode= "fill_width", source= table_row['PortImg'], vertical_align= "center")
    LandPanel = ColumnPanel()
    
    self.init_components(**properties)
    self.add_component(LandPanel)
    LandPanel.add_component(LandImg, full_width_row=True)
    LandImg.role="LandingImg"
    #self.add_component(LandImg)


  # Any code you write here will run before the form opens.

