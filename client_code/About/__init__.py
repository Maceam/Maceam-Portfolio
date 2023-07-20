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
          machines = anvil.server.call('get_all_machines')
          self.apply_view(machines)
    def about_image(self, view):
      filerow = app_tables.personal_brand.get(name=logoglitchyy)
      logoglitchy = Image(source= filerow)
      printf (filerow)
    # Any code you write here will run before the form opens.
