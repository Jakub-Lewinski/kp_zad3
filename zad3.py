import argparse

MONTHS = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
DAYS = ["pn", "wt", "sr", "czw", "pt", "sob", "nd"]


def reformat_zakresy(zakres):   #jeśli element zakresu not in days to .index rzuca wyjątek
  zakresy = zakres.split('-')
  start = DAYS.index(zakresy[0])
  end = DAYS.index(zakresy[-1])
  return DAYS[start : end + 1]


def create_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('--miesiąc', type=str, default=['styczeń'], nargs='+', choices=MONTHS, dest='months',
                      help='usage: --miesiąc styczeń luty kwiecień      domyślnie: styczeń')
  parser.add_argument('--zakresy', type=reformat_zakresy, nargs='+',
                      help='usage: --zakresy pn-pt wt     liczba zakresów = liczbie miesięcy')
  parser.add_argument('--pory', nargs='*', default=[], choices=['r', 'w'],
                      help='usage: --pory r r w     liczba pór = liczbie dni; r (rano) lub w (wieczorem)')
  parser.add_argument('-t', '--create_file', action='store_true',
                      help='usage: -t     tworzy pliki (bez tej flagi pliki są odczytywane)')
  fmt = parser.add_mutually_exclusive_group()
  fmt.add_argument('-c', '--csv', dest='format', action='store_const', const='csv',
                   help='format CSV (domyślny)')
  fmt.add_argument('-j', '--json', dest='format', action='store_const', const='json',
                   help='format JSON')
  parser.set_defaults(format='csv')
  return parser


def main():
  parser = create_parser()
  args = parser.parse_args()

  print(args)





if __name__ == '__main__':
  main()