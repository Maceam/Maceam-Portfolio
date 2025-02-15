from ._anvil_designer import D0tmatrixTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class D0tmatrix(D0tmatrixTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.RepeatD0t()
    self.TextD0t()
    
  def RepeatD0t(self, **event_args):
    D0tflowPanel= FlowPanel(align= "center")
    self.add_component(D0tflowPanel)
    # Makes the images appear in the main app
    FolioWork= app_tables.showcase.search(Name=q.like('D0t%'))
    AddText= False
    for Name in FolioWork:
      if AddText == False: #This should only occur once, this seperates the hero image from the others. 
        AddText= True
        #the below adds the first image
        img = Image(display_mode= "fill_width", source= Name['PortImg'], vertical_align= "center", role= "faded", horizontal_align= "center", tooltip=Name['AltTxt'])
        D0tflowPanel.add_component(img, width= 660)
      else:
        img = Image(display_mode= "fill_width", source= Name['PortImg'], vertical_align= "center", role= "faded", horizontal_align= "center", tooltip=Name['AltTxt'])
        D0tflowPanel.add_component(img, width= 660)
        
  # Makes the text appear in the main app
  def TextD0t(self, **event_args):
    ProjectTextData= app_tables.showcase.get(Name= q.like('D0tmatrixHero%'))
    ProjectText= RichText(content= ProjectTextData['Describe'], role= "FadedTxt", align= "left")
    self.add_component(ProjectText)