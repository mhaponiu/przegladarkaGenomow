from unittest.case import TestCase

# from django.test import TestCase
from zpr.database.new.sggw_data import Links3


class Links3Test(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.links3 = Links3()

    def test_max_ncbi_ctg_id(self):
        self.assertEqual(16547, self.links3.max_ncbi_ctg_id())

    def test_min_ncbi_ctg_id(self):
        self.assertEqual(1, self.links3.min_ncbi_ctg_id())

    def test_min_scaffold_id(self):
        self.assertEqual(0, self.links3.min_scaffold_id())

    def test_max_scaffold_id(self):
        self.assertEqual(13128, self.links3.max_scaffold_id())

    def test_amount_of_scfld_with_only_one_ctg(self):
        self.assertEqual(12283, self.links3.amount_of_scfld_with_only_one_ctg())

    def test_col_num_contigs_in_super(self):
        self.assertTrue(self.links3.check_amount_of_contigs_in_scaffold_with_col_num_contigs_in_super())
