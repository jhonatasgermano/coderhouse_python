class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        area = self.base * self.altura
        return area

    def calc_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro
