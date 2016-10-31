#!/usr/bin/python
          # -*- coding: utf-8 -*-
import Tkinter as tk
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from zprapp.models import *

class DbBase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        StaticLiveServerTestCase.setUpClass()
        # super(StaticLiveServerTestCase, cls).setUpClass()
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

    @classmethod
    def tearDownClass(cls):
        StaticLiveServerTestCase.tearDownClass()

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='functional_tests/chromedriver')
        # self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        # o = Organism(name="Organizm_testowy_1", id=1)
        # o.save()

    def tearDown(self):
        self.browser.close()
        # self.browser.quit()
        # time.sleep(2)

class StandardUserFromStartToEnd(DbBase):
    def test_copy_seq_chosen_scaff(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1200, 600)
        bar = self.browser.find_element_by_class_name('navbar-brand')
        self.assertEqual(bar.text, u'PRZEGLĄDARKA GENOMÓW')
        self.browser.find_element_by_link_text('Organizm_testowy_1').click()
        chr2 = self.browser.find_element_by_link_text('chromosom 2')
        # WebDriverWait(self.browser, 2).until(expected_conditions.element_to_be_selected(chr2))
        time.sleep(1)
        chr2.click()
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

class EraseOrganism(DbBase):
    # @unittest.skip("nie wiedzieć czemu angular nie dodaje do responsa ciasteczna z tokenem i serwer zwraca 403\n")
    def test_erase_organism(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1200, 600)
        orgs_len_before = Organism.objects.all().__len__()
        tbody = self.browser.find_element_by_tag_name("tbody")
        trs = tbody.find_elements_by_tag_name('tr')
        self.assertEqual(trs.__len__(), 2)
        tds = trs[1].find_elements_by_tag_name('td')
        self.assertEqual(tds.__len__(), 2)
        button = tds[1].find_element_by_tag_name('button')
        actions = ActionChains(self.browser)
        actions.move_to_element(tds[1]).perform()
        actions.move_to_element(button).perform()
        # time.sleep(1)
        WebDriverWait(self.browser, 2).until(expected_conditions.visibility_of(button))
        # time.sleep(1)
        actions.click(button).perform()
        time.sleep(1)
        self.assertEqual(Organism.objects.all().__len__(), orgs_len_before-1)

class Partial(DbBase):
# class OrganismUrlAndTable(DbBase):
#     def test(self):
    def test_organism_url_and_table(self):
        self.browser.get(self.live_server_url+'/#/organizmy')
        self.browser.set_window_size(1200, 600)
        trs = self.browser.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        self.assertEqual(trs.__len__(),2)

class ChromosomeUrlAndTable(DbBase):
    def test(self):
    # def test_chromosome_url_and_table(self):
        self.browser.get(self.live_server_url+'/#/organizm/1/chromosomy/')
        self.browser.set_window_size(1200, 600)
        trs = self.browser.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        self.assertEqual(trs.__len__(),2)

class ScaffoldUrlAndTable(DbBase):
    def test(self):
    # def test_scaffold_url_and_table(self):
        self.browser.get(self.live_server_url+'/#/organizm/1/chromosom/2/scaffoldy/')
        self.browser.set_window_size(1200, 600)
        trs = self.browser.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        self.assertEqual(trs.__len__(),2)

class SequenceUrlAndSequenceContent(DbBase):
    def test(self):
    # def test_sequence_url_and_sequence_content(self):
        self.browser.get(self.live_server_url+'/#/organizm/1/chromosom/2/scaffold/1/sekwencja')
        self.browser.set_window_size(1200, 600)
        well = self.browser.find_element_by_class_name('well')
        self.assertEqual(well.text, u'AGTCA')

class SequenceCopy(DbBase):
    def test(self):
    # def test_sequence_copy(self):
        self.browser.get(self.live_server_url+'/#/organizm/1/chromosom/2/scaffold/1/sekwencja')
        self.browser.set_window_size(1200, 600)
        self.browser.find_element_by_id("button_copy").send_keys(Keys.ENTER)
        root = tk.Tk()
        root.withdraw()
        self.assertEqual(root.clipboard_get(), "AGTCA")

