from ._anvil_designer import PortfolioTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil_extras import *
from ..Portfolio.HomeOdyssey import HomeOdyssey
from ..Portfolio.BuildersCradle import BuildersCradle
from ..Portfolio.D0tmatrix import D0tmatrix
from ..Portfolio.Onlied import Onlied

class Portfolio(PortfolioTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.C2CButton()
    self.OnliedButton()
    self.D0tmatrixButton()
    self.HomeOdButton()
    
    

  def C2CButton(self, **event_args):
    ButtonExp= Button(text= "The Builders Cradel", align= "full", font_size= 22, spacing_above= "none", spacing_below= "none")
    ButtonExp.role= "ButtonPortfolio"
    self.add_component(ButtonExp)
    ButtonExp.add_event_handler('click', self.C2CButton_click)

  def C2CButton_click(self, **event_args):
    ReAdd= Portfolio() 
    BuildersCradleForm= BuildersCradle()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(ReAdd)
    get_open_form().content_panel.add_component(BuildersCradleForm)

  def D0tmatrixButton(self, **event_args):
    ButtonExp= Button(text= "D0tmatrix: Typeface", align= "full", font_size= 22, spacing_above= "small", spacing_below= "small")
    ButtonExp.role= "ButtonPortfolio"
    self.add_component(ButtonExp)
    ButtonExp.add_event_handler('click', self.D0tmatrixButton_click)

  def D0tmatrixButton_click(self, **event_args):
    ReAdd= Portfolio() 
    D0tmatrixForm= D0tmatrix()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(ReAdd)
    get_open_form().content_panel.add_component(D0tmatrixForm)

  def HomeOdButton(self, **event_args):
    ButtonExp= Button(text= "Home Odyssey, Viynl Concept", align= "full", font_size= 22, spacing_above= "small", spacing_below= "small")
    ButtonExp.role= "ButtonPortfolio"
    self.add_component(ButtonExp)
    ButtonExp.add_event_handler('click', self.HomeOdButton_click)

  def HomeOdButton_click(self, **event_args):
    ReAdd= Portfolio() 
    HomeOdForm= HomeOdyssey()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(ReAdd)
    get_open_form().content_panel.add_component(HomeOdForm)

  def OnliedButton(self, **event_args):
    ButtonExp= Button(text= "Onlied: Awareness", align= "full", font_size= 22, spacing_above= "small", spacing_below= "small")
    ButtonExp.role= "ButtonPortfolio"
    self.add_component(ButtonExp)
    ButtonExp.add_event_handler('click', self.OnliedButton_click)

  def OnliedButton_click(self, **event_args):
    ReAdd= Portfolio() 
    OnliedForm= Onlied()
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(ReAdd)
    get_open_form().content_panel.add_component(OnliedForm)