from ._anvil_designer import canvas_drawingsTemplate
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
import time

class canvas_drawings(canvas_drawingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def canvas_1_reset(self, **event_args):
    """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
    i = 1
    c = self.canvas_1
    while i < 20: 
      print(i)
      time.sleep(.05)
      c.stroke_style = "#2196F3"
      c.line_width = 3+i
    
    
      # Draw a filled rectangle
  
      # Draw a rectangle outline 25 pixels right of it
      c.stroke_rect(125, 100, 50, 75)
      c.stroke_rect(4, 200,50, 75)
      c.stroke()
      i += 1
  



    
