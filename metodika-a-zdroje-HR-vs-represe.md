# Metodika a zdroje: datový rozbor harm reduction vs. represe v ČR

Doprovodný dokument k souboru `harm-reduction-vs-represe-CR.md`. Vysvětluje, jak jsem postupoval, proč jsem volil daný postup, a uvádí úplný soupis všech zdrojů, se kterými jsem pracoval - rozdělený podle toho, jak silně jsou ověřené.

Konvence (převzato ze zadání): čeština s plnou diakritikou, pouze krátké pomlčky (-), plné URL na samostatném řádku.

---

## Část A: Jak jsem postupoval a proč

### A.1 Cíl a rámcování

Cílem bylo kvantitativně podložit tezi, že přístup orientovaný na snižování rizik (harm reduction) a léčbu je v ČR výhodnější než represivní alokace veřejných prostředků. Od začátku jsem pracoval s tím, že **oficiální český výpočet poměru "HR je X-krát levnější než represe" neexistuje** - jde o vlastní syntézu českých vstupů a mezinárodních effect sizes, ne o oficiální číslo. Národní strategie 2019-2027 takovou cost-effectiveness analýzu teprve ukládá jako budoucí úkol.

### A.2 Třístupňový postup

**Krok 1 - hloubková rešerše literatury (effect sizes a nákladová efektivita).**
Nejdřív jsem napříč vědeckými databázemi (PubMed, Cochrane, OpenAlex, doplňkově web) vyhledal recenzované meta-analýzy a nákladové studie, které dávají *účinnost* a *nákladovou efektivitu* harm reduction. Z nich pochází jádro mezinárodní evidence (MacArthur 2012, Aspinall 2014, Platt Cochrane 2017, Bernard 2017 atd.). Tato čísla jsou **zahraniční** a jako zahraniční je v reportu označuji.

**Krok 2 - ověření českých dat z primárních PDF.**
Klíčová česká čísla za rok 2024 jsem nebral ze sekundárních zdrojů, ale stáhl jsem si primární PDF a hledal v nich konkrétní hodnoty přímo. Fyzicky jsem otevřel a prohledal tyto dokumenty (uloženy jako textový extrakt v pracovním adresáři):

- Souhrnná zpráva o závislostech v ČR 2025 / Souhrn zprávy o nelegálních drogách 2025 (data za rok 2024) - NMS
- Výroční zpráva Národní protidrogové centrály 2024 - NPC
- Výroční zpráva Vězeňské služby ČR za rok 2024 - VS ČR

Z těchto tří zdrojů pochází všechny údaje značené v reportu symbolem **✔** (269 nových HIV / 6 injekčně, 218 odvrácených předávkování naloxonem, rozpočet vězeňství 13,35 mld. Kč, 19 430 vězněných, 14 402 drogově závislých ve věznicích, výdaje VZP 527 mil. Kč na nelegální drogy atd.).

**Krok 3 - kalkulace s explicitními předpoklady.**
Teprve nad ověřenými vstupy jsem postavil modelové výpočty (sekce 5 reportu). Ty jsou transparentně označené jako **ilustrativní scénáře**, ne jako přesná oficiální čísla - největší nejistota je na straně kontrafaktuálu (co by se stalo bez harm reduction).

### A.3 Proč zrovna takhle

- **Oddělení ověřeného od modelovaného.** Symbol ✔ odlišuje primárně ověřená data od scénářů. Bez tohohle se snadno smíchá fakt s odhadem.
- **Dva rámce rozpočtu, ne jeden.** Rozlišuji "rozpočet adiktologických služeb" (frame B, bez policie/justice/věznic) od "integrovaného rozpočtu včetně represe" (frame A). Záměna těchto dvou je nejčastější chyba v téhle debatě - ve frame B harm reduction a léčba dominují, ale ve frame A pohlcuje represe ~52 %.
- **Rozpětí, ne jedno marketingové číslo.** Často citované "7 USD ušetřeno na 1 USD" nemá jeden primární zdroj; uvádím proto rozpětí (ROI 2 až 27x) podle toho, co se do kalkulace započítá.
- **Náklad na vězně jako hrubý dopočet.** VS ČR nezveřejňuje samostatný nákladový per-diem za 2024, proto počítám rozpočet (13,35 mld.) deleno stav vězňů (19 430) = ~687 tis. Kč/rok. Označuji to jako hrubý dopočet, protože rozpočet obsahuje i položky nesouvisející přímo s vězněním (např. ~1,19 mld. Kč výplat důchodů).

