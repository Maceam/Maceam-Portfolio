from ._anvil_designer import HomeOdysseyTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class HomeOdyssey(HomeOdysseyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.RepeatHomeOd()
    self.TextHomeOd()  
    
  def RepeatHomeOd(self, **event_args):
    HomeOdflowPanel= FlowPanel(align= "center")
    self.add_component(HomeOdflowPanel)
    # Makes the images appear in the main app
    FolioWork= app_tables.showcase.search(Name=q.like('Home%'))
    AddText= False
    for Name in FolioWork:
      if AddText == False: #This should only occur once, this seperates the hero image from the others. 
        AddText= True
        #the below adds the first image
        img = Image(display_mode= "fill_width", source= Name['PortImg'], vertical_align= "center", role= "faded", horizontal_align= "center", tooltip=Name['AltTxt'])
        HomeOdflowPanel.add_component(img, width= 660)
      else:
        img = Image(display_mode= "fill_width", source= Name['PortImg'], vertical_align= "center", role= "faded", horizontal_align= "center", tooltip=Name['AltTxt'])
        HomeOdflowPanel.add_component(img, width= 660)
        
  # Makes the text appear in the main app
  def TextHomeOd(self, **event_args):
    ProjectTextData= app_tables.showcase.get(Name= q.like('HomeHero%'))
    ProjectText= RichText(content= ProjectTextData['Describe'], role= "FadedTxt", align= "left")
    self.add_component(ProjectText)