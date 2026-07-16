class SalesService:
    def __init__(self, data):
        self.data = data
        self._sellers = []
        self.extract_sellers()

    @property
    def sellers(self):
        return self._sellers

    @sellers.setter
    def sellers(self, value):
        self._sellers = value

    def extract_sellers(self):
        tmp_list = []
        for s in self.data:
            tmp_list.append(s["sprzedawca"])
        self.sellers = tmp_list
        return self.sellers

    def overall_earnings(self):
        wyniki = {}
        for p in self.data:
            sprzedawca = p["sprzedawca"]
            ilosc = int(p["ilosc"])
            cena = float(p["cena_jednostkowa"])
            przychod = ilosc * cena
            if sprzedawca not in wyniki:
                wyniki[sprzedawca] = 0
                wyniki[sprzedawca] += przychod
        return wyniki
