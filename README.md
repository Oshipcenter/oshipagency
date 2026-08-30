# Oship Agency — strona internetowa

Strona typu one-page dla Oship Agency (agencja social media / fotografii / videografii, Trojmiasto).

## Pliki

- index.html - gotowa strona do hostowania (Vercel / GitHub Pages). Zdjecia ladowane sa ze wzglednych sciezek (assets/...), wiec plik jest lekki.
- index_template.html - zrodlowy szablon strony, z placeholderami na zdjecia (__LOGO__, __AVATAR_DAWID__, __GALLERY_DATA__, __CLIENT_LOGOS__). To jest plik do edycji tresci/stylu.
- build.py - skrypt budujacy. python3 build.py generuje trzy warianty: pelny base64 index.html, lekki podglad oship-agency-strona-podglad-lite.html, oraz index-web.html (wersja ze wzglednymi sciezkami - ta wersja jest kopiowana jako index.html w tym repozytorium przy deployu).
- oship-agency-strona-podglad-lite.html - lekka wersja podgladowa bez galerii zdjec.
- assets/ - zdjecia i logo, wymagane przez index.html oraz przez build.py.

## Budowanie

python3 build.py

Do deployu na Vercel/GitHub Pages uzywany jest plik wygenerowany jako index-web.html, wgrany do repo pod nazwa index.html (razem z folderem assets/).
