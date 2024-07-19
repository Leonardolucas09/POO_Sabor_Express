from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = [];

    def __init__(self, nome, categoria):
        self._nome = nome.title();
        self._categoria = categoria.title();
        self._ativo = False;
        self._avaliacao = [];
        Restaurante.restaurantes.append(self);
 
    def __str__(self):
        return f"{self._nome} | {self.categoria}";

    @classmethod   
    def listar_restaurantes(cls):
        print(f"{"NOME DO RESTAURANTE".ljust(20)} | {"CATEGORIA".ljust(25)} | {"AVALIAÇÃO".ljust(25)} |  {"STATUS"}");
        # print();
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |  {restaurante.ativo}");

    @property
    def ativo(self):
        return "V" if self._ativo else "F";

    def alternar_estado(self):
        self._ativo = not self._ativo;

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota);
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-";

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao);
        quantidade_de_notas = len(self._avaliacao);

        media = round(soma_das_notas / quantidade_de_notas, 1);
        return media;

# restaurante_praca = Restaurante("Praça", "Gourmet");
# restaurante_praca.alternar_estado();
# restaurante_beco = Restaurante("beco", "Finlandesa");

# restaurantes = [restaurante_praca, restaurante_beco];

# print(restaurante_praca);
# print(restaurante_beco);

# Restaurante.listar_restaurantes();