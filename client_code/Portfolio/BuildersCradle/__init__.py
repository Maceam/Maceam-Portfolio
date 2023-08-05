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
    self.RepeatC2C()
    
  def RepeatC2C(self, **event_args):
    HeroPanel= ColumnPanel()
    C2CFlowPanel= FlowPanel()
    spacertest= Spacer()
    self.add_component(HeroPanel)
    self.add_component(spacertest)
    self.add_component(C2CFlowPanel)
    HeroWork= app_tables.showcase.search(Name=q.like('C2CHero%'))
    for Name in HeroWork:
      HeroImg= Image(display_mode= 'full_width', source= Name['PortImg'], vertical_align= "center", role= "faded")
      HeroPanel.add_component(HeroImg)
      
    FolioWork= app_tables.showcase.search(Name=q.like('C2C%'))
    for Name in FolioWork:
      img = Image(source= Name['PortImg'], vertical_align= "center", role= "faded", height= 400)
      C2CFlowPanel.add_component(img)

    
    

