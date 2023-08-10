from prettytable import PrettyTable
table = PrettyTable()

def update_table(ar):
    table.clear_rows()
    table.add_row(["0", ar[0][0], ar[0][1], ar[0][2]])
    table.add_row(["---", "---", "---", "---"])
    table.add_row(["1", ar[1][0], ar[1][1], ar[1][2]])
    table.add_row(["---", "---", "---", "---"])
    table.add_row(["2", ar[2][0], ar[2][1], ar[2][2]])
    print(table)


def to_continue():
    cont = input("Would you like to play again? Type 'Y', if you want to continue. And 'N' - if you don't. ").upper()
    if cont == 'Y':
        return True
    else:
        return False

def check_winner(sign):
    if ar[0][0] == ar[0][1] == ar[0][2] == sign or ar[1][0] == ar[1][1] == ar[1][2] == sign or ar[2][0] == ar[2][1] == ar[2][2] == sign or ar[0][0] == ar[1][0] == ar[2][0] == sign or ar[0][1] == ar[1][1] == ar[2][1] == sign or ar[0][2] == ar[1][2] == ar[2][2] == sign or ar[0][0] == ar[1][1] == ar[2][2] == sign or ar[0][2] == ar[1][1] == ar[2][0] == sign:
        return True
    else:
        return False


print('Welcome to the game Tic Tac Toe')

start = True
while start:
    ar = [["", "", ""], ["", "", ""], ["", "", ""]]
    table.field_names = ["Col\nRow", "0", "1", "2"]
    update_table(ar)

    num = 2
    go_on = True

    while go_on:

        if num % 2 == 0:
            print("Player1's turn (X)")
            sign = 'X'
            player = 1
        else:
            print("Player2's turn (O)")
            sign = 'O'
            player = 2
        row = int(input("Choose row number: "))
        col = int(input("Choose column number: "))
        if row < 3 and col < 3:
            if ar[row][col] == "":
                ar[row][col] = sign
                if num == 10:
                    update_table(ar)
                    print("Game over. Draw!")
                    go_on = False
                    start = to_continue()
                elif check_winner(sign):
                    update_table(ar)
                    print(f"Game over. The winner is Player{player}")
                    go_on = False
                    start = to_continue()

                num += 1
                update_table(ar)
        else:
            print("You selected the wrong cell. Try again.")






