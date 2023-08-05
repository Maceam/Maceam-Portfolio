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
    self.HeroC2C()
    self.Herospacer()
    self.RepeatC2C()
    
  def RepeatC2C(self, **event_args):
    C2CFlowPanel= FlowPanel()
    self.add_component(C2CFlowPanel)
    #table_row_total= len(app_tables.showcase.search()) #not nessesary just tells the total table size
    FolioWork= app_tables.showcase.search(Name=q.like('C2C%'))
    for Name in FolioWork:
      img = Image(width= 100, source= Name['PortImg'], vertical_align= "center", role= "faded",horizontal_align= "center", )
      C2CFlowPanel.add_component(img)
    
    
  def HeroC2C(self, **event_args):
    C2CHeroPanel= ColumnPanel(spacing_below= "small")
    self.add_component(C2CHeroPanel,full_width_row=True)
    #table_row_total= len(app_tables.showcase.search()) #not nessesary just tells the total table size
    HeroWork= app_tables.showcase.get(Name=q.like('C2CHero%'))
    HeroImg = Image(source= HeroWork['PortImg'], vertical_align= "center", role= "faded", height= 800, display_mode= "fill_width")
    C2CHeroPanel.add_component(HeroImg)

  def Herospacer(self, **event_args):
    Herospace= Spacer(spacing_above= "small", height= 4)
    self.add_component(Herospace, full_width_row= True)