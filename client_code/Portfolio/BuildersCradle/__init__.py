from ._anvil_designer import BuildersCradleTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BuildersCradle(BuildersCradleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def whatever(self, **event_args):
    pass

    #self.ButtonExpander() this has been moved and not needed for now if readded add below self.init_compnents
    # Any code you write here will run before the form opens.
#we have moved the button expander elsewhere
"""def ButtonExpander(self, **event_args):
    ButtonExp= Button(text= "The Builders Cradel", align= "center")
    ButtonExp.role= "ButtonPortfolio"
    self.add_component(ButtonExp)

   def ButtonExpander_click(self, **event_args):"""
#we may need it here later so it stays for now.
