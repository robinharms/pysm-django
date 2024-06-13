from django.contrib.auth import get_user_model
from django.test import TestCase
from statemachine.exceptions import TransitionNotAllowed

from mywf.models import MyContext
from mywf.statemachines import MySM

User = get_user_model()


class WFTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Runs once
        cls.one = MyContext.objects.create()

    def setUp(self):
        # Runs before every test
        self.two = MyContext.objects.create()

    def test_one(self):
        # This test will fail
        with self.assertRaises(TransitionNotAllowed):
            self.one.wf.send("publish")

    def test_two(self):
        # This works as expected
        with self.assertRaises(TransitionNotAllowed):
            self.two.wf.send("publish")

    def test_three(self):
        # Managing this instance works if I call it like this instead.
        # So this test works
        wf = MySM(self.one)
        with self.assertRaises(TransitionNotAllowed):
            wf.send("publish")
    def test_async_w_db_op(self):
        user = User.objects.create_user('user')
        self.one.user = user
        self.one.save()
        wf = MySM(self.one)
        wf.send("notify_user")
        # And clear model cache, casing user to be loaded later on
        self.one = MyContext.objects.get(pk=self.one.pk)
        wf = MySM(self.one)
        wf.send("notify_user")
