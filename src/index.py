from varasto import Varasto


def tulosta_getterit(olutta):
    print(
        "Olut getterit:\n",
        f"saldo = {olutta.saldo}\n",
        f"tilavuus = {olutta.tilavuus}\n",
        f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}\n",
        sep="",
    )


def muokkaa_mehua(mehua):
    print("Mehu setterit:\nLisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def tulosta_virheelliset_varastot():
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def tulosta_liian_suuri_lisays(mehua, olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def tulosta_virheellinen_otto(mehua, olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(
        f"saatiin {saatiin}",
        f"Olutvarasto: {olutta}",
        f"Mehuvarasto: {mehua}",
        "mehua.otaVarastosta(-32.9)",
        sep="",
    )
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def tulosta_virhetilanteet(mehua, olutta):
    print("Virhetilanteita:")
    tulosta_virheelliset_varastot()
    tulosta_liian_suuri_lisays(mehua, olutta)
    tulosta_virheellinen_otto(mehua, olutta)


def main():
    # very long comment that goes against pylint rules to check CI workflow, some words are still needed
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(
        "Luonnin jälkeen:\n",
        f"Mehuvarasto: {mehua}\n",
        f"Olutvarasto: {olutta}",
        sep="",
    )

    tulosta_getterit(olutta)
    muokkaa_mehua(mehua)
    tulosta_virhetilanteet(mehua, olutta)


if __name__ == "__main__":
    main()
