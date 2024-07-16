from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Portfolio import Portfolio
from ..About import About
from ..Contact import Contact
import time
class Landing(LandingTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Set Form properties and Data Bindings.
    self.ClickMeMethod()
    self.CanvasLoader()

    
  def ClickMeMethod(self, **event_args): 
    ButtonMoving = Button(role= "CallToAction", text= "Come Explore", font= "D0tmatrix", font_size= 24)
    self.add_component(ButtonMoving)
    ButtonMoving.add_event_handler('click', self.ClickMeMethod_click)

  def ClickMeMethod_click(self, **event_args): 
    portfolio_panel = Portfolio()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(portfolio_panel)

  def CanvasLoader(self, **event_args): 
    self.canvas_data.visible = True
    self.canvas_design.visible = True
    self.canvas_data_show()
    self.canvas_design_show()

  def canvas_data_show(self, **event_args):
    c = self.canvas_data
    c.visible = True

    # Draw an image at position (100,100)
    n = 1
    while n < 100:
      c.fill_style = "rgba(n,111,222,22)"
      c.fill_rect(n, 22, n, 222)
      n= n + 1 
      time.sleep(5)

  def canvas_design_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    pass
 

