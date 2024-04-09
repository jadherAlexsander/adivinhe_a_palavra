import os

palavra_secreta = "comer"
palavra_formada = '*' * len(palavra_secreta)
contagem_tentativas = 0  
chute = ""
i = 0

while True: 
  i = 0
  chute = input("Digite seu chute: ").lower()
  contagem_tentativas += 1 

  if(len(chute) < 1 or chute == " "):
    print("Digite pelo menos uma letra.")
    continue
  elif not chute.isalpha():
    print("A letra deve ser do alfabeto.")
    continue
  elif(len(chute) > 1):
    print("Digite apenas uma letra.")
    continue

  if chute in palavra_secreta:
    for c in palavra_secreta:
      if c == chute and palavra_formada.count(c) < palavra_secreta.count(c):
        palavra_formada = palavra_formada[:i:] + c + palavra_formada[i+1::]
        
        if palavra_formada.count(c) == palavra_secreta.count(c) and '*' in palavra_formada:
          print(palavra_formada)
      i += 1 

  if palavra_formada == palavra_secreta:
    os.system("cls")
    print(f'Parabéns! Você acertou todas as letras! \nA palavra é: '\
          f'{palavra_formada.capitalize()}. \nVocê acertou em {contagem_tentativas}'\
            'x tentativas')
    contagem_tentativas = 0  
    palavra_formada = '*' * len(palavra_secreta)
    continue