### A.4 Co vědomě NEDĚLÁM (guardraily)

- Nepřiřazuji represi zdravotní výstup - žádný měřitelný neexistuje (literatura o odstrašení: přísnost sankcí nesnižuje spotřebu).
- Netvrdím, že existuje oficiální český výpočet poměru.
- Nepoužívám chybu z některých draftů ("léčba HIV stojí 8 mil. Kč ročně 30-40 let" = nereálných 240 mil. na osobu); pracuji s doživotním nákladem jako jedním ověřeným číslem (~4 mil. Kč, diskontovaný mezinárodní odhad).
- Nevydávám zahraniční číslo za české.

### A.5 Doporučený upgrade na verzi 2

Na základě porovnání s metodickým zadáním doporučuji do reportu doplnit pět prvků, které posílí jeho obhajitelnost:

1. literaturu o odstrašení (Nagin 2013; National Research Council 2014) a přerámovat argument o represi na **asymetrii** místo poměru,
2. přirozený experiment z Bukurešti (Des Jarlais 2020) jako **kauzální kotvu** kontrafaktuálu,
3. explicitní **práh rentability** (break-even) sítě harm reduction,
4. větu, že oficiální český CEA výpočet neexistuje (Strategie ho ukládá jako úkol),
5. **citlivostní analýzu** s diskontními sazbami 0 / 3 / 5 %.

Ilustrativní výpočet prahu rentability (jen HIV, konzervativně): roční rozpočet "snižování rizik" ~512 mil. Kč deleno doživotní náklad 1 HIV ~4 mil. Kč = práh ~128 odvrácených nákaz HIV ročně, aby se síť zaplatila. A to je práh počítaný jen na HIV, bez HCV, předávkování a kriminality, které ho dále snižují.

---

## Část B: Úplný soupis zdrojů

Zdroje jsou rozdělené do tří úrovní podle toho, jak jsem s nimi pracoval:

- **Úroveň 1** - primární PDF, která jsem fyzicky otevřel a prohledal (zdroj všech dat ✔ za rok 2024).
- **Úroveň 2** - recenzovaná literatura a mezinárodní data použitá v reportu (z hloubkové rešerše).
- **Úroveň 3** - doporučená doplnění z metodického zadání, která ještě v reportu nejsou, ale do verze 2 patří.

### Úroveň 1: Primární ověřené zdroje (data 2024, fyzicky prohledáno)

**[R32] Souhrnná zpráva o závislostech v ČR 2025 / Souhrn zprávy o nelegálních drogách 2025 (data za rok 2024), NMS - Úřad vlády ČR.**
Co z ní pochází: nové případy HIV (269) a injekční přenos (6), HCV (1 445 / z toho 668 injekčně), naloxon (982 dávek, 218 odvrácených předávkování), klienti nízkoprahových programů (41 tis.), vydané stříkačky (9,1 mil.), substituce (1 991 v registru), rizikoví uživatelé (47,5 tis.), drogová mortalita (73), výdaje na adiktologické služby (1 631,1 mil. Kč a jejich rozpad), úhrady VZP (1 592 mil. Kč, z toho 527 mil. na nelegální drogy), společenské náklady (6-7 mld. Kč), primární drogové trestné činy (4,2 tis.), odsouzení (2 545), přestupky (10 369), novely 2025/2026.
https://www.drogy-info.cz/zprava-o-zavislostech/

**[R33] Výroční zpráva Národní protidrogové centrály SKPV Policie ČR za rok 2024.**
Co z ní pochází: hodnota zkonfiskovaných drog (401,6 mil. Kč), celková "újma" zločineckým skupinám (542,4 mil. Kč).
https://policie.gov.cz/clanek/vyrocni-zprava-narodni-protidrogove-centraly-za-rok-2024.aspx

**[R34] Výroční zpráva Vězeňské služby ČR za rok 2024.**
Co z ní pochází: čerpaný rozpočet vězeňství (13 352,1 mil. Kč; rozpočet po změnách 13 507,5 mil.), stav vězněných (19 430 k 31. 12. 2024, z 19 569 v 2023), drogově závislí ve věznicích (14 402, z 13 052 v 2023; ~30 % populace), substituce v 10 věznicích, adiktologická péče v 11 jednotkách, dobrovolné léčení v 11 věznicích, HIV+ ve věznicích (55), úmrtí (57).
https://www.vs.gov.cz/

