#!/usr/bin/python
          # -*- coding: utf-8 -*-
import Tkinter as tk

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from zprapp.models import *


class StandardUserTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        StaticLiveServerTestCase.setUpClass()
        o1 = Organism(name="Organizm_testowy_1", id=1)
        o2 = Organism(name="Organizm_testowy_2", id=2)
        ch1 = Chromosome(organism=o1, number=1, length=40, id=1)
        ch2 = Chromosome(organism=o1, number=2, length=30, id=2)
        sc1 = Scaffold(chromosome=ch2, length=5, order=0, start=3, id=1)
        seq1 = Sequence(scaffold=sc1, sequence="AGTCA", id=1)
        sc2 = Scaffold(chromosome=ch2, length=7, order=1, start=11, id=2)
        seq2 = Sequence(scaffold=sc2, sequence="GTCAGTC", id=2)
        for obj in [o1, o2, ch1, ch2, sc1, seq1, sc2, seq2]:
            obj.save()
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        # o = Organism(name="Organizm_testowy_1", id=1)
        # o.save()
    def tearDown(self):
        self.browser.quit()

    def test_copy_seq_chosen_scaff(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1200, 600)
        bar = self.browser.find_element_by_class_name('navbar-brand')
        self.assertEqual(bar.text, u'PRZEGLĄDARKA GENOMÓW')
        self.browser.find_element_by_link_text('Organizm_testowy_1').click()
        self.browser.find_element_by_link_text('chromosom 2').click()
        inputbox_from = self.browser.find_element_by_id("view_from")
        inputbox_from.clear()
        inputbox_from.send_keys("10")
        inputbox_to = self.browser.find_element_by_id("view_to")
        inputbox_to.clear()
        inputbox_to.send_keys("20")
        self.browser.find_element_by_id('button_insert_data').click()
        self.browser.find_element_by_link_text('scaffold 2').click()
        self.browser.find_element_by_id("button_copy").send_keys(Keys.ENTER)
        root = tk.Tk()
        root.withdraw()
        self.assertEqual(root.clipboard_get(), "GTCAGTC")

    # def test_zoom_in_scaffold(self):
    #     self.browser.ge