class ScaffoldNavFromToInput(DbBase):
    def test(self):
    # def test_scaffold_nav_from_to_input(self):
        self.browser.get(self.live_server_url+'/#/organizm/1/chromosom/2/scaffoldy/')
        self.browser.set_window_size(1200, 600)
        inputbox_from = self.browser.find_element_by_id("view_from")
        inputbox_from.clear()
        inputbox_from.send_keys("10")
        inputbox_to = self.browser.find_element_by_id("view_to")
        inputbox_to.clear()
        inputbox_to.send_keys("20")
        self.browser.find_element_by_id('button_insert_data').click()
        time.sleep(1)
        trs = self.browser.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        self.assertEqual(trs.__len__(),1)
        self.assertEqual(trs[0].text, u'scaffold 2 7 11 1')

class ScaffoldNavTextArea(DbBase):
    def test(self):
        self.browser.get(self.live_server_url+'/#/organizm/1/chromosom/2/scaffoldy/')
        self.browser.set_window_size(1200, 600)
        self.browser.find_element_by_id('toggleTextArea').click()
        time.sleep(1)
        textarea = self.browser.find_element_by_id('textAreaSequence')
        self.assertEqual(textarea.text, 'NNNAGTCANNNGTCAGTCNNNNNNNNNNNN')

class ScaffoldNavArrows(DbBase):
    def test(self):
        self.browser.get(self.live_server_url+'/#/organizm/1/chromosom/2/scaffoldy/')
        self.browser.set_window_size(1200, 600)
        inputbox_from = self.browser.find_element_by_id("view_from")
        inputbox_from.clear()
        inputbox_from.send_keys("10")
        inputbox_to = self.browser.find_element_by_id("view_to")
        inputbox_to.clear()
        inputbox_to.send_keys("20")
        self.browser.find_element_by_id('button_insert_data').click()
        toggletextarea = self.browser.find_element_by_id('toggleTextArea')
        toggletextarea.click()
        time.sleep(1)
        textarea = self.browser.find_element_by_id('textAreaSequence')
        self.assertEqual(textarea.text, 'NGTCAGTCNN')
        inputbox_skok = self.browser.find_element_by_id("inputSkok")
        inputbox_skok.clear()
        inputbox_skok.send_keys("4")
        self.browser.find_element_by_id('rightArrow').click()
        toggletextarea.click()
        time.sleep(1)
        self.assertEqual(textarea.text, 'AGTCNNNNNN')
        inputbox_skok.clear()
        inputbox_skok.send_keys("2")
        self.browser.find_element_by_id('leftArrow').click()
        toggletextarea.click()
        time.sleep(1)
        self.assertEqual(textarea.text, 'TCAGTCNNNN')

class ScaffoldNavZooms(DbBase):
   def test(self):
       self.browser.get(self.live_server_url+'/#/organizm/1/chromosom/2/scaffoldy/')
       self.browser.set_window_size(1200, 600)
       self.browser.find_element_by_id("zoomIn").click()
       time.sleep(1)
       inputbox_from = self.browser.find_element_by_id("view_from")
       self.assertEqual(inputbox_from.get_attribute("value"), u'8')
       inputbox_to = self.browser.find_element_by_id("view_to")
       self.assertEqual(inputbox_to.get_attribute('value'), u'23')

       input_zoom = self.browser.find_element_by_id('inputZoom')
       input_zoom.clear()
       input_zoom.send_keys("90")
       self.browser.find_element_by_id("zoomOut").click()
       time.sleep(1)
       self.assertEqual(inputbox_from.get_attribute("value"), u'7')
       inputbox_to = self.browser.find_element_by_id("view_to")
       self.assertEqual(inputbox_to.get_attribute('value'), u'24')

class ScaffoldNavReset(DbBase):
    def test(self):
        self.browser.get(self.live_server_url+'/#/organizm/1/chromosom/2/scaffoldy/')
        self.browser.set_window_size(1200, 600)
        self.browser.find_element_by_id("zoomIn").click()
        time.sleep(1)
        self.browser.find_element_by_id('reset').click()
        time.sleep(1)
        inputbox_from = self.browser.find_element_by_id("view_from")
        self.assertEqual(inputbox_from.get_attribute("value"), u'0')
        inputbox_to = self.browser.find_element_by_id("view_to")
        self.assertEqual(inputbox_to.get_attribute('value'), u'30')


