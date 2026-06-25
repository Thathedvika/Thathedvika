# Zbývající vstupy k doplnění zdroje (verze 3)

Krátký seznam toho, co ještě musí dodat autorka, aby model přestal stát na odhadech a stál plně na ověřených českých číslech. U každé položky je, kde se to hledá. Vstupy jsou v `harm_reduction_model.py` označené statusem `[DOPLNIT ZDROJ]`.

Jazyk: čeština. Pomlčky: krátké (-). URL na samostatném řádku.

---

## 1. Český per-case náklad léčby HCV (DAA kúra) - VYŘEŠENO ve verzi 4

- Proměnná v modelu: `NAKLAD_HCV_PRIPAD_*` (nyní 510-850 tis. Kč, střední 620 tis.).
- Zdroj doplněn: SÚKL, Seznam cen a úhrad (SCAU) k 1. 5. 2025 - úhrady DAA: Zepatier ~511 tis., Maviret ~524 tis., Epclusa ~650 tis., Vosevi ~844 tis. Kč/kúra.
https://www.sukl.cz/prumysl/leciva/ceny-a-uhrady/prehledy-cen-a-uhrad-leciv/

- Možné další upřesnění (volitelné): průměrný mix předepisovaných DAA u injekčních uživatelů (váží reálný průměrný náklad), z dat plátců/center.

---

## 2. Kalibrace kontrafaktuální roční incidence bez harm reduction (HIV a HCV)

- Proměnné v modelu: `INCIDENCE_HIV_*` (0,5-2 %/rok), `INCIDENCE_HCV_*` (5-15 %/rok).
- Co chybí: empiricky podložené rozpětí roční incidence, která by nastala, kdyby síť HR nefungovala. Teď je kalibrované řádově z ohnisek (Des Jarlais 2020), ne z přesných měr.
- Proč na tom záleží: tornado ukazuje, že tohle je vstup s největší pákou na ROI.
- Kde hledat:

Des Jarlais et al. 2020, Lancet HIV (ohniska mezi PWID, přesné prevalence/incidence po městech):
https://www.thelancet.com/journals/lanhiv/article/PIIS2352-3018(20)30082-5/abstract

EUDA / EMCDDA - drug-related infectious diseases (incidence HIV/HCV mezi PWID v EU):
https://www.euda.europa.eu/publications/european-drug-report/2023/drug-related-infectious-diseases_en

NMS bio-behaviorální studie séroprevalence HIV/HCV mezi PWID v ČR:
https://www.drogy-info.cz/

---

## 3. Drogově přiřaditelné výdaje represe (izolace) - VYŘEŠENO ve verzi 4

- Proměnná v modelu: `VYDAJE_REPRESE_DROGY_ROK` (nyní 1,16 mld. Kč).
- Zdroj doplněn: NMS Zaostřeno 6/2020 - Policie ČR vč. NPC ~1,16 mld. Kč (2019; 56 % integrovaného rozpočtu 2 071,6 mil. Kč).
https://www.drogy-info.cz/data/obj_files/33389/1077/Z6_2020.pdf

- Zbývající limit: jde o data za rok 2019; kategorie "Protidrogová politika" byla ve státním rozpočtu později zrušena, takže novější izolované číslo neexistuje. Pokud autorka chce aktuálnější odhad, lze ho jen rekonstruovat z dílčích rozpočtů (NPC + odhad drogové agendy policie/justice) a označit jako odhad.

---

## 4. (volitelné) Přesné prevalenční hodnoty měst u Des Jarlais 2020

- Co chybí: report uvádí ohniska kvalitativně (desítky až >1 000 nových HIV) a Atény jako vlajkový případ. Pokud chce autorka uvést konkrétní procentní skok prevalence (např. Atény, Bukurešť), je potřeba ho vzít přímo z primárního článku, ne z parafráze.
- Kde hledat:

Des Jarlais et al. 2020, Lancet HIV:
https://www.thelancet.com/journals/lanhiv/article/PIIS2352-3018(20)30082-5/abstract

---

## Co je naopak už dořešené (verze 3 a 4)

- Doživotní náklad HIV: odvozen z českých dat (VZP ~210 tis. Kč/pacient/rok x diskontovaná anuita), britské proxy nahrazeno. [R45]
- **Náklad HCV per případ: ověřen z úhrad SÚKL (SCAU 1. 5. 2025), 510-850 tis. Kč. [R47] (v4)**
- **Izolované drogově přiřaditelné výdaje represe: ~1,16 mld. Kč (Policie + NPC, 2019), Zaostřeno 6/2020. [R42] (v4)**
- Roční ROI přes incidenci a náklad na odvrácenou infekci: dopočítáno (skript).
- HCV: domodelováno (RR 0,26 z Platt Cochrane 2017).
- Bukurešťská citace: ověřena a opravena na přesný název (multiměstský článek). [R38]
- Parametrizovaný skript a tornado graf: dodáno (`harm_reduction_model.py`, `tornado.png`).

## Jediná zbývající otevřená mezera

Po verzi 4 zůstává jako jediný modelový vstup bez tvrdého zdroje **kalibrace kontrafaktuální incidence HIV/HCV bez harm reduction** (bod 2 výše) - má v tornadu největší páku na ROI. Vše ostatní je ozdrojováno.
