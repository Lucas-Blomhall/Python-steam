# HEMTENTAN

## LÄS DETTA FÖRST

**DENNA TENTA ÄR INDIVIDUELL - Att kopiera eller dela sin lösning behandlas som fusk och kan leda till avstängning**

**Deadline**: 60 minuter innan din individuella tid du tilldelats via email ska din kod vara pushad till github

**Komplettering 1 Deadline**: 2023/11/3 23:59

**Komplettering 1 Deadline**: 2023/11/10 23:59


**Betyg**: U, G, VG

- För att få **G** så ska du visa god förståelse för koden du skrivit, du ska helst ha implementerat samtliga metoder för G-nivå och kunna svara på diverse frågor om grundläggande python. Du kan bli godkänd trots att du ej implementerat samtliga metoder om du visar på god förståelse för det du lyckats avklara.

- För att få **VG** ska du ha gjort klart samtliga metoder för G och VG-nivå, du kommer inte kunna få högsta betyget om något har lämnats oavklarat. Du ska dessutom kunna visa på djupare förståelse för objektorienterad programmering och kunna svara mer detaljerat på de frågor jag ställer. Du ska visa på problemlösningsförmåga vid eventuella uppdagade fel / buggar, dvs. felsökning.

## Inlämning

- Pusha till github senast 60 minuter innan din utsatta tid
- Ta bort alla onödiga filer, filen som redovisas ska heta main.py och din kod bör vara på den huvudsakliga branchen "main" eller "master".
- Se till att du körde git clone på din EGEN repository för hemtentan.
- Feedback ges muntligt och inte skriftligt

# Beskrivning:

Likt tidigare labbar har du fått en specifikation med kod. Du ska färdigställa metoderna, helst utifrån den rekommenderade ordning de är numrerade med (syns som en grön kommentar i varje metod). Datan är verklig och är tagen från en världens största digitala affär och plattform för tv-spel (Steam store). Du ska skapa en enklare applikation som låter en användare begära ut information.

Denna hemtenta tvingar dig till att använda två klasser som på ett logiskt sätt ska samspela. Din databas-klass kommer stå för vissa mer generella operationer, medan din Menu-klass ska implementera presentationslogiken (input, print, menyn som ger användaren val) och det mer specifika kopplat till just denna applikation. Båda klasserna ska använda sig av errorhantering, men det är primärt din Menu-klass som faktiskt ska utnyttja errors för att utföra handlingar. 

- Försök först förstå helheten genom att läsa beskrivningarna för båda klasserna, följt av deras enskilda metoder. Kom ihåg att vissa metoder endast krävs för VG.
- Utgå från numreringen jag satt
- Databas-klassen kommer ofta använda sig av "raise"-keywordet när du gör try-except, du hanterar sedan detta i din Menu-klass
- Genom att separera dessa två klasser gör vi Databas-klassen mer återanvändbar - fundera på varför!