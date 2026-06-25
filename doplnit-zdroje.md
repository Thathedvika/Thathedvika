# Zbývající vstupy k doplnění zdroje (verze 3)

Krátký seznam toho, co ještě musí dodat autorka, aby model přestal stát na odhadech a stál plně na ověřených českých číslech. U každé položky je, kde se to hledá. Vstupy jsou v `harm_reduction_model.py` označené statusem `[DOPLNIT ZDROJ]`.

Jazyk: čeština. Pomlčky: krátké (-). URL na samostatném řádku.

---

## 1. Český per-case náklad léčby HCV (DAA kúra + následná péče)

- Proměnná v modelu: `NAKLAD_HCV_PRIPAD_*` (teď 300-875 tis. Kč, střední 600 tis.).
- Co chybí: přesný český náklad na jednu vyléčenou epizodu HCV moderními přímo působícími antivirotiky (DAA), po vyjednaných úhradách, ne list. cena.
- Proč na tom záleží: HCV táhne většinu odvrácených nákladů (objem 668 nových injekčních případů 2024), takže přesnost tohoto čísla nejvíc ovlivní ROI.
- Kde hledat:

SÚKL - ceny a úhrady léčiv (DAA):
https://sukl.gov.cz/prumysl/leciva/ceny-a-uhrady/prehledy-cen-a-uhrad-leciv/

VZP - náklady na léčbu virových hepatitid:
https://www.vzp.cz/o-nas/aktuality/klienty-vzp-trapi-chronicka-virova-hepatitida-jeji-lecba-stala-vloni-909-6-milionu

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

## 3. Drogově přiřaditelné výdaje represe (izolace od celého vězeňství)

- Proměnná v modelu: `VYDAJE_REPRESE_DROGY_ROK` (teď None).
- Co chybí: roční výdaje na drogovou represi = rozpočet Národní protidrogové centrály + drogová agenda policie (a justice), jako samostatné číslo, ne celý rozpočet vězeňství.
- Proč na tom záleží: argument asymetrie a oportunitního nákladu se má vztahovat k tomuto izolovanému číslu, ne k celým 13,35 mld. nebo k odvozeným 9,9 mld. (to je 74 % celku a většina těch lidí nesedí za drogový TČ).
- Pozn.: kategorie "Protidrogová politika" byla ve státním rozpočtu zrušena, takže nejnovější izolované číslo nemusí existovat - pak je nutné použít poslední dostupný rok a označit ho.
- Kde hledat:

NMS - Zaostřeno 6/2020, výdaje na protidrogovou politiku podle resortů vč. policie a NPC:
https://www.drogy-info.cz/data/obj_files/33389/1077/Z6_2020.pdf

Výroční zpráva Národní protidrogové centrály (rozpočet/náklady NPC):
https://policie.gov.cz/clanek/vyrocni-zprava-narodni-protidrogove-centraly-za-rok-2024.aspx

---

## 4. (volitelné) Přesné prevalenční hodnoty měst u Des Jarlais 2020

- Co chybí: report uvádí ohniska kvalitativně (desítky až >1 000 nových HIV) a Atény jako vlajkový případ. Pokud chce autorka uvést konkrétní procentní skok prevalence (např. Atény, Bukurešť), je potřeba ho vzít přímo z primárního článku, ne z parafráze.
- Kde hledat:

Des Jarlais et al. 2020, Lancet HIV:
https://www.thelancet.com/journals/lanhiv/article/PIIS2352-3018(20)30082-5/abstract

---

## Co je naopak už dořešené ve verzi 3

- Doživotní náklad HIV: nově odvozen z českých dat (VZP ~210 tis. Kč/pacient/rok x diskontovaná anuita), britské proxy nahrazeno. [R45]
- Roční ROI přes incidenci a náklad na odvrácenou infekci: dopočítáno (skript).
- HCV: domodelováno (RR 0,26 z Platt Cochrane 2017).
- Bukurešťská citace: ověřena a opravena na přesný název (multiměstský článek). [R38]
- Parametrizovaný skript a tornado graf: dodáno (`harm_reduction_model.py`, `tornado.png`).
