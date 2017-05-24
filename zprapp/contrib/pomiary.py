import time
import random
from zprapp.calc.calc_webomics.build import calc
from pprint import pprint


def generuj_string(n):
    random.choice(['A','C', 'T', 'G'])
    return "".join([random.choice(['A','C', 'T', 'G']) for a in range(n)])


pattern = generuj_string(1000)
bm = calc.BM()
bm.prepare(pattern)

def bm_test():
    tlo = generuj_string(10000000)
    print("BM TEST, tlo ", len(tlo))
    print("dlugosc wzorca, bm, kmp [s]")
    for length in range(1000, 1000000, 10000):
        pattern = generuj_string(length)
        bm = calc.BM()
        start = time.time()
        bm.prepare(pattern)
        bm.compute(tlo)
        end = time.time()
        bm_time = end - start

        kmp = calc.KMP()
        start = time.time()
        kmp.calculateTable(pattern)
        kmp.compute(tlo)
        end = time.time()
        kmp_time = end - start
        print len(pattern), bm_time, kmp_time


    # print("KMP TEST, tlo ", len(tlo))
    # for length in range(500, 20000, 500):
    #     pattern = generuj_string(length)
    #     kmp = calc.KMP()
    #     start = time.time()
    #     kmp.calculateTable(pattern)
    #     kmp.compute(tlo)
    #     end = time.time()

# bm_test()

def sw_test1():
    # przeszukiwana 5000
    # wzorzec od 50 do 450

    match = 2
    mismach = -1
    gap_open = -3
    gap_extended = -1

    print "SW TEST1 zmienny wzorzec"
    print "dlugosc wzorca, czas[s], sekwencja przeszukiwana 5000"
    tlo = generuj_string(5000)
    for pattern_len in range(100, 500, 50):
        pattern = generuj_string(pattern_len)
        sw = calc.SW()
        start = time.time()
        sw.fastComputeWithStringsResult(match, mismach, gap_open, gap_extended, tlo, pattern)
        end = time.time()
        czas = end - start
        print pattern_len, czas


def sw_test2():
    # wzorzec 500
    # przeszukiwana od 1000, 10000
    match = 2
    mismach = -1
    gap_open = -3
    gap_extended = -1

    print "SW TEST2 zmienne tlo"
    print "dlugosc tla, czas[s], wzorzec 500"
    pattern = generuj_string(500)
    for tlo_len in range(1000, 10000, 1000):
        tlo = generuj_string(tlo_len)
        sw = calc.SW()
        start = time.time()
        sw.fastComputeWithStringsResult(match, mismach, gap_open, gap_extended, tlo, pattern)
        end = time.time()
        czas = end - start
        print tlo_len, czas


def blast_test():
    w = 11
    t = 0.001
    c = 5
    cutoff = 10
    results = []
    # random.seed(time.time())
    # print(pattern)
    print "dlugosc tla, czas[s], wzorzec 5000"
    for tlo_len in range(5000, 5001, 1):
        res_search = False
        tlo = generuj_string(tlo_len)
        while not res_search:
            pattern = generuj_string(20)
            blast = calc.Blast(w, t, c)
            start = time.time()
            blast.prepare(pattern)
            blast.addSequence('6969', tlo)
            res_search = blast.search()
        assert res_search is True
        res_estimate = blast.estimate()
        assert res_estimate is True
        res_extend = blast.extend()
        assert res_extend is True
        res_evaluate = blast.evaluate()
        assert res_evaluate is True

        aligns = blast.getAligns(cutoff)
        aligns_len = len(aligns)
        for align in aligns:
            same = align.getSame()
            align_len = align.getAlignLength()
            seq_id = align.getSequenceId()
            print same, align_len, seq_id
            result = {}
            result['ID'] = str(seq_id)
            result['SCORE'] = str(align.getScore())
            result['IDENTITY'] = str((float(same) / float(align_len) * 100.00))
            result['GAPS'] = str(align.getGaps())
            result['LENGTH'] = str(align_len)
            result['SEQ_START_INDEX'] = str(align.getSeqStart())
            result['SEQ_END_INDEX'] = str(align.getSeqEnd())
            results.append(result)

        end = time.time()
        czas = end - start
        pprint(results)
        print tlo_len, czas


# sw_test2()
blast_test()

# match = 2
# mismach = -1
# gap_open = -3
# gap_extended = -1
# sw = calc.SW()
# sw.fastComputeWithStringsResult(match, mismach, gap_open, gap_extended, generuj_string(5000), generuj_string(100))
