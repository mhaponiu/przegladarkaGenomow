#### Generacja słownika {chromosom: contigi} dla bazy
chromosom 0: zbiór contigów niezmapowanych na chromosom  
chromosomy 1 - 7 lista zmapowanych chromosomow

    from zpr.database.v3.contigs import ChromosomesContigFactory
    chr = ChromosomesContigFactory().produce_chromosomes()

### Wstawienie organizmu v3 z chromosomami i contigami

    from zpr.database.v3.db_inserter import Inserter
    inserter = Inserter()
    inserter.clear_db()
    inserter.insert()
    
albo uruchom:

    python zpr/database/v3/db_inserter.py