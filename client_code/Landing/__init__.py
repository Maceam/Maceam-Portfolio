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
import pyautogui
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

  def canvas_design_show(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    pass

  def canvas_data_mouse_enter(self, x, y, **event_args):
    n = 1
    while n = < 100
      c = self.canvas_data
      c.stroke_style = "#2196F3"
      c.line_width = 3
      c.fill_style = "#E0E0E0"
    
      # Draw a filled rectangle  
      c.fill_rect(mouseX, 100, 50, 75)
    
      # Draw a rectangle outline 25 pixels right of it
      c.stroke_rect(125, 100, 50, 75)
    
      # Remove colour from a smaller rectangle
      c.clear_rect(120, 125, 20, 30)
 

