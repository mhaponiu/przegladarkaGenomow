import time
from django.db import transaction
from drop_exception import drop_exception
from zpr.database.v4.data_structures.combinationData import CombinationData
from zpr.database.v4.data_structures.fastaData import FastaData
from zpr.database.v4.data_structures.gffData import GffData



# @drop_exception(msg="\nEXCEPTION OCCURED")
@transaction.atomic
def run():
    # fasta_stats = FastaStats()
    # print len(fasta_stats)

    fasta_data = FastaData()
    # print len(fasta_data.dict)
    print fasta_data.sum_all_sequences()
    # print len(fasta_data.contigs_id_list)

    # gff_data = GffData()
    # print len(gff_data)
    # print gff_data.types()
    # print gff_data.contigs_id_list()
    # print gff_data.contigs_amount()

    combination_data = CombinationData()
    # print combination_data.joint_ctg_id_list()
    print combination_data.joint_ctgs_amount()
    print len(combination_data.dict_fasta_filtered_by_gff_contigs)
    print combination_data.sum_sequences()
    print combination_data.sum_sequences()
    print combination_data.sum_sequences()
    print combination_data.sum_sequences()

    # raise Exception