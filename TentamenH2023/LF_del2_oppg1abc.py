from film import Film

# a) Var å lage klassen Film - se filen "film.py"
# b) Første oppave var bare å lage et film objekt:
imitation_game = Film("The Imitation Game", 
                          "Morten Tyldum", 
                          ["Nora Grossman", "Ido Ostrowsky", "Teddy Schwarzman"], 
                           "2014-11-28")

print(imitation_game)

# c) Vis antall dager siden premiere
imitation_game.print_antall_dager()

