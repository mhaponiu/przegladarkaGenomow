# from zpr.database.v4_refresh.parser import Fasta_B10v2_c_corr, Gff_annotation
from anytree import Node, RenderTree, PreOrderIter
from gffData import GffData


class Tree():
    def __init__(self, gff_data= GffData()):
        ''':param gff_data -- zpr.database.v4_refresh.data_structures.gffData.GffData (property records needed)'''
        self.journal = {}
        self.records = gff_data.records[:50] # todo
        # GffRecord(ctg_id=1, type='exon', start=147134, end=147174,
        #           info={'ID': 'Cucsat.PASA.G7.T39.E6', 'Parent': 'Cucsat.PASA.G7.T39'})
        self.root = Node('Cucsat')
        self.pasa = Node('PASA', parent=self.root)

    def create(self):
        self.journal['root'] = self.root

        for record in self.records:
            gff_id = record.info['ID']
            node_id = gff_id.split('.')[-1]
            try:
                parent_id = record.info['Parent']
                parent = self.journal[parent_id]
            except KeyError:
                parent = self.start_node
            self.journal[gff_id] = Node(node_id, id=node_id,record=record, parent=parent)

    @property
    def start_node(self):
        return self.pasa

    @property
    def journal(self):
        return self.journal

    def render_id(self):
        return RenderTree(self.start_node).by_attr('id')

    def render(self):
        return RenderTree(self.start_node)

    def preorder_iter(self):
        return PreOrderIter(self.start_node)

    def __str__(self):
        return str(self.root)


