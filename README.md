# OppdragMusikk
Oppdrag om Databaser i python
i dette oppdraget skulle vi lage en database som har 2 tables, en med id or artister og den andre med id, sanger, og artisten til sangen
denne python kode skulle ha muligheten til å la brukeren skrive inn sanger or artisten og få den inni databasen

step 1 - lage bruker og database
startet med å lage en ny bruker og lage selve databasen, dette var ganske lett

step 2 - connecte til brukeren og gå inni databasen
lage tabellen innafor databasen

<img width="552" height="291" alt="image" src="https://github.com/user-attachments/assets/e813d4e8-cdcc-4939-846d-70c5a70ee2ba" />

på starten av koden bruker jeg "mysql.connector.connect" for å connecte til brukeren som jeg lagde på rasbarry pien
inni her har jeg host, som er ip adressen til pi-en, user, som en navn på brukeren, password, som er passwordet til brukeren og database, dette er databasen jeg er inni og jobber med

step 3 - lage tabell innafor databasen

<img width="700" height="536" alt="image" src="https://github.com/user-attachments/assets/f1ccdf1b-d047-4e5d-ae42-27924ae8da7a" />

"mycursor.execute" er brukt for å gjøre kommandoer innafor python, med dette lagde jeg denne Artister tabelen, denne trenger jeg fordi
jeg skal lage en Sanger tabell med en refrence inni Artister

<img width="732" height="286" alt="image" src="https://github.com/user-attachments/assets/850554d1-3989-4702-85c2-ed4e81e8544a" />

etter jeg lagde denne tabellen var jeg ferdig med dette og jeg må få till input

Step 4 - Input And Meny

her skal jeg lage en meny hvor du kan selecte hva du skal gjøre, og at jeg skjer

<img width="1109" height="972" alt="image" src="https://github.com/user-attachments/assets/314d1049-0300-4132-9cba-4f291fe9b5ef" />

def meny(); er brukt for å håndtere valg av commandor også har jeg def addsong(); og addart(); som logiken bak å lage en ny sang og en ny artist innafor de to tabellene




