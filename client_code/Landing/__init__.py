from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js import window

class Landing(LandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    table_row= app_tables.showcase.get(Name=q.like('LandingGirl'))
    LandImg = Image(width= window.innerWidth, height= window.innerHeight, display_mode= "zoom_to_fill", source= table_row['PortImg'])


    #self.add_component(LandImg)

    self.init_components(**properties)
    self.add_component(LandImg)
    #table_row= app_tables.showcase.get(Name=q.like('LandingGirl'))
    #self.LandImg.source = table_row['PortImg']

  #def LandImg_show(self, **event_args):
    #pass
  # Any code you write here will run before the form opens.
  #def Landing(self, **event_args):