### Úroveň 2: Recenzovaná literatura a mezinárodní data (použito v reportu)

**[R1] Zábranský T. a kol. (2011). Společenské náklady užívání alkoholu, tabáku a nelegálních drog v ČR v roce 2007. Centrum adiktologie 1. LF UK a VFN.**
https://www.adiktologie.cz/file/198/01-coi-monografie-web.pdf

**[R2] Akční plán politiky v oblasti závislostí 2023-2025. Úřad vlády ČR.** (integrovaný rozpočet, podíl represe 52 %)
https://vlada.gov.cz/assets/ppov/zavislosti/strategie-a-plany/Akcni-plan-politiky-v-oblasti-zavislosti-2023-2025_fin.pdf

**[R4] Vězeňská služba ČR, Výroční zpráva 2023 (oficiální per-diem 1 916 Kč/den za 2023).**
https://www.vs.gov.cz/

**[R5] Popis sítě substituční léčby v ČR. Klinika adiktologie.** (cena substituce ~35 tis. Kč/rok)
https://www.adiktologie.cz/popis-site-substitucni-lecby

**[R6] Mravčík V. a kol. Report to the EMCDDA - Czech Republic (Reitox).** (prevalence HIV mezi PWID)
https://www.drugsandalcohol.ie/5737

**[R8] Zábranský T., Mravčík V. a kol. (2006). HCV among IDUs in the CR. Eur Addict Res 12(3):151-160.** (séroprevalence HCV; věznění jako rizikový faktor)
https://doi.org/10.1159/000092117

**[R10] EMCDDA / EUDA - Czechia Country Drug Report (drogová mortalita).**
https://www.euda.europa.eu/countries/czechia_en

**[R11] MacArthur G.J. a kol. (2012). OST and HIV transmission. BMJ 345:e5945.** (OST a riziko HIV -54 %)
https://doi.org/10.1136/bmj.e5945

**[R12] Aspinall E.J. a kol. (2014). NSP and HIV. Int J Epidemiol 43(1):235-248.** (NSP a přenos HIV -48 %)
https://doi.org/10.1093/ije/dyt243

**[R13] Platt L. a kol. (2017). OST + NSP and HCV. Cochrane Database Syst Rev 9:CD012021.** (NSP+OST a HCV -74 %)
https://doi.org/10.1002/14651858.CD012021.pub2

**[R14] Lifetime cost of HIV (UK). PLOS One 2015.** (doživotní náklad 1 HIV ~4-5 mil. Kč)
https://doi.org/10.1371/journal.pone.0125018

**[R15] Holtgrave D.R. a kol.; Alistar S.S. a kol. - cost per HIV infection averted (NSP).**
https://pubmed.ncbi.nlm.nih.gov/9663636/

**[R16] Policie ČR - Držení drog / Množství větší než malé; nař. vlády 467/2009 Sb.**
https://policie.gov.cz/clanek/drzeni-drog.aspx
https://www.zakonyprolidi.cz/cs/2009-467

**[R17] Ústavní soud ČR - zrušení zmocnění k určení "množství většího než malého".**
https://www.usoud.cz/aktualne/

**[R18] Institut pro kriminologii a sociální prevenci (IKSP) - penologická recidiva (64-70 %).**
http://www.ok.cz/iksp/docs/439.pdf

**[R19] RAND Drug Policy Research Center - treatment vs. incarceration (léčba ~7x efektivnější; drug courts).**
https://www.rand.org/pubs/commentary/2016/10/drug-dependence-treatment-over-incarceration.html

**[R20] Open Society Foundations - Treatment Versus Incarceration.**
https://www.opensocietyfoundations.org/

**[R21] NIDA/NIH - treatment cost savings (návratnost 4-7 USD na 1 USD).**
https://www.nih.gov/news-events/news-releases/nida-announces-recommendations-treat-drug-abusers-save-money-reduce-crime

**[R22] UNODC/INCB - prevention ROI.**
https://www.unodc.org/

**[R23] Transform Drugs / EMCDDA / SICAD - Portugal facts.**
https://transformdrugs.org/blog/portugal-drug-decriminalisation-the-facts

**[R24] Hughes C.E. & Stevens A. (2010). Portuguese decriminalization. Brit J Criminol 50(6):999-1022.**
https://doi.org/10.1093/bjc/azq038

