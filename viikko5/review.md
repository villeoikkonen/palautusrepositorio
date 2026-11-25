# Mitä huomioita agentti teki koodistasi
↳ Explore finished · Review tennis refactor standards
Tarkastelin muutoksia komennolla git diff main...tennis_refactoring.
Löydökset
- [Pieni] viikko5/tennis/src/tennis_game.py:27, 39 — Tyhjillä riveillä on perässä välilyöntejä; git diff --check ilmoittaa niistä. Korjaus: poista rivien lopusta välilyönnit.
- [Pieni] viikko5/tennis/src/tennis_game.py:19 — Ehtojen and/or-järjestys tekee pistehaaran tarkoituksesta vaikeasti hahmotettavan. Tasatilanne on jo käsitelty aiemmin, joten pistemäärät ovat tässä haarassa eri; abs(...) >= 1 on siksi tarpeeton. Korjaus: selkeytä ehto esimerkiksi muotoon if self.p1_score >= 4 or self.p2_score >= 4:.
Testit menevät läpi (1 passed). En löytänyt haaran muutoksille määrittelyä, joten vaatimustenmukaisuutta ei voi arvioida. Käytettävissä ei myöskään ollut koodityyliohjeita.
Yhteenveto: 2 pientä löydöstä; testit läpäisevät.

# Olivatko ehdotetut muutokset hyviä
Kyllä. Tyhjät rivit olivat jääneet epähuomiossa ja tuo if/else/and/or/hell oli syntynyt järkyttyneessä mielentilassa ilman sen suurempia pitkän aikavälin suunnitelmia.

# Kuinka hyödylliseksi koit agentin tekemän katselmoinnin
Mielestäni se oli yllättävän hyvä. Odotin agentin tekeytyvän hyödylliseksi ja keksivän vähän sitä sun tätä kehitettävää ja ulostavan perinteisen wall of textin, mutta se antoikin ihan järkevää palautetta.

# Huomasiko agentti jotain, minkä olisit itse jättänyt huomaamatta? Entä jäikö siltä jotain oleellista huomaamatta?
Kyllä, nuo tyhjät välimerkit esim. oli jäänyt täysin huomaamatta. En myöskään olisi pushannut tuollaista ehtohelvettiä, jos aivot eivät olisi olleet aivan näin solmussa.

# Miltä agentin kommentit tuntuivat verrattuna siihen, että saman palautteen olisi antanut tiimikaveri? Mitä palautteen antamisessa kannattaa ottaa huomioon, kun katselmoijana on ihminen?
Agentti antanee melko teknistä palautetta, eikä oikeastaan antanut mitään palautetta itse refactoroinnista. Uskoisin että olisin saanut tiimikaverilta enemmän palautetta itse refactorista.
Palautteen antamisessa tulee pyrkiä antamaan sellaista palautetta, joka johtaa kehitykseen ja on psykologisesti turvallista, eli ettei siitä tule tarpeettoman paha mieli. Eli posin kautta liikkeelle.
