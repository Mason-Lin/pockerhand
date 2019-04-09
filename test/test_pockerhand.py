import pytest
from src import pockerhand


class TestPockerHand(object):
    def test_1(self, capsys):
        p1 = pockerhand.Player('Mason', 'S1, S3, S5, S7, S8')
        p2 = pockerhand.Player('Rina', 'H1, H3, D5, D7, C9')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Mason win: Flush'

    def test_2(self, capsys):
        p1 = pockerhand.Player('Mason', 'H1, H3, D5, D7, C9')
        p2 = pockerhand.Player('Rina', 'S1, S3, S5, S7, S8')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Rina win: Flush'

    def test_3(self, capsys):
        p1 = pockerhand.Player('Mason', 'S1, S3, S5, S7, S8')
        p2 = pockerhand.Player('Rina', 'S1, S3, S5, S7, S8')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'draw Flush Flush'

    def test_4(self, capsys):
        p1 = pockerhand.Player('Mason', 'H1, H3, D5, D7, C9')
        p2 = pockerhand.Player('Rina', 'H1, H3, D5, D7, C9')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'draw High card High card'

    def test_5(self, capsys):
        p1 = pockerhand.Player('Mason', 'H1, H3, D5, D7, C9')
        p2 = pockerhand.Player('Rina', 'H3, H3, D5, D7, C9')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Rina win: One Pair'

    def test_6(self, capsys):
        p1 = pockerhand.Player('Mason', 'H1, H3, D5, D7, C9')
        p2 = pockerhand.Player('Rina', 'H3, H3, D5, D5, C9')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Rina win: Two Pairs'

    def test_7(self, capsys):
        p1 = pockerhand.Player('Mason', 'H1, H3, D5, D7, C9')
        p2 = pockerhand.Player('Rina', 'H3, H3, D3, D5, C9')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Rina win: Three of a kind'

    def test_8(self, capsys):
        p1 = pockerhand.Player('Mason', 'H1, D1, S1, C1, C9')
        p2 = pockerhand.Player('Rina', 'H1, H3, D5, D7, C9')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Mason win: Four of a Kind'

    def test_9(self, capsys):
        p1 = pockerhand.Player('Mason', 'H1, H3, D5, D7, C9')
        p2 = pockerhand.Player('Rina', 'H3, H3, D3, D5, C5')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Rina win: Full house'

    def test_10(self, capsys):
        p1 = pockerhand.Player('Mason', 'S1, S3, S5, S7, S8')
        p2 = pockerhand.Player('Rina', 'H3, H3, D3, D5, C5')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Rina win: Full house'

    def test_11(self, capsys):
        p1 = pockerhand.Player('Mason', 'S2, D3, D4, C5, C6')
        p2 = pockerhand.Player('Rina', 'H3, H3, D3, D5, C9')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Mason win: Straight'

    def test_12(self, capsys):
        p1 = pockerhand.Player('Mason', 'S2, S3, S4, S5, S6')
        p2 = pockerhand.Player('Rina', 'H3, H3, D3, D5, C9')
        game = pockerhand.Game(p1, p2)
        game.play()

        captured = capsys.readouterr()
        assert captured.out.strip() == 'Mason win: Straight Flush'
