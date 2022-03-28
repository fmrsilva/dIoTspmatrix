position = tuple[int, int]


def position_create(row: int, col: int) -> position:
    if not (type(row) is int and row >= 0) or not (type(col) is int and col >= 0):
        raise ValueError('position_create: invalid arguments')
    return row, col


def position_is(pos: position) -> bool:
    if not (type(pos) is tuple):
        return False
    return True


def position_row(pos: position) -> int:
    if not (type(pos) is tuple and pos[0] >= 0):
        raise ValueError('position_row: invalid arguments')
    return pos[0]


def position_col(pos: position) -> int:
    if not (type(pos) is tuple and pos[1] >= 0):
        raise ValueError('position_col: invalid arguments')
    return pos[1]


def position_equal(pos1: position, pos2: position) -> bool:
    if not (type(pos1) is tuple) or not (type(pos2) is tuple):
        raise ValueError('position_equal: invalid arguments')
    if (pos1[0] == pos2[0]) and (pos1[1] == pos2[1]):
        return True
    return False


def position_str(pos: position) -> str:
    if not (type(pos) is tuple):
        raise ValueError('position_str: invalid arguments')
    return"(" + str(pos[0]) + ", " + str(pos[1]) + ")"
