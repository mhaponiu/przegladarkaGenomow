### Genom v4, listopad 2017

#### Fasta

- **215 666 rekordów** (contigów), zgadza się z idkami sprawdzanymi z konsoli (`less`)

- id od 0 do 215 665

- **184 603 960 suma wszystkich sekwencji** `FastaData().sum_all_sequences()`  
(zgadza sie z wagą pliku ~190mega)


#### Gff

- **475 456 rekordów** `len( GffData() )`

- **1057 contigów (0.4901% całości fasta)** `GffData().contigs_amount()`  
(są dziury, nie ciągły)

- **typy:** ['start_codon', 'stop_codon', 'intron', 'exon', 'mRNA', 'CDS', 'gene']  
`GffData().types()`


#### Porównanie fasta i gff

- **909 494 (0.4927% całości fasta)** suma wspólnych sekwencji (wspólnych contigów - wszystkie co w gff)
`CombinationData().sum_sequences`



### Struktury danych:

##### Fasta:
- słownik {contig_id:sekwencja} `FastaData().dict`
- lista contigów id [ctg_id] `FastaData().contigs_id_list`


##### Gff:

- lista contigów id [ctg_id] `GffData().contigs_id_list`


##### Kombinacja gff i fasta:

- lista wspólnych ctg id [ctg_id] `CombinationData().joint_ctgs_amount()`
- liczba wspólnych contigów `CombinationData().joint_ctgs_amount`  
zgodnie z przewidywaniami - tyle co contigów w gff


- słownik fasta {contig_id:sekwencja} przefiltrowany o gffy  
`CombinationData().dict_fasta_filtered_by_gff_contigs`