import itertools
import numpypy as numpy
def main(zods):   
    all_zods = [aqu,pis,ari,tau,gem,can,leo,vir,lib,sco,sag,cap]
    scoring_matrix = numpy.array(((0,5,10,15,10,5,0,-5,-10,-15,-10,-5),
                                  (5,0,-5,-10,-15,-10,-5,0,5,10,15,10),
                                  (10,-5,0,5,-10,15,-10,5,0,-5,10,-15),
                                  (15,-10,5,0,-5,10,-15,10,-5,0,5,-10),
                                  (10,-15,-10,-5,0,5,-10,15,10,5,0,-5),
                                  (5,-10,15,10,5,0,-5,-10,-15,10,-5,0),
                                  (0,-5,-10,-15,-10,-5,0,5,10,15,10,5),
                                  (-5,0,5,10,15,-10,5,0,-5,-10,-15,10),
                                  (-10,5,0,-5,10,-15,10,-5,0,5,-10,15),
                                  (-15,10,-5,0,5,10,15,-10,5,0,-5,-10),
                                  (-10,15,10,5,0,-5,10,-15,-10,-5,0,5),
                                  (-5,10,-15,-10,-5,0,5,10,15,-10,5,0)))

    def score(combo,combo_proc_seq,combo_len):
        running_score = [0]*combo_len
        for i in combo_proc_seq:
            running_score[i[0]] = scoring_matrix[combo[i[0]],combo[i[1]]] + scoring_matrix[combo[i[0]],combo[i[2]]]
        return running_score

    def combo_to_name(combo):
        naming = ['Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn']
        combo_name = []
        for i in combo:
            combo_name.append(naming[i])
        return combo_name
    
    running_best_combo = []
    running_best_combo_scores = []
    running_best_score_sum = -1000
    combo_proc_seq = []
    combo_len = len(zods)
    number_of_missing_zods = 10-combo_len
    for i in range(0,10):
        combo_proc_seq.append([i,int((i+1)%10),i-1])
    filler_combos = itertools.combinations_with_replacement(all_zods,number_of_missing_zods)
    for filler in filler_combos:
        combos = itertools.permutations(list(filler)+zods)
        for combo in combos:
            combo_score = score(combo,combo_proc_seq,10)
            sum_combo_score = sum(combo_score)
            if sum_combo_score >= running_best_score_sum:
                running_best_score_sum = sum_combo_score
                running_best_combo = combo
                running_best_combo_scores = combo_score
##            if sum(combo_score) == running_best_score_sum:
##                running_best_combo.append(combo_to_name(combo))
##                running_best_combo_scores.append(combo_score)

        print_out = []
        names = combo_to_name(running_best_combo)
        for i in range(0,len(names)):
            print_out.append('%s - %s'%(names[i],running_best_combo_scores[i]))
        print running_best_score_sum, print_out            


aqu = 0;pis = 1;ari = 2;tau = 3;gem = 4;can = 5;leo = 6;vir = 7;lib = 8;sco = 9;sag = 10;cap = 11        


main([lib,vir,vir,vir,cap,cap,sag,sag,ari,leo])
