from ._anvil_designer import ContactTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Contact(ContactTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
  
  def ButtonSubmit_show(self, **event_args):
    self.ButtonSubmit.role = "Submit"
    
  def ButtonSubmit_click(self, **event_args):
    """This method is called when the button is clicked"""
    Name = self.NameTxt.text
    Email = self.EmailTxt.text
    Subject = self.SubjectTxt.text
    Message = self.MsgTxt.text
    Captcha = self.VerifyTxt.text.lower()
    
    if Name and Email and Subject and Message and Captcha == "hot":
      anvil.server.call('add_contact_info', Name, Email, Subject, Message)
      alert("Thanks for getting in touch!")
      self.NameTxt.text = ""
      self.EmailTxt.text = ""
      self.SubjectTxt.text = ""
      self.MsgTxt.text = ""
      self.VerifyTxt.text = ""
    else:
      alert("Please fill out the entire form before submitting.")




