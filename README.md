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
"mycursor.execute"
