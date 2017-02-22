/**
 * @author: Piotr Róż
 * @note: Plik testujący klasę BLAST_PY
 * Kompilacja: cl /EHsc /I E:\boost\boost_1_51 test.cpp ..\Blast.cpp ..\Word.cpp ..\Alignment.cpp
 */

#include <iostream>
#include <string>

#include "../Blast.hpp"

int main(int argc, char *args[])
{
	algorithms::BLAST * blast = new algorithms::BLAST(11, 0.005, 5);

	//bool result = blast->prepare("CACAAAATCAACAATCATTACATTATATTTCCTTCAAACATAGAGGACAGATCGAG");
	bool result = blast->prepare("ATCGTCTCCCATGAAGCCAAAGTTCATGTGTTTTTATTAAGCTAAGCAATACTATTATGA");

	std::cout << "\nWynik PREPARE: " << result << std::endl << std::endl;

	blast->addSequence("0","GAAAGTTCAAGAAAATATGAGAAAATTTCTCACTAGCCTTCAAACATAGAGGACAGATCGAGGGGGAGGCATTTTTTGGGAGCTTTTTTTTGTCACGATTTCAGAGCTATTGAGGGACCCAAAGACCATAGTCCAAATCAAAATATTGATTCTACGTGACCTGCCTGTTTTCCAAATTGCTGAAAAAAGACGTTTATCCATTGGAGAGGCAGATTTTAAGTGAGTCGAAAGAGACTTAACGGAAAATCAGCCTTGAGGATCAATGGACCATGATCTATAATTGTCGGAGTTTACCACTTTTTCAAAAGAGAGAAGGCAAAGCAGTGATTTAAAATCTACAAAGTCATCATCCTTCAGACTTCTTCTAAAGGACCAAGAGGAGGTATCTTGGTCCCAATGTGCTGCAACTGATCCAGTGGGCAAAAGAGTAATTCTAAAGAGCCTAGAATATTGCTTTTTAAAGGGGGCGTTACCTACCCAAATATCTGTCCAAAAGCCCAAATTTTCTATACAAACCTTTGTTTAAGTGAGTGGTTCTCAATCCTAGGAAATATTTCAGATTGCCTAAATCTTTCACTTAATAGTAATTTTAGGTTTCTTACTTATTCTTCATGACGTCACATGGAGGAATAATGTGTCATCCTCATATAATAATCACTATATTTAGGATTTAAGAATGTTTGATTAAAAGAGTAATTAGATTTCCTCAACTTTTGAGATATTGAAGCTCTTGAAGAACCAAAGATTGTTTTGGAAGCATTATTCATTAAGGGGCCGTTTGGGGGAAGGGTTGAGTTATGGAAGGGTTAGAGTTATATGATAAAACTAGTGTTATGATAAAACTAGTTTTATGATAAAAGTTGTTTGGGGAAGGGTTATGTGAGTAGTGTTATGATAAGATGTGTTTGGGGGAAGGGTTATTTAGGTAGTGTTATGATAGTTTATGATAAGATGTGTTTGGGGGAAGGTTAT");
	blast->addSequence("1","GTCTATCTCAGGTAGACAGAGATAAACTACTATCACTAATAGATTGATTAGATTTGGCACAAAATCGTTTAAATTGGATATACGATCATTTAGATTTGGTACAAAATCAACCATTTAAACTGGGTACAATATCGTTTAAACTAGTTACAAGGGTACAAGATCGTTTATACTTGGTGCAAAGGTATAAGATCGTTTAGACTTGCTAAAAAATTGTTTAGCGATTGTGTTCACACTTGTTTAGACTTGGTACAAAGGTACAACTTCGTTTAGACTTGGTACAAGATTGTTTAGATTTGATGTAAAATCATTTTTTCACTCGTGTGCAACTAATTAATCACGAGGATATTTTTGTTATTTCATCTTGTAGATTTTTTCTTTTTAAAATTATTCGATAGAGTGTAAACATTTTTCCACTATGTTCTATCTTTTAAATTTTAAAAACTCCTAATTTCTACCAAAGAAATTATAATAGGTGAATATGTTTTCAAATTTTATATTTTGTGAAAAATCTAATAATTAAAAAATGAAAATGGCAACAAACAACTAAAATTAAGTTTGGCAAAGTATACACACAAAAATTAGATATATTAAAAGGAAATTATTTTAATTCTATAATAATTATTTATTAGCATCATCATGAGGAGTTGTTGTTTTCAAATGTTATCTCCTTTTTCTATTTATTTATTAAGAATAAGAACGTCGTCCCCTTTTTCTTTCTTTTGTATCATTGGGGAATCATAACATCATTTTCATCATCTCATTTGTTTGTATTATTTTTGGTAATATATGTTAGTATAGTTTAGCTTTTAATGATTAAGACATCTCATTCTTTTTTATAATTAATGGTCCAATTTTTTTCTTCATGATGTGTCACGGAGAAATTAAATTTATCATCATCTATAGACAGTATAAATTTTATATCAGTTGAACTATACTTATTTACGTAATTGATGGTAAGAGTTCTCTTTCAATAATATAGTAGATCGTTGTTATTTACTTTCATATTTTTTAGAGTTTTTTAAAAAATATAACAAATCAACAAAATATTTACACTGTATAAAATAATTTCGAAAATGGAAAAAGTTCACAGGTCACATTGTAAAATACCAAAAATGTCTCAATCAACACGCGATTAATTTATCACTTGGACATAATATATTTGGTACAAAAACGTTTAGATTTGATTACATGATCGTTAAATTTAGCTACCGAAATCTAAACGATTGTGAACCAACATCCCAAACATTTTTTTTAAGATCTTAAAATAATGCAAGATTTATGATTGATTGAAAACAAAGATCGTGGTTTTAAAAAAATATAAAAAAATTGCGAAAGACGGTGGAAATGAAAAGAAAAATTACTAAAGAAGACAAGAAAGAGATGAAAAGAAAAGATAAGCGTGAACTATTTAGAAAAAATGGCTTTATGAACTTTTTAATTTTGTTACATGGTAGTAAATATTTTAGTATTTTAGGGATAGTTTGATAACCCATTTGTTTTAAATTTTTGTTTTAGAAAAGACATATTTGGTAATTACTTCACTATTTTTTTTTTAAACAAAAAACTTGTTTTTAAAATTACGAACAAAAACTAAAAGTGATAAAAAGAAGCTTTAAGAAAATTAAAAAAAATAGGGTTAATCAAACATATATGGGTTAATCAAACATATATAGTTTTCTTAATAAACAAAAATTTTAAAAACAAAAAATTAAAATAATTACTAAACAAGATTTAAAGATCAAAATGTTTTGATCCTTTCAAATTTGTGAAAGATGTTTTGCATACAAGTATAGAGTTTATATGAATTATAAACTTTGGGTTAAAGTGAGCATTTATGTGTCACAGTGGAATCGTCTTTTGGGTTCTAATTTAAGAGTTTTTGTCAACTACATTTATTCGTGTTAATATGAGTATAAGGACTCAACTCACAAAAATATAACGATCGTCCATCAAAATATCAAAATTAGAATCCTTTCGATGTATAGACAAAGATTGGATTTATCACTTGTGTCTATATTTTTCATCCATTACTTCATTAGTTACATGTGTTTTTTTAAAGTATAATTATGTCATTTGGATGGTGTTAGACTTGTGGAAAAGATATAATAAACAATATGTTATAAACAAAGAGTTAGTTAACAGATACACAAATATAGAACACTATTCGATTGATATTGGCTAAGATAGGAGCAATCAGACAAAGATATAGATAAAGATAGAGGACAGATAGACATTGACATTCTCTTTTGTTACTTTCACTTCTTTTTCTTTCTTAATTTGTTTTTCTTCTGCCTTTTCTTTAGATTTCGTTGCTTTGCTAGTTGATGTTGCTTGCTTTTTGCTCACCATCTATTTTTTTTATATAAAATAGGGTTAACTTACACAGAATAAGAGTGGTTATTACATTAAATAAAACAAAGATATATTATTTTTTGTATGGAAGATAGATCGAGTTAGATTTGGTTGTGGAACCAAAATATTGAGCAATGACCAAAATGTCAGAAACAAATTTCAAAAGAATTGATGGAGTACAAAATGTAAATAACAAGATGAAGAACAATTTCAGAAGTTTGGTTGAAGAAGGTAAGTGGAAATGAACGATCGAAGAAGATGTACGACGAAAATGATATGAAGAAAACGAAGTTGTCTGAACAAGAGAAAAAGTATGAACAAAAGGATTCTCATTTTTATAGCGCGTTGATTTGGATAGTATTTTTTAAGGACTAACAGAAAAAATAGCAAAATTGAAGGTTTACTTTGGATAAATAACAAAATTTAATTTAAATTGATAAAATAGCAAAATAAAAAAATATGAAAAAAATGGTGCAACAATATCTTAAATGCCCCTAATCTAATGAAAAAATGCTGCAACATATACTCCATAATTGATTCAAACTCCAAAAAGAAAAAAAGAATGATTATATCTATCTCCTAATTTTTCTCTATTAACACAACAAAATCAATTAAAACCTATCAAAATTTTAATTTCCTTCAAAAATCCAAAATTCCTCTCCATCAAAACTTCAAATTCCAAACAAAATTTGGACAGTCATTTCATATTTTCTTAACTTATGCACGAAAGAACATTATCATATGTTACAAACCCATCAAATCCTTCACACCTTTCAAACATTTCAAGCATTCAAACATTTAGGGAAAAGAGGTTCACCGAAAAATATT");
	blast->addSequence("2","AGGAAGTCAACCAAGATGAGGAATTACAGAAAACCATTAAAGAATTGAAACAGAATCCAGAGGGAATTAGCAAATTTAGCTGGGAGAATGGGAAACTGTTCCACAAGAAGAGAGTGGTATTATCAAAGAAGTCGTCAGTGATTCCCACATTGCTGCATACATTCCATGACTCCATAGGGCTGTAATTCCTCAAATAAATAGGGCTGTTTTCAAATATAGCAAGTTAGGGCATATTGTACTTTTAGGGGAATCAAGTGTTTATATGTCATAAAATTCCTTATCCTTTTTAAGTTTGATGTTTTGTGTTTACTTCCTGGTTATATATTTATCTTTGTTGTGTTGTTTTGGCTATATTTTTGGAATTTCTAATGTCTGTAAGGTTTGCTTTTATCTATTTAGATTGTATTTGTTTTTTGAAAAGGAGACGGTCTCTTTATTAATATAATAATAATGAGACAAAAGCTCATAGTACAAGAGAATTATACAATGAACATATGTAACCATTGATCAGGGTGTGCACCTGAGCATCTCAACTAGGTTGACACCCCCTTAGCACCCTCATCATATCCAAACAAGCTAAAGACCAAAACAAAGAAGTAATGTCCAAAGGCAAAACAACACCAAAAGAAGTACAAAGAAATACAAATACAAATAAAAGACTAGCAGACATCCATCAACTCGCGCTAAGACAAACTTGAGATCCTTGGAGAAGGAACACCACGAGGACGCTAAGAGATGACGACTCCATCGAGGTTTTATGTGTAGAAGCTTGCTTGGTAAAAAAACTCTAGGATCTTCCCAAACACAATTCGTGATCGAAATCCATTTTCCAAATTAGATTAACGAATCGACGTAGACTTCGGTAATCCCATAAAATTTTCTAGCTTTAATACAAAGGAATGAAAAAAAAATTCCAACAGGAGCTGACGACCACTAACATTGGTTGATTATAACTCCTTCTTTCCAG");
	blast->addSequence("3","AAAAAAAAAAAAAATACACAAAGGAAGTTAAATTATTCCGATTAACAATCATTACATTATATTTTATATTGCAATTATTGTACTATTGATATCTTAAAATTAAGAATAAGATAAAAAATAAATAATTTTTCTAGTATAAGAATAAACAAATAATTAAGACCTTAAAAAGTGAAAGAATAAATAAATAATGAATAGAGCATTCAAAAGAGAAAGATAAATAAGTTATGGAAGAATAGTTTATGAATAATAACAAATTTAATTTGCAAAAATCTAAAACAATAGGATATAATTGGAGATATAATTGGTATATGTGAAAATGTTATCTTCTACAAATTTTCAATTTTCTAAACTTATTTTTAAGATTAGAAAAAAAAAAAACTTGATAGAGATGACCTGAATCATAGTATGTACCCTTTTCAATCTTCTTTTAAGACTATTTCCAAACCTTTGATTCTGATTAACCAATGAAAAGATATAAATACATTTTCAAAATTCTTTCTTTAATTTAAAAGTTCCATTATCTAAATTTCATCTTTTAGTCCAAGGAAAATATCGATTTATTGAGAATCTGTTGGATATTACTTCTTGTAACTTCTTGTTTTTTCTTTTTTCTTTCTATGTTTCTCAATTTTCAAGAAACTCTTGTTTCATAAATAATTAAATTTCAATTTAGAAACATTTGGGTGAAGTTTGAAAACCCACACCAACTAATTTCTCTCTTTTCTCTTTTTGAAAAAATTCCAAATGAATAGATCACAACAACCATGGTTGAATCGAAAACATCACACAACAACTAACTAAATCCAAAATCATTTACAAAAAACAATAGAATATTTTAATAAAAAATCCAGATGAGAACAAAAACAACACTCTACATCTACATCATTCTTCCATATAATATTTTTTTTTAAAAAAATAGATATAAATTTATAAACAATATTATCAATGAATAATAAAAAAAAAAAACTAGAAGAGTAGGCAGTGCCCAGTGGAGGGGGCTGCTGCAGGAGAGAATATTCGGGGAGGGTGAGGTTAAGAGAAAAAAAAACAAAATTAAGCTTCACTTTGGTGATAACCCATATGGTTCTTCCTCACCTCTCACTTTGACCCCATCCAAATTAATATTATTATTACTCAATTAAACTCAATTATATACATAAATTAAAATTAATTCAACATTAATAACGCCATGTCCTCACCATTTTTTAAGTTCCTCTTCATTATATAATCACCCCAAACTTTCATCTAACCCTACATTCTCTTCCTTCAACTTAATTCTCTCCTTCTCTTTCTCTTCCAAATTTAAATGTAACCCTAGACAAAAAATATAACCCTTTTTATCATATATCCACTACTAGCTATGCCGATCGATACCTCTGCAATTTCAGGCCAAACTGTGTGCGTCACCGGCGCCGGAGGCTTCATTGCTTCATGGCTTGTAAAGCTTCTTCTTGAGAAGGGATACACTGTTAGGGGAACTGTTAGAAACCCAGATGACCAAAAGAATGCTCATTTGACAAACTTACAAGGAGCTAAAGACAGGCTTTCTTTGTTTAGTGCTGATCTTCTTGATTTTGAAAGCCTTCAAGCAGCCATTACCGGTTGTCATGGCGTTTTCCACACCGCCTCTCCGGTCACCGACGACCCTGTAAGAACTTCAACCAATATCTATCCTCTGTTTTTCTAATAGTTATGTTTCTAAATATTTTCAACAAAATTTTCATTTAAAACAATTTTCCAACGAAGAACAAAATCATGGTATTAATAGC");
	blast->addSequence("4","GTCTCCCATCAAGCCAAAGTTCATGTGTTATTATTAAGCTAAGAAATACTTTTATGATTTATTTATTTATTTATCATTTCTTTGAGACTATATATTTGTCAACTTGAGTTCAAATATTAGTTGATCAGTGTACAACAATTTAGTTTCATGCTTATGTTTCTAATAACAAGGGAAATCCAATATGCAGGCAGAACTATATTGTAATGATACAACAACAATCTTCCCTTTTACATCTAAAAAACCATTCATATGGCATAACATTTGTTATCTATTTTTCATAACACTAAATGTCATCTCAATATGTTAGCATAATTATTTTACATTTACATAATAGATTAACCTCATGGTTTTTCGTGCCATATTGTCAAGATTAAAGTACATATTTCATTGAAGAATTGATGATGGCTATAAGATGATTATTGTCATCCTCAACCAAAATTTCAAATGTCCTTGGTTGTAACTTTCTCTTGATGGGATACAAGAATGATTGAATGCGTGTTGTTTTCGTATGTTGGGGACCAACCTAAGGTCTCTTTATATATTTAATTCAATTAGGTTCCTATTAAGACCTAATCAATGTAGGAATCAGCTTCTACTCACTTAGTTCATAATCAATTAGGAATCTAGGGTCTTAATCAAGTAGATCACGTAATAGGCCAAATCTAATAAAGCATCCTAATAAAATAAGTGAAATTGCATCAAATGACAAAAACATTTAAGAAAAAACAGCTCATGACACCTAATTTTTGCATACGGTGAATATGACATAATTAGTGATATTAGGTGGTAATCATACGGCTATCAAAAGGCTATCAAAGGGCTATCAGAAAACTATCAGACGGTAATCACAGGGTTATCGACTTTTAAATTTGCTACTTTTGCAATTTAAAAAATGTAGTGACATGTGCCCTATATTATCATAATTTTTTTGTTGTTTTTGCAAGGGTCCCATAAAATAACTTGATGTGATAAATTATTGATCTACATACATAGCTGAAAGAAGTTTTCGAGGAGGGGTTGTAAGGCCCTGATCCTAAAAAGGGAGTCATGTGGTGAAGGACCATTGCTGAAAGGTTGTTGCAGATAAGTGTTGAGATGTCCTAAAAGAAATGATGTGAAAAGGGAGTTGGCGATGGAAAGATAGGCGTAAGCCAAAAGTTCTATCACGTGAAGGTAGGCAACACAATAAGGGTGACTGGCGAGGAAGGTGTTGAGTTAGGTGCCAAGAGGAGGCATTTGGCAAGATACTATGAGAAGAAGTATCTATGCCCAAGAGATTAAGGCGAAGAAGTAAATGTATTGTCAAAGTAACATGACAACTAGCTGTGAGAAAGGAAAGGATAGTCAGATAATTAAGAGTTTGGCTTCCCAAAGAGATAAGGTGTGTGTCTCAAGGAAAAGTCAAATTGTCGCTGACAGTTATTAGATTATGTGTCAAGCTTGGCTTGGTGGCATTCTGCGGCGTGTTAGTAAAGTGACACGTGTAAAGCATGGATGTGACCTATGGAGGTGAAAGGCCTCTATAAATAGGATCGAAAGCCAAAAGAAAAGAAAGTTTTTTGGACAAGAGACTCTAGATTTTCTGATGAAAGTGAGAGGAGAAGGTTTTGAATGCTAAACAGACGGTTCCATCAACTGTTAAACGAAGGAAGAAAGTCGAAAGTCAAGAAGGAAGAAGTTGAGGCTAAGTATCTTATGTGAGTAACCAAAATGGATTACATGTTTTATGTGTGAGTGATACATTGTTTATACCGTTTTACAGTATTGTTGACAGTAATAAATGTGATTTATAAACGTTCTAATGGTCGATTATCTTACTGTGAATAATCAAACACGTTTTATATGCTTTATTGTTGTAAGTAATAAGATCTGTTTTATAAACAATTTTGAATGAAGAATCGAATATCGAATGTAACTTCTAAACTTTGACTATCATTTCACAAAAGAAATGTTCTATAAACGTGATATTTTGTGTATTCTTTCCCCTGTGCTTGTATTTATAAGATGCTTTACTAATCTGTGATAATCTGTACTATTAGTAAGTAGGAAGTCGTTGCTTCCTTACTATATTCGAGTGGTTTTGGAATGTGGTGTATTCATCAGATGAGACGCTGCTTGAGCATGACTCCCAAGTCTGAGAATGATTGAATGTGGCAGGACGCTGGTGGAAATCTCAGGTCTATGTTTTCTATCCTTTCTCGCCCTTCTTTGTTTCCTATGATTTCTTCATATACTTAGTGAAGAAAGCATGCCAACTGACTTCCTAGCAGCCGAACTTGTAACTTTTTTAGAATTTCTGTATGGGAGATACTCTCAGACATGATAGTCAAGAGATTAAGTGACTTGAATGAAGGATAGAAAGATAACGTTAGTGCATATGAGAAATACTTTTGTAATGATGATAACTAATGAAATTGATATTTAGGGCTGAGTGAAGAATTGTGTTTGGCTATTGGTTGCAAACTGTGTGTGATGGACTTGGTGGTTTTGCATTTGTATGGTGCATATGTCACGAACACAGAGAATTGTTTCCAGATATTAGTTCTAGGGTTTACTTATCATTTAGGCATTATAACAATTAATTTAAAAGAATATAAAAAGAACTAAAACTACTTACTTACACCTAGAGACTTATGCACAGGAGAATAAATTATGGCAAGATGGAAGATTGAGCAAACTAACTTGTATGCAAGAGAAAGGTGAATGAAGGTCTATGCATTATTAGACGATTAAGCAATGCGAGAGCCTTGATGTGATATAACTTGCATAATCAGTCAATGATTAAGGAGACCTTCTCTCGAAGTATTTAGAACGCTACACTTCCTCACCTTTCGGGATGCAAATGACTACGGTTGATTACGCAAGATGTATCTAGAAGATTTCACTTATAATACTTATACAATGGATCATGGGTGAGCTATTCTCACCATGTATTTAGTATTCTTCCATGGTTGGTTGAATGAAGGTTACTATTGTGGCAGGTACTAAATATGTGTGAGCTTAGTTAGCAAAATGATTCCTTAACCATGTGTGAGCTATTCTCGATAGTATATATCGACGTTCTGCTATGGTAGGCCATTATATGGTACACGCTTATTGGCAAATGCCTATGATTTACAGTAAAATTGTGATATTAACATTTTAATTATTATTTCATTATCGATGCCTTATTTAAACATTTTTTAGAGTATGTTTACGAGTTTTAGTTTTAAAAAATTTACCACTCAATGAGTTTTAGCTCATATTTTCAATGTTTTCTCCCCCTCTCCTCCAGGTCAAGGTCCAAGCATTCATTGAACTTCCCGTCATTGATTGTAAAATCTCATTTTTTGTATGTATATATACCTAAGTCTTGTATTGCATCATGGATGGTTAGCAGTAGCAAGATCAATCACCTTAAGGACTTGCATTTTGGGAGATCCCTTGTTAGACTATACTTTTGTAACTAATTCCTAGTTGATTGTATAAACTCTATTTGAGACTCTGGATTTGTAGGATGAGTGTGTGGTGAGACACATTTAATATTATTTAGTAGAGATGATGCCAAATTTTTTTTATAGAATTTTATAAAACATGGGCGTTTGACTTTTAGGTTGAAAAATGTTCATTCAAAAAGTGTTTTCATGCCACGATCTAGGTTAATTAGTAGAAAAAATCTAAAATGAGGTGTGATAGATCTTGTTAATTAAGGTAACTGATCATGTTAGTTATGATAAGCGATCGCGTAGTTCAATGTAAATAATCGTGAAAAACTTCAAATCTAATGTTCGTGTTGATAATTTAAAACAATATTTAAACGATCTTGATATTTTCGAATATGAGGAAGATGAAGAAGAATATTGAAACAATCGTGAAATAACTTCAAAGTATTTTACTGATGAAAATGAAATAAGAGATTAAAAAAAAATTGTGTAAAAATAGAAGGAAAAAAATATGGAAGAGGAGATTAAGAAAGCGCAAAAAAGAATAATAATAATAATAAAACCTTATAAATGGTTTTGTAATATTCAAGGGCAAATCTAGAATTTATGAATTATGAAAATACAACTGTGGAGGCTTTTAGTTTTTGTTACAAAGGCTGTAAATATTTTTGGGTTTTGTTACATTTATATAAATTAGGGGTCTTTTTAAAAATTAAACAAAGCGCCAAAATATTTATGATAATAGGGCTCAAGTCACTACATTTTCTAAATTACAAAAGTAGCAAATTTTAAAAACCGATAACCCTATGATTATCGTCTTTTAGCCTATGATTACCATCTGATAGTCGTTTGATATAACTAATTTTTCCATATTCATAATATGCAAAAAACAGGTGTCATGAACGATTTTTTTCTAAATGTTTTTT");
	blast->addSequence("5","AATGAAGTAAACTTGTTACCAAACCAACCTCCTACATTTTAAACAAAAATATTATGATCGAAGGGATAACATTGAGACGAAAAATCAAATATGGCCACTAAATGATGAACCTCTCCATAGGCCATAAACCCCAAAAAGATGTTTCTTTCAATCTCACTCAAAACCATATTCAAAGAATCAGTTTCAAAAGAATTAGCTTTTGAAGGAAATCCTTAAAGAATCACATTTTCTTTATCGTTCACTTCAAGTTCTTCGACAGTTTGAAGATTCAATTCCACTGTAACCAATGTGTCGTTGTTCTGCTCGGTGTTTGATACTTCTTTTTCATCTTCTTCATTGGATTTTTCTTCACTTGAGACCATTTCAAAATCAACATTTTTAAATTATGTTTTTCAATTTTATCTTCATGGTTTTCTATTCGAAAATTTTCCAACCGTGATTTCTTTGTTTTTTCTTCTGTATATGAAACAAATCTGTTCTTGGACTCTTGCCAATAAATTGATGGTTGATCTACATGTTGAGTCATTCTCCCCAATGAACGTTGATTTCTTGGGAAATGGGTTTGATTGGATCGTTGGGCCATATTTTGATATTGTCGCCTTCTTGTTCTGTCCAAAACTGTCTTAGAAACATCATCGGAGTCACTAGAATCACTAGAATCAATTTTCCAATTTGGATGATGATAGGCTTTTTGAGAAAATCGAGCAGGGTCAAAATTTGAATGTTGAAATTCTTCTTCTGAATCACTTGAATCAGAACATTGTTTATGGAAGTAAAATTTATTTTCTTGTCTATACCATCTGCTGGTTTTTTTCTTAGATATCTTCTTTGATCGATAGTAGTCTGTTCTTGCAAAATACTCTTGGTGCATGGGGATGGGATCTCCCCTTCAATCTACCAATTTGAAGTAATCTAAGTAACTTCAAGGAAAAATCCTTCAAGAACCAAGATTATGGATTTTTTATTAGAATGAATAATATACTTATCTATAGAGTTCTATTGCAATTGGGTAAAAGGGAATTAACCTAGAATATTACCTAATTACCCAATTAACCCTCAGTCTTCTATCATCAAAAACCCAAGAAAGGAGAAGGAGAAGACGACAAATCCATCTAACAGAGGATCAAAACAACTAAATGATTCCCAAAGGAGGATAAAGATATAATGGGACTAGGCAGAGATATCCCTCACCCAGTCATTCTGAAAAGTTGGTGCAACAAAGCTCAAGCCCTGGAAGCAAAATCCTCAAGGTCAAATCACTCTCTCCAACTCTAAAAAATTCACTCAATCTGATTTCACAATTCCTGTTTCTTCTTCACATTTAACGCGAGAGGTTCTAGAAAACCAATCCAGCCCATGCCGCAAGAGAAGAAATCAAGGGTCGACAAGCTATTCAAGGAGGAACCTCAAACAGAGGAGGTTTCGACAAAAGGCCTAGTAAGTATGATACAACTGGTTGAACAATTATTGTTTTTTAGCAGTTTTGTGGTTTCATATTAGTGAAGATTCAGTAAGCTGGTTGTTTGTGCTCTTGGCATTGCCTCTTCACTCATCTCGAAGCTTATCGTGGACATGTTGTCAACTTTCTTTGGATTCCTTTTGACAATCTGTTTTAATTACTTTGTACCTAGTTTACATTCTAGATTCCATTTGTTGTTCTAGGATTTTGATTAGCGAGCTGCTATTCCTGTCTTTGTTTTGGTTATTGTTTGTATATGTTTTAGTCGTTTGGCACTCTGTATAATTCTCTTGTACTTTGAGCGTTAGTCTCTCTTTTATTATTAATGAAGAGGCTTGTCTCCATTTCAAAAGAAAATAAAGATGAAACTCCACAGCACTTATATTCAGTAATTGAGGCTTGTGATATCACTTTTGCTTAACAATTCAAGGCGTATTCTTGGGATACAACGTTTCTTCTGTAATTGGCCAGTAGAAAATTCCTTCTTGAGTCAATCGCGGGCTGGGAGACTTAACAAAAAAGAAAATGAATGTCTATGGATTCGGGAAGATAATGTGACCGATGAAGTTTCTTCGAAGGAGATACACTCCGATCATAGGAAAAGAATATGATGCACGTACTAAATTTATCAGGCTAAAGATGGGGGTTGAAAGTACTGGTTTTTCTTTCATAGGTTTTCAGCAGCAAAAAGGAGGAGAAACTTGATTCCTAGCTCACAATAATCATGGCTAGTCTGTAGAAAGTCGTGTTGAAAGATTATTGAACTTCAAGGGTTAGTGCAAGACTTTTTCCAGGGTAAGTTTCGAAAGAAGATTCAATCTCTGGGTTTGAGAGATAATCCAGCAGCTGAATTCGTGGATCAGATGTTCTCATGTTATCCTGTTTTGCTCTTGTTCTAATTTAGTGGCTGATTTTGTATTTTTGCTTTGTTTTTGGTCTTATGATGTAATCTTTGTAAGTAATTCTTTTTAGCTTGAGAAGTGCTTTAGATGTTGATCAAATGTTCAGCTTGTTGCGAGCACTAAGTGGGTGTCACCCTAGGGGTACAATCTTAGCTCCTTTCACTCTTAGTATATTTCTCTGGTACATCGAGCATTAGACTCATTCCATTTATTAATGAAGAGGCTCGAATCCTTATCTGAAAAAAAAAAGATATCCCTCAACCACTGGTCTGTTTTTCCAATAGTAGATAACCCAACTGCTCCCAATGTTAATATGAATAAATTGAGAAGTCAGGTGCAATTACTTTCCACGAATTTCAAGAGGTGCCCTTTTAATCCCTCACCAATTTATTCATAGGAACGAGGCTTGTATTTGCTAACAATAACCTTGTGTCAAAGGCCACTGGCTTCATGATAGAATAACCAGGCCATTTAGCCAACAGGGTTGTGTTTCTTGTCCTAACATTCGAACTACCTAAACTCCAAGTCCACAAACTTAGAGAAGTCACTCGTAAGCTTATCCATTTCCTTTCCAGTCCAAGACAATACTCCAAAGAGAGACAAAAATTAAATAGGGAAGCCACTTGGGACCAATTGGAAATAGTGAGTCTCCAAAAATCTCAAGGAGAAATCCCAAGAACCCAAATAGAATGAAGGGAATACCCCAACCTCGCAACCCACATGGTTGGCCTACCTCTCAATTTTGAAAGAATCGTAATTAATGCCCAAAATTTGATATTTGTCTATGTATATTCTAAGGCCTGAGGTCATCTCAATTCTCAAGAAAAGCTACCATATGATTCAAATTGATAAAGGACTCTCCATTTGATTGTGGTAATTTTTCATCCATTTTGTTTTTCAACTTTAAGCATCCATTTTCATTTTATATCCATGAGTGTCCGAGTCAACTTACCCGCACCTCAACTAATCTCAACCTACCTGACCATACAATGAAAAAATACAACATTTAAACAAGACTCCAAGAAGCATGATATTATCTAATCAAAGATGAACTCCTCCAGTTCAGGCTAATGTCTTGGATGGAGTAGGCTTCACAAGCTTTAGCTAAGGAGCACCAAGAGGATGCAATCATTTTAGCACATTTCAATCTAATCATTCAATTGGAGGCCTTGTTTTGGAAAATTCTTTGATTTCACTCAAACCAAATTAATGAAAGAAGGGCCTTAATAGCGTTTGACCATAACAATCTTGATTTTTCTTTAAAATTGGAGTGATTAGGAGTTGCAATACATTTTTCTTGAATCCATAATCAAAAGCCCAACTGATGATGAAACATCCTAAGAGTTCAAGCCAAGAATTCTCTGCGAAGGAACACTTCGAAAACTGTTCCTTAGAAAACAGATGCTGTAAATCTTCGTATTCCTGCAAACATATAAGACAAATGTTTGGAGATAAGCTGTGAAAGGGAAGTTCCAGTTGTAAAACCGAGGAACAGTTCAGAAGCCCTTGTTAACCCTTTCATTCCAAACCTTGAATCGATTGTTCAAGATTTACAATCGATGGATGTGTATCAGCTTATCTAATGAAAATTTCCGTTTTGATTCAGCTAGTCGTCAAACTTCTCCATGGTGTTCAAGAGAAATTAAGGGCACGTTTGATAAAGTTCATGTTTCTTACCATTTTTTAGGAAACAAAGATGTTTTGTTACCATTCTCGTTTCTCGTTCCCAAAATTTAAGGAAAGTTTCTAAAAATTGGGTAAAAATAGAGAAATTATGGGGAATAGTCTCTCAATTCTGTTCCAATTTTTTTTATTTTATTTCTATCACGTTTTAAAATCTCTAATTGGCTTGTTGGTTGGGAGTCATGCCTATTTTTACTTTTGACATAAAGATCTTGAGTTCAACATAAAGATCTTGAGTTCAATTCCCAACTTTGATGATATTTTTTTATT");
	blast->addSequence("6","AAAAAATCTTATATCTTCAAATGAGCTTATAGTTGACTTCATGACTTAGGGAGTCTTCTAATTATTGGGAGAATTTCTCTCTAGACTTTATGAAGTAAAAAATTTTCAACCCTTGCAAATGAGGAGAATTCCTCTCTTTATAGAGTTCACTGGCGAGCTTTATAGGTTTAAACCTGGTTGGGCGAGCTTTATAGGTTTAAATCTGGTTGGTCCATGGACCAGACCTATGGACTCAACCATATGGATTTAGGTTATATTTAGTCATTGGGCTCAATTACACTTATTTTTGGGCTTAATTGAACTTAGTCCAAGGAAATAATATTTAATTGAACCAAAATGATTAACTTAATCCAACGATTAAGATGAAAGCATGTGGCATTATTAGAATGATTAATTTATGTTTTTTCAGTTCTTTAATTTGAGGGCACATGTCAATTTTAATTAGTCACAAATTTAATTATTTGTACTTTTCATCCTTAACTTAATAAATGATGTAGCAATTTGTGATTGATCTCAAAATTTCTTAATTAAACCGTCTTTTCTTTTCAATCTTTTTTACATAATCGTTATGCACGAGTAAATTATTAATTTTATTATTTAATTTACCAAATCGTTCTAGTTTTTGTGATACAGGATAAAAAAAAACAAGTCAAGCGGCGTAATTACAATAAATTACCTAATTCAAGACTAAAAAGAAAAAATATTCACCTAGTTGTACCAAATTCTTAAGTTTAAAAACAAGTTATGTTTTTTAAATAAAAAGATTAAAATTAACAAAACTCTTAGGATAAAAATTATATAAATTATAAATGAGAAAAAAATAGAATAAATAATATTTAAATTTAAATGAGTTAATTATAAATAATAAAGGGTTAAAATAGGGTTGGAGTGGTTGAGGACGGGTTATGATAACTCTTCCCCTTAATCTTTTCCACGCCCAAACACTCCGAGGTGTGAGAATTTAGGAAAATTAGGGAAGGGTTTTAGCCTAAACTTTCTTTGGACCAAGGGTTTGCAAAATTGGAGATTAGGGTTAAATAACTCTACAAATTTTTCTACTTCATCTTATCATAATACTACACTCATAACTGTTCCCCAAACGCATATTATCATAATACTACAACAATAATAATTCTTTCCCCAAACACATATTACCATAACATTATAATTCATATTCTTTCCCCAAAACACATATTACCAACCCAACCCCAAACACATATTATCATAACACTAAGATTATAGATTATTATAATAATCCTAGGATTATTCATAATCTTTTTTCCCATAACTCTTTCCATCCTCCGAACGTTTGTCATATGGTGTAATTTCTCATTAATTTTTAGGATGCAACGTTGAAATTAAAAAAATTTAGTAATAAAGTTCAAAGCAGACGAGAGTATAGTTTAAAATGACACCAAAGTAGTGTTTCAAATTCCACTAAACCCTAACAATTGTACTACATAAATGGAGTTGAAATAAATGTTTTAAGGTTGTAAATATAACACCCAAAATTTGGTCCTTTCATTAGGAAGGAAAAATCCCCTTCAAAGAAATTTGACCTCCTAGTAGAAGAAGCTATAAGGTTTTTACACAAATTAAAAAATCTAACTTATTAAAATTGTTACTTTTCTTTAATATATAGTAGAAAGGCCAGCTATATAACAACTTTTTTCAAAAAGATTTTAAAATTAATATATATCCTCCTTACCAAAAATATTATAAAAAAATGTTCAACATTAAAACTAAACTATATATTTAAGTCATAACTGGAAGTACATCATACTCTGGATGCATAGCTTAGAAGAAATAAGTTTCTGCAGTGCTGTCTCGAGAAAGAGCCAACACTAACTAATAGAGAAACCCTGTTCGTAAATGCTGTATAGGATTTATAGTTATGTATAGGATTTATAGTTATGTATAGGATTTCAGCAACTAAATCCTATACATAACCTTATCGAATAACAATGTAAGCATTAAGCAATCGAACAATATGGAACACCATTTTTTAACACAGAAATTGACCTGCTAGCTAAATGCTGTAATTAGCTACAGCTAAAAGTGAAGAATTACAGTTTTATGGCACAAGATGCATTAATAGTTGCTCAATCTTAGCATAATATTTTTCTCCTCCCTACAAAATGACAACAGGCATACAAAAATACCTTCACTGCTGCGCATGTGAAGTTTTGCTGCTATTAGCAGAAGCACTCCAGAATCTGGGTGGCCGCTCCAGAAAGGCAGGTGGCCGCTCGAACACTAAGGAAGCTGCCTTGATCAAGATACCAGCAGTCAGAGCCCAGATCACATACTTTTGGTTCTCACATTCGTAGTCAAAAAAGTGTAGTAGATAATTATATCCCATCCATTCCTTCTCCTCTGCTCTTCTTTTCTCATCCTGTGGCAACTTCGAAGTGTGAGACTAATACAGAATGAAACAACAATCACAACCATTCTGTGTAATTTAATTTAATCAGAGTTAACATAAAAAAATATGACGAACCTTAAGGAACATTTCCAAGGGAACATCAAATACTGCATCTACTTCAGCAGCATTTGGAGTTGGATTGAATGCTTCCTTGCTAGATAATAGGCCAAGGACAGGAACTACAGTCATACCCTTCTGCACAGAGAATACACATCATATGTGAAATGGTGGGAAATTCATAAATTACACGAGACAACAACCACCAAAAAGGGTTCGAATTAGCAGCAAAATGCAAAATATGGTTTAAAAGCAATTCCTGGTTAATCTAATAAGCCAAGTTCAAAAGTTCCCCGGACAATGTTAAATGAATACTGGATGGGAATGTGAATCTATCGATAAACTGGAGAGAGGAAAGTTTTTTGTAGGGTCTATTTGATAACCATTTAAATCTGGTAGGGTAACCATTTCATTTTTGGTTTTTAGTTTTTCAAAGAAGCATACTTTCTGTTTGCATCTTTCATAAGTACAAAAGTTGAATTCTTAGTCAAATTCCAAAAGTACGAAAGTTGAATTTTGAGTCAAATTCCAAAAGTACAGAAGTTGAATTCTTAGTCAAATTCCAACGGCAATAATGAATTTGACTTGATGTTTTGAATAATTGGTAAAAATGAGATAACAAACCCAAAAACTTGGAAGTGAAAGAGGTGTTTACAGGTTTAATTCCAAAAACTAAAACAACCAAATGGTAACCAAATGTGGCCTTAGCTTTTGAAAAGTAATTTTATGAACACCAATATAATTACACCTATGAGTTCCCTTGTTTTGTTATCTAAGTGTAAGCCTAGTTTTGATGTATTAACAAAGAAGTTCTGACGACAACAAGCTAATTTTATATATCCTTGTTCACCAAGACAAAGTACAGATTGTACAGTGAATAAGCTACATGGACAAACAGAATCTAAACTCAATATTGAAAACAAAAAGACATGTAAACCTTATTAACAAATGGTTGAAGAACAGTGATGATGTTAACAAGAGAAGGGGTTAATCCAATTTCCTCTTCTGCCTCCCTCAATGCGGTCGCAACATCATCGGCGTCACTCACATCCCTTTTTCCGCCGGGGAGTGCAACGTCCCCTGCACCCTGAATGTCAATTATGGAATCGTCGTGCTAATCTATTGCCCCCTTCAAAACGAATTTCAAATTTACAAACATGAATTAGGGTTTGGGATTGAGACTTACCAGAGTGGGAAGAAAGCGTAGAGGCTCGCTTTGTGAGAATGACGCGGAGCTCGCCAATGTCGGTTAGGAAGAGGCAGATGAGAACAGCAGCACGGTTGGTGAGTTGAGCTGCTGCCGGAGTTGGTGGCAGCGAGGGCAGAGATTGAGAAGAATTGCTTGTGCGGAAATGTTCTGCTAAAGCCTTCAATCTGTGGAGAATGTGTTCTCCAGAGGGTTTGGAGGCCATGGACATGGAGCCTGGAGGAGGATGAGGGTGCTGCTTCTTTGTGTCTTGCTATTTCTTCATCTTTGAGATGTATTTGGTAGGAAATACTATATTACAATCTTATAAGCAATGAAGATTGATGTCACGTAATCATGTACCTCAATTGTATTGAAACACACAAGTGAATTGATAAATGTAGGTTAGCAATAAAAGCAGTGGGTTCCATTTGGAGAGGAGAGGTCTATAGTTTTGTATTCTAATATGGGGTTATTATTGTCTATGTTTGCATGCACATTATTTTTTGGTGGACATTATTATTATTTGTATACAAGTAGGAGTTTGAAGATTAATTAATTTAAAATATAACCCTATTATCATAAGTTAACTATAAAATTAGTACAAATCTTAAACAATATATGGACTCAAATTAATTGACCCCTTTTTAAAGTTCTAAAAATTAAAAAATTACAAAAATATTAGTTAAAGAAAAATGGAATCACATAAACATTTAGAAAAGAAACCCTTCTATAATATAATTTTTTTTTTTTTGCATATTTACATATTGCGAATATGACAAACATGACAAGTAATTAATGATATTAGACGACTATTAAAAAAATTATTAGAAAGTTATTAGATGAATTATTCACTTTCAAATTTTCTTCTTTTACCATTTAAAAAGTTGACCATT");
	blast->addSequence("7","GGTTTCCAAATAGGATTGTGTTAAGACACTTCCCTGCACTCAGAAAAACTCAACGCAATACAGATACAGAAATGATATTCTGTAGTTCTTTGTATATAGATATAAACCAACAAGAATCGTTCACTACGATAGTTCAAACAGAGAAGGTAAATATAGTAAGGCAACAGTAAGAAAACAGTAGAACAACACCCCCAGCAATTCGAGAAGCTGGTTTTCTCCCTAAAAGCTCTCACCGCAGCTTTTTACAAAAATAAAACCTACCTCACCAATCCCTAAAAACATTCCTTAAATACCTCTCTCCCCAGGCGGGCCCTACACCCAAATATTCTTTTCATTTAATTCAATTGGCTGAGCTGCCTTCTTGAACCATCACCTTTTTACCCTTGCGTTTGTAGGTGTGTATGATAGGAGGTCTAACAATACCGTCGGGCTCAAAACTCACCTTGTCCTCAAGGTGAAACGAAGGATACTGTTAGTTCATCGCATAAACAGATTCCCAAGTCGCTTCACTGTCATGTAACCCCTTCCATTTCACCAACCAATCATTAGCTCCCATCTCGCTGTTCCAGCGAACTCCCAGCACTGCTTCCGGTTCCACTTGCAGCTCAAAATCTTCAGT");
	blast->addSequence("8","GGTGGCTTCTTCTCGCCATCAACCAATCTAAGAACTCGAACTAGTGGGCCAGATACTTTAAGCGCGAAAACAATTGTAGTCCAAAAACTAGCCAACAAAATAGTCTGAACTACTCGTTTCCCTTGTTGCTCCTTACTCCATTTGCTGTCCTTCCATTCATCTGAAGTAAACATCTTCCTCAGATTATTCTTTTGACGATGTATACTCGATAATGTAATGCAAGCAGTAGCAAAACGAGTCTTAGCTGGTCTAACTAACTCCTTTTGGTTAGTAAAACGTCGCATCATGTTTAACAATCCAGGACGAACGTATATGAAATTGCTGATCTCTATGCCTCTTTTCAATGCTTTGCGAATATTCGAGATCTTGTATATATCCTCCAACATCAAATCTAAGCAATGAGCGGCACACGGAGACCATATTAACTGTGGTCGTTTTGCTTCTAACAATCTCCCTATTAACAAAGAAAATAAGTACACATTTAAAGTAGAACTCAACTAAATCTAATAAATTAAAGTTATAACTTGTAAGTAGTCTACATTCTTACCTGCCATCACATTTGCTGAGGCACTATCGGTAACTACTTGTACAACATTCGCTTCTCCAATTTGGTCTACAAAATTATCAAGTAACTCGAACATCTTCTATCCATCTTTCACATAAAATGAAGCATCGATGGACTCAATAAACATGGTGCTTTTAGGACTATTTAACTAAAAAGTTAATTAATGTCCTATTTCTTCTATCGGTCCATCCATCAGCCATAACAGTGCATCCAACCTTGGCCCACTCTACCTTATGGTTACTCATCAACTCATTTGTTGCTTCTAATTCCTTCTTCAAACATGGAACTCTTAACTCATGATAAGATGGTGGTTTCAATCCAGGACCGAATTGCTCAATTGACTCAATCATAGGGGCAAAACTTTCATATGTGCAAGCATTCAGAGGCACTCCTGCATCATAAAACCATCGAGCAATTCTTTGGATGGTGTGCTCTCTCATTTCCTTCTTGTATGTCGCATTCAATGAAGTTTGTTTTCCTTTGTCCTTTCTATTTTGGGGTTAGGAGTAAAAAATGCATCCATTGGACCCTTTTGCCTTGGCTTCTTCAAGCTCGGGCCCCTTGGTGTTGCTTTGTTGTTTACACTAACATTCCCTTCATCTTTATCCTCAATACCGTAATCTTCTACATCAATGTCCACAATCAGATGTCTTTGTTCTTTAATATCTTTTTCTTGGACATGTACTCTTTAATTTCTTCCTTCACGTGATCCGGACATTTTGTACAGGCGGTGACATTTCTATAACCACCAACGAGGTGTTGTTTCATTCTATATACCCCTCATTTTGTTACTTTCGAACAAAATCCACAGACAAACGTATTTATATTTTGGTCATTTTGCAATTGACCATATTTCCATGTCGGATCTTTTCTCGAACTTTCATCAGCCATCTATGATCTAAGTTATAAAAAAAACACAGAACTA");
	blast->addSequence("9","CAGTACTTGGCGCCAGGATAATACTATTGTTCAGAAATGTATTTGACATCCTAACAGAACCAAGATCATAACATAGAAAAGTTTGCCTTTCAAGCTTGATATAAGTAAACAAAATATATACATTCTTACCTTCTTATTATTATTAATATTCGTGCATAGAAAATTCGATCATAATATTGCTTTAATTGGTAGAATTTTGTTATCTTAGTGCTCTTTTATGTCTTTTTCCTTTGCCACTCAGATCAGAAATTGCGTGGAGGGATGCAAAATATGCTCAAATATATGAGTACCTTCGGGAAGAGTACGAGGTCACCCAGCGCTTTGGGAATCTAGATTTCAAATTGAAGTTTGTGGAGGTAATTTCATTCTATTCCATTCATTCCTTCAAAGTGGTTTTTTCCGTATAGTTGAGCCTCTTCTCTTGAACGTTCTTCTTAAATATCGTGGCAATAGCCAACTTGAAAGCAATATTATCTACTTTTGGTTATATGCAATGGAAAATGTGTTGAGAGGACGTGTAACCTCGTGAAAACTTTCGTATTTTCTTTAGTATTCTTTTTAAGGGAAAGAAAACCAATTTATACTAAATGTTGTATTAACTAAATCTCTCAACTTTCACAAGTGAATGAATTTAAATCCTTCATTCTTATTTCATTTTAAAATCGTTAAATCGTTAATGCATAATATTCACACATGTACAAGGCTTTAAATTCAAGGATTGGAACGTATTAAATCAAATGGATACTAGCAGCTTCTGATTAATTTTATTGGTTTTATCATATTCTTGTCCACTCTTTCTTCACTTATTTAGAAAAAGTTACATAACAACTTTTCCTACTGCTTCGGTAGAATTTTAGGAAAAGAATTTTTTTATTTAACAGTTTGGATGGTGGATATTATTTCGTGGGTATGAGCATTATTATCCCTAGACATTTAGATCCCAATGTTCAAGAATTAAATGTTTATTTTTTTAAAAGAAGAAGAATAAAAAAAATAAAATATTGACATCAATATTCTAATCCGTGGTGAAGGGACGTGGTCCTATCAAAAGCTAGCTACTATTGTAGGAGAATCAATTCATAGTTCTTCAAGGAGTGAAGTTTTGAGGACTCTCTTTATTTAATTAGTTTAGAATGTTTCTTTAAGAAATTGGTTCTGCTAAATTGTTTCCAAGTGTTTGTGCTGTCCATCTGAAGTTTGTGTATTCTGAAGCTGACCCAAAATAATGCAAATGAAATCAGGGAGTGGTGTGTGTTCCTTTTCCAAAAGCCGAGCTAAGGAAAAATAATCAACATTCTCATTGTGATTTCCTTATTTAAATCTTTAACCTAGATTCTTCCACTTATATCATACTCACTGGAAGGAGGTTCTTTTACTTTTATGGAAATGATATTTCTTGAGATAGAACAATGTTTAATTCTTCTCTAATAAATTTGCACCTTCCTTGCAGCATAACATTCATTTTCTTCAAGAAGTCCTCCAGAATAGGAAATCAGATCTCTTGGAATGGTGCATCATTGGCCTATTGAGCATTGAAAACATTATATCATTATATGAGATTGTTAAGGATTCAACTCCCATGCAACTCTGATTTGCCAGCGTCGCGGATGCAATTTTTGATCTGCAATTAGTAAAGTCTAATTTTGTTTTTGTTGTACTAATTATTTTATCATAAAGATAATAATCTGATTTTCTTATATTTTTATTTGATCCTCCAGCTCTCCATATTACATTATGCTCATGTTGTCTTACATTATTGCATTATATATATAGATGCGCATAAACATACAACTATTGTAACTCGAACAAAATTCAGTTGGAGAAATTCATTACTATTTTACCTTCTAGTTTTCTTTTATGTAAATAACTATTGAAAAGTTTCCTAAAGTATGTTGATGTTGAGCCATAGCAAGTACTTTTAGAAGATGCAACTTATTCTCTCTAGGGAGAGATTCTTGAAACTGATCACAGATACAAAATTGTGTACATTTACAATAAGTTTAGGATACTGTAATAGGTAGCAAAATAAGTTGAGATATTTTGCAAATGTGTCTTCCAGATTTCTACTATTGCAAATATGAGAAAGAATTCAAGTTATGATTTTGGTTATTTCTTTATATCCATTTATCTTCTTGATGAACCTAAACAAAGTTCCTACTTTCTCTTTTTTTTTTGCCATTTGCATGCATGATCTTTTTCTCCTCTCAACATTTTTCTTCTTCGCAAGTGTGGTCTCAATCCTTATTTTCTTTGTCTTGACCATGATCAATAACTCAACTTTGAGGCGGTAGACGGTGTGGTGTTTGAGAAATTGTCAAGTGATTTTTATTATCTAATATGAAGTGTATGATAACATTCTTAGATCTATAAATTTACAAATTATTTACATCTGCAAACCTTTTATCAAAATAACAATGGACAGCAACAACGAGACAGTCAATTAATACATTATATAGCAAGTCTTCCATTTCGGGGAACAACTAACTATAGTCAAATTCATCACCATCTTCTCACAATTTCTACCATTTTACAACAACTCCATAGGTCTTCCGCAACATTCCAAGTCAGTAGCTAATCTTAAGTACAAAAGTTCCTATGAGGGAGGCATAGTAGCTCTAAAATTTCTCATCCCACAAAAGTGTGTGTTGACGGACGATTAGAGAATTCGTCCAAGGAAAAGACTTAGAATTTTGAGGATTCACCTCAAGTTCAGTTGTAATTTTCCTGTATTTCATTTTATTTGATTGAATTTATTAATGAAATATTCAGTTTATAATCACTTCTTGGTTCACTGTGGTTTACACGAGATCTTTATAGAGAAATTTAATTTGTGAACTCCAACTTGTATTAATAATGTATTTATGTTGATTTGATGCAATGAGTCATTTGATCTCCTGATTCTCTATCACTTAGATGCTTATGCTTGATTTGAGGAAGCAGAGCACGTGACGTTCTTGAAGTTGGAGTCTTGAAAGAAAGTTTGTATCTTCAAATGAAGGGAACTCCAGTATCTATAGAGTTCTTTAGTGGCTTTTATGAACTTGAGTCTGGTTGATTTATGGACCAGAGCTAAATTAAATTTATTTTTTTGGCTCAATTGAATTTTAGTCTTAACCAAGTAAATAATATTAATTAAACTAAATATTATTTGATCCAAACATGTGTATCATC");

//	result = blast->search();
//
//	std::cout << "\nWynik SEARCH: " << result << "\n" << std::endl;
//
//	result = blast->estimate();
//
//	std::cout << "\nWynik ESTIMATE: " << result << "\n" << std::endl;
//
//	//blast->printWords();
//
//	result = blast->extend();
//
//	std::cout << "\nWynik EXTEND: " << result << "\n" << std::endl;
//
//	result = blast->evaluate();
//
//	std::cout << "\nWynik EVALUATE: " << result << "\n" << std::endl;
//
//	algorithms::Alignments aligns = blast->getAligns(10);
//	blast->printAlignsFrom(aligns);

	//blast->printAligns();

	algorithms::Alignments aligns = blast->run(5);
	std::cout << blast->getAlignString(aligns) << std::endl;
	//blast->printAlignsFrom(aligns);

	return 0;
}
