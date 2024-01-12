class IpariForradalom:
    def __init__(self, evszam, leiras, varos=None):
        self.evszam = evszam
        self.leiras = leiras
        self.varos = varos

    def bemutatkozas(self):
        print(f"Ipari Forradalom ({self.evszam}-től)")
        print(self.leiras)
        if self.varos:
            print(f"Az ipari forradalom egyik központja volt {self.varos}.")
            print(f"További információk: [Wikipédia {self.varos}](https://hu.wikipedia.org/wiki/{self.varos})")
        print()

# Ipari forradalom Birminghammal
ipari_forradalom_birmingham = IpariForradalom(1760, "Az ipari forradalom az ipari termelés és gyártás átalakulását jelentette, a kézi munka helyett gépek és ipari folyamatok bevezetését.", "Birmingham")
