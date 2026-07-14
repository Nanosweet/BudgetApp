class GradeService:
    def __init__(self, students):
        self.students = students
        
    @property
    def przedmioty(self):
        return [
            'matematyka',
            'fizyka',
            'historia',
            'jezyk_angielski'
        ]
        
    def get_avg_grade(self):
        srednia = []
        for oceny in self.students:
            suma = 0
            licznik = 0
            
            for p in self.przedmioty:
                if oceny[p] != "":
                    ocena = int(oceny[p])
                    suma += ocena
                    licznik +=1
                    
            srednia = suma / licznik if licznik > 0 else 0
            srednia.append((oceny['imie'], round(srednia, 1)))
            
        return srednia
    def get_empty_grade(self):
        empty = []
        for s in self.students:
            for p in self.przedmioty:
                if s[p] == "":
                    empty.append(s['imie'])
        return f"Oceny brakuje co najmniej {len(empty)} uczniom"
    
