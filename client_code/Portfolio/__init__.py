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
    self.FolioPanelMethod()
    self.ButtonExpander()

  #Portfolio Panel constructor
  def FolioPanelMethod(self, **event_args):
    Work1= HomeOdyssey()
    Work2= BuildersCradle()
    Work3= D0tmatrix()
    Work4= Onlied()
    WorkPanel= FlowPanel(align= "center")
    self.add_component(WorkPanel)
    WorkPanel.add_component(Work1)
    WorkPanel.add_component(Work2)
    WorkPanel.add_component(Work3)
    WorkPanel.add_component(Work4)

  def ButtonExpander(self, **event_args):
    ButtonExp= Button(text= "The Builders Cradel", align= "center")
    ButtonExp.role= "ButtonPortfolio"
    self.add_component(ButtonExp)

  def ButtonExpander_click(self, **event_args):
    pass