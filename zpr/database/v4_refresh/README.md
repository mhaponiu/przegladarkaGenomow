data.structures.tree.Tree
(see: *anytree* package)


    t = Tree()
    t.create()
    t.render()

    Node('/Cucsat/PASA')
    ├── Node('/Cucsat/PASA/G1', id='G1', record=GffRecord(ctg_id=1, type='gene', start=29514, end=31144, info={'ID': 'Cucsat.PASA.G1'}))
    │   └── Node('/Cucsat/PASA/G1/T1', id='T1', record=GffRecord(ctg_id=1, type='transcript', start=29514, end=31144, info={'ID': 'Cucsat.PASA.G1.T1', 'Parent': 'Cucsat.PASA.G1'}))
    │       ├── Node('/Cucsat/PASA/G1/T1/E1', id='E1', record=GffRecord(ctg_id=1, type='exon', start=29514, end=30001, info={'ID': 'Cucsat.PASA.G1.T1.E1', 'Parent': 'Cucsat.PASA.G1.T1'}))
    │       ├── Node('/Cucsat/PASA/G1/T1/E2', id='E2', record=GffRecord(ctg_id=1, type='exon', start=30443, end=31144, info={'ID': 'Cucsat.PASA.G1.T1.E2', 'Parent': 'Cucsat.PASA.G1.T1'}))
    │       ├── Node('/Cucsat/PASA/G1/T1/U1', id='U1', record=GffRecord(ctg_id=1, type='UTR', start=29514, end=30001, info={'ID': 'Cucsat.PASA.G1.T1.U1', 'Parent': 'Cucsat.PASA.G1.T1'}))
    │       └── Node('/Cucsat/PASA/G1/T1/U2', id='U2', record=GffRecord(ctg_id=1, type='UTR', start=30443, end=31144, info={'ID': 'Cucsat.PASA.G1.T1.U2', 'Parent': 'Cucsat.PASA.G1.T1'}))
    ├── Node('/Cucsat/PASA/G2', id='G2', record=GffRecord(ctg_id=1, type='gene', start=30405, end=36850, info={'ID': 'Cucsat.PASA.G2'}))
    │   └── Node('/Cucsat/PASA/G2/T1', id='T1', record=GffRecord(ctg_id=1, type='transcript', start=30405, end=36850, info={'ID': 'Cucsat.PASA.G2.T1', 'Parent': 'Cucsat.PASA.G2'}))
    │       ├── Node('/Cucsat/PASA/G2/T1/E1', id='E1', record=GffRecord(ctg_id=1, type='exon', start=30405, end=33283, info={'ID': 'Cucsat.PASA.G2.T1.E1', 'Parent': 'Cucsat.PASA.G2.T1'}))
    │       ├── Node('/Cucsat/PASA/G2/T1/E2', id='E2', record=GffRecord(ctg_id=1, type='exon', start=36143, end=36850, info={'ID': 'Cucsat.PASA.G2.T1.E2', 'Parent': 'Cucsat.PASA.G2.T1'}))

    t.preorder_iter()
