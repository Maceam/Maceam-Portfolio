from ._anvil_designer import AboutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.image
import anvil.media
from anvil_extras.animation import animate, fade_in


class About(AboutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    table_row= app_tables.personal_brand.get(name=q.like('logoglitchyy'))
    self.logoglitchy.source = table_row['portfolioImages']
    
    self.AboutTxt.border = "8px"
    self.AboutTxt.font_size = 24

  def AboutTxt_show(self, **event_args):
    animate(self.AboutTxt, fade_in, duration=3000)

  def logoglitchy_show(self, **event_args):
    animate(self.logoglitchy, fade_in, duration=1000)



