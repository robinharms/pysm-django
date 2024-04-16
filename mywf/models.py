from django.db import models
from statemachine.mixins import MachineMixin


class MyContext(models.Model, MachineMixin):
    state = models.CharField(max_length=30, blank=True, null=True)
    state_machine_name = "mywf.statemachines.MySM"
    state_machine_attr = "wf"
    let_me_be_visible = False