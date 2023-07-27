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
    LandImg = Image(width= window.innerHeight, height= window.innerWidth, source="_/theme/Asset%2022img.png", display_mode= "fill_width")
    #self.add_component(LandImg)

    self.init_components(**properties)
    self.add_component(LandImg)
    
  #def LandImg_show(self, **event_args):
    #pass
  # Any code you write here will run before the form opens.
  #def Landing(self, **event_args):
