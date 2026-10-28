import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_setup_haarat(self):
        varasto = Varasto(-1, -1)
        self.assertEqual(varasto.tilavuus, 0)
        self.assertEqual(varasto.saldo, 0)

        varasto = Varasto(5, 10)
        self.assertEqual(varasto.saldo, varasto.tilavuus)

    def test_lisaa_varastoon_haarat(self):
        original = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, original)

        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_haarat(self):
        varasto = Varasto(10, 10)
        self.assertEqual(varasto.ota_varastosta(-5), 0)
        self.assertEqual(varasto.ota_varastosta(15), 10)

    def test_str_palautus(self):
        correct = "saldo = 0, vielä tilaa 10"
        self.assertEqual(correct, str(self.varasto))

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