**[R25] Frei A. a kol. (2000). Cost-Benefit Analysis of Heroin Maintenance Treatment. Karger, Basel.** (čistý přínos ~26 USD/pacient/den)
https://www.karger.com/Book/Home/221544

**[R26] Killias M., Aebi M. a kol. - heroin prescription and crime (Švýcarsko).**
https://popcenter.asu.edu/sites/default/files/library/CrimePrevention/Volume_11/04-Killias.pdf

**[R27] Nguyen T.Q. a kol. (2014) AIDS Behav; Kwon J.A. a kol. (2012) AIDS.** (ROI NSP 2-7,6x)
https://doi.org/10.1097/QAD.0b013e3283565dd9

**[R28] Bernard C.L. a kol. (2017). OAT cost-effectiveness. PLoS Med 14(5):e1002312.** (OAT <20 000 USD/QALY)
https://doi.org/10.1371/journal.pmed.1002312

**[R29] Langham S. a kol. (2018). Naloxone cost-effectiveness. Value in Health.**
https://pubmed.ncbi.nlm.nih.gov/29680097/

**[R30] Andresen M.A. & Boyd N. (2010). Vancouver Insite benefit-cost (~5:1). Int J Drug Policy.**
https://pubmed.ncbi.nlm.nih.gov/19423324/

**[R31] Wilson D.P. a kol. (2015). The cost-effectiveness of harm reduction. Int J Drug Policy 26:S5-S11.**
https://doi.org/10.1016/j.drugpo.2014.11.007

### Úroveň 3: Doplnění verze 2 a další doporučené zdroje

**Všech těchto deset zdrojů z metodického zadání je nyní zapracováno do reportu verze 2** jako [R35]-[R44]. Níže s mapováním a místem použití.

**[N1 = R35] Nagin D.S. (2013). Deterrence in the Twenty-First Century. Crime and Justice 42(1).** Použito v sekci 3.5 a verdiktu - opora pro asymetrii (přísnost sankcí nesnižuje spotřebu).
https://doi.org/10.1086/670398

**[N2 = R36] National Research Council (2014). The Growth of Incarceration in the United States.** Sekce 3.5 - represe bez měřitelného zdravotního výstupu.
https://nap.nationalacademies.org/catalog/18613/

**[N6 = R37] Národní strategie 2019-2027 (s. 28: CEA jako budoucí úkol).** Metodická poznámka a limity - žádný oficiální český výpočet neexistuje.
https://vlada.gov.cz/assets/ppov/protidrogova-politika/strategie-a-plany/Narodni_strategie_2019-2027_fin01.pdf

**[N3 = R38] Des Jarlais D.C. a kol. (2020). Bucharest natural experiment. Lancet HIV.** Sekce 5.2 a 5.5 - kauzální kotva kontrafaktuálu.
https://www.thelancet.com/journals/lanhiv/article/PIIS2352-3018(20)30082-5/abstract

**[N4 = R39] Sordo L. a kol. (2017). Mortality risk during and after OST. BMJ 357:j1550.** Sekce 2.4 - OST a mortalita.
https://pmc.ncbi.nlm.nih.gov/articles/PMC5421454/

**[N5 = R40] Santo T. Jr. a kol. (2021). OAT and mortality. JAMA Psychiatry 78(9).** Sekce 2.4 - OAT a mortalita (přehled ~15 mil. osoboroků).
https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2780655

**[N7 = R42] NMS - Zaostřeno 6/2020 (výdaje podle resortů včetně policie a NPC).** Sekce 1.2 frame A - doplňkový zdroj integrovaného rozpočtu.
https://www.drogy-info.cz/data/obj_files/33389/1077/Z6_2020.pdf

**[N8 = R41] NAUTA 2022 - společenské náklady 56,2 mld / drogy 6,7 mld.** Sekce 1.1 - novější potvrzení společenských nákladů.
https://mzd.gov.cz/wp-content/uploads/2023/05/NAUTA_2022.pdf

**[N9 = R43] Slovenský poměr 1:3 a popis české sítě (CEE funding crisis).** Sekce 4.3 - zahraniční externí validace (označeno jako zahraniční).
https://pmc.ncbi.nlm.nih.gov/articles/PMC7579931/

**[N10 = R44] Ukrajinská cost-effectiveness studie (487 USD NSP / 1 146 USD OST).** Sekce 4.3 - zahraniční externí validace (označeno jako zahraniční).
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4396789/

