from project import check_win

def main():
    test_check_win1()
    test_check_win2()
    test_check_win3()


def test_check_win1():
    board = ["test", "+", "+", "+", " ", " ", " ", " ", " ", " "]
    assert check_win("+",board) == True
    board = ["test", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    assert check_win("+",board) == False

def test_check_win2():
    board = ["test", "O", "O", "O", " ", " ", " ", " ", " ", " "]
    assert check_win("O",board) == True
    board = ["test", "O", " ", " ", " ", " ", " ", " ", " ", "O"]
    assert check_win("O",board) == False

def test_check_win3():
    board = ["test", " ", " ", " ", "O", "O", "O", " ", " ", " "]
    assert check_win("O",board) == True
    board = ["test", "O", " ", " ", " ", " ", " ", " ", " ", "O"]
    assert check_win("+",board) == False

if __name__ == "__main__":
    main()
