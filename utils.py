from datetime import datetime

def waliduj_wiersz(row):
    try:
        datetime.strptime(row['data'], '%Y-%m-%d')
        float(row['kwota'])
        assert row['typ'] in ['wydatek', 'przychod']
        return True
    except (ValueError, AssertionError, KeyError):
        return False
        # datetime.strptime(row['data'], '%Y-%m-%d').strftime('%d-%m-%Y')
    #print(row)
    #print(float(row['kwota']))
    

    
    #print (datetime.strptime(wiersz['data'], '%Y-%m-%d').date())
    #for klucz in enumerate( wiersz.keys()):
       # print(klucz)



#FORMATY_DATY = ['%Y-%m-%d', '%d-%m-%Y', '%d.%m.%Y', '%m/%d/%Y']

#DATY = ['05/01/2024','2024/07/01','10/01/2024','15/01/2024','31/01/2024']

#for format in FORMATY_DATY:
   # try:
   #     print (datetime.strptime(wiersz['data'], format))
  #  except ValueError:
  #      raise ValueError(f'Nieznany format daty')

#data = waliduj_wiersz()
#print(data.strftime('%d-%m-%Y'))
    
    #print(wiersz["data"])
    #print(datetime.strptime(wiersz['data'], '%Y-%m-%d'))
    #try:
        #print(datetime.strptime(wiersz['data'], '%Y-%m-%d').date())
        #if (datetime.strptime(wiersz['data'], '%Y-%m-%d').date()):
            #datetime.strptime('%d:%m:%Y')
            #data = datetime.strptime('2024-05-01', '%Y-%m-%d')
            #print(data.strftime('%d-%m-%Y'))
       # data = datetime.strptime(wiersz['data'], '%Y-%m-%d')
       # print(data.strftime('%d/%m/%Y'))
# → 01-05-2024
    #except ValueError:
      #  print("Zły format daty")