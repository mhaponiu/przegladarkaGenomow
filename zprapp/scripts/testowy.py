from django.db import transaction
from pprint import pprint
from drop_exception import drop_exception
# from zpr.database.v4_refresh.parser import Gff_annotation
# from zpr.database.v4_refresh.parser import Fasta_B10v2_c_corr

# from zpr.database.v4_refresh.data_structures.fastaData import FastaData
# from zpr.database.v4_refresh.data_structures.gffData import GffData

from zpr.database.v4_refresh.data_structures.tree import Tree
from anytree import RenderTree

from zprapp.models import Organism, Annotation, AnnotationType, Aggregation
from zpr.database.v4_refresh.data_structures.db_info import DbInfo

# @drop_exception(msg="\nEXCEPTION OCCURED")
@transaction.atomic
def run():
    # f = Fasta_B10v2_c_corr().generator()
    # i = next(f)
    # print(i.ctg_id, i.id_from_file)

    # g = Gff_annotation().generator()
    # print(next(g))

    # f = FastaData()

    # g = GffData()
    # pprint(g.records[:3])
    # pprint(g.types)

    t = Tree()
    t.create()
    # print t.render()


    org = Organism.objects.get(id=58)
    for i in t.preorder_iter():
        if i.name == t.start_node.name: continue

        record = i.record

        parent = i.parent
        if parent.name == t.start_node.name:
            annotation_master = Annotation.objects.get(
                name=record.ctg_id,
                chromosome__organism=org)
        else:
            parent_name = parent.record.info['ID']
            annotation_master = Annotation.objects.get(
                name= parent_name,
                chromosome__organism=org
            )
        ann_type = AnnotationType.objects.get_or_create(name=record.type)[0]

        start_chr = annotation_master.start_chr + record.start
        length = record.end - record.start
        assert length > 0
        # assert  start_chr + length < annotation_master.start_chr + annotation_master.length
        annotation = Annotation.objects.create(
            type=ann_type,
            chromosome=annotation_master.chromosome,
            start_chr=start_chr,
            length=length,
            name=record.info['ID']
        )
        aggregation = Aggregation.objects.create(
            start_local=record.start,
            annotation_slave=annotation,
            annotation_master=annotation_master
        )
        print record



    # raise Exception