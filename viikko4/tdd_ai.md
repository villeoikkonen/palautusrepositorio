## Päätyikö agentti hyvään toteutukseen ja laadukkaisiin testeihin?
Aivan ensimmäisenä Agentti47 lähti seikkailulle ja kosketteli epäsopivilla tavoilla useita tiedostoja. Kun Agentin käytöstä korjattiin täsmällisemmällä promptilla englanniksi, alkoi käytös olemaan vähemmän rangaistavaa.
Testien nimet mielestäni eivät ole parhaat mahdolliset, mutta kuitenkin ymmärrettävää clankeria.

## Pysyikö agentti osassa A minimitoteutuksessa, ja jättikö se testit rauhaan?
Yst. kts. kohta 1.
Agentin käytöksen sain kuriin muotoilemalla promptin seuraavalla tavalla, joka johti toivottuun käytökseen:
Follow TDD protocol. I have added a test that doesn't pass. Develop ostoskori.py so the tests pass. Make only minimal changes to code so my tests pass. NOTHING ELSE.

## Yrittikö agentti missään vaiheessa “huijata”, esim. kovakoodaamalla testin odottaman arvon?
Aluksi tosiaan Herra47 lähti pyhiinvaellukselle ja rakensi kertalaakista vähän sitä sun tätä. Onneksi opencodessa on komento /mistätäältäpääseepois, eikun /undo, jolla pääsi aloittamaan alusta ilman gitin kautta koko repositorion palautusta.
Varsinaista kovakoodaamista ei kuitenkaan ollut havaittavissa.

## Kumpi työnjako, A vai B, tuntui paremmalta, ja miksi?
Muutin työnjakoon B promptia vain hieman, koska aiempi prompti lopulta toimi erittäin hyvin. Kohdan B prompti oli:

Follow TDD protocol. First make unit tests for the feature and then develop ostoskori.py so the tests pass. Make only minimal changes to code so my tests pass. NOTHING ELSE.

The feature I want: "Kahden saman tuotteen lisäämisen jälkeen ostoskori sisältää tasan yhden ostoksen"

Jälkikäteen koodia tarkastellessa A on piirun verran selkeämpää ja ymmärrettävämpää, koska testien nimet ovat ihmismäisemmät, mutta lopputulos oli molemmilla tavoilla yhtenevä muutoin.
