from zprapp.calc.calc_webomics.build import calc

# /**
# 			 * Zwrocenie wartosci podobienstwa porownywanych tekstow
# 			 */
# 			int getValue();

if __name__ == '__main__':
    sw = calc.SW()
    # match=2, mismatch=-1, gap_open=-3, gap_extend=-1, str(obj.sequence), str(pattern)
    s = sw.fastComputeWithStringsResult(2, -1, -3, -1, b'#####AaKAa#####', b'@@@@AaLAa@@@')

    score = s.getValue() # int
    print("score (getValue)", score) # SCORE wartosc podobienstwa porownywanych tekstow -> suma matchy , kar itd dla tekstu

    pat_after = s.getPattern() #std::string wspolny podobny fragment patterna
    print("pat_after (getPattern)", pat_after)

    seq_after = s.getText() #std::string odnaleziony fragment w szukanej sekwencji ale z  "-" tak gdzie znak sie nie zgadza (jest inny albo brakuje)
    print("seq_after (getText)", seq_after)

    align_len = len(s.getText())
    print("align_len (len getText)", align_len)
    gaps = 0
    same = 0
    for i, l in enumerate(seq_after):
        if l == '-':
            gaps += 1
        elif l == pat_after[i]: # takie same
            same+=1

    print("gaps", gaps)
    print("same", same)
    print("identity", float(same)/float(align_len))
    seq_end_index = s.getPositionJ()
    aim_end_index = s.getPositionI()
    aim_start_index = aim_end_index - len(seq_after)
    print("aim end_index", aim_end_index)
    print("aim start_index", aim_start_index)
    print("seq_end_index", seq_end_index)
    seq_start_index = seq_end_index - len(str(seq_after).replace("-", ""))
    print("seq_start_index", seq_start_index)
