# get-apartments-data-bot

Projekt ma na celu automatyczne pobieranie informacji o dostępnych mieszaniach do wynajęcia z witryny Apartments.com oraz wprowadzanie tych informacji do formularza Google.


## Web Scraping z Apartments.com:

- Skrypt rozpoczyna od wywołania zapytania HTTP do strony Apartments.com, aby pobrać listę dostępnych mieszkań do wynajęcia w określonym obszarze (San Francisco, CA).
- Wykorzystuje bibliotekę `requests` do pobrania zawartości strony internetowej.
- Następnie używa biblioteki `BeautifulSoup` do analizy kodu źródłowego strony i wyizolowania informacji o cenach mieszkań, adresach oraz linkach do ogłoszeń.

## Nawigacja i Zbieranie Danych:

- Skrypt używa biblioteki `Selenium`, aby nawigować po stronach z wynikami i zbierać informacje z wielu stron.
- Po zebraniu danych z jednej strony, przechodzi do kolejnej strony, klikając przycisk "Next", aż wszystkie dostępne strony zostaną przeszukane.

## Wprowadzanie Danych do Formularza Google:

- Po zebraniu informacji o cenach, adresach i linkach do ogłoszeń, skrypt przechodzi do kolejnej części, która polega na wprowadzaniu tych danych do formularza Google.
- Używa biblioteki `Selenium`, aby automatycznie wypełniać pola formularza danymi, takimi jak adres mieszkania, cena i link do ogłoszenia.
- Następnie kliknie przycisk "Submit", aby przesłać dane do formularza Google.

## Konfigurowalność:

- Skrypt jest dostosowywalny i może być używany do przeszukiwania innych lokalizacji lub dostosowania formularza Google do różnych celów.
