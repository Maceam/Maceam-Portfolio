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
import random
import datetime

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
    
  def canvas_data_mouse_enter(self, x, y, **event_args):
    # animation loop for data section
    animation_count = 0
    while animation_count < 1000:
      now = datetime.datetime.now()
      timestamp = int(now.timestamp())
      rand = random.randrange(1,100,1)
      c = self.canvas_data
      c.line_width = 3
      c.fill_style = "#2116F3"
      
      # Draw a filled rectangle  
      c.fill_rect(animation_count + 1, rand, 10, 10)
      
      c.fill_style = "#0016FF"
      c.fill_rect(animation_count +1, rand, 10, 10)
      animation_count  =  animation_count  + 1

      c.fill_style = "#00FFFF"
      c.fill_rect(animation_count, rand, 10, timestamp)
      animation_count =  animation_count + 1
      time.sleep(.001)

      c.clear_rect(animation_count, rand, 10, timestamp)

  