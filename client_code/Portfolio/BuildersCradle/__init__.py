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
    self.TextC2C()
    
  def RepeatC2C(self, **event_args):
    C2CFlowPanel= FlowPanel(align= "center")
    self.add_component(C2CFlowPanel)
    #startaddingtextfromdatabase
    #ProjectText= RichText()
    #ProjectTextData= app_tables.showcase.get(Name=q.like('C2CHero%'), Describe="Name")
    #self.add_component(ProjectText)
    #endaddingtextfromdatabase I think we need to build it elsewhere
    #table_row_total= len(app_tables.showcase.search()) #not nessesary just tells the total table size
    FolioWork= app_tables.showcase.search(Name=q.like('C2C%'))
    AddText= False
    for Name in FolioWork:
      if AddText == False:
        #self.add_component(ProjectText) #may be moving this elsewhere
        wuw= "text" #testing the if statement should only run once then else should run every other time
        print(wuw)
        AddText= True
        #the below adds the first image
        img = Image(display_mode= "fill_width", source= Name['PortImg'], vertical_align= "center", role= "faded", horizontal_align= "center")
        C2CFlowPanel.add_component(img, width= 660)
      else:
        img = Image(display_mode= "fill_width", source= Name['PortImg'], vertical_align= "center", role= "faded", horizontal_align= "center")
        C2CFlowPanel.add_component(img, width= 660)

  def TextC2C(self, **event_args):
    ProjectTextData= app_tables.showcase.get(Name= q.like('C2CHero%'))
    ProjectText= RichText(content= ProjectTextData['Describe'], role= "FadedTxt", align= "left")
    self.add_component(ProjectText)