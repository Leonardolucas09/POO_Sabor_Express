from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet");
restaurante_praca.receber_avaliacao("Gui", 5);
restaurante_praca.receber_avaliacao("Lucia", 4);
restaurante_praca.receber_avaliacao("Josué", 1);
# restaurante_beco = Restaurante("beco", "Finlandesa");
# restaurante_cachorro_careca = Restaurante("Cachorro Careca", "Brasileiro")

# restaurante_cachorro_careca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main();