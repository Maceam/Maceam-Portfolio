from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
from ..Portfolio import Portfolio
from ..About import About
from ..Contact import Contact

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
