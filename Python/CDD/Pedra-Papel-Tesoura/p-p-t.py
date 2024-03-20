resp = 'S'
while resp in 'Ss':
    pts1 = 0
    pts2 = 0
    for rodadas in range(3):
        print('1.Pedra')
        print('2.Papel')
        print('3.Tesoura')
        player1 = int(input(' Player 1\nQual quer jogar?'))
        player2 = int(input(' Player 2\nQual quer jogar?'))
        if player1 == 1 and player2 == 2:
            print('PLAYER 2 WINS')
            pts2 += 1
        elif player1 == 2 and player2 == 3:
            print('PLAYER 2 WINS')
            pts2 += 1
        elif player1 == 3 and player2 == 1:
            print('PLAYER 2 WINS')
            pts2 += 1
        elif player1 == 2 and player2 == 1:
            print('PLAYER 1 WINS')
            pts1 += 1
        elif player1 == 3 and player2 == 2:
            print('PLAYER 1 WINS')
            pts1 += 1
        elif player1 == 1 and player2 == 3:
            print('PLAYER 1 WINS')
            pts1 += 1
        else:
            print('TIE')
            pts1 += 1
            pts2 += 1
        print('PLACAR\nPLAYER 1: {} X PLAYER 2: {}'.format(pts1, pts2))
    resp = input('Gostaria de jogar novamente? [S/N] ')
else:
    print('Jogo Finalizado')