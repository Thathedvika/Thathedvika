#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
harm_reduction_model.py

Ekonomicky model: vyplati se v CR harm reduction (HR)? Verze 3.

Reprodukovatelny, parametrizovany, deterministicky vypocet pro report
"harm-reduction-vs-represe-CR.md". Po spusteni vytiskne vsechna cisla,
ktera se objevuji v reportu (jeden zdroj pravdy), a ulozi tornado.png.

Spusteni:
    python3 harm_reduction_model.py

Zavazna pravidla:
- Argument o represi je ASYMETRIE, ne pomer-versus-pomer.
- Kazdy vstup ma zdroj, nebo status [DOPLNIT ZDROJ].
- Zahranicni cisla jsou oznacena jako zahranicni.
- Symbol "OK" v komentari = overeno z primarniho PDF za rok 2024 (v reportu znacka skrtky).
"""

from __future__ import annotations

# ===========================================================================
# 1. KONFIGURACNI SEKCE - vsechny vstupy jako pojmenovane promenne se zdrojem
# ===========================================================================

# --- Strana harm reduction (rocni) ---------------------------------------
ROZPOCET_HR_ROK = 512_000_000          # Kc. 31,4 % z 1 631,1 mil. Kc na sluzby.
                                       # Zdroj: NMS Souhrnna zprava 2025 (data 2024). [OK]
POCET_PWID = 42_000                    # Injekcni uzivatele drog (PWID) v CR.
                                       # Zdroj: NMS 2024 (~42,5 tis.). [OK]
POCET_KLIENTU_HR = 41_000              # Klienti nizkoprahovych programu.
                                       # Zdroj: NMS 2024. [OK]

# --- Jednotkove naklady odvracene skody ----------------------------------
# HIV: cesky odvozeny dozivotni naklad = rocni ARV naklad * diskontovana anuita.
NAKLAD_HIV_ROK_CZ = 210_000            # Kc/pacient/rok (antiretrovirova lecba).
                                       # Zdroj: VZP 2022 (~423 mil. Kc / ~2 011 pacientu).
                                       # https://www.vzp.cz/o-nas/aktuality/lecba-hiv-pozitivnich-stala-vzp-rekordnich-420-mil-korun
HORIZONT_HIV_LET = 35                  # Predpokladany pocet let lecby (HIV = chronicke).
                                       # PREDPOKLAD - oznaceno v reportu jako modelovy.
# HCV: jednorazova DAA kura + nasledna pece (per pripad).
NAKLAD_HCV_PRIPAD_MID = 600_000        # Kc. Stredni odhad.
NAKLAD_HCV_PRIPAD_LOW = 300_000        # Kc. Dolni (modernejsi vyjednane ceny DAA).
NAKLAD_HCV_PRIPAD_HIGH = 875_000       # Kc. Horni (~35 000 EUR, list. cena DAA).
                                       # Kontext: VZP ~91 000 Kc/rok/pac. chronicka hepatitida (2020).
                                       # https://www.vzp.cz/o-nas/aktuality/klienty-vzp-trapi-chronicka-virova-hepatitida-jeji-lecba-stala-vloni-909-6-milionu
                                       # Status: [DOPLNIT ZDROJ - cesky naklad HCV per pripad, SUKL/VZP]

# --- Kontrafaktualni rocni incidence BEZ harm reduction ------------------
# Kalibrace z Des Jarlais 2020 (ohniska <100 az >1000 novych HIV/PWID po oslabeni HR).
# Vyjadreno jako rocni incidence (podil PWID). Status: [DOPLNIT - kalibrace incidence].
INCIDENCE_HIV_LOW = 0.005              # 0,5 %/rok (~210 novych HIV/rok pri 42 tis. PWID)
INCIDENCE_HIV_MID = 0.010              # 1,0 %/rok (~420 novych HIV/rok)
INCIDENCE_HIV_HIGH = 0.020             # 2,0 %/rok (~840 novych HIV/rok)
INCIDENCE_HCV_LOW = 0.05               # 5 %/rok
INCIDENCE_HCV_MID = 0.10               # 10 %/rok
INCIDENCE_HCV_HIGH = 0.15              # 15 %/rok

# --- Effect sizes (relativni rizika z meta-analyz) -----------------------
RR_HIV_MID = 0.36                      # NSP+OST proti HIV (kombinace).
RR_HIV_LOW = 0.26                      # silnejsi ucinek (vice odvracenych)
RR_HIV_HIGH = 0.52                     # slabsi ucinek
                                       # Zdroj: Aspinall 2014 (NSP -48 %); MacArthur 2012 (OST -54 %).
RR_HCV_MID = 0.26                      # NSP+OST proti HCV (-74 %).
RR_HCV_LOW = 0.18
RR_HCV_HIGH = 0.40                     # Zdroj: Platt Cochrane 2017. [OK pro RR]

# --- Diskontni sazby (konvence pro CEA; v CR neni fixni ICER prah) --------
DISKONT_SAZBY = [0.0, 0.03, 0.05]      # testuj 0 / 3 / 5 %
DISKONT_DEFAULT = 0.03

# --- Overene rocni toky 2024 (kontext, ne vstup modelu) ------------------
NOVE_HIV_INJEKCNE_2024 = 6             # [OK] NMS 2024
NOVE_HCV_INJEKCNE_2024 = 668          # [OK] NMS 2024

# --- Strana represe (izolovana, NE cely rozpocet veznice) ----------------
VYDAJE_REPRESE_DROGY_ROK = None        # Kc. Drogove priraditelne vydaje represe
                                       # (Narodni protidrogova centrala + drogova agenda policie).
                                       # Zdroj: NMS Zaostreno 6/2020 (vydaje podle resortu).
                                       # Status: [DOPLNIT ZDROJ - konkretni polozka a rok]
ROZPOCET_VEZENSTVI = 13_350_000_000    # Kc. [OK] VS CR 2024. KONTEXT systemovych nakladu.
NAKLAD_VEZEN_ROK = 687_000             # Kc/vezen/rok (rozpocet / stav). [OK] VS CR 2024.
ZAVISLI_VE_VEZNICICH = 14_402          # [OK] VS CR 2024 (~30 % populace veznic).

# Zahranicni validacni cisla (NIKDY se nevydavaji za ceska) ----------------
ZAHR_NAKLAD_ODVR_HIV_USD = (487, 34_278)   # USD/odvracenou HIV (Ukrajina-NSP az ruzne modely)
ZAHR_SLOVENSKO_ROI = 3                       # 1:3 (Slovensko)
KURZ_USD_CZK = 23.0                          # orientacni prepocet


# ===========================================================================
# 2. FUNKCE
# ===========================================================================

def dozivotni_naklad_hiv(rocni: float, roky: int, sazba: float) -> float:
    """Diskontovana soucasna hodnota anuity rocnich nakladu ARV lecby."""
    if sazba == 0:
        return rocni * roky
    return rocni * (1 - (1 + sazba) ** (-roky)) / sazba


def odvracene_infekce(pocet_pwid: float, incidence: float, rr: float) -> float:
    """Rocni pocet odvracenych infekci = populace * incidence_bez_HR * (1 - RR)."""
    return pocet_pwid * incidence * (1 - rr)


def odvracene_naklady(odvr_hiv: float, naklad_hiv: float,
                      odvr_hcv: float, naklad_hcv: float) -> float:
    """Hodnota odvracenych infekci (HIV + HCV) v Kc/rok."""
    return odvr_hiv * naklad_hiv + odvr_hcv * naklad_hcv


def roi(odvr_naklady: float, rozpocet_hr: float) -> float:
    """Rocni navratnost: odvracene naklady / rozpocet HR. >1 => vyplati se."""
    return odvr_naklady / rozpocet_hr


def prah_rentability(rozpocet_hr: float, naklad_na_pripad: float) -> float:
    """Pocet infekci, ktere musi sit rocne odvratit, aby se zaplatila."""
    return rozpocet_hr / naklad_na_pripad


def naklad_na_odvracenou(rozpocet_hr: float, odvracene_celkem: float) -> float:
    """Naklad HR na 1 odvracenou infekci (HIV+HCV dohromady)."""
    return rozpocet_hr / odvracene_celkem


# ===========================================================================
# 3. ZAKLADNI VYPOCET (stredni scenar, diskont 3 %)
# ===========================================================================

def zakladni_scenar(sazba: float = DISKONT_DEFAULT) -> dict:
    naklad_hiv = dozivotni_naklad_hiv(NAKLAD_HIV_ROK_CZ, HORIZONT_HIV_LET, sazba)
    naklad_hcv = NAKLAD_HCV_PRIPAD_MID

    odvr_hiv = odvracene_infekce(POCET_PWID, INCIDENCE_HIV_MID, RR_HIV_MID)
    odvr_hcv = odvracene_infekce(POCET_PWID, INCIDENCE_HCV_MID, RR_HCV_MID)

    on = odvracene_naklady(odvr_hiv, naklad_hiv, odvr_hcv, naklad_hcv)
    roi_hr = roi(on, ROZPOCET_HR_ROK)

    prah_hiv = prah_rentability(ROZPOCET_HR_ROK, naklad_hiv)         # jen HIV
    prah_kombi = prah_rentability(ROZPOCET_HR_ROK, naklad_hcv)        # jen HCV (per pripad)

    naklad_odvr = naklad_na_odvracenou(ROZPOCET_HR_ROK, odvr_hiv + odvr_hcv)

    return {
        "sazba": sazba,
        "naklad_hiv": naklad_hiv,
        "naklad_hcv": naklad_hcv,
        "odvr_hiv": odvr_hiv,
        "odvr_hcv": odvr_hcv,
        "odvracene_naklady": on,
        "roi": roi_hr,
        "prah_hiv": prah_hiv,
        "prah_kombi_hcv": prah_kombi,
        "naklad_na_odvracenou": naklad_odvr,
    }


# ===========================================================================
# 4. CITLIVOSTNI ANALYZA
# ===========================================================================

def citlivost_diskont() -> list:
    """Prah rentability (jen HIV) a dozivotni naklad HIV pres diskontni sazby."""
    out = []
    for s in DISKONT_SAZBY:
        nh = dozivotni_naklad_hiv(NAKLAD_HIV_ROK_CZ, HORIZONT_HIV_LET, s)
        out.append({"sazba": s, "naklad_hiv": nh,
                    "prah_hiv": prah_rentability(ROZPOCET_HR_ROK, nh)})
    return out


def _roi_pro_vstupy(naklad_hiv, naklad_hcv, inc_hiv, inc_hcv, rr_hiv, rr_hcv) -> float:
    oh = odvracene_infekce(POCET_PWID, inc_hiv, rr_hiv)
    oc = odvracene_infekce(POCET_PWID, inc_hcv, rr_hcv)
    return roi(odvracene_naklady(oh, naklad_hiv, oc, naklad_hcv), ROZPOCET_HR_ROK)


def tornado_data() -> list:
    """Jednosmerna citlivost ROI: kazdy vstup dolni/horni, ostatni stredni."""
    naklad_hiv_mid = dozivotni_naklad_hiv(NAKLAD_HIV_ROK_CZ, HORIZONT_HIV_LET, DISKONT_DEFAULT)
    naklad_hiv_low = dozivotni_naklad_hiv(NAKLAD_HIV_ROK_CZ, HORIZONT_HIV_LET, 0.05)  # nizsi naklad
    naklad_hiv_high = dozivotni_naklad_hiv(NAKLAD_HIV_ROK_CZ, HORIZONT_HIV_LET, 0.0)  # vyssi naklad

    base = dict(naklad_hiv=naklad_hiv_mid, naklad_hcv=NAKLAD_HCV_PRIPAD_MID,
                inc_hiv=INCIDENCE_HIV_MID, inc_hcv=INCIDENCE_HCV_MID,
                rr_hiv=RR_HIV_MID, rr_hcv=RR_HCV_MID)
    baseline = _roi_pro_vstupy(**base)

    # (popisek, klic, dolni hodnota, horni hodnota)
    promenne = [
        ("Doziv. naklad HIV (diskont 5->0 %)", "naklad_hiv", naklad_hiv_low, naklad_hiv_high),
        ("Naklad HCV/pripad", "naklad_hcv", NAKLAD_HCV_PRIPAD_LOW, NAKLAD_HCV_PRIPAD_HIGH),
        ("Kontrafakt. incidence HIV", "inc_hiv", INCIDENCE_HIV_LOW, INCIDENCE_HIV_HIGH),
        ("Kontrafakt. incidence HCV", "inc_hcv", INCIDENCE_HCV_LOW, INCIDENCE_HCV_HIGH),
        ("RR HIV (ucinnost NSP+OST)", "rr_hiv", RR_HIV_LOW, RR_HIV_HIGH),
        ("RR HCV (ucinnost NSP+OST)", "rr_hcv", RR_HCV_LOW, RR_HCV_HIGH),
    ]
    rows = []
    for popis, klic, lo, hi in promenne:
        a = dict(base); a[klic] = lo
        b = dict(base); b[klic] = hi
        roi_lo = _roi_pro_vstupy(**a)
        roi_hi = _roi_pro_vstupy(**b)
        rows.append({"popis": popis, "roi_lo": roi_lo, "roi_hi": roi_hi,
                     "rozpeti": abs(roi_hi - roi_lo)})
    rows.sort(key=lambda r: r["rozpeti"], reverse=True)
    return baseline, rows


def uloz_tornado(baseline: float, rows: list, cesta: str = "tornado.png") -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    popisky = [r["popis"] for r in rows][::-1]
    lo = [min(r["roi_lo"], r["roi_hi"]) for r in rows][::-1]
    hi = [max(r["roi_lo"], r["roi_hi"]) for r in rows][::-1]
    y = range(len(popisky))

    fig, ax = plt.subplots(figsize=(9, 4.5))
    for i, (l, h) in enumerate(zip(lo, hi)):
        ax.barh(i, h - l, left=l, color="#4C72B0", edgecolor="black", height=0.6)
    ax.axvline(baseline, color="#C44E52", linestyle="--",
               label=f"zakladni ROI = {baseline:.1f}")
    ax.axvline(1.0, color="gray", linestyle=":", label="prah vyplatnosti (ROI = 1)")
    ax.set_yticks(list(y))
    ax.set_yticklabels(popisky)
    ax.set_xlabel("Rocni ROI harm reduction (odvracene naklady / rozpocet HR)")
    ax.set_title("Jednosmerna citlivostni analyza (tornado) - ROI harm reduction")
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(cesta, dpi=120)
    print(f"\n[graf] ulozeno: {cesta}")


# ===========================================================================
# 5. TISK VYSLEDKU (markdown-ready)
# ===========================================================================

def kc(x: float) -> str:
    return f"{x:,.0f}".replace(",", " ") + " Kc"


def main() -> None:
    print("=" * 70)
    print("EKONOMICKY MODEL HARM REDUCTION vs. REPRESE - verze 3")
    print("=" * 70)

    z = zakladni_scenar()
    print("\n--- ZAKLADNI SCENAR (diskont 3 %, stredni vstupy) ---")
    print(f"Dozivotni naklad 1 HIV (CZ, diskont):   {kc(z['naklad_hiv'])}")
    print(f"Naklad 1 HCV (per pripad):              {kc(z['naklad_hcv'])}")
    print(f"Odvracene HIV/rok:                      {z['odvr_hiv']:.0f}")
    print(f"Odvracene HCV/rok:                      {z['odvr_hcv']:.0f}")
    print(f"Odvracene naklady/rok:                  {kc(z['odvracene_naklady'])}")
    print(f"ROCNI ROI harm reduction:               {z['roi']:.1f}x")
    print(f"Prah rentability (jen HIV):             {z['prah_hiv']:.0f} nakaz/rok")
    print(f"Prah rentability (jen HCV, per pripad): {z['prah_kombi_hcv']:.0f} pripadu/rok")
    print(f"Naklad HR na 1 odvracenou infekci:      {kc(z['naklad_na_odvracenou'])}")

    print("\n--- VYSLEDKOVA TABULKA (markdown) ---")
    print("| Ukazatel | Hodnota |")
    print("|---|---|")
    print(f"| Rocni ROI harm reduction (stredni) | **{z['roi']:.1f}x** |")
    print(f"| Dozivotni naklad 1 HIV (CZ, 3 %) | {kc(z['naklad_hiv'])} |")
    print(f"| Naklad 1 HCV (per pripad, stredni) | {kc(z['naklad_hcv'])} |")
    print(f"| Prah rentability - jen HIV | ~{z['prah_hiv']:.0f} nakaz/rok |")
    print(f"| Naklad na 1 odvracenou infekci | ~{kc(z['naklad_na_odvracenou'])} |")

    print("\n--- CITLIVOST: diskontni sazba -> prah rentability (jen HIV) ---")
    print("| Sazba | Doziv. naklad HIV | Prah (nakaz/rok) |")
    print("|---|---|---|")
    for r in citlivost_diskont():
        print(f"| {r['sazba']*100:.0f} % | {kc(r['naklad_hiv'])} | ~{r['prah_hiv']:.0f} |")

    print("\n--- CITLIVOST: ROI pres diskontni sazby (stredni vstupy) ---")
    for s in DISKONT_SAZBY:
        zz = zakladni_scenar(s)
        print(f"  diskont {s*100:>2.0f} %  ->  ROI = {zz['roi']:.1f}x")

    baseline, rows = tornado_data()
    print(f"\n--- TORNADO (zakladni ROI = {baseline:.1f}x) ---")
    print("| Vstup | ROI dolni | ROI horni | rozpeti |")
    print("|---|---|---|---|")
    for r in rows:
        print(f"| {r['popis']} | {r['roi_lo']:.1f}x | {r['roi_hi']:.1f}x | {r['rozpeti']:.1f} |")

    print("\n--- ZAHRANICNI VALIDACE (radu, NE ceske cislo) ---")
    lo_kc = ZAHR_NAKLAD_ODVR_HIV_USD[0] * KURZ_USD_CZK
    hi_kc = ZAHR_NAKLAD_ODVR_HIV_USD[1] * KURZ_USD_CZK
    print(f"Zahr. naklad/odvracenou HIV: {ZAHR_NAKLAD_ODVR_HIV_USD[0]}-{ZAHR_NAKLAD_ODVR_HIV_USD[1]} USD "
          f"(~{kc(lo_kc)} - {kc(hi_kc)})")
    print(f"Cesky modelovy naklad/odvracenou infekci: ~{kc(z['naklad_na_odvracenou'])} (v radu)")

    print("\n--- ASYMETRIE (kontext, NE pomer) ---")
    print(f"Rozpocet veznice (cely):   {kc(ROZPOCET_VEZENSTVI)} [OK]")
    print(f"  z toho ~74 % ~ {kc(0.74*ROZPOCET_VEZENSTVI)} odpovida {ZAVISLI_VE_VEZNICICH} "
          f"zavislym veznum (vetsina NE za drogovy TC)")
    print(f"Drogove priraditelne vydaje represe: {VYDAJE_REPRESE_DROGY_ROK} "
          f"[DOPLNIT ZDROJ - Zaostreno 6/2020]")
    print("Represe nema dolozeny merielny zdravotni vystup (Nagin 2013; NRC 2014)")
    print("  => nelze spocitat naklad na jednotku zdravotniho prinosu (jmenovatel chybi).")

    uloz_tornado(baseline, rows)
    print("\nHOTOVO.")


if __name__ == "__main__":
    main()
