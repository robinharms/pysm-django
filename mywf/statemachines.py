from statemachine import State
from statemachine import StateMachine


class MySM(StateMachine):
    draft = State("Draft", initial=True, value="draft")
    published = State("Published", value="published")

    publish = draft.to(published, cond="let_me_be_visible")