### Úroveň 4: Doplnění verze 3 (české jednotkové náklady, izolace represe, oprava citace)

Verze 3 přidala reprodukovatelný skript `harm_reduction_model.py` (graf `tornado.png`) a tyto zdroje/úpravy:

**[R45] VZP ČR (2023). Léčba HIV pozitivních stála VZP rekordních 420 mil. korun.** Sekce 5.2 - český doživotní náklad HIV (~423 mil. Kč / ~2 011 pacientů ≈ ~210 tis. Kč/pacient/rok ARV), kterým je nahrazeno britské proxy [R14].
https://www.vzp.cz/o-nas/aktuality/lecba-hiv-pozitivnich-stala-vzp-rekordnich-420-mil-korun

**[R46] VZP ČR. Klienty VZP trápí chronická virová hepatitida (909,6 mil.).** Sekce 5.2 - kontext českého nákladu HCV (~91 tis. Kč/rok/pacient chronická hepatitida 2020). Přesný per-case náklad DAA zůstává [DOPLNIT ZDROJ].
https://www.vzp.cz/o-nas/aktuality/klienty-vzp-trapi-chronicka-virova-hepatitida-jeji-lecba-stala-vloni-909-6-milionu

**[R38 - oprava] Des Jarlais D.C., Sypsa V., Feelemyer J., Abagiu A.O., et al. (2020). HIV outbreaks among people who inject drugs in Europe, North America, and Israel. Lancet HIV 7(6):e434-442.** Ověřen přesný název (dříve parafráze); je to multiměstská analýza (Atény jako vlajkový případ, Bukurešť analogický). Sekce 5.2 a 5.5.
https://www.thelancet.com/journals/lanhiv/article/PIIS2352-3018(20)30082-5/abstract

**[R42 - rozšíření] Zaostřeno 6/2020** je nově určeno i jako zdroj pro izolaci drogově přiřaditelných výdajů represe (NPC + drogová agenda policie), sekce 3.1. Konkrétní položka/rok zůstává [DOPLNIT ZDROJ] - viz `doplnit-zdroje.md`.

Zbývající chybějící vstupy (per-case HCV, kalibrace incidence, izolované výdaje represe) jsou shrnuté v samostatném souboru `doplnit-zdroje.md`.

### Úroveň 5: Doplnění verze 4 (ověřené náklady HCV, izolace represe)

**[R47] Státní ústav pro kontrolu léčiv (2025). Seznam cen a úhrad léčivých přípravků a PZLÚ (SCAU), platnost k 1. 5. 2025.** Sekce 5.2 - per-case náklad DAA kúry HCV (Zepatier ~511 tis., Maviret ~524 tis., Epclusa ~650 tis., Vosevi ~844 tis. Kč). Nahrazuje dřívější odhad a uzavírá mezeru [DOPLNIT - HCV].
https://www.sukl.cz/prumysl/leciva/ceny-a-uhrady/prehledy-cen-a-uhrad-leciv/

**[R42 - dotaženo] Zaostřeno 6/2020** poskytuje konkrétní izolované číslo: drogově přiřaditelné výdaje represe (Policie + NPC) ~1,16 mld. Kč (2019; 56 % integrovaného rozpočtu 2 071,6 mil. Kč). Sekce 3.1 a 3.5 - asymetrie se nově vztahuje k tomuto číslu (~2,3× rozpočtu HR), ne k celému vězeňství. Uzavírá mezeru [DOPLNIT - izolované výdaje represe].

Po verzi 4 zůstává jediná otevřená mezera: kalibrace kontrafaktuální incidence HIV/HCV (viz `doplnit-zdroje.md`).

---

## Část C: Poznámka k poctivosti

Tento dokument záměrně rozlišuje, co je ověřené z primárního zdroje (✔, úroveň 1), co je recenzovaná zahraniční evidence (úroveň 2), doporučené/doplněné zdroje (úroveň 3), doplnění verze 3 (úroveň 4) a doplnění verze 4 (úroveň 5). Žádné číslo v reportu nestojí bez zdroje; tam, kde je vstup modelový nebo nejistý, je to v reportu i tady označeno výslovně (status [DOPLNIT ZDROJ]). Mezinárodní čísla jsou označena jako zahraniční a nejsou vydávána za česká. Modelová čísla sekce 5 jsou generována ze skriptu `harm_reduction_model.py` (jeden zdroj pravdy).
