System zgloszen fundacji zobaczycmorze.

Rekomenduje utworzenie sobie wirtualnego srodowiska pythona 
python -m venv venv 
Aby uruchomic platforme nalezy wykonac ponizsze kroki w folderze projektu:

python manage.py migrate
python manage.py createsuperuser
postepowac wedlug monitow - podac login email password, kiedy haslo jest za krotkie potwierdzic mimo to.
python manage.py runserver
uruchomic przegladarke i w polu adresu wpisac:
localhost:8000
zobaczymy pusta strone bez rejsow. 
do panelu admina mozna przejsc wpisujac adres:
localhost:8000/admin
zalogowac sie kontem utworzonym przez createsuperuser.
panel administracyjny powinien byc prosty i intuicyjny, jezeli nie jest prosze o zgloszenie.
