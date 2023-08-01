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
    #print(len(app_tables.showcase.search())) #this just returns the number of rows in a table
    self.RepeatC2C() #this needs to be changed to not load until a button in portfolio is clicked.
    
  def RepeatC2C(self, **event_args):
    C2CRepeaterPanel= RepeatingPanel()
    C2CFlowPanel= FlowPanel()
    self.add_component(C2CFlowPanel)
    #table_row_total= len(app_tables.showcase.search()) #not nessesary just tells the total table size
    FolioWork= app_tables.showcase.search(Name=q.like('C2C%'))
    for Name in FolioWork:
      img = Image(display_mode= "fill_width", source= Name['PortImg'], vertical_align= "center")
      C2CFlowPanel.add_component(img)

    #self.ButtonExpander() this has been moved and not needed for now if readded add below self.init_compnents
    # Any code you write here will run before the form opens.
#we have moved the button expander elsewhere
"""def ButtonExpander(self, **event_args):
    ButtonExp= Button(text= "The Builders Cradel", align= "center")
    ButtonExp.role= "ButtonPortfolio"
    self.add_component(ButtonExp)

   def ButtonExpander_click(self, **event_args):"""
#we may need it here later so it stays for now.
