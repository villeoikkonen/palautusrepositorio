import unittest
from unittest.mock import ANY, Mock

from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        self.tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipä", 3),
        }
        self.saldot = {1: 10, 2: 5}
        self.varasto_mock.saldo.side_effect = lambda tuote_id: self.saldot.get(tuote_id, 0)
        self.varasto_mock.hae_tuote.side_effect = self.tuotteet.get

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", ANY, 5
        )

    def test_maksettaessa_kaksi_eri_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", ANY, 8
        )

    def test_maksettaessa_kaksi_samaa_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", ANY, 10
        )

    def test_maksettaessa_tuote_loppu_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.saldot[2] = 0

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", ANY, 5
        )
