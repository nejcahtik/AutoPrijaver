# Program za avtomatsko prijavljanje na obštudijske dejavnosti UL

## Kako inštalirat

Če mi zaupaš, lahko zloudaš /dist mapo, v kateri se nahaja main.exe file, ki ga zaženeš. To bi mogl delat, če ne, mi piši

Če mi ne zaupaš, lahko zloudaš celo kodo, jo preveriš, da to ni virus, si na računalnik, če še nimaš, inštaliraš python, in potem s pythonom zaženeš main.py

## Kako program dela

Torej ko zalaufaš program te bo najprej uprašau, na kater termin za izbrano dejavnost bi se rd prjavu. Vneseš številko od 1 (za prijavo na prvi oz. najbl zgodn termin oz. termin k je lociran prvi v seznamu terminov na popru na spletni strani od te dejavnosti) do tolk kokr je terminov. Npr. za plezanje uneseš številko '1' za termin k je ob 19:30 in '2' za termin k je ob 21h.

Pol bo program probau dobit točn čas iz interneta, zato da preveri kok ti na kompu zaostaja ura in če ti dela internet povezava. V primeru, da bo uspešn, se bo na terminalu izpisal, kolk zaostaja tvoj čas u primerjavi z dobljenim časom iz serverja. Ponavad je ta številka med 0 in 2 sekundi. Preveri, če je ta številka možna (npr. da program ne izpiše, da ti ura zaostaja za 20 ur, čeprou zgleda točna). Če ni možna, probi še enkrat zalaufat program.

Pol se ti bo odpru browser na login spletni strani popr.uni-lj.si.
Ko se naloži spletna stran maš 3 minute časa, da se prijaviš v popr, klikneš na Search -> Events, greš na uno dejavnost, na katero se hočeš prjavt in klikneš nanjo, tko da se ti odpre spletna stran, na kateri se bo ob 6h zjutri pojavu modr gumb 'Book', na katerga se klikne za prijavo na dejavnost

Ko to nardiš, greš lahk spat. Program bo umes usake 5 min avtomatsko osvežiu spletno stran, zato da te ne odjavi (ta interval mejbi lah tud podalšam, ker ne vem po kolkem času te popr avtomatsko odjavi) in ob 2 sekunde čez 6h, če bo use šlo po planu,
bo avtomatsko refreshau stran, kliknu na gumb 'Book' in potrdiu prijavo, tko da ko se zbudiš boš že prjavlen.

Če ti na konzoli piše neke nepomembne errorje, jih ignoriri. Pojma nimam, kaj so te errorji, ampak men kljub temu use deluje.
Primer nepomembnga errorja:
[20296:18672:0202/223010.004:ERROR:interface_endpoint_client.cc(702)] Message 1 rejected by interface blink.mojom.WidgetHost

POMEMBNO!!!
- Naštimi si komp tko da se ti ne bo ugasnu ponoč oz. šou u sleep mode oz. izklopu interneta al pa kej podobnega.
- Kkšne dejavnosti (plezanje ni med njimi) majo tko, da po tem k klikneš na gumb 'Book', morš še odgovorit na neki uprašanj oz. izpolnt anketo, predn lah klikneš na 'Submit' za potrditeev prijave. U tem primeru program ne bo delau
