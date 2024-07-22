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
    self.ClickMeMethodDesign()
    self.CanvasLoader()
  
    
  def ClickMeMethod(self, **event_args): 
    ButtonMoving = Button(role= "CallToAction", text= "Data Analysis", font= "D0tmatrix", font_size= 28)
    self.add_component(ButtonMoving)
    ButtonMoving.add_event_handler('click', self.ClickMeMethod_click)

  def ClickMeMethod_click(self, **event_args): 
    time.sleep(.2)
    portfolio_panel = Portfolio()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(portfolio_panel)

  def ClickMeMethodDesign(self, **event_args): 
    ButtonMovingRight = Button(role= "CallToActionRight", text= "Deisgn", font= "D0tmatrix", font_size= 28)
    self.add_component(ButtonMovingRight)
    ButtonMovingRight.add_event_handler('click', self.ClickMeMethod_click)

  def ClickMeMethodDesign_click(self, **event_args): 
    time.sleep(.7)
    portfolio_panel = Portfolio()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(portfolio_panel)

  def CanvasLoader(self, **event_args): 
    self.canvas_data.visible = True
    self.canvas_design.visible = True
    
  def canvas_data_mouse_enter(self, x, y, **event_args):
    # animation loop for data section
    random_animation = random.randrange(1,4,1)
    animation_count = 0
    if random_animation == 1:
      while animation_count < 1000:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp())
        rand = random.randrange(1,100,1)
        c = self.canvas_data
        c.line_width = 2
        c.fill_style = "#3F0691"
        
        # Draw a filled rectangle  
        c.fill_rect(animation_count + 1, rand, 16, rand^2)
        
        c.fill_style = "#9EAECA"
        c.fill_rect(animation_count +1, rand, 16, 16^16)
        animation_count  =  animation_count  + 1
  
        c.fill_style = "#DFE3EF"
        c.fill_rect(animation_count, rand, 4, timestamp)
        animation_count =  animation_count + 1
        time.sleep(.002)
  
        c.clear_rect(animation_count, rand, 2, timestamp)
  
        c.fill_style = "#3F0691"
        c.fill_rect(animation_count, rand, 4, timestamp)
        animation_count =  animation_count + 1
        
    elif random_animation == 2:
      while animation_count < 1000:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp())
        rand = random.randrange(1,100,1)
        c = self.canvas_data
        c.line_width = 16
        c.fill_style = "#3F0691"
        
        # Draw a filled rectangle  
        c.fill_rect(animation_count + 1, rand, 4, 4^4)
        
        c.fill_style = "#3F0691"
        c.fill_rect(animation_count +1, rand, 16, 4)
        animation_count  =  animation_count  + 1
  
        c.fill_style = "#DFE3EF"
        c.fill_rect(animation_count, rand, 2, timestamp)

        time.sleep(.005)
    
    elif random_animation == 3:
      
      while animation_count < 1000:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp())
        rand = random.randrange(1,100,1)
        c = self.canvas_data
        c.line_width = 16
        
        c.fill_style = "#DFE3EF"
        # Draw a filled rectangle  
        c.fill_rect(animation_count + 1, rand, 4, 4)
        
        c.fill_style = "#3F0691"
        c.fill_rect(animation_count +1, rand, 10, 16^2)
        animation_count  =  animation_count  + 1
  
        c.fill_style = "#3F0691"
        c.fill_rect(animation_count, rand, 16, timestamp)
        animation_count =  animation_count + 1
        time.sleep(.0001)
  
        c.fill_style = "#121218"
        c.fill_rect(animation_count, rand, 4, timestamp)
        animation_count =  animation_count + 1

    elif random_animation == 4:
      while animation_count < 1000:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp())
        rand = random.randrange(1,100,1)
        c = self.canvas_data
        c.line_width = 16
        
        c.fill_style = "#DFE3EF"
        c.fill_rect(animation_count + 1, rand, 16, 16)
        
        c.fill_style = "#3F0691"
        c.fill_rect(animation_count +1, rand, 16, 16^2)
        animation_count  =  animation_count  + 1
        
        c.fill_style = "#9EAECA"
        c.fill_rect(animation_count, rand, 16, timestamp)
        animation_count =  animation_count + 1
        time.sleep(.00001)
        
        c.fill_style = "#DFE3EF"
        c.fill_rect(animation_count, rand, rand, timestamp^timestamp)
        animation_count =  animation_count + 1

  def canvas_design_mouse_enter(self, x, y, **event_args):
 # animation loop for data section
    random_animation = random.randrange(1,3,1)
    animation_count = 0
    if random_animation == 1:
      while animation_count < 1000:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp())
        rand = random.randrange(1,512,1)
        c = self.canvas_design
        c.line_width = 2
        c.fill_style = "#121218"
        
        # Draw a filled rectangle  
        c.fill_rect(animation_count + 1, rand, 16, rand^2)
        
        c.fill_style = "#9EAECA"
        c.fill_rect(animation_count +1, rand, 16, 16^16)
        animation_count  =  animation_count  + 1
  
        c.fill_style = "#3F0691"
        c.fill_rect(animation_count, rand, 4, timestamp)
        animation_count =  animation_count + 1
        time.sleep(.002)
  
        c.clear_rect(rand, rand, rand, timestamp^timestamp)
  
        c.fill_style = "#3F0691"
        c.fill_rect(animation_count, rand, 4, timestamp)
        animation_count =  animation_count + 1
        
    elif random_animation == 2:
      while animation_count < 1000:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp())
        rand = random.randrange(1,256,1)
        c = self.canvas_design
        c.line_width = 2
        c.fill_style = "#3F0691"
        
        # Draw a filled rectangle  
        c.fill_rect(0, animation_count + 1, 16, rand^2)
        
        c.fill_style = "#9EAECA"
        c.fill_rect(animation_count +1, rand, 16, 16^16)
        animation_count  =  animation_count  + 1
  
        c.fill_style = "#121218"
        c.fill_rect(animation_count, rand, 128, 16)
        animation_count =  animation_count + 1
        time.sleep(.002)
  
        c.clear_rect(rand, rand, rand, timestamp^2)
  
        c.fill_style = "#3F0691"
        c.fill_rect(animation_count+1, rand*2, 128, 2)
        animation_count =  animation_count + 1
    
    elif random_animation == 3:
      while animation_count < 1000:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp())
        rand = random.randrange(1,16,1)
        c = self.canvas_design
        c.line_width = 2
        animation_count =  animation_count + 1
        time.sleep(.002)
        c.clear_rect(animation_count, rand, 16, 128)
  
