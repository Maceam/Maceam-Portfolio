from ._anvil_designer import CanvasTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Canvas(CanvasTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.test_canvas
    
  def test_canvas(self, **event_args):
    t = Canvas()
    get_open_form().content_panel.add_component(t)
    
  def math_canvas(self, **event_args):
    c = self.test_canvas
  
    # Set the stroke and fill styles
    c.stroke_style = "#2196F3"
    c.line_width = 3
    c.fill_style = "#E0E0E0"
  
    # Draw a filled rectangle  
    c.fill_rect(100, 100, 50, 75)
  
    # Draw a rectangle outline 25 pixels right of it
    c.stroke_rect(125, 100, 50, 75)
  
    # Remove colour from a smaller rectangle
    c.clear_rect(120, 125, 20, 30)