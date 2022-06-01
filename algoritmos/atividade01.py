class BookSale:
  def __init__(self, bookAmount):
    self.bookAmount = bookAmount

  def calcBookValue(self):
    self.criterioA = (0.25 * self.bookAmount) + 7.5
    self.criterioB = (0.5 * self.bookAmount) + 2.5
    self.criterioC = (0.65 * self.bookAmount) + 1.5
  
  def verifyEqualValues(self):
    if (self.criterioA == self.criterioB == self.criterioC):
      return ['Criterios com valores iguais', self.criterioA]
    elif (self.criterioA == self.criterioB):
      return [2, self.criterioC]
    elif (self.criterioA == self.criterioC):
      return [1, self.criterioB]
    elif (self.criterioB == self.criterioC):
      return [0, self.criterioA]
    else:
      criteriosList = [self.criterioA, self.criterioB, self.criterioC]
      maxCriterioValue = max(criteriosList)

      return [criteriosList.index(maxCriterioValue), maxCriterioValue]

def makeASale():
  criterios = ['A', 'B', 'C']

  bookAmountSale = input('Insira a quantidade de livros comprados: ')

  sale = BookSale(bookAmountSale)
  sale.calcBookValue()
  usedCriterio = sale.verifyEqualValues()[0]
  discountValue = sale.verifyEqualValues()[1]

  print('Criterio utilizado: {}'.format(criterios[usedCriterio]))
  print('Valor do desconto: R${:.2f}'.format(discountValue))

makeASale()
