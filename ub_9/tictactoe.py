from wypp import *

# Ein Spieler wird entweder durch ein 'x' oder ein 'o' repraesentiert.
Player = Literal["x", "o"]

# Eine Markierung ist entweder das Zeichen eines Spielers oder ein freies Feld '-'
Mark = Literal["x", "o", "-"]

# Game stellt das Spielfeld dar und enthaelt eine Liste an Reihen, die Listen von Marks sind
Game = list[list[Mark]]


# --- Aufgabe 1 ---
# Prüft ob alle Felder des Spiels gefüllt sind.
# Eingang: Game
# Ausgang: Sind alle befuellt?
def gameFull(game: Game) -> bool:
    return not any(any(item == "-" for item in row) for row in game)


check(gameFull([["x", "x", "x"], ["o", "x", "o"], ["o", "x", "x"]]), True)
check(gameFull([["x", "x", "x"], ["x", "x", "x"], ["x", "x", "-"]]), False)

# --- Aufgabe 2 ---
xWinHorizontal = [["x", "x", "x"], ["-", "-", "-"], ["-", "-", "-"]]
xWinVertical = [["x", "-", "-"], ["x", "-", "-"], ["x", "-", "-"]]
xWinDiagonal1 = [["x", "-", "-"], ["-", "x", "-"], ["-", "-", "x"]]
xWinDiagonal2 = [["-", "-", "x"], ["-", "x", "-"], ["x", "-", "-"]]
noneWin = [["x", "-", "-"], ["-", "o", "-"], ["-", "-", "x"]]

# Prueft ob Spieler alle in einer Reihe hat
# Eingang: Game, Player
# Ausgang: Hat gewonnwn?
def isHorizontalWin(game: Game, player: Player) -> bool:
    return any(not any(item != player for item in row) for row in game)


check(isHorizontalWin(xWinHorizontal, "x"), True)
check(isHorizontalWin(noneWin, "x"), False)

# Prueft ob Spieler alle in einer Spalte hat
# Eingang: Game, Player
# Ausgang: Hat gewonnen?
def isVerticalWin(game: Game, player: Player) -> bool:
    return any(
        not any(game[y][x] != player for y in range(len(game)))
        for x in range(len(game[0]))
    )


check(isVerticalWin(xWinVertical, "x"), True)
check(isVerticalWin(noneWin, "x"), False)


# Prueft ob Spieler alle in einer der Diagonalen hat
# Eingang: Game, Player
# Ausgang: Hat gewonnen?
def isDiagonalWin(game: Game, player: Player) -> bool:
    return (not any(game[i][i] != player for i in range(len(game)))) or (
        not any(game[i][len(game) - 1 - i] != player for i in range(len(game)))
    )


check(isDiagonalWin(xWinDiagonal1, "x"), True)
check(isDiagonalWin(xWinDiagonal2, "x"), True)
check(isDiagonalWin(noneWin, "x"), False)

# Prueft, ob uebergebener Spieler gewonnen hat
# Eingang: Game
# Ausgang: Hat Spieler gewonnen
def checkIfWin(game: Game, player: Player) -> bool:
    return (
        isHorizontalWin(game, player)
        or isVerticalWin(game, player)
        or isDiagonalWin(game, player)
    )


check(checkIfWin(xWinHorizontal, "x"), True)
check(checkIfWin(xWinVertical, "x"), True)
check(checkIfWin(xWinDiagonal1, "x"), True)
check(checkIfWin(xWinHorizontal, "o"), False)
check(checkIfWin([["x", "-", "-"], ["x", "-", "-"], ["-", "-", "-"]], "x"), False)


# Prueft ob das Spiel einen Gewinner hat und gibt diesen ggf. zurück.
# Eingang: Game
# Ausgang: Spieler, der gewonnen hat oder None
def checkWinner(game: Game) -> Optional[Player]:
    return "x" if checkIfWin(game, "x") else ("o" if checkIfWin(game, "o") else None)


check(checkWinner(xWinHorizontal), "x")
check(checkWinner(xWinVertical), "x")
check(checkWinner(xWinDiagonal1), "x")
check(checkWinner([["o", "-", "-"], ["o", "-", "-"], ["o", "-", "-"]]), "o")
check(checkWinner([["x", "-", "-"], ["x", "-", "-"], ["-", "-", "-"]]), None)

# -- Aufgabe 3 --
# Bricht das Programm mit einer Fehlermeldung ab.
# Eingang: Nachricht: str
# Ausgang: None
def error(msg: str) -> None:
    raise Exception(msg)


# Platziert die Markierung eines Spielers auf dem Spielfeld.
# Eingang: Game, i: int, j: int, Player
# Ausgang: None
# SEITENEFFEKT: veraendert game
def placePlayer(game: Game, i: int, j: int, player: Player) -> None:
    if i > 2 or j > 2 or game[i][j] != "-":
        error("Forbidden game operation")
    game[i][j] = player


game1 = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
placePlayer(game1, 0, 0, "x")
check(game1[0][0], "x")
placePlayer(game1, 2, 2, "o")
check(game1[2][2], "o")

# --- Aufgabe 4 ---
# Berechnet die String-Darstellung eines Spiels
# Eingang: Game
# Ausgang: Darstellung als String: str
def gameToString(game: Game) -> str:
    return "| " + " |\n| ".join([" | ".join(row) for row in game]) + " |"


check(
    gameToString([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]),
    "| - | - | - |\n| - | - | - |\n| - | - | - |",
)

check(
    gameToString(game1),
    "| x | - | - |\n| - | - | - |\n| - | - | o |",
)

# --- Aufgabe 5 ---
# Liest von der Konsole den Zug eines Spielers.
# Eingang: Player
# Ausgang: Userinput i,j: tuple[int, int]
def getMove(player: Player) -> tuple[int, int]:
    move = input(f"  Eingabe Spieler {player} in der Form Zeile,Spalte: ").split(",")
    return (int(move[0]), int(move[1]))


# --- Aufgabe 6 ---
# Fuehrt einen Halbzug durch.
# Eingang: Game, Player
# Ausgang: Ist Spiel zuende: bool
def halfMove(game: Game, player: Player) -> bool:
    print(gameToString(game))
    move = getMove(player)
    placePlayer(game, move[0], move[1], player)
    winner = checkWinner(game)
    if winner != None:
        print(f"Gewinner: {winner}")
        return True
    if gameFull(game):
        print("Spielende. Unentschieden.")
        return True
    return False


# Fuerht einen Spielzug aus
# Eingang: Game
# Ausgang: Ist Spiel zuende?: bool
def move(game: Game) -> bool:
    return halfMove(game, "x") or halfMove(game, "o")


# --- Aufgabe 7 ---
# Spielt ein komplettes Spiel durch
# Eingang: None
# Ausgang: None
def fullGame() -> None:
    game = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    for i in range(5):
        print(f"Zug {i+1}")
        if move(game):
            break
