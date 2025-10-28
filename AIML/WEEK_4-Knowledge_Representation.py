from sympy import symbols,Or,Not,Implies,Xor,satisfiable

Rain = symbols('Rain')
Harry_Visited_Hagrid =symbols(' Harry_Visited_Hagrid')
Harry_Visited_Dumbledore = symbols('Harry_Visited_Dumbledore')
sentence_1=Implies(Not(Rain),Harry_Visited_Hagrid)
sentence_2=Xor(Harry_Visited_Hagrid,Harry_Visited_Dumbledore)
sentence_3=Harry_Visited_Dumbledore
Knowledge_base = sentence_1 & sentence_2 & sentence_3
solution = satisfiable(Knowledge_base,all_models=True)
for model in solution:
    if model[Rain]:
        print("it rained today")
    else:
        print("There is no rained today.")
