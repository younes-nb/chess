class PieceCopy:
    def __init__(self, pieces, x, y):
        super().__init__()
        self.pieces = pieces
        self.position = [x, y]
        self.team = None
        self.type = None
        self.selected = False
        self.is_painted = False
        self.target = False
        self.checker = False


class KingCopy(PieceCopy):
    def __init__(self, pieces, x, y, team):
        super().__init__(pieces, x, y)
        self.team = team
        self.is_checked = False
        self.is_check_mate = False
        match self.team:
            case "White":
                self.type = "WKing"
            case "Black":
                self.type = "BKing"

    def all_moves(self):
        moves = []
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            x = self.position[0] + dx
            y = self.position[1] + dy
            if x not in range(8) or y not in range(8):
                continue
            if self.pieces[x][y].team == self.team:
                continue
            moves.append((x, y))

        return moves


class QueenCopy(PieceCopy):
    def __init__(self, pieces, x, y, team):
        super().__init__(pieces, x, y)
        self.team = team
        match self.team:
            case "White":
                self.type = "WQueen"
            case "Black":
                self.type = "BQueen"

    def all_moves(self):
        moves = []
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            for i in range(1, 8):
                x = self.position[0] + (dx * i)
                y = self.position[1] + (dy * i)
                if x not in range(8) or y not in range(8):
                    continue
                if self.pieces[x][y].team == self.team:
                    break
                moves.append((x, y))
                if self.pieces[x][y].type != "Blank":
                    break

        return moves


class BishopCopy(PieceCopy):
    def __init__(self, pieces, x, y, team):
        super().__init__(pieces, x, y)
        self.team = team
        match self.team:
            case "White":
                self.type = "WBishop"
            case "Black":
                self.type = "BBishop"

    def all_moves(self):
        moves = []
        for (dx, dy) in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            for i in range(1, 8):
                x = self.position[0] + (dx * i)
                y = self.position[1] + (dy * i)
                if x not in range(8) or y not in range(8):
                    continue
                if self.pieces[x][y].team == self.team:
                    break
                moves.append((x, y))
                if self.pieces[x][y].type != "Blank":
                    break

        return moves


class KnightCopy(PieceCopy):
    def __init__(self, pieces, x, y, team):
        super().__init__(pieces, x, y)
        self.team = team
        match self.team:
            case "White":
                self.type = "WKnight"
            case "Black":
                self.type = "BKnight"

    def all_moves(self):
        moves = []
        for (dx, dy) in ((2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
            x = self.position[0] + dx
            y = self.position[1] + dy
            if x not in range(8) or y not in range(8):
                continue
            if self.pieces[x][y].team == self.team:
                continue
            moves.append((x, y))

        return moves


class RookCopy(PieceCopy):
    def __init__(self, pieces, x, y, team):
        super().__init__(pieces, x, y)
        self.team = team
        match self.team:
            case "White":
                self.type = "WRook"
            case "Black":
                self.type = "BRook"

    def all_moves(self):
        moves = []
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            for i in range(1, 8):
                x = self.position[0] + (dx * i)
                y = self.position[1] + (dy * i)
                if x not in range(8) or y not in range(8):
                    continue
                if self.pieces[x][y].team == self.team:
                    break
                moves.append((x, y))
                if self.pieces[x][y].type != "Blank":
                    break

        return moves


class PawnCopy(PieceCopy):
    def __init__(self, pieces, x, y, team):
        super().__init__(pieces, x, y)
        self.team = team
        match self.team:
            case "White":
                self.type = "WPawn"
            case "Black":
                self.type = "BPawn"

    def all_moves(self):
        moves = []
        x = None
        y = self.position[1]
        match self.team:
            case "White":
                x = self.position[0] - 1
                if self.position[0] == 6:
                    if self.pieces[x][y].team == "None" and self.pieces[x - 1][y].team == "None":
                        moves.append((x - 1, y))
            case "Black":
                x = self.position[0] + 1
                if self.position[0] == 1:
                    if self.pieces[x][y].team == "None" and self.pieces[x + 1][y].team == "None":
                        moves.append((x + 1, y))

        for dy in (-1, 0, 1):
            y = self.position[1] + dy
            if x not in range(8) or y not in range(8):
                continue
            if dy != 0:
                if self.pieces[x][y].team != self.team and self.pieces[x][y].team != "None":
                    moves.append((x, y))
                else:
                    continue
            if self.pieces[x][y].team == "None":
                moves.append((x, y))

        return moves


class BlankCopy(PieceCopy):
    def __init__(self, pieces, x, y):
        super().__init__(pieces, x, y)
        self.team = "None"
        self.type = "Blank"
