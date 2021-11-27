class UserCanVote:
  def __init__(self): 
    self.voteRequired = self.voteOptional = self.voteNotAllowed = self.userQuantity = 0
  
  def menuSelection(self):
    checkContinue = int(input('Deseja verificar outro cidadao? \n' 
    '[1] Sim \n'
    '[2] Nao \n'))

    while (checkContinue != 1 and checkContinue != 2):
      checkContinue = int(input('Opcao Invalida, tente novamente: \n'
      'Deseja verificar outro cidadao? \n' 
      '[1] Sim \n' 
      '[2] Nao \n'))
    
    if (checkContinue == 2):
      print('Programa encerrado, resultados: ')
      self.showResults()
      return False

  def checkUserVote(self):
    userAge = input('Insira a idade: ')
    self.userQuantity += 1

    if (userAge >= 18 and userAge <= 69): self.voteRequired += 1
    elif (userAge >= 16 or userAge >= 70): self.voteOptional += 1
    else: self.voteNotAllowed += 1

  def showResults(self):
    print(
    'Total de moradores: {} \n'
    'Eleitores obrigatorios: {} \n'
    'Eleitores facultativos: {} \n'
    'Nao Eleitores: {}'
    .format(self.userQuantity, self.voteRequired, self.voteOptional, self.voteNotAllowed))

def countCityVotes():
  cityVoting = UserCanVote()
  isFinished = False

  while(not isFinished):
    cityVoting.checkUserVote()
    selection = cityVoting.menuSelection()

    if(selection == False): break

countCityVotes()
