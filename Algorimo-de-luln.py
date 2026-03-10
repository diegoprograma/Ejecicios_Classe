class TarjetaCredito:
    def __init__(self, numero,):
        self.numero = numero
        
    def convertir_a_digitos(self):

        return [int(d) for d in str(self.numero)]

     def invertir_digitos(self, digitos): #reverse
            digitos = list(reversed(digitos))
            return digitos
    
    def duplicar_impares(self, digitos):
        for i in range(1, len(digitos), 2):
            digitos[i] *= 2
            if digitos[i] > 9:
                digitos[i] -= 9
        return digitos
    
    def sumar_digitos(self, digitos):
        return sum(digitos)
    
    def validar(self):
        digitos = self.convertir_a_digitos()
        digitos_invertidos = self.invertir_digitos(digitos)
        digitos_duplicados = self.duplicar_impares(digitos_invertidos)
        suma_total = self.sumar_digitos(digitos_duplicados)
        return suma_total % 10 == 0
    
    #testing : 4532015112830366 y 4532015112830367
    def test_tarjeta_valida():
        tarjeta = TarjetaCredito(4532015112830366)
        assert tarjeta.validar() == True, "La tarjeta debería ser válida"
        