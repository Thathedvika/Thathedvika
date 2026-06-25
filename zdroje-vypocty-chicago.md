# Zdroje použité k výpočtům — ekonomický model harm reduction vs. represe

Citováno v **Chicago stylu** (notes–bibliography / bibliography format). Tento seznam pokrývá zdroje, které přímo vstupují do výpočtů poslední verze modelu (`harm_reduction_model.py`, verze 3/3b) — tedy vstupy konfigurační sekce skriptu a hodnoty v sekci 5 reportu. Plná bibliografie celého reportu (R1–R46, vč. kontextových a mezinárodních zdrojů) je v samotném reportu.

Datum sestavení: červen 2026.

---

## A. České primární zdroje (hlavní vstupy modelu)

Národní monitorovací středisko pro drogy a závislosti. *Souhrn Zprávy o nelegálních drogách v České republice 2025* (data za rok 2024). Praha: Úřad vlády České republiky, 2025.
https://www.drogy-info.cz/zprava-o-zavislostech/

> Vstupy: roční rozpočet harm reduction (~512 mil. Kč = 31,4 % z 1 631,1 mil.), počet injekčních uživatelů (~42 000), počet klientů nízkoprahových programů (~41 000), nové případy HIV (269) a HCV mezi injekčními uživateli (668) za rok 2024.

Vězeňská služba České republiky. *Výroční zpráva Vězeňské služby ČR za rok 2024*. Praha: Vězeňská služba ČR, 2025.
https://www.vs.gov.cz/

> Vstupy: čerpaný rozpočet vězeňství (13,35 mld. Kč), stav vězněných (19 430), drogově závislí ve věznicích (14 402), dopočet nákladu na vězně (~687 tis. Kč/rok).

Národní protidrogová centrála SKPV, Policie České republiky. *Výroční zpráva 2024*. Praha: Policie ČR, 2025.
https://policie.gov.cz/clanek/vyrocni-zprava-narodni-protidrogove-centraly-za-rok-2024.aspx

Národní monitorovací středisko pro drogy a závislosti. „Zaostřeno 6/2020: Výdaje na protidrogovou politiku v ČR podle resortů." Praha: Úřad vlády ČR, 2020.
https://www.drogy-info.cz/data/obj_files/33389/1077/Z6_2020.pdf

> Vstup: izolované drogově přiřaditelné výdaje represe — Policie ČR včetně Národní protidrogové centrály, ~1,16 mld. Kč (2019; 56 % z integrovaného rozpočtu 2 071,6 mil. Kč).

Úřad vlády České republiky. *Akční plán politiky v oblasti závislostí 2023–2025*. Praha: Úřad vlády ČR, 2023.
https://vlada.gov.cz/assets/ppov/zavislosti/strategie-a-plany/Akcni-plan-politiky-v-oblasti-zavislosti-2023-2025_fin.pdf

> Vstup: integrovaný rozpočet (frame A), podíl prosazování práva ~52 % (2021).

Úřad vlády České republiky. *Národní strategie prevence a snižování škod spojených se závislostním chováním 2019–2027*. Praha: Úřad vlády ČR, 2019.
https://vlada.gov.cz/assets/ppov/protidrogova-politika/strategie-a-plany/Narodni_strategie_2019-2027_fin01.pdf

> Metodická opora: cost-effectiveness analýza je v ČR uložena jako budoucí úkol (s. 28) — oficiální výpočet poměru neexistuje.

---

## B. Jednotkové náklady léčby (HIV, HCV, substituce, věznění)

Státní ústav pro kontrolu léčiv. *Seznam cen a úhrad léčivých přípravků a potravin pro zvláštní lékařské účely (SCAU), platnost k 1. 5. 2025*. Praha: SÚKL, 2025.
https://www.sukl.cz/prumysl/leciva/ceny-a-uhrady/prehledy-cen-a-uhrad-leciv/

> Vstup: náklad léčby HCV na případ (DAA kúra) — Zepatier 12 týdnů ~511 tis. Kč, Maviret 8 týdnů ~524 tis. Kč, Epclusa 12 týdnů ~650 tis. Kč, Vosevi 12 týdnů ~844 tis. Kč (salvage). Modelový rozsah 510–850 tis. Kč, střední ~620 tis. Kč.

Všeobecná zdravotní pojišťovna ČR. „Léčba HIV pozitivních stála VZP rekordních 420 mil. korun." VZP ČR, 2023.
https://www.vzp.cz/o-nas/aktuality/lecba-hiv-pozitivnich-stala-vzp-rekordnich-420-mil-korun

> Vstup: roční náklad antiretrovirové léčby ~210 tis. Kč/pacient (~423 mil. Kč na ~2 011 pacientů, 2022); z něj odvozen doživotní náklad HIV diskontovanou anuitou (~4,5 mil. Kč při 3 %).

Všeobecná zdravotní pojišťovna ČR. „Klienty VZP trápí chronická virová hepatitida, její léčba stála vloni 909,6 milionu." VZP ČR.
https://www.vzp.cz/o-nas/aktuality/klienty-vzp-trapi-chronicka-virova-hepatitida-jeji-lecba-stala-vloni-909-6-milionu

> Kontext: ~91 tis. Kč/rok na pacienta s chronickou hepatitidou (2020); celkové výdaje VZP na hepatitidy.

Klinika adiktologie 1. LF UK a VFN v Praze. „Popis sítě substituční léčby v ČR." Praha: Klinika adiktologie.
https://www.adiktologie.cz/popis-site-substitucni-lecby

> Vstup: roční náklad substituční léčby ~35–73 tis. Kč/pacient (poměr k věznění ~10–20×).

Vězeňská služba České republiky. *Výroční zpráva 2023*. Praha: Vězeňská služba ČR, 2023.
https://www.vs.gov.cz/

> Vstup: oficiální per-diem věznění 1 916 Kč/den (~699 tis. Kč/rok, 2023) jako srovnání s dopočtem 2024.

---

## C. Účinnost intervencí — meta-analýzy (relativní rizika)

Aspinall, Esther J., Dhanya Nambiar, David J. Goldberg, Matthew Hickman, Amanda Weir, Eva Van Velzen, Norah Palmateer, Joseph S. Doyle, Margaret E. Hellard, and Sharon J. Hutchinson. „Are Needle and Syringe Programmes Associated with a Reduction in HIV Transmission among People Who Inject Drugs? A Systematic Review and Meta-Analysis." *International Journal of Epidemiology* 43, č. 1 (2014): 235–248.
https://doi.org/10.1093/ije/dyt243

> Vstup: relativní riziko HIV při výměnných programech (NSP), −48 %.

MacArthur, Georgie J., Silvia Minozzi, Natasha Martin, Peter Vickerman, Steve Deren, Julie Bruneau, Louisa Degenhardt, and Matthew Hickman. „Opiate Substitution Treatment and HIV Transmission in People Who Inject Drugs: Systematic Review and Meta-Analysis." *BMJ* 345 (2012): e5945.
https://doi.org/10.1136/bmj.e5945

> Vstup: relativní riziko HIV při substituční léčbě (OST), −54 %.

Platt, Lucy, Silvia Minozzi, Jennifer Reed, Peter Vickerman, Holly Hagan, Clare French, Ashly Jordan, et al. „Needle Syringe Programmes and Opioid Substitution Therapy for Preventing Hepatitis C Transmission in People Who Inject Drugs." *Cochrane Database of Systematic Reviews*, č. 9 (2017): CD012021.
https://doi.org/10.1002/14651858.CD012021.pub2

> Vstup: relativní riziko HCV při kombinaci NSP + OST, RR 0,26 (−74 %).

---

## D. Kontrafaktuál a metodická opora (asymetrie)

Des Jarlais, Don C., Vana Sypsa, Jonathan Feelemyer, Adrian O. Abagiu, Vivian Hope, Marie Jauffret-Roustide, Dimitrios Paraskevis, et al. „HIV Outbreaks among People Who Inject Drugs in Europe, North America, and Israel." *The Lancet HIV* 7, č. 6 (2020): e434–e442.
https://www.thelancet.com/journals/lanhiv/article/PIIS2352-3018(20)30082-5/abstract

> Vstup: kalibrace kontrafaktuální incidence bez harm reduction (ohniska <100 až >1 000 nových HIV mezi injekčními uživateli po oslabení HR; vlajkový případ Atény, analogicky Bukurešť).

Nagin, Daniel S. „Deterrence in the Twenty-First Century: A Review of the Evidence." *Crime and Justice* 42, č. 1 (2013): 199–263.
https://doi.org/10.1086/670398

> Opora pro argument asymetrie: přísnost sankcí spotřebu/kriminalitu významně nesnižuje — represe nemá doložený měřitelný zdravotní výstup.

National Research Council. *The Growth of Incarceration in the United States: Exploring Causes and Consequences*. Washington, DC: National Academies Press, 2014.
https://nap.nationalacademies.org/catalog/18613/

> Opora pro argument asymetrie (chybějící zdravotní výstup represe).

---

## E. Mezinárodní nákladová validace (validace řádu — NE česká čísla)

Alistar, Sabina S., Douglas K. Owens, and Margaret L. Brandeau. „Effectiveness and Cost Effectiveness of Expanding Harm Reduction and Antiretroviral Therapy in a Mixed HIV Epidemic: A Modeling Analysis for Ukraine." *PLoS Medicine* 8, č. 3 (2011): e1000423.
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4396789/

> Validace řádu: náklad na odvrácenou HIV ~487 USD (NSP) / ~1 146 USD (OST) — *zahraniční*.

„Lifetime Cost of HIV Treatment in the UK." *PLoS ONE* 10, č. 4 (2015): e0125018.
https://doi.org/10.1371/journal.pone.0125018

> Validace řádu: doživotní náklad léčby 1 případu HIV ~£185 200 (~4–5 mil. Kč) — *zahraniční*; nahrazeno česky odvozeným nákladem (viz oddíl B, VZP).

---

## Poznámka k použití

- Symbol „✔" v reportu = údaj ověřený z primárního PDF za rok 2024 (oddíl A).
- Mezinárodní čísla (oddíl C, D, E) jsou v reportu i zde označena jako zahraniční a neslouží jako česká data, nýbrž jako effect sizes nebo validace řádu.
- Modelové vstupy se statusem „[DOPLNIT ZDROJ]" (kalibrace kontrafaktuální incidence, případně další upřesnění per-case nákladu HCV) jsou shrnuty v souboru `doplnit-zdroje.md`.
