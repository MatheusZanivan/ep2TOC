file = open("entrada.txt", "r") 
file_list = file.readlines() 
file_list = [line.strip('\n') for line in file_list] 
file_list = [line.replace(' ', '') for line in file_list] 

#qa = estado de aceitacao 
  
#q = q0  # Estado Atual 
head_position = 1  # Posição do cabecote

# Estado Inicial
def alphabet():
    for word in file_list:
        if word[0] == "A":
            alph = list(word)
            alph.pop(0)
            return alph
def states():
    for word in file_list:
        if word[0] == "Q":
            states = list(word)
            states.pop(0)
            return states

def initial_state():
    for word in file_list:
        if word[0] == "q":
            q0 = list(word)
            q0.pop(0)
            return q0

def final_state():
    for word in file_list:
        if word[0] == "F":
            qF = list(word)
            qF.pop(0)
            return qF

def transitions():
    for word in file_list:
        if word[0] == "T":
            trans = list(word)
            trans.pop(0)
            return trans
def words():
    for word in file_list:
        word_list = []
        if word[0] == "P":
            word_string = list(word)
            word_string.pop(0)
            word_list.append(word_string)
    return word_list

def main():
    #print(alphabet(),states(),initial_state(),final_state(),transitions(),words())
    print(words())
if __name__ == "__main__":
    main()
 