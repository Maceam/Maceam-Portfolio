from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Portfolio import Portfolio
from ..About import About
from ..Contact import Contact

class Landing(LandingTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Set Form properties and Data Bindings.
    self.LandginMethod()
    self.ClickMeMethod()


  #make a def (aka method) for adding the panel  
  
  def LandginMethod(self, **event_args): 
  # Any code you write here will run before the form opens.
    table_row= app_tables.showcase.get(Name=q.like('MelbourneFed'))
    LandImg = Image(display_mode= "fill_width", source= table_row['PortImg'], vertical_align= "center")
    HeroImg= Link()
    LandPanel = ColumnPanel()
    self.add_component(HeroImg)
    HeroImg.add_component(LandPanel)
    LandPanel.add_component(LandImg, full_width_row=True)
    LandImg.role="LandingImg"
    HeroImg.add_event_handler('click', self.ClickMeMethod_click)
    
  def ClickMeMethod(self, **event_args): 
    ButtonMoving = Button(role= "CallToAction", text= "Come Explore", align= "right", font= "D0tmatrix", font_size= 24)
    self.add_component(ButtonMoving)
    ButtonMoving.add_event_handler('click', self.ClickMeMethod_click)

  def ClickMeMethod_click(self, **event_args): 
    portfolio_panel = Portfolio()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(portfolio_panel)
