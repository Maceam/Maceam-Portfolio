from ._anvil_designer import AboutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.image

class About(AboutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.logoglitchy = app_tables.personal_brand.get(q.like(name))
    self.repeating_panel_1.items=app_tables.table_0.search()