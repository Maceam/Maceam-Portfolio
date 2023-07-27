from ._anvil_designer import Form1Template
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

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def canvas_1_show(self, **event_args):
    c = self.canvas_1
    
  def canvas_1_reset(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.canvas_1
  
    c.begin_path()
    c.move_to(100,100)
    c.line_to(100,200)
    c.line_to(200,200)
    c.close_path()
  
    c.stroke_style = "#2196F3"
    c.line_width = 3
    c.fill_style = "#E0E0E0"
  
    c.fill()
    c.stroke()