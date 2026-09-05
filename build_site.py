# -*- coding: utf-8 -*-
"""Generates the static Prabha Varma site into ./site"""
import os, html

OUT = "site"
os.makedirs(OUT, exist_ok=True)

NAV = [
    ("index.html", "Home", "ഹോം"),
    ("works.html", "Works", "കൃതികൾ"),
    ("honours.html", "Honours", "പുരസ്കാരങ്ങൾ"),
    ("stage.html", "On Stage & Screen", "രംഗവേദിയിലും ചലച്ചിത്രത്തിലും"),
    ("writings.html", "Readings", "വായന"),
    ("about.html", "Life", "ജീവിതം"),
    ("contact.html", "Contact", "ബന്ധപ്പെടുക"),
]

def b(en, ml):
    """bilingual inline"""
    return f'<span class="en">{en}</span><span class="ml">{ml}</span>'

def page(fname, title_en, title_ml, body, desc_en):
    nav = "".join(
        f'<a href="{f}" class="{"active" if f==fname else ""}">{b(en, ml)}</a>'
        for f, en, ml in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title_en)} · Prabha Varma</title>
<meta name="description" content="{html.escape(desc_en)}">
<meta property="og:title" content="{html.escape(title_en)} · Prabha Varma">
<meta property="og:description" content="{html.escape(desc_en)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://prabhavarma.in/{fname if fname!="index.html" else ""}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300;1,6..72,400&family=Noto+Serif+Malayalam:wght@400;500;600&family=Manjari:wght@400;700&display=swap" rel="stylesheet">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="canonical" href="https://prabhavarma.in/{fname if fname!="index.html" else ""}">
<meta property="og:image" content="https://prabhavarma.in/images/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Prabha Varma",
  "alternateName": "പ്രഭാവർമ്മ",
  "jobTitle": ["Poet", "Lyricist", "Journalist"],
  "nationality": "Indian",
  "knowsLanguage": ["ml", "en"],
  "birthPlace": {{"@type": "Place", "name": "Thiruvalla, Kerala, India"}},
  "award": ["Saraswati Samman (2023)", "Sahitya Akademi Award (2016)", "National Film Award for Best Lyrics (Rajat Kamal)", "Vayalar Award (2013)", "Kerala Sahitya Akademi Award"],
  "url": "https://prabhavarma.in/",
  "image": "https://prabhavarma.in/images/portrait.jpg",
  "sameAs": ["https://en.wikipedia.org/wiki/Prabha_Varma", "https://www.wikidata.org/wiki/Q16136840"]
}}
</script>
</head>
<body>
<header class="site-header">
  <a class="brand" href="index.html"><span class="brand-ml">പ്രഭാവർമ്മ</span><span class="brand-en">Prabha Varma</span></a>
  <nav class="site-nav">{nav}</nav>
  <div class="lang-switch" role="group" aria-label="Language">
    <button data-lang="en" class="on">EN</button><span>/</span><button data-lang="ml">മലയാളം</button>
  </div>
  <button class="menu-btn" aria-label="Menu">☰</button>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="foot-grid">
    <div>
      <p class="foot-name">Prabha Varma <span class="dot">·</span> പ്രഭാവർമ്മ</p>
      <p class="foot-note">{b("Poet · Lyricist · Journalist. Saraswati Samman · Sahitya Akademi Award · Rajat Kamal.",
                            "കവി · ഗാനരചയിതാവ് · മാധ്യമപ്രവർത്തകൻ. സരസ്വതി സമ്മാൻ · കേന്ദ്ര സാഹിത്യ അക്കാദമി പുരസ്കാരം · രജത കമലം.")}</p>
    </div>
    <div class="foot-links">{nav}</div>
    <div>
      <p class="foot-note">{b("This site is maintained by the Prabha Varma Literary Archive, on behalf of the poet's family and readers. Texts and images are © the author and are reproduced with permission.",
                            "കവിയുടെ കുടുംബത്തിനും വായനക്കാർക്കും വേണ്ടി പ്രഭാവർമ്മ സാഹിത്യ ആർക്കൈവ് ആണ് ഈ വെബ്‌സൈറ്റ് പരിപാലിക്കുന്നത്. കൃതികളും ചിത്രങ്ങളും ഗ്രന്ഥകർത്താവിന്റെ അനുമതിയോടെ.")}</p>
      <p class="foot-note small">© 2026 Prabha Varma. All rights reserved.</p>
    </div>
  </div>
</footer>
<script src="site.js"></script>
</body>
</html>"""

# ---------------------------------------------------------------- CONTENT
def sec_head(num, en, ml, sub_en="", sub_ml=""):
    sub = f'<p class="sec-sub">{b(sub_en, sub_ml)}</p>' if sub_en else ""
    return f'<div class="sec-head"><span class="sec-num">{num}</span><h2>{b(en, ml)}</h2>{sub}</div>'

# ---- HOME
home = f"""
<section class="hero">
  <div class="hero-text">
    <p class="eyebrow">{b("Poet · Lyricist · Journalist", "കവി · ഗാനരചയിതാവ് · മാധ്യമപ്രവർത്തകൻ")}</p>
    <h1><span class="h1-ml">പ്രഭാവർമ്മ</span><span class="h1-en">Prabha Varma</span></h1>
    <p class="hero-lede">{b(
      "Malayalam poet whose novels in verse — <em>Shyama Madhavam</em>, <em>Kanal Chilambu</em>, <em>Roudra Sathwikam</em>, <em>Adayala Vakyam</em> — brought the long narrative poem back to the centre of Indian literature. Recipient of the Saraswati Samman, the Sahitya Akademi Award and the National Film Award for lyrics.",
      "<em>ശ്യാമമാധവം</em>, <em>കനൽച്ചിലമ്പ്</em>, <em>രൗദ്രസാത്വികം</em>, <em>അടയാളവാക്യം</em> എന്നീ കാവ്യാഖ്യായികകളിലൂടെ ദീർഘകാവ്യത്തെ ഭാരതീയ സാഹിത്യത്തിന്റെ കേന്ദ്രത്തിലേക്ക് തിരികെ കൊണ്ടുവന്ന മലയാള കവി. സരസ്വതി സമ്മാൻ, കേന്ദ്ര സാഹിത്യ അക്കാദമി പുരസ്കാരം, ഗാനരചനയ്ക്കുള്ള ദേശീയ ചലച്ചിത്ര പുരസ്കാരം എന്നിവ നേടിയ എഴുത്തുകാരൻ.")}</p>
    <div class="hero-cta">
      <a class="btn" href="works.html">{b("Explore the works", "കൃതികൾ")}</a>
      <a class="btn ghost" href="writings.html">{b("Read an excerpt", "ഒരു ഭാഗം വായിക്കാം")}</a>
    </div>
  </div>
  <figure class="hero-portrait">
    <div class="portrait-frame">
      <img src="images/portrait.jpg" alt="Prabha Varma" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
      <div class="portrait-placeholder"><span>Portrait</span></div>
    </div>
    <figcaption>{b("Thiruvananthapuram", "തിരുവനന്തപുരം")}</figcaption>
  </figure>
</section>

<section class="honour-strip" aria-label="Major honours">
  <div><b>{b("Saraswati Samman", "സരസ്വതി സമ്മാൻ")}</b><span>2023 · <em>Roudra Sathwikam</em></span></div>
  <div><b>{b("Sahitya Akademi Award", "കേന്ദ്ര സാഹിത്യ അക്കാദമി")}</b><span>2016 · <em>Shyama Madhavam</em></span></div>
  <div><b>{b("National Film Award", "രജത കമലം")}</b><span>{b("Best Lyrics", "മികച്ച ഗാനരചന")} · <em>Kolaambi</em></span></div>
  <div><b>{b("Vayalar Award", "വയലാർ അവാർഡ്")}</b><span>2013 · <em>Shyama Madhavam</em></span></div>
  <div><b>{b("70+ honours", "70-ലധികം പുരസ്കാരങ്ങൾ")}</b><span>{b("in literature, lyrics, music and media", "സാഹിത്യം, ഗാനം, സംഗീതം, മാധ്യമം")}</span></div>
</section>

<section class="verse-band">
  <blockquote>
    <p class="en">Flocks of birds come from afar,<br>gathering together for a while.<br>Roost on the branches of a tree,<br>then fly away without a trace.</p>
    <p class="ml">[ശ്യാമമാധവം — മൂലം മലയാളത്തിൽ ചേർക്കേണ്ട ഭാഗം]</p>
    <cite>{b("— <em>Lament of the Dusky Lord</em> (Shyama Madhavam), translated from the Malayalam", "— <em>ശ്യാമമാധവം</em>")}</cite>
  </blockquote>
</section>

<section class="sec">
  {sec_head("01", "Four novels in verse", "നാല് കാവ്യാഖ്യായികകൾ",
            "The <em>kavyakhyayika</em> — a full-length story told entirely in metre — is the form Prabha Varma made his own.",
            "പൂർണ്ണമായും വൃത്തത്തിൽ പറയുന്ന കഥ — കാവ്യാഖ്യായിക — പ്രഭാവർമ്മ സ്വന്തമാക്കിയ രൂപമാണ്.")}
  <div class="works-grid">
    <a class="work-card" href="works.html#shyama">
      <img class="card-cover" src="images/covers/shyama-madhavam.jpg" alt="" loading="lazy">
      <span class="work-year">2010s</span>
      <h3>Shyama Madhavam<small>ശ്യാമമാധവം</small></h3>
      <p>{b("Krishna's last hours, told from inside his own remorse. Fifteen chapters; Sahitya Akademi Award, Vayalar Award, Kerala Sahitya Akademi Award. Chosen by the State Library Council as the book of the decade. Translated into ten languages.",
           "കൃഷ്ണന്റെ അവസാന നിമിഷങ്ങൾ, അദ്ദേഹത്തിന്റെ തന്നെ പശ്ചാത്താപത്തിലൂടെ. പതിനഞ്ച് അധ്യായങ്ങൾ; കേന്ദ്ര-കേരള സാഹിത്യ അക്കാദമി പുരസ്കാരങ്ങൾ, വയലാർ അവാർഡ്. ദശകത്തിലെ മികച്ച പുസ്തകം. പത്ത് ഭാഷകളിലേക്ക് പരിഭാഷ.")}</p>
      <span class="work-eng">Lament of the Dusky Lord</span>
    </a>
    <a class="work-card" href="works.html#kanal">
      <img class="card-cover" src="images/covers/anklet-of-fire.jpg" alt="" loading="lazy">
      <span class="work-year">Novella</span>
      <h3>Kanal Chilambu<small>കനൽച്ചിലമ്പ്</small></h3>
      <p>{b("Seven chapters of love, power, revenge and a riddle older than Kalidasa: why did the milkmaid laugh when her pot of milk broke? Staged professionally on more than 500 stages across Kerala.",
           "പ്രണയം, അധികാരം, പ്രതികാരം — കാളിദാസനേക്കാൾ പഴക്കമുള്ള ഒരു കടങ്കഥയും: പാൽക്കുടം പൊട്ടിയപ്പോൾ ഗോപിക എന്തിനു ചിരിച്ചു? കേരളത്തിലുടനീളം 500-ലധികം വേദികളിൽ നാടകമായി.")}</p>
      <span class="work-eng">Anklet of Fire</span>
    </a>
    <a class="work-card" href="works.html#roudra">
      <img class="card-cover" src="images/covers/roudra-sathwikam.jpg" alt="" loading="lazy">
      <span class="work-year">2022</span>
      <h3>Roudra Sathwikam<small>രൗദ്രസാത്വികം</small></h3>
      <p>{b("Art against power, the individual against the state. Kalidasa reimagined outside history. Saraswati Samman, 2023 — the first Malayalam work to win it in twelve years.",
           "കലയും അധികാരവും, വ്യക്തിയും രാഷ്ട്രവും തമ്മിലുള്ള സംഘർഷം. ചരിത്രത്തിനു പുറത്ത് പുനർഭാവന ചെയ്ത കാളിദാസൻ. 2023-ലെ സരസ്വതി സമ്മാൻ — പന്ത്രണ്ട് വർഷത്തിനു ശേഷം മലയാളത്തിന്.")}</p>
      <span class="work-eng">Ferocious Piety</span>
    </a>
    <a class="work-card" href="works.html#adayala">
      <span class="work-year">Recent</span>
      <h3>Adayala Vakyam<small>അടയാളവാക്യം</small></h3>
      <p>{b("A murder, a mind, and modern medicine — perhaps India's only detective novel written in verse.",
           "ഒരു കൊലപാതകം, ഒരു മനസ്സ്, ആധുനിക വൈദ്യശാസ്ത്രം — ഒരുപക്ഷേ ഇന്ത്യയിലെ ഏക പദ്യ കുറ്റാന്വേഷണ നോവൽ.")}</p>
      <span class="work-eng">Novel in verse</span>
    </a>
  </div>
</section>

<section class="sec two-col">
  <div>
    {sec_head("02", "The poet, by his peers", "സമകാലികരുടെ വാക്കുകളിൽ")}
    <div class="quote-stack">
      <blockquote class="peer"><p>{b("“He has inherited the subtle poetic richness of Vyloppilly Sreedhara Menon, who himself picked up the quality from Kumaran Asan.”", "“വൈലോപ്പിള്ളിയുടെ സൂക്ഷ്മമായ കാവ്യസമൃദ്ധി അദ്ദേഹത്തിനു കൈവന്നിരിക്കുന്നു — കുമാരനാശാനിൽനിന്ന് വൈലോപ്പിള്ളിക്കു ലഭിച്ചതു പോലെ.”")}</p><cite>O. N. V. Kurup, {b("Jnanpith laureate", "ജ്ഞാനപീഠ ജേതാവ്")}</cite></blockquote>
      <blockquote class="peer"><p>{b("“Prabha Varma is a born poet.”", "“പ്രഭാവർമ്മ ജന്മനാ കവിയാണ്.”")}</p><cite>Prof. M. Krishnan Nair</cite></blockquote>
      <blockquote class="peer"><p>{b("“He has demonstrated that it is still possible to be modern in sensibility and diction while following the natural metrical formation that is intrinsic to the language.”", "“ഭാഷയ്ക്കു സഹജമായ വൃത്തഘടന പിന്തുടർന്നുകൊണ്ടുതന്നെ ഭാവുകത്വത്തിലും ഭാഷയിലും ആധുനികനാകാൻ കഴിയുമെന്ന് അദ്ദേഹം തെളിയിച്ചു.”")}</p><cite>K. Jayakumar</cite></blockquote>
    </div>
  </div>
  <div>
    {sec_head("03", "Beyond the page", "കടലാസിനപ്പുറം")}
    <ul class="fact-list">
      <li><b>{b("Songs", "ഗാനങ്ങൾ")}</b>{b("National Film Award (Rajat Kamal) for <em>Kolaambi</em>; Kerala State Award for lyrics in 2006, 2013 and 2017; “Oru Chempaneer Poo…” and “Kanna Nee Ninaippathare…” each crossed twenty million views within a year.",
                                    "<em>കോളാമ്പി</em>ക്ക് ദേശീയ പുരസ്കാരം (രജത കമലം); 2006, 2013, 2017 വർഷങ്ങളിൽ സംസ്ഥാന പുരസ്കാരം; “ഒരു ചെമ്പനീർ പൂ…”, “കണ്ണാ നീ നിനൈപ്പതാരേ…” എന്നിവ ഒരു വർഷത്തിനകം രണ്ടു കോടിയിലധികം കാഴ്ചകൾ.")}</li>
      <li><b>{b("Carnatic music", "കർണാടക സംഗീതം")}</b>{b("More than sixty <em>kritis</em> and two dozen Mohiniyattam <em>padams</em>; full-length thematic concerts of Prabha Varma Kritis have been staged across Kerala; honoured at Rashtrapati Bhavan by President Pranab Mukherjee in 2016.",
                                                 "അറുപതിലധികം കൃതികൾ, രണ്ടു ഡസനിലധികം മോഹിനിയാട്ട പദങ്ങൾ; പ്രഭാവർമ്മ കൃതികളുടെ പ്രത്യേക കച്ചേരികൾ; 2016-ൽ രാഷ്ട്രപതി പ്രണബ് മുഖർജി രാഷ്ട്രപതി ഭവനിൽ ആദരിച്ചു.")}</li>
      <li><b>{b("Stage", "രംഗവേദി")}</b>{b("<em>Shyama Madhavam</em> and <em>Kanal Chilambu</em> as professional plays directed by M. Santhosh — more than 300 and 500 performances respectively; mural exhibitions, classical dance productions and a novel written in response to his work.",
                                         "എം. സന്തോഷ് സംവിധാനം ചെയ്ത <em>ശ്യാമമാധവം</em>, <em>കനൽച്ചിലമ്പ്</em> നാടകങ്ങൾ — യഥാക്രമം 300, 500-ലധികം വേദികളിൽ; ചുവർച്ചിത്ര പ്രദർശനങ്ങൾ, നൃത്താവിഷ്കാരങ്ങൾ.")}</li>
      <li><b>{b("Journalism", "മാധ്യമപ്രവർത്തനം")}</b>{b("Covered both houses of Parliament for over a decade; Director (News) of Kairali/People TV, 2001–2010; Kerala State Award for best general reporting, 1996. Later Media Secretary to the Chief Minister of Kerala.",
                                                "ഒരു ദശകത്തിലധികം പാർലമെന്റിന്റെ ഇരുസഭകളും റിപ്പോർട്ട് ചെയ്തു; കൈരളി/പീപ്പിൾ ടിവി ന്യൂസ് ഡയറക്ടർ 2001–2010; മികച്ച റിപ്പോർട്ടിങ്ങിനുള്ള സംസ്ഥാന പുരസ്കാരം 1996. പിന്നീട് മുഖ്യമന്ത്രിയുടെ മീഡിയ സെക്രട്ടറി.")}</li>
    </ul>
    <a class="link-arrow" href="stage.html">{b("On stage and screen →", "രംഗവേദിയിലും ചലച്ചിത്രത്തിലും →")}</a>
  </div>
</section>

<section class="photo-band">
  <figure><img src="images/library.jpg" alt="Prabha Varma reading in his library" loading="lazy"><figcaption>{b("In the study, Thiruvananthapuram", "പഠനമുറിയിൽ, തിരുവനന്തപുരം")}</figcaption></figure>
  <figure><img src="images/rashtrapati-bhavan.jpg" alt="Honoured by President Pranab Mukherjee at Rashtrapati Bhavan" loading="lazy"><figcaption>{b("Rashtrapati Bhavan, 2016 — honoured by President Pranab Mukherjee", "രാഷ്ട്രപതി ഭവൻ, 2016 — രാഷ്ട്രപതി പ്രണബ് മുഖർജി ആദരിക്കുന്നു")}</figcaption></figure>
  <figure><img src="images/recital-choir.jpg" alt="Prabha Varma reciting with a choir" loading="lazy"><figcaption>{b("Reciting with a chorus, Mar Ivanios College", "മാർ ഇവാനിയോസ് കോളേജിൽ കാവ്യാലാപനം")}</figcaption></figure>
</section>

<section class="sec cta-band">
  <div>
    <p class="eyebrow">{b("For juries, editors and researchers", "പുരസ്കാര സമിതികൾക്കും ഗവേഷകർക്കും")}</p>
    <h2>{b("A verified record of the work", "കൃതികളുടെ ആധികാരിക രേഖ")}</h2>
    <p>{b("Complete bibliography, dated list of honours, translations, adaptations and downloadable biographical notes in English and Malayalam.",
         "സമ്പൂർണ്ണ ഗ്രന്ഥസൂചി, തീയതി സഹിതം പുരസ്കാരപ്പട്ടിക, പരിഭാഷകൾ, ആവിഷ്കാരങ്ങൾ, ഇംഗ്ലീഷിലും മലയാളത്തിലും ജീവചരിത്രക്കുറിപ്പുകൾ.")}</p>
  </div>
  <div class="cta-links">
    <a class="btn" href="honours.html">{b("Honours", "പുരസ്കാരങ്ങൾ")}</a>
    <a class="btn ghost" href="contact.html">{b("Press & permissions", "മാധ്യമം · അനുമതി")}</a>
  </div>
</section>
"""

# ---- WORKS
def booklist(items):
    return "<ol class='booklist'>" + "".join(
        f"<li><span class='bk-title'>{t}</span>{('<span class=bk-ml>'+m+'</span>') if m else ''}<span class='bk-pub'>{p}</span></li>"
        for t, m, p in items) + "</ol>"

works = f"""
<section class="page-head">
  <p class="eyebrow">{b("Bibliography", "ഗ്രന്ഥസൂചി")}</p>
  <h1>{b("Works", "കൃതികൾ")}</h1>
  <p class="lede">{b("Over forty books across five decades: four novels in verse, twelve collections of poems, three novels, criticism, memoir, travel, media studies and a volume of Carnatic compositions. All Malayalam titles are published by DC Books unless noted.",
                    "അഞ്ചു പതിറ്റാണ്ടിൽ നാൽപതിലധികം പുസ്തകങ്ങൾ: നാല് കാവ്യാഖ്യായികകൾ, പന്ത്രണ്ട് കവിതാസമാഹാരങ്ങൾ, മൂന്ന് നോവലുകൾ, നിരൂപണം, ഓർമ്മക്കുറിപ്പുകൾ, യാത്ര, മാധ്യമപഠനം, കർണാടക സംഗീത കൃതികൾ.")}</p>
</section>

<section class="sec">
  {sec_head("01", "Novels in verse", "കാവ്യാഖ്യായികകൾ")}
  <article class="book" id="shyama">
    <div class="book-cover"><img src="images/covers/shyama-madhavam.jpg" alt="" onerror="this.parentElement.classList.add('nocover')"><span>ശ്യാമമാധവം</span></div>
    <div>
      <h3>Shyama Madhavam <small>ശ്യാമമാധവം · <em>Lament of the Dusky Lord</em></small></h3>
      <p>{b("A fifteen-chapter narrative poem set in the last moments of Krishna's earthly life, after the hunter's arrow finds his foot. Arjuna, Karna, Dhritarashtra, Jayadratha, Ashwatthama, Draupadi, Rukmini and Radha return to his consciousness one by one, each reopening a moral debt. The poem argues that Krishna's life was not a sequence of ecstasies but of agonies — and that his courage lay in facing them. It ranges across dandakas and classical metres while speaking in a fully modern voice.",
           "വേടന്റെ അമ്പ് കാലിൽ തറച്ച ശേഷമുള്ള കൃഷ്ണന്റെ അവസാന നിമിഷങ്ങളിൽ നടക്കുന്ന പതിനഞ്ച് അധ്യായങ്ങളുള്ള കാവ്യാഖ്യായിക. അർജുനൻ, കർണ്ണൻ, ധൃതരാഷ്ട്രർ, ജയദ്രഥൻ, അശ്വത്ഥാമാവ്, ദ്രൗപദി, രുക്മിണി, രാധ — ഓരോരുത്തരായി ബോധത്തിലേക്ക് മടങ്ങിവരുന്നു. കൃഷ്ണജീവിതം ആനന്ദങ്ങളുടെയല്ല, വേദനകളുടെ പരമ്പരയായിരുന്നു എന്ന് കാവ്യം വാദിക്കുന്നു.")}</p>
      <ul class="tags"><li>Sahitya Akademi Award 2016</li><li>Vayalar Award 2013</li><li>Kerala Sahitya Akademi Award</li><li>Malayattoor Award 2013</li><li>{b("Book of the Decade — Kerala State Library Council, 2020", "ദശകത്തിലെ പുസ്തകം — സംസ്ഥാന ലൈബ്രറി കൗൺസിൽ 2020")}</li><li>{b("Translated into 10 languages incl. English, Hindi, Sanskrit, Tamil, Telugu, Kannada, Assamese", "10 ഭാഷകളിൽ പരിഭാഷ")}</li><li>{b("Only poetry title in Malayala Manorama's 25 books of the quarter-century (2026)", "മനോരമയുടെ കാൽനൂറ്റാണ്ടിലെ 25 പുസ്തകങ്ങളിൽ ഏക കവിത (2026)")}</li></ul>
    </div>
  </article>
  <article class="book" id="kanal">
    <div class="book-cover"><img src="images/covers/anklet-of-fire.jpg" alt="" onerror="this.parentElement.classList.add('nocover')"><span>കനൽച്ചിലമ്പ്</span><em class="cover-note">Anklet of Fire — English edition</em></div>
    <div>
      <h3>Kanal Chilambu <small>കനൽച്ചിലമ്പ് · <em>Anklet of Fire</em></small></h3>
      <p>{b("A novella in verse in seven chapters — love, lust, intrigue, power, revenge and incest, the full apparatus of tragedy — built around a riddle said to date from Kalidasa's time: why did the milkmaid laugh when her pot of milk fell and broke? Dr M. Leelavathy's essay on the work, <em>The Inscrutability of Existence</em>, reads it as a poem about the mind's compulsion to decode what cannot be decoded.",
           "ഏഴ് അധ്യായങ്ങളുള്ള ഖണ്ഡകാവ്യാഖ്യായിക — പ്രണയം, കാമം, കുതന്ത്രം, അധികാരം, പ്രതികാരം. കാളിദാസകാലത്തെ ഒരു കടങ്കഥയെ ചുറ്റിപ്പറ്റി: പാൽക്കുടം വീണുടഞ്ഞപ്പോൾ ഗോപിക എന്തിനു ചിരിച്ചു? ഡോ. എം. ലീലാവതിയുടെ പ്രശസ്ത പഠനം ഈ കൃതിയെക്കുറിച്ചാണ്.")}</p>
      <ul class="tags"><li>{b("Professional drama — 500+ stages", "നാടകം — 500-ലധികം വേദികൾ")}</li><li>{b("Translated into English, Sanskrit and other languages", "ഇംഗ്ലീഷ്, സംസ്കൃതം തുടങ്ങിയ ഭാഷകളിൽ")}</li><li>{b("Inspired the novel <em>Chilamboli</em> by Shobha Varma and a mural exhibition series", "ശോഭാ വർമ്മയുടെ <em>ചിലമ്പൊലി</em> എന്ന നോവലിനും ചുവർച്ചിത്ര പ്രദർശനങ്ങൾക്കും പ്രേരണ")}</li></ul>
    </div>
  </article>
  <article class="book" id="roudra">
    <div class="book-cover"><img src="images/covers/roudra-sathwikam.jpg" alt="" onerror="this.parentElement.classList.add('nocover')"><span>രൗദ്രസാത്വികം</span></div>
    <div>
      <h3>Roudra Sathwikam <small>രൗദ്രസാത്വികം · <em>Ferocious Piety</em></small></h3>
      <p>{b("Published 2022. The title fuses two opposites — <em>roudram</em> (ferocity) and <em>sathwikam</em> (piety) — and the poem lives in the space between them. Kalidasa is lifted out of history and placed inside a story about art and power, the individual and the state, peace and violence, priestly ethos and Machiavellian scheming. The K. K. Birla Foundation's citation praised a work that “transcends the concept of time and space” in addressing the predicament of dharma and adharma.",
           "2022-ൽ പ്രസിദ്ധീകരിച്ചു. രൗദ്രം, സാത്വികം എന്നീ വിപരീതങ്ങളെ സംയോജിപ്പിച്ച ശീർഷകം. ചരിത്രത്തിൽനിന്ന് അടർത്തിയെടുത്ത കാളിദാസൻ — കലയും അധികാരവും, വ്യക്തിയും രാഷ്ട്രവും, സമാധാനവും ഹിംസയും തമ്മിലുള്ള സംഘർഷത്തിന്റെ കഥയിൽ. ധർമ്മ-അധർമ്മ സന്ദിഗ്ധതയെ കാലദേശാതീതമായി സമീപിക്കുന്ന കൃതി എന്ന് ബിർള ഫൗണ്ടേഷന്റെ പ്രശംസ.")}</p>
      <ul class="tags"><li>Saraswati Samman 2023</li><li>{b("English translation: <em>Ferocious Piety</em> (DC Books)", "ഇംഗ്ലീഷ് പരിഭാഷ: <em>Ferocious Piety</em>")}</li></ul>
    </div>
  </article>
  <article class="book" id="adayala">
    <div class="book-cover"><img src="images/covers/adayala-vakyam.jpg" alt="" onerror="this.parentElement.classList.add('nocover')"><span>അടയാളവാക്യം</span></div>
    <div>
      <h3>Adayala Vakyam <small>അടയാളവാക്യം</small></h3>
      <p>{b("The fourth <em>kavyakhyayika</em>: the labyrinthine psyche behind the murder of an innocent woman, set against psychology and modern medical science. Very possibly the only detective novel in verse written in India.",
           "നാലാമത്തെ കാവ്യാഖ്യായിക: ഒരു നിരപരാധിയായ സ്ത്രീയുടെ കൊലപാതകത്തിനു പിന്നിലെ മനസ്സിന്റെ ഇരുണ്ട വഴികൾ — മനഃശാസ്ത്രത്തിന്റെയും ആധുനിക വൈദ്യശാസ്ത്രത്തിന്റെയും പശ്ചാത്തലത്തിൽ. ഇന്ത്യയിലെ ഏക പദ്യ കുറ്റാന്വേഷണ നോവൽ എന്നു പറയാം.")}</p>
    </div>
  </article>
</section>

<section class="photo-band two">
  <figure><img src="images/kanal-chilambu-release.jpg" alt="Release of Kanal Chilambu" loading="lazy"><figcaption>{b("Chief Minister Pinarayi Vijayan releases <em>Kanal Chilambu</em> by handing the first copy to the poet Sugathakumari; ONV Kurup applauds at left.", "മുഖ്യമന്ത്രി പിണറായി വിജയൻ <em>കനൽച്ചിലമ്പ്</em> പ്രകാശനം ചെയ്യുന്നു — ആദ്യ പ്രതി കവയിത്രി സുഗതകുമാരിക്ക്; ഇടത് ഒ. എൻ. വി. കുറുപ്പ്.")}</figcaption></figure>
  <figure><img src="images/anklet-of-fire-release-delhi.jpg" alt="Release of Anklet of Fire at Kerala House, New Delhi" loading="lazy"><figcaption>{b("Governor Arif Mohammed Khan releases <em>Anklet of Fire</em> at Kerala House, New Delhi.", "ഗവർണർ ആരിഫ് മുഹമ്മദ് ഖാൻ <em>Anklet of Fire</em> കേരള ഹൗസിൽ, ന്യൂഡൽഹിയിൽ പ്രകാശനം ചെയ്യുന്നു.")}</figcaption></figure>
</section>

<section class="sec">
  {sec_head("02", "Shyama Madhavam in other languages", "ശ്യാമമാധവം മറ്റു ഭാഷകളിൽ",
            "The verse novel has been translated into ten languages. Editions shown: English (Indus), Hindi, Telugu and Kannada (Sahitya Akademi), and the Sanskrit-titled edition edited by Dr Dharmaraj Adat.",
            "പത്തു ഭാഷകളിലേക്ക് പരിഭാഷപ്പെടുത്തിയ കാവ്യാഖ്യായിക. ഇവിടെ: ഇംഗ്ലീഷ് (ഇൻഡസ്), ഹിന്ദി, തെലുങ്ക്, കന്നഡ (സാഹിത്യ അക്കാദമി), ഡോ. ധർമ്മരാജ് അടാട്ട് എഡിറ്റ് ചെയ്ത പതിപ്പ്.")}
  <div class="shelf">
    <figure><img src="images/covers/lament-of-the-dusky-lord.jpg" alt="Lament of the Dusky Lord" loading="lazy"><figcaption><b>Lament of the Dusky Lord</b><span>English · tr. Anitha Madhavan · Indus</span></figcaption></figure>
    <figure><img src="images/covers/shyama-madhavam-hindi.jpg" alt="Shyam Madhavam, Hindi" loading="lazy"><figcaption><b>श्याम माधवम्</b><span>Hindi · tr. A. Aravindakshan · Sahitya Akademi</span></figcaption></figure>
    <figure><img src="images/covers/shyama-madhavam-telugu.jpg" alt="Shyama Madhaviyam, Telugu" loading="lazy"><figcaption><b>శ్యామ మాధవీయం</b><span>Telugu · tr. L. R. Swamy · Sahitya Akademi</span></figcaption></figure>
    <figure><img src="images/covers/shyama-madhavam-kannada.jpg" alt="Shyama Madhava, Kannada" loading="lazy"><figcaption><b>ಶ್ಯಾಮ ಮಾಧವ</b><span>Kannada · tr. Ashok Kumar · Sahitya Akademi</span></figcaption></figure>
    <figure><img src="images/covers/karumai-nirak-kannan-tamil.jpg" alt="Karumai Nirak Kannan, Tamil" loading="lazy"><figcaption><b>கருமை நிறக் கண்ணன்</b><span>Tamil</span></figcaption></figure>
    <figure><img src="images/covers/syamamadhavam-adat.jpg" alt="Syamamadhavam, edited by Dr Dharmaraj Adat" loading="lazy"><figcaption><b>Śyāmamādhavam</b><span>ed. Dr Dharmaraj Adat</span></figcaption></figure>
    <figure><img src="images/covers/ferocious-piety.jpg" alt="Ferocious Piety" loading="lazy"><figcaption><b>Ferocious Piety</b><span>Roudra Sathwikam · English · tr. by the poet · Folio</span></figcaption></figure>
  </div>
</section>

<section class="sec">
  {sec_head("03", "From the shelf", "ഗ്രന്ഥശാലയിൽ നിന്ന്")}
  <div class="shelf small">
    <figure><img src="images/covers/aparigraham.jpg" alt="Aparigraham" loading="lazy"><figcaption><b>അപരിഗ്രഹം</b><span>Poems · Mathrubhumi</span></figcaption></figure>
    <figure><img src="images/covers/kalaprayaga.jpg" alt="Kalaprayaga" loading="lazy"><figcaption><b>കാലപ്രയാഗ</b><span>Poems · DC Books</span></figcaption></figure>
    <figure><img src="images/covers/chandana-nazhi.jpg" alt="Chandana Nazhi" loading="lazy"><figcaption><b>ചന്ദനനാഴി</b><span>Poems · Mulberry</span></figcaption></figure>
    <figure><img src="images/covers/avicharitham.jpg" alt="Avicharitham" loading="lazy"><figcaption><b>അവിചാരിതം</b><span>Poems · DC Books</span></figcaption></figure>
    <figure><img src="images/covers/ottikkoduthaalum.jpg" alt="Ottikkoduthaalum Enneyen Snehame" loading="lazy"><figcaption><b>ഒറ്റിക്കൊടുത്താലും എന്നെയെൻ സ്നേഹമേ</b><span>Poems · DC Books</span></figcaption></figure>
    <figure><img src="images/covers/ponnin-kolussu.jpg" alt="Ponnin Kolussu" loading="lazy"><figcaption><b>പൊന്നിൻ കൊലുസ്സ്</b><span>Poems · DC Books</span></figcaption></figure>
    <figure><img src="images/covers/manjinodu-veyil.jpg" alt="Manjinodu Veyil Enna Poleyum" loading="lazy"><figcaption><b>മഞ്ഞിനോട് വെയിൽ എന്ന പോലെയും</b><span>Poems · SPCS, 2010</span></figcaption></figure>
    <figure><img src="images/covers/prabha-varmayude-kavithakal.jpg" alt="Prabha Varmayude Kavithakal" loading="lazy"><figcaption><b>പ്രഭാവർമ്മയുടെ കവിതകൾ</b><span>Collected poems · DC Books</span></figcaption></figure>
    <figure><img src="images/covers/kalapasam.jpg" alt="Kalapasam" loading="lazy"><figcaption><b>കാലപാശം</b><span>Novel · DC Books</span></figcaption></figure>
    <figure><img src="images/covers/after-the-aftermath.jpg" alt="After the Aftermath" loading="lazy"><figcaption><b>After the Aftermath</b><span>Novel in English · Indus</span></figcaption></figure>
    <figure><img src="images/covers/rathiyude-kavyapadam.jpg" alt="Rathiyude Kavyapadam" loading="lazy"><figcaption><b>രതിയുടെ കാവ്യപദം</b><span>Criticism · DC Books</span></figcaption></figure>
    <figure><img src="images/covers/shakespeareum-vailoppilliyum.jpg" alt="Shakespeareum Vailoppilliyum" loading="lazy"><figcaption><b>ഷേക്സ്പിയറും വൈലോപ്പിള്ളിയും</b><span>Linguistics · Bookmark</span></figcaption></figure>
    <figure><img src="images/covers/thantree-laya-samanvitam.jpg" alt="Thantree Laya Samanvitam" loading="lazy"><figcaption><b>തന്ത്രീലയസമന്വിതം</b><span>Criticism</span></figcaption></figure>
    <figure><img src="images/covers/kavya-prabandhangal.jpg" alt="Prabha Varmayude Kavya Prabandhangal" loading="lazy"><figcaption><b>പ്രഭാവർമ്മയുടെ കാവ്യപ്രബന്ധങ്ങൾ</b><span>Essays</span></figcaption></figure>
    <figure><img src="images/covers/dalamarmaram.jpg" alt="Dalamarmaram" loading="lazy"><figcaption><b>ദളമർമ്മരം</b><span>Memoir · Saindhava</span></figcaption></figure>
    <figure><img src="images/covers/sandehiyude-ekanthayatra.jpg" alt="Sandehiyude Ekantha Yatra" loading="lazy"><figcaption><b>സന്ദേഹിയുടെ ഏകാന്തയാത്ര</b><span>Memoir</span></figcaption></figure>
    <figure><img src="images/covers/shyama-madhavam-rose-edition.jpg" alt="Shyama Madhavam, later edition" loading="lazy"><figcaption><b>ശ്യാമമാധവം</b><span>Later edition · DC Books</span></figcaption></figure>
  </div>
</section>

<section class="sec cols-2">
  <div>
    {sec_head("04", "Collections of poems", "കവിതാസമാഹാരങ്ങൾ")}
    {booklist([
      ("Souparnika", "സൗപർണിക", "DC Books, 1990 · Vyloppilli Award, Ankanam Award"),
      ("Arkkapoornima", "അർക്കപൂർണിമ", "DC Books · Kerala Sahitya Akademi Award"),
      ("Chandana Nazhi", "ചന്ദനനാഴി", "Mulberry"),
      ("Kalaprayaga", "കാലപ്രയാഗ", "DC Books"),
      ("Ardram", "ആർദ്രം", "DC Books"),
      ("Manjinodu Veyil Enna Poleyum", "മഞ്ഞിനോട് വെയിൽ എന്ന പോലെയും", "SPCS"),
      ("Aparigraham", "അപരിഗ്രഹം", "Mathrubhumi"),
      ("Ponnin Kolussu", "പൊന്നിൻ കൊലുസ്സ്", "DC Books"),
      ("Avicharitham", "അവിചാരിതം", "DC Books"),
      ("Ottikkoduthaalum Enneyen Snehame", "ഒറ്റിക്കൊടുത്താലും എന്നെയെൻ സ്നേഹമേ", "DC Books"),
      ("Prabha Varmayude Thiranjedutha Kavithakal", "പ്രഭാവർമ്മയുടെ തിരഞ്ഞെടുത്ത കവിതകൾ", "DC Books"),
      ("Pranayathinte Kaavya Pusthakam", "പ്രണയത്തിന്റെ കാവ്യപുസ്തകം", "DC Books"),
    ])}
    {sec_head("05", "Novels", "നോവലുകൾ")}
    {booklist([
      ("After the Aftermath", "", "English · Indus Publishers, Bangalore"),
      ("Kalapasam", "കാലപാശം", "DC Books"),
      ("Shadkalam", "ഷഡ്കാലം", "DC Books"),
    ])}
    {sec_head("06", "Translations of his work", "പരിഭാഷകൾ")}
    {booklist([
      ("Lament of the Dusky Lord", "", "English · DC Books"),
      ("Anklet of Fire", "", "English · DC Books"),
      ("Ferocious Piety", "", "English · DC Books"),
      ("Sixth Tempo", "", "English"),
      ("Shyama Madhavam", "", "Hindi · Sanskrit · Tamil (<em>Karumai Nirak Kannan</em>) · Telugu · Kannada · Assamese"),
    ])}
  </div>
  <div>
    {sec_head("07", "Criticism & essays", "നിരൂപണം · ഉപന്യാസം")}
    {booklist([
      ("Rathiyude Kavyapadam", "രതിയുടെ കാവ്യപദം", ""),
      ("Thantree Laya Samanvitam", "തന്ത്രീലയസമന്വിതം", ""),
      ("Paarayanathinte Reethibhedangal", "പാരായണത്തിന്റെ രീതിഭേദങ്ങൾ", ""),
      ("Kevalathvavum Bhavukathvavum", "കേവലത്വവും ഭാവുകത്വവും", ""),
      ("Sandehiyude Ekanthayatra", "സന്ദേഹിയുടെ ഏകാന്തയാത്ര", ""),
      ("Prabha Varmayude Kavya Prabandhangal", "പ്രഭാവർമ്മയുടെ കാവ്യപ്രബന്ധങ്ങൾ", ""),
      ("Enthukondu Fascism", "എന്തുകൊണ്ട് ഫാസിസം", "General essay"),
      ("Shakespeareum Vailoppilliyum", "ഷേക്സ്പിയറും വൈലോപ്പിള്ളിയും", "Linguistics"),
    ])}
    {sec_head("08", "Memoir & autobiography", "ഓർമ്മ · ആത്മകഥ")}
    {booklist([
      ("Dalamarmaram", "ദളമർമ്മരം", "Memoir"),
      ("Pin Nilaapaatha", "പിൻനിലാപ്പാത", "Autobiography, Part 1 (<em>Namami Manasa Shirasa</em>)"),
      ("Dil Se, Dilli Se", "ദിൽ സേ, ദില്ലി സേ", "Autobiography, Part 2"),
    ])}
    {sec_head("09", "Media, travel, music", "മാധ്യമം · യാത്ര · സംഗീതം")}
    {booklist([
      ("A Study on Culture and Electronic Media", "", "Media study"),
      ("Innilekkoru Jalakam", "ഇന്നിലേക്കൊരു ജാലകം", "Media study"),
      ("Diary of Malaysia", "", "Travelogue"),
      ("Tripura Diary", "", "Travelogue"),
      ("Prabha Varmayude Karnataka Sangeetha Kruthikal", "പ്രഭാവർമ്മയുടെ കർണാടക സംഗീത കൃതികൾ", "State Language Institute"),
    ])}
    {sec_head("10", "Studies on his work", "പഠനങ്ങൾ")}
    {booklist([
      ("Forty essays on Shyama Madhavam", "", "State Language Institute"),
      ("Two studies on the aesthetics of Shyama Madhavam and Kanal Chilambu", "", "Dr N. V. P. Unithiri"),
      ("Women writers on Kanal Chilambu", "", "ed. Sivadasan"),
      ("Kavithayude Raga Poornima — The Art and Vision of Prabha Varma", "", "Dr T. K. Santhosh Kumar"),
      ("Prabha Poornima", "", "Santha Tulasidharan"),
    ])}
  </div>
</section>
"""

# ---- HONOURS
poetry_awards = ["Saraswati Samman (2023, for <em>Roudra Sathwikam</em>)", "Sahitya Akademi Award — National Academy of Letters (2016, for <em>Shyama Madhavam</em>)", "Kerala Sahitya Akademi Award (for <em>Arkkapoornima</em>)", "Vayalar Award (2013)", "Vallathol Award", "Asan Prize", "Ulloor Award", "Vyloppilli Award (1990)", "Changampuzha Award (1997)", "Padma Prabha Award", "Krishnageethi Puraskar (1994)", "O. N. V. Award", "Sugatha Kumari Award", "G. Kumara Pillai Award (2015)", "Kerala State Library Council — Best Book of the Decade (2020)", "Edassery Award (2020)", "Mahakavi Pandalam Kerala Varma Award (2016)", "Mahakavi P. Kunhiraman Nair Award", "Venmani Award", "N. V. Krishna Warrier Award", "P. Kesavadev Award", "Mahakavi Vennikulam Award (2003)", "Premji Award (2012)", "Mullanezhi Award (2012)", "Abraham Madamakkal Literary Award", "State Bank of Travancore Literary Award", "Kunchupilla Award (1993)", "V. T. Kumaran Master Award", "V. V. K. Vaalath Award", "J. K. V. Award", "Kadammanitta Kavita Puraskaram", "A. P. Kalakkad Award (2006)", "Abu Dhabi Sakthi Award", "Mooloor Award (1995)", "Kadathanad Udayavarma Raja Puraskaram (2006)", "Ankanam Award", "Prof. Kozhissery Balaraman Award", "Ulloor Service Cooperative Bank Award", "Kannassa Award (2011)", "Siddhartha Sahitya Puraskaram", "Sri Ramotsava Literary Award", "Kunchan Nambiar Award", "Kovalam Kavikal Smriti Puraskaram", "Madhava Mudra Literary Award (Travancore Devaswom Board)", "Akshara Deepam Kavyashree Award", "Kompara Narayanan Nair Award", "Malayattoor Award (2013)", "Malayattoor Saraswati Award", "Bahrain Kerala Samajam Award", "Thikkurissi Award", "Prabodhini Sahitya Puraskaram", "Kollam Library Council Award", "Vayalar Rama Varma Samskarika Samiti Award", "Ezhumangalam Award", "T. S. Thirumumpu Award", "Khasak Award", "World Literature Forum Award", "Ekalavya Sahithya Puraskaram", "Azhakath Padmanabha Kuruppu Award", "Mahakavi P Puraskaram (1997)", "Kadavanad Award (1999)", "World Malayalee Council Award"]
lyric_awards = ["Rajat Kamal — National Film Award for Best Lyrics (<em>Kolaambi</em>)", "Kerala State Film Award for Best Lyricist — 2006, 2013, 2017 (four times in all)", "Kerala Sangeetha Nataka Akademi Award — three times", "Kerala State Award for Best Lyrics, professional drama — three times", "Film Critics Award — <em>Nagaravadhu</em> (2008), <em>Nadan</em> (2013)", "Satyajit Ray Foundation Award", "Adoor Bhasi Movie–TV Award", "Prem Nazeer Suhruth Samithi Award", "J. C. Daniel Foundation Award", "Kerala Vision Cinema Award", "Drishya Award (Malayalam television news)", "Big Screen Award"]
culture_awards = ["Honoured at Rashtrapati Bhavan by President Pranab Mukherjee for contribution to the performing arts (2016)", "Mar Gregorios Award", "Vakkom Maulavi Foundation Trust Award", "Prof. A. Sudhakaran Memorial Award", "Dr N. A. Karim Foundation Award", "Kerala Kala Puraskaram", "Kuwait Kala — V. Sambasivan Award", "Ambedkar National Award", "Srikanteswaram Award", "Indywood Award"]
media_awards = ["Kerala State Government Award for Best General Reporting (1996)", "K. C. Sebastian Award, Trivandrum Press Club (1988–90)", "Media Trust International Award — presented by Justice K. G. Balakrishnan", "K. C. Daniel Award", "K. Madhavan Kutty Award — best feature in English", "Dr B. R. Ambedkar Award", "Kerala State special mention for writings on electronic media"]

def award_ol(items):
    return "<ol class='award-list'>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

honours = f"""
<section class="page-head">
  <p class="eyebrow">{b("Recognition", "അംഗീകാരം")}</p>
  <h1>{b("Honours", "പുരസ്കാരങ്ങൾ")}</h1>
  <p class="lede">{b("More than seventy awards across literature, film lyrics, music, theatre and journalism. He is among the very few Indian writers to hold the Saraswati Samman, the Sahitya Akademi Award and the National Film Award (Rajat Kamal) together.",
                    "സാഹിത്യം, ചലച്ചിത്രഗാനം, സംഗീതം, നാടകം, മാധ്യമപ്രവർത്തനം — എഴുപതിലധികം പുരസ്കാരങ്ങൾ. സരസ്വതി സമ്മാൻ, കേന്ദ്ര സാഹിത്യ അക്കാദമി പുരസ്കാരം, രജത കമലം എന്നിവ ഒരുമിച്ചു നേടിയ അപൂർവം ഇന്ത്യൻ എഴുത്തുകാരിൽ ഒരാൾ.")}</p>
</section>

<section class="sec honour-photo">
  <figure><img src="images/saraswati-samman.jpg" alt="Receiving the Saraswati Samman"><figcaption>{b("Receiving the Saraswati Samman for <em>Roudra Sathwikam</em> from the K. K. Birla Foundation, 2024.", "<em>രൗദ്രസാത്വിക</em>ത്തിനുള്ള സരസ്വതി സമ്മാൻ കെ. കെ. ബിർള ഫൗണ്ടേഷനിൽനിന്ന് സ്വീകരിക്കുന്നു, 2024.")}</figcaption></figure>
  <figure><img src="images/sahitya-akademi-award.jpg" alt="Receiving the Sahitya Akademi Award"><figcaption>{b("Receiving the Sahitya Akademi Award for <em>Shyama Madhavam</em>, New Delhi, 2017.", "<em>ശ്യാമമാധവ</em>ത്തിനുള്ള കേന്ദ്ര സാഹിത്യ അക്കാദമി പുരസ്കാരം സ്വീകരിക്കുന്നു, ന്യൂഡൽഹി, 2017.")}</figcaption></figure>
</section>
<section class="honour-photo">
  <figure><img src="images/rajat-kamal.jpg" alt="Receiving the Rajat Kamal from Vice-President Venkaiah Naidu"><figcaption>{b("Vice-President M. Venkaiah Naidu presents the Rajat Kamal, National Film Award for Best Lyrics, for <em>Kolaambi</em>.", "ഉപരാഷ്ട്രപതി എം. വെങ്കയ്യ നായിഡു <em>കോളാമ്പി</em>ക്കുള്ള രജത കമലം സമ്മാനിക്കുന്നു.")}</figcaption></figure>
  <figure><img src="images/vayalar-award.jpg" alt="Receiving the Vayalar Award"><figcaption>{b("The Vayalar Award for <em>Shyama Madhavam</em>, 2013.", "<em>ശ്യാമമാധവ</em>ത്തിനുള്ള വയലാർ അവാർഡ്, 2013.")}</figcaption></figure>
</section>
<section class="honour-photo">
  <figure><img src="images/kerala-sahitya-akademi-mt.jpg" alt="Receiving the Kerala Sahitya Akademi Award from M. T. Vasudevan Nair"><figcaption>{b("Jnanpith laureate M. T. Vasudevan Nair presents the Kerala Sahitya Akademi Award for <em>Arkkapoornima</em>.", "ജ്ഞാനപീഠ ജേതാവ് എം. ടി. വാസുദേവൻ നായർ <em>അർക്കപൂർണിമ</em>യ്ക്കുള്ള കേരള സാഹിത്യ അക്കാദമി പുരസ്കാരം സമ്മാനിക്കുന്നു.")}</figcaption></figure>
  <figure><img src="images/rashtrapati-bhavan-2.jpg" alt="President Pranab Mukherjee presenting a citation to Prabha Varma"><figcaption>{b("President Pranab Mukherjee presents the citation for his contribution to the performing arts, Rashtrapati Bhavan, 2016.", "പ്രകടനകലകൾക്കുള്ള സംഭാവനയ്ക്ക് രാഷ്ട്രപതി പ്രണബ് മുഖർജി പ്രശസ്തിപത്രം സമ്മാനിക്കുന്നു, രാഷ്ട്രപതി ഭവൻ, 2016.")}</figcaption></figure>
</section>
<section class="honour-photo">
  <figure><img src="images/state-film-award-2017.jpg" alt="Receiving the Kerala State Film Award from the Chief Minister, with Mohanlal"><figcaption>{b("Kerala State Film Award for Best Lyricist from Chief Minister Pinarayi Vijayan, with Mohanlal, 2017.", "മുഖ്യമന്ത്രി പിണറായി വിജയനിൽനിന്ന് മികച്ച ഗാനരചയിതാവിനുള്ള സംസ്ഥാന ചലച്ചിത്ര പുരസ്കാരം; സമീപം മോഹൻലാൽ, 2017.")}</figcaption></figure>
  <figure><img src="images/asan-prize-2014.jpg" alt="Receiving the Asan Prize"><figcaption>{b("The Asan Prize for poetry, Asan Memorial Association, Chennai, 2014.", "ആശാൻ കവിതാ പുരസ്കാരം, ആശാൻ മെമ്മോറിയൽ അസോസിയേഷൻ, ചെന്നൈ, 2014.")}</figcaption></figure>
</section>
<section class="sec big-three">
  <article>
    <span class="yr">2023</span>
    <h3>{b("Saraswati Samman", "സരസ്വതി സമ്മാൻ")}</h3>
    <p>{b("K. K. Birla Foundation's annual award for the outstanding work in any Indian language, for <em>Roudra Sathwikam</em>. Selected by a committee chaired by Justice A. K. Sikri from a shortlist of five works in five languages; the first Malayalam winner in twelve years.",
         "ഏതൊരു ഇന്ത്യൻ ഭാഷയിലെയും മികച്ച കൃതിക്ക് കെ. കെ. ബിർള ഫൗണ്ടേഷൻ നൽകുന്ന വാർഷിക പുരസ്കാരം — <em>രൗദ്രസാത്വികം</em> എന്ന കൃതിക്ക്. ജസ്റ്റിസ് എ. കെ. സിക്രി അധ്യക്ഷനായ സമിതി തിരഞ്ഞെടുത്തു; പന്ത്രണ്ട് വർഷത്തിനു ശേഷം മലയാളത്തിന്.")}</p>
  </article>
  <article>
    <span class="yr">2016</span>
    <h3>{b("Sahitya Akademi Award", "കേന്ദ്ര സാഹിത്യ അക്കാദമി പുരസ്കാരം")}</h3>
    <p>{b("India's National Academy of Letters, for <em>Shyama Madhavam</em>. His acceptance speech, <em>Literature in Changing Times</em>, is reproduced on the Readings page.",
         "ഭാരതത്തിന്റെ ദേശീയ സാഹിത്യ അക്കാദമി, <em>ശ്യാമമാധവം</em> എന്ന കൃതിക്ക്. സ്വീകരണ പ്രസംഗം വായന പേജിൽ.")}</p>
  </article>
  <article>
    <span class="yr">{b("National Film Award", "ദേശീയ ചലച്ചിത്ര പുരസ്കാരം")}</span>
    <h3>{b("Rajat Kamal — Best Lyrics", "രജത കമലം — മികച്ച ഗാനരചന")}</h3>
    <p>{b("For the songs of <em>Kolaambi</em>, presented at the 2021 National Film Awards.", "<em>കോളാമ്പി</em> എന്ന ചിത്രത്തിലെ ഗാനങ്ങൾക്ക്, 2021-ലെ ദേശീയ ചലച്ചിത്ര പുരസ്കാരം.")}</p>
  </article>
</section>

<section class="sec cols-2 award-cols">
  <div>{sec_head("01", "Poetry & literature", "കവിത · സാഹിത്യം")}{award_ol(poetry_awards)}</div>
  <div>
    {sec_head("02", "Lyrics & music", "ഗാനം · സംഗീതം")}{award_ol(lyric_awards)}
    {sec_head("03", "Cultural", "സാംസ്കാരികം")}{award_ol(culture_awards)}
    {sec_head("04", "Journalism", "മാധ്യമപ്രവർത്തനം")}{award_ol(media_awards)}
    {sec_head("05", "Positions held", "വഹിച്ച സ്ഥാനങ്ങൾ")}
    <ul class="plain">
      <li>{b("Member, General Council, Sahitya Akademi, New Delhi (2007–2012); later Executive Board member; Convener of the Southern Regional Board and of the Language Advisory Committee (till 2022)", "സാഹിത്യ അക്കാദമി ജനറൽ കൗൺസിൽ അംഗം (2007–2012); പിന്നീട് എക്സിക്യൂട്ടീവ് ബോർഡ് അംഗം; ദക്ഷിണ മേഖലാ ബോർഡ് കൺവീനർ (2022 വരെ)")}</li>
      <li>{b("Vice-President, Kerala Sahitya Akademi (2008–2010)", "കേരള സാഹിത്യ അക്കാദമി വൈസ് പ്രസിഡന്റ് (2008–2010)")}</li>
      <li>{b("Member, final jury, Jnanpith Award", "ജ്ഞാനപീഠ പുരസ്കാര അന്തിമ ജൂറി അംഗം")}</li>
      <li>{b("Member, Senate, Cochin University of Science and Technology", "കുസാറ്റ് സെനറ്റ് അംഗം")}</li>
      <li>{b("Media Secretary to the Chief Minister of Kerala", "കേരള മുഖ്യമന്ത്രിയുടെ മീഡിയ സെക്രട്ടറി")}</li>
    </ul>
  </div>
</section>
"""

# ---- STAGE & SCREEN
stage = f"""
<section class="page-head">
  <p class="eyebrow">{b("Lyrics · Music · Theatre · Dance", "ഗാനം · സംഗീതം · നാടകം · നൃത്തം")}</p>
  <h1>{b("On Stage & Screen", "രംഗവേദിയിലും ചലച്ചിത്രത്തിലും")}</h1>
  <p class="lede">{b("Prabha Varma's words have a second life in performance — as film songs heard by tens of millions, as Carnatic kritis sung in concert, as Mohiniyattam padams, and as full-length plays that have toured Kerala for years.",
                    "പ്രഭാവർമ്മയുടെ വാക്കുകൾക്ക് അവതരണത്തിൽ രണ്ടാമതൊരു ജീവിതമുണ്ട് — കോടിക്കണക്കിനു പേർ കേട്ട ചലച്ചിത്രഗാനങ്ങളായി, കച്ചേരികളിലെ കൃതികളായി, മോഹിനിയാട്ട പദങ്ങളായി, കേരളമാകെ സഞ്ചരിച്ച നാടകങ്ങളായി.")}</p>
</section>

<section class="sec">
  {sec_head("01", "Film songs", "ചലച്ചിത്രഗാനങ്ങൾ")}
  <div class="song-grid">
    <div class="song"><b>Oru Chempaneer Poo…</b><span>{b("from <em>Sthithi</em> · 20 million+ views within a year", "<em>സ്ഥിതി</em> · ഒരു വർഷത്തിനകം രണ്ടു കോടിയിലധികം കാഴ്ചകൾ")}</span></div>
    <div class="song"><b>Kanna Nee Ninaippathare…</b><span>{b("from <em>Marakkar: Arabikkadalinte Simham</em>", "<em>മരയ്ക്കാർ: അറബിക്കടലിന്റെ സിംഹം</em>")}</span></div>
    <div class="song"><b>Kolaambi</b><span>{b("National Film Award for Best Lyrics (Rajat Kamal)", "മികച്ച ഗാനരചനയ്ക്കുള്ള ദേശീയ പുരസ്കാരം")}</span></div>
    <div class="song"><b>Nagaravadhu · Nadan</b><span>{b("Film Critics Awards, 2008 and 2013", "ഫിലിം ക്രിട്ടിക്സ് അവാർഡ്, 2008, 2013")}</span></div>
  </div>
  <p class="note">{b("Kerala State Film Award for Best Lyricist in 2006, 2013 and 2017. A complete filmography with audio links will be added here.",
                    "2006, 2013, 2017 വർഷങ്ങളിൽ മികച്ച ഗാനരചയിതാവിനുള്ള സംസ്ഥാന ചലച്ചിത്ര പുരസ്കാരം. സമ്പൂർണ്ണ ഗാനപ്പട്ടിക ഉടൻ.")}</p>
</section>

<section class="sec cols-2">
  <div>
    {sec_head("02", "Carnatic music & dance", "കർണാടക സംഗീതം · നൃത്തം")}
    <p>{b("More than sixty classical <em>kritis</em> and over two dozen Mohiniyattam <em>padams</em>, collected in <em>Prabha Varmayude Karnataka Sangeetha Kruthikal</em> (State Language Institute). Concerts devoted entirely to his compositions — two and a half hours of Prabha Varma Kritis — have been held across Kerala and beyond. Dancers including Dr Rajashree Warrier, Dr Kalamandalam Sheeba Krishnakumar, Dr Shruthi Shobhi, Sithara Balakrishnan, Anjana and Regatta Chandran have built productions on his poems, staged across India including Delhi. In 2016 President Pranab Mukherjee honoured him at Rashtrapati Bhavan for his contribution to the performing arts.",
         "അറുപതിലധികം കൃതികളും രണ്ടു ഡസനിലധികം മോഹിനിയാട്ട പദങ്ങളും — <em>പ്രഭാവർമ്മയുടെ കർണാടക സംഗീത കൃതികൾ</em> (ഭാഷാ ഇൻസ്റ്റിറ്റ്യൂട്ട്). അദ്ദേഹത്തിന്റെ കൃതികൾ മാത്രം ഉൾക്കൊള്ളുന്ന രണ്ടര മണിക്കൂർ കച്ചേരികൾ കേരളത്തിലുടനീളം. ഡോ. രാജശ്രീ വാര്യർ, ഡോ. കലാമണ്ഡലം ഷീബ കൃഷ്ണകുമാർ തുടങ്ങിയ നർത്തകർ അദ്ദേഹത്തിന്റെ കവിതകൾ അരങ്ങിലെത്തിച്ചു. 2016-ൽ രാഷ്ട്രപതി പ്രണബ് മുഖർജി രാഷ്ട്രപതി ഭവനിൽ ആദരിച്ചു.")}</p>
  </div>
  <div>
    {sec_head("03", "Theatre & visual art", "നാടകം · ചിത്രകല")}
    <p>{b("Sangeetha Nataka Akademi awardee M. Santhosh directed professional plays based on <em>Shyama Madhavam</em> and <em>Kanal Chilambu</em>; between them they have played more than 800 packed houses across Kerala. <em>Shyama Madhavam</em> was also staged as a musical drama seen by hundreds of thousands. Narayanan Kutty and his team from Malappuram have mounted mural-painting exhibitions on the two poems, and Shobha Varma's novel <em>Chilamboli</em> was written in response to <em>Kanal Chilambu</em>. He has twice won the Kerala Sangeetha Nataka Akademi Award for songs in plays.",
         "സംഗീത നാടക അക്കാദമി പുരസ്കാര ജേതാവ് എം. സന്തോഷ് സംവിധാനം ചെയ്ത <em>ശ്യാമമാധവം</em>, <em>കനൽച്ചിലമ്പ്</em> നാടകങ്ങൾ 800-ലധികം വേദികളിൽ. <em>ശ്യാമമാധവം</em> സംഗീതനാടകമായും അരങ്ങേറി. മലപ്പുറത്തെ നാരായണൻകുട്ടിയും സംഘവും ചുവർച്ചിത്ര പ്രദർശനങ്ങൾ ഒരുക്കി; ശോഭാ വർമ്മയുടെ <em>ചിലമ്പൊലി</em> എന്ന നോവൽ <em>കനൽച്ചിലമ്പി</em>നോടുള്ള പ്രതികരണമാണ്. നാടകഗാനങ്ങൾക്ക് രണ്ടു തവണ സംഗീത നാടക അക്കാദമി പുരസ്കാരം.")}</p>
  </div>
</section>

<section class="photo-band">
  <figure><img src="images/with-yesudas.jpg" alt="K. J. Yesudas presents a flute to Prabha Varma" loading="lazy"><figcaption>{b("K. J. Yesudas presents him a flute", "കെ. ജെ. യേശുദാസ് ഓടക്കുഴൽ സമ്മാനിക്കുന്നു")}</figcaption></figure>
  <figure><img src="images/stage-night.jpg" alt="Prabha Varma on stage" loading="lazy"><figcaption>{b("On stage", "അരങ്ങിൽ")}</figcaption></figure>
  <figure><img src="images/recital-choir.jpg" alt="Prabha Varma reciting with a chorus" loading="lazy"><figcaption>{b("Leading a choral recitation, Mar Ivanios College, Thiruvananthapuram", "മാർ ഇവാനിയോസ് കോളേജിൽ സംഘഗാനാവതരണം നയിക്കുന്നു")}</figcaption></figure>
  <figure><img src="images/onv-smriti-2024.jpg" alt="Speaking at ONV Smriti Sayahnam, 2024" loading="lazy"><figcaption>{b("ONV Smriti Sayahnam, University College, February 2024", "ഒഎൻവി സ്മൃതിസായാഹ്നം, യൂണിവേഴ്സിറ്റി കോളേജ്, ഫെബ്രുവരി 2024")}</figcaption></figure>
</section>

<section class="sec">
  {sec_head("04", "Recordings", "റെക്കോർഡിംഗുകൾ")}
  <div class="video-grid">
    <div class="video-ph"><span>{b("Recitation — coming soon", "കാവ്യാലാപനം — ഉടൻ")}</span></div>
    <div class="video-ph"><span>{b("Sahitya Akademi acceptance speech", "അക്കാദമി പുരസ്കാര പ്രസംഗം")}</span></div>
    <div class="video-ph"><span>{b("Prabha Varma Kritis — concert", "പ്രഭാവർമ്മ കൃതികൾ — കച്ചേരി")}</span></div>
  </div>
</section>
"""

# ---- READINGS (excerpts)
writings = f"""
<section class="page-head">
  <p class="eyebrow">{b("Excerpts · Essays · Speeches", "ഭാഗങ്ങൾ · പഠനങ്ങൾ · പ്രസംഗങ്ങൾ")}</p>
  <h1>{b("Readings", "വായന")}</h1>
  <p class="lede">{b("Selected passages from the English translations of the verse novels, with critical essays by O. N. V. Kurup, Dr M. Leelavathy and K. Jayakumar, and the poet's Sahitya Akademi acceptance speech. Malayalam originals will be added alongside each excerpt.",
                    "കാവ്യാഖ്യായികകളുടെ ഇംഗ്ലീഷ് പരിഭാഷകളിൽനിന്ന് തിരഞ്ഞെടുത്ത ഭാഗങ്ങൾ; ഒ. എൻ. വി. കുറുപ്പ്, ഡോ. എം. ലീലാവതി, കെ. ജയകുമാർ എന്നിവരുടെ പഠനങ്ങൾ; സാഹിത്യ അക്കാദമി പുരസ്കാര പ്രസംഗം. മലയാള മൂലം ഓരോ ഭാഗത്തിനൊപ്പവും ചേർക്കും.")}</p>
</section>

<section class="sec reading">
  {sec_head("01", "From <em>Lament of the Dusky Lord</em>", "<em>ശ്യാമമാധവ</em>ത്തിൽ നിന്ന്")}
  <div class="verse">
    <p>Flocks of birds come from afar,<br>gathering together for a while.<br>Roost on the branches of a tree,<br>then fly away without a trace.</p>
  </div>
  <p class="src">Shyama Madhavam · {b("English translation, DC Books", "ഇംഗ്ലീഷ് പരിഭാഷ, ഡി. സി. ബുക്സ്")}</p>
</section>

<section class="sec reading">
  {sec_head("02", "From <em>Anklet of Fire</em>", "<em>കനൽച്ചിലമ്പി</em>ൽ നിന്ന്")}
  <div class="verse">
    <p>The milk pot fell from your head and broke into pieces,<br>but still, O milkmaid, tears did not well up in your eyes!<br>Not only did tears not fill the eyes —<br>the mischief in the large dark eyes did not vanish either.</p>
  </div>
  <p class="src">Kanal Chilambu · {b("English translation, DC Books", "ഇംഗ്ലീഷ് പരിഭാഷ, ഡി. സി. ബുക്സ്")}</p>
</section>

<section class="sec reading">
  {sec_head("03", "From <em>Ferocious Piety</em>", "<em>രൗദ്രസാത്വിക</em>ത്തിൽ നിന്ന്")}
  <div class="verse">
    <p>… a flash of light moving along with the golden saucer,<br>flying away and away to the boundless skies,<br>until it integrated into the core of the splendid sun.</p>
  </div>
  <p class="src">Roudra Sathwikam · {b("English translation, DC Books", "ഇംഗ്ലീഷ് പരിഭാഷ, ഡി. സി. ബുക്സ്")}</p>
</section>

<section class="photo-band two">
  <figure><img src="images/portrait-listening.jpg" alt="Prabha Varma" loading="lazy"><figcaption>{b("Listening, at a reading", "ഒരു കാവ്യസദസ്സിൽ")}</figcaption></figure>
  <figure><img src="images/portrait-profile.jpg" alt="Prabha Varma" loading="lazy"><figcaption>{b("Thiruvananthapuram", "തിരുവനന്തപുരം")}</figcaption></figure>
</section>

<section class="sec">
  {sec_head("04", "Critical essays", "പഠനങ്ങൾ")}
  <div class="essay-list">
    <article><h3>Shyama Madhavam — A Poem of Epic Dimensions</h3><p class="by">Prof. O. N. V. Kurup</p><p>{b("Placing the poem beside Kumaran Asan's <em>Chinthavishtayaya Sita</em>, Khandekar's <em>Yayati</em> and Kazantzakis's <em>Odyssey: A Modern Sequel</em>.", "കുമാരനാശാന്റെ <em>ചിന്താവിഷ്ടയായ സീത</em>, ഖാണ്ഡേക്കറുടെ <em>യയാതി</em>, കസാൻദ്സാക്കിസിന്റെ <em>ഒഡിസി</em> എന്നിവയോടു ചേർത്തുവയ്ക്കുന്ന പഠനം.")}</p><span class="soon">{b("Full text coming", "പൂർണ്ണരൂപം ഉടൻ")}</span></article>
    <article><h3>The Inscrutability of Existence</h3><p class="by">Dr M. Leelavathy</p><p>{b("On <em>Kanal Chilambu</em> as a key to a riddle the mind cannot stop trying to solve.", "മനസ്സിനു പരിഹരിക്കാനാകാത്ത കടങ്കഥയുടെ താക്കോലായി <em>കനൽച്ചിലമ്പ്</em>.")}</p><span class="soon">{b("Full text coming", "പൂർണ്ണരൂപം ഉടൻ")}</span></article>
    <article><h3>Prabha Varma's Modern Classic</h3><p class="by">K. Jayakumar</p><p>{b("Why <em>Shyama Madhavam</em> could be modern in sensibility while staying loyal to metre and rhyme.", "വൃത്തത്തോടും പ്രാസത്തോടും വിശ്വസ്തത പുലർത്തിക്കൊണ്ട് <em>ശ്യാമമാധവം</em> എങ്ങനെ ആധുനികമായി.")}</p><span class="soon">{b("Full text coming", "പൂർണ്ണരൂപം ഉടൻ")}</span></article>
    <article><h3>Literature in Changing Times</h3><p class="by">Prabha Varma — {b("Sahitya Akademi acceptance speech", "സാഹിത്യ അക്കാദമി പുരസ്കാര പ്രസംഗം")}</p><p>{b("The poet on what literature owes its moment, delivered on receiving the National Academy of Letters award.", "ദേശീയ അക്കാദമി പുരസ്കാരം സ്വീകരിച്ചുകൊണ്ട് കവി നടത്തിയ പ്രസംഗം.")}</p><span class="soon">{b("Full text coming", "പൂർണ്ണരൂപം ഉടൻ")}</span></article>
  </div>
</section>
"""

# ---- ABOUT
about = f"""
<section class="page-head">
  <p class="eyebrow">{b("Biography", "ജീവചരിത്രം")}</p>
  <h1>{b("Life", "ജീവിതം")}</h1>
  <p class="lede">{b("Born at Kadapra, Thiruvalla, in Kerala. A degree in English literature, a master's in Political Science and a degree in law. Fifty years of writing, completed in 2025.",
                    "കേരളത്തിലെ തിരുവല്ല കടപ്രയിൽ ജനനം. ഇംഗ്ലീഷ് സാഹിത്യത്തിൽ ബിരുദം, രാഷ്ട്രമീമാംസയിൽ ബിരുദാനന്തര ബിരുദം, നിയമബിരുദം. 2025-ൽ എഴുത്തിന്റെ അമ്പതു വർഷം പൂർത്തിയാക്കി.")}</p>
</section>

<section class="sec cols-2 bio">
  <div>
    <h3>{b("The poet", "കവി")}</h3>
    <p>{b("His first collection, <em>Souparnika</em> (1990), won the Vyloppilli and Ankanam awards; his second, <em>Arkkapoornima</em>, the Kerala Sahitya Akademi Award. Critics have read in his work a confluence of tradition and modernity: a fidelity to the natural metres of Malayalam joined to a contemporary sensibility, philosophical insight, and a gift for the long narrative form that most of his generation had abandoned. O. N. V. Kurup traced his lineage through Vyloppilly to Kumaran Asan; M. Krishnan Nair called him a born poet.",
         "ആദ്യ സമാഹാരം <em>സൗപർണിക</em> (1990) വൈലോപ്പിള്ളി, അങ്കണം പുരസ്കാരങ്ങൾ നേടി; രണ്ടാമത്തേത് <em>അർക്കപൂർണിമ</em> കേരള സാഹിത്യ അക്കാദമി പുരസ്കാരവും. പാരമ്പര്യവും ആധുനികതയും സംഗമിക്കുന്ന കവിത — മലയാളത്തിന്റെ സഹജ വൃത്തങ്ങളോടുള്ള വിശ്വസ്തതയും സമകാലിക ഭാവുകത്വവും ദാർശനിക ഉൾക്കാഴ്ചയും, തലമുറ കൈവിട്ട ദീർഘാഖ്യാന രൂപത്തിലുള്ള അസാധാരണ പ്രാവീണ്യവും.")}</p>
    <h3>{b("The journalist", "മാധ്യമപ്രവർത്തകൻ")}</h3>
    <p>{b("He covered both houses of the Indian Parliament for over a decade, reported the Non-Aligned Summit, the Commonwealth meet and the G-15, and presented a paper on emerging democracies at the UN-backed Doha international meet. He was Director (News) of People TV and Kairali TV from 2001 to 2010, presenting the weekly analysis programme <em>India Inside</em>, and Resident Editor of Deshabhimani. He delivered the keynote at the North American Press Club's media conference in New York in 2009, and later served as Media Secretary to the Chief Minister of Kerala.",
         "ഒരു ദശകത്തിലധികം പാർലമെന്റിന്റെ ഇരുസഭകളും റിപ്പോർട്ട് ചെയ്തു; ചേരിചേരാ ഉച്ചകോടി, കോമൺവെൽത്ത് സമ്മേളനം, ജി-15 എന്നിവ റിപ്പോർട്ട് ചെയ്തു. 2001 മുതൽ 2010 വരെ പീപ്പിൾ ടിവി, കൈരളി ടിവി ന്യൂസ് ഡയറക്ടർ; <em>ഇന്ത്യ ഇൻസൈഡ്</em> എന്ന വാരാന്ത്യ വിശകലന പരിപാടിയുടെ അവതാരകൻ; ദേശാഭിമാനി റസിഡന്റ് എഡിറ്റർ. 2009-ൽ ന്യൂയോർക്കിൽ നോർത്ത് അമേരിക്കൻ പ്രസ് ക്ലബ്ബിന്റെ മാധ്യമ സമ്മേളനത്തിൽ മുഖ്യപ്രഭാഷണം. പിന്നീട് കേരള മുഖ്യമന്ത്രിയുടെ മീഡിയ സെക്രട്ടറി.")}</p>
  </div>
  <div>
    <h3>{b("Public life", "പൊതുജീവിതം")}</h3>
    <p>{b("A member of the General Council of the Sahitya Akademi (2007–2012) and later of its Executive Board, where he convened the Southern Regional Board and the Language Advisory Committee until 2022. Vice-President of the Kerala Sahitya Akademi (2008–2010), a member of the final jury of the Jnanpith Award, and a member of the Senate of Cochin University of Science and Technology. A regular contributor to Malayalam and English dailies including <em>The Times of India</em>.",
         "സാഹിത്യ അക്കാദമി ജനറൽ കൗൺസിൽ അംഗം (2007–2012), പിന്നീട് എക്സിക്യൂട്ടീവ് ബോർഡ് അംഗം; ദക്ഷിണ മേഖലാ ബോർഡിന്റെയും ഭാഷാ ഉപദേശക സമിതിയുടെയും കൺവീനർ (2022 വരെ). കേരള സാഹിത്യ അക്കാദമി വൈസ് പ്രസിഡന്റ് (2008–2010), ജ്ഞാനപീഠ അന്തിമ ജൂറി അംഗം, കുസാറ്റ് സെനറ്റ് അംഗം. <em>ടൈംസ് ഓഫ് ഇന്ത്യ</em> ഉൾപ്പെടെയുള്ള പത്രങ്ങളിൽ സ്ഥിരം എഴുത്തുകാരൻ.")}</p>
    <h3>{b("Family", "കുടുംബം")}</h3>
    <p>{b("He lives in Thiruvananthapuram with his wife Manorema. Their daughter Jyotsna is married to Col. K. V. Mahendra; the grandchildren are Jhanvi and Jyothir.",
         "ഭാര്യ മനോരമയോടൊപ്പം തിരുവനന്തപുരത്ത് താമസം. മകൾ ജ്യോത്സ്ന, മരുമകൻ കേണൽ കെ. വി. മഹേന്ദ്ര, പേരക്കുട്ടികൾ ജാഹ്നവി, ജ്യോതിർ.")}</p>
    <div class="timeline">
      <h3>{b("Milestones", "നാഴികക്കല്ലുകൾ")}</h3>
      <dl>
        <dt>1975</dt><dd>{b("First published writing", "ആദ്യ രചന പ്രസിദ്ധീകരിക്കുന്നു")}</dd>
        <dt>1990</dt><dd><em>Souparnika</em> — {b("first collection", "ആദ്യ സമാഹാരം")}</dd>
        <dt>1996</dt><dd>{b("State award for best general reporting", "മികച്ച റിപ്പോർട്ടിങ്ങിനുള്ള സംസ്ഥാന പുരസ്കാരം")}</dd>
        <dt>2001–10</dt><dd>{b("Director (News), Kairali / People TV", "ന്യൂസ് ഡയറക്ടർ, കൈരളി / പീപ്പിൾ ടിവി")}</dd>
        <dt>2013</dt><dd>{b("Vayalar Award, <em>Shyama Madhavam</em>", "വയലാർ അവാർഡ്, <em>ശ്യാമമാധവം</em>")}</dd>
        <dt>2016</dt><dd>{b("Sahitya Akademi Award; honoured at Rashtrapati Bhavan", "കേന്ദ്ര സാഹിത്യ അക്കാദമി പുരസ്കാരം; രാഷ്ട്രപതി ഭവനിൽ ആദരം")}</dd>
        <dt>2021</dt><dd>{b("National Film Award, <em>Kolaambi</em>", "ദേശീയ ചലച്ചിത്ര പുരസ്കാരം, <em>കോളാമ്പി</em>")}</dd>
        <dt>2024</dt><dd>{b("Saraswati Samman, <em>Roudra Sathwikam</em>", "സരസ്വതി സമ്മാൻ, <em>രൗദ്രസാത്വികം</em>")}</dd>
        <dt>2025</dt><dd>{b("Fifty years of writing", "എഴുത്തിന്റെ അമ്പതാണ്ട്")}</dd>
      </dl>
    </div>
  </div>
</section>
<section class="sec">
  {sec_head("02", "Photographs", "ചിത്രങ്ങൾ")}
  <div class="gallery">
    <figure class="tall"><img src="images/college-years.jpg" alt="Prabha Varma in his college years" loading="lazy"><figcaption>{b("College years", "കോളേജ് കാലം")}</figcaption></figure>
    <figure class="wide"><img src="images/cheruthazham-temple.jpg" alt="At the Cheruthazham temple" loading="lazy"><figcaption>{b("Cheruthazham temple — where his first poem was written", "ചെറുതാഴം ഇല്ലത്തെ ക്ഷേത്രം — ആദ്യ കവിത രചിച്ച സ്ഥലം")}</figcaption></figure>
    <figure class="tall"><img src="images/young-smiling.jpg" alt="Prabha Varma as a young man" loading="lazy"><figcaption>{b("Early years", "ആദ്യകാലം")}</figcaption></figure>
    <figure class="wide"><img src="images/leelavathy-fellowship.jpg" alt="Presenting the Sahitya Akademi Fellowship to Dr M. Leelavathy" loading="lazy"><figcaption>{b("Presenting the Sahitya Akademi Fellowship to Dr M. Leelavathy, as Akademi Executive Board member", "അക്കാദമി എക്സിക്യൂട്ടീവ് അംഗമെന്ന നിലയിൽ ഡോ. എം. ലീലാവതിക്ക് സാഹിത്യ അക്കാദമി ഫെലോഷിപ്പ് സമർപ്പിക്കുന്നു")}</figcaption></figure>
    <figure class="wide"><img src="images/with-ek-nayanar.jpg" alt="With E. K. Nayanar" loading="lazy"><figcaption>{b("With E. K. Nayanar, Chief Minister of Kerala, in the late 1990s", "മുഖ്യമന്ത്രി ഇ. കെ. നായനാർക്കൊപ്പം, 1990-കളുടെ അവസാനം")}</figcaption></figure>
    <figure class="tall"><img src="images/press-years.jpg" alt="Prabha Varma as a journalist" loading="lazy"><figcaption>{b("The reporting years", "റിപ്പോർട്ടിങ് കാലം")}</figcaption></figure>
    <figure class="wide"><img src="images/n-ramachandran-foundation.jpg" alt="Felicitation by the N. Ramachandran Foundation" loading="lazy"><figcaption>{b("Felicitated by the N. Ramachandran Foundation; Dr Shashi Tharoor at left", "എൻ. രാമചന്ദ്രൻ ഫൗണ്ടേഷന്റെ ആദരം; ഇടത് ഡോ. ശശി തരൂർ")}</figcaption></figure>
    <figure class="tall"><img src="images/with-t-padmanabhan.jpg" alt="With T. Padmanabhan" loading="lazy"><figcaption>{b("Honoured by the writer T. Padmanabhan", "എഴുത്തുകാരൻ ടി. പത്മനാഭൻ ആദരിക്കുന്നു")}</figcaption></figure>
    <figure class="tall"><img src="images/with-s-ramesan-nair.jpg" alt="With poet S. Ramesan Nair" loading="lazy"><figcaption>{b("With the poet S. Ramesan Nair", "കവി എസ്. രമേശൻ നായരോടൊപ്പം")}</figcaption></figure>
    <figure class="wide"><img src="images/vayalar-shyamamadhavam.jpg" alt="At the Vayalar Award function" loading="lazy"><figcaption>{b("At the Vayalar Award function for <em>Shyama Madhavam</em>", "<em>ശ്യാമമാധവ</em>ത്തിനുള്ള വയലാർ അവാർഡ് ചടങ്ങിൽ")}</figcaption></figure>
    <figure class="tall"><img src="images/high-court-lawyer.jpg" alt="As a lawyer at the Kerala High Court" loading="lazy"><figcaption>{b("A brief stint at the Bar — Kerala High Court", "അഭിഭാഷകനായി ഒരിടവേള — കേരള ഹൈക്കോടതി")}</figcaption></figure>
    <figure class="wide"><img src="images/sahitya-akademi-speaking.jpg" alt="Speaking at the Sahitya Akademi" loading="lazy"><figcaption>{b("At the Sahitya Akademi, New Delhi", "സാഹിത്യ അക്കാദമിയിൽ, ന്യൂഡൽഹി")}</figcaption></figure>
    <figure class="wide"><img src="images/with-jerry-amaldev.jpg" alt="With composer Jerry Amaldev" loading="lazy"><figcaption>{b("With the composer Jerry Amaldev", "സംഗീതസംവിധായകൻ ജെറി അമൽദേവിനൊപ്പം")}</figcaption></figure>
    <figure class="wide"><img src="images/with-sarada.jpg" alt="With actress Sarada" loading="lazy"><figcaption>{b("With the actress Sarada", "നടി ശാരദയോടൊപ്പം")}</figcaption></figure>
    <figure class="tall"><img src="images/painted-portrait.jpg" alt="Painted portrait of Prabha Varma" loading="lazy"><figcaption>{b("Portrait in oils, by an admirer", "ഒരു ആരാധകൻ വരച്ച ഛായാചിത്രം")}</figcaption></figure>
    <figure class="wide"><img src="images/sahitya-akademi-reading.jpg" alt="Reading at the Sahitya Akademi book exhibition" loading="lazy"><figcaption>{b("Reading at the Sahitya Akademi's national book exhibition", "സാഹിത്യ അക്കാദമി ദേശീയ പുസ്തകപ്രദർശനത്തിൽ കാവ്യാലാപനം")}</figcaption></figure>
    <figure class="wide"><img src="images/london-cultural-evening.jpg" alt="Speaking at a cultural evening in London" loading="lazy"><figcaption>{b("A cultural evening in London", "ലണ്ടനിൽ ഒരു സാംസ്കാരിക സന്ധ്യ")}</figcaption></figure>
    <figure class="wide"><img src="images/with-mt-vasudevan-nair.jpg" alt="With M. T. Vasudevan Nair" loading="lazy"><figcaption>{b("With M. T. Vasudevan Nair", "എം. ടി. വാസുദേവൻ നായർക്കൊപ്പം")}</figcaption></figure>
    <figure class="tall"><img src="images/doha.jpg" alt="At the Commonwealth seminar, Doha" loading="lazy"><figcaption>{b("Commonwealth seminar, Doha", "കോമൺവെൽത്ത് സെമിനാർ, ദോഹ")}</figcaption></figure>
    <figure class="wide"><img src="images/vagbhatananda-mt.jpg" alt="Presenting the Vagbhatananda Puraskaram citation to M. T. Vasudevan Nair" loading="lazy"><figcaption>{b("Presenting the Vagbhatananda Puraskaram citation to M. T. Vasudevan Nair", "എം. ടി. വാസുദേവൻ നായർക്ക് വാഗ്ഭടാനന്ദ പുരസ്കാര പ്രശസ്തിപത്രം സമർപ്പിക്കുന്നു")}</figcaption></figure>
    <figure class="tall"><img src="images/garden.jpg" alt="In the garden at home" loading="lazy"><figcaption>{b("At home", "വീട്ടിൽ")}</figcaption></figure>
    <figure class="wide top"><img src="images/caricatures.jpg" alt="Caricatures of Prabha Varma by various artists" loading="lazy"><figcaption>{b("As cartoonists have seen him", "കാർട്ടൂണിസ്റ്റുകളുടെ കണ്ണിൽ")}</figcaption></figure>
    <figure class="tall"><img src="images/portrait-seated.jpg" alt="Prabha Varma" loading="lazy"><figcaption>{b("Thiruvananthapuram, 2024", "തിരുവനന്തപുരം, 2024")}</figcaption></figure>
    <figure class="wide"><img src="images/library.jpg" alt="In his library" loading="lazy"><figcaption>{b("The study", "പഠനമുറി")}</figcaption></figure>
  </div>
</section>
"""

# ---- CONTACT
contact = f"""
<section class="page-head">
  <p class="eyebrow">{b("Enquiries", "അന്വേഷണങ്ങൾ")}</p>
  <h1>{b("Contact", "ബന്ധപ്പെടുക")}</h1>
  <p class="lede">{b("For invitations, press, translation and performance rights, and permission to reproduce texts.", "ക്ഷണങ്ങൾ, മാധ്യമം, പരിഭാഷ-അവതരണ അവകാശങ്ങൾ, കൃതികൾ പുനഃപ്രസിദ്ധീകരിക്കാനുള്ള അനുമതി എന്നിവയ്ക്ക്.")}</p>
</section>
<section class="sec contact-grid">
  <div>
    <h3>{b("Office of the poet", "കവിയുടെ കാര്യാലയം")}</h3>
    <p>Aardram, 308 A, 3rd Avenue<br>AKG Nagar, Peroorkada<br>Thiruvananthapuram, Kerala 695005</p>
    <p><a href="mailto:advisorpcm@gmail.com">advisorpcm@gmail.com</a></p>
  </div>
  <div>
    <img class="press-portrait" src="images/portrait-maroon.jpg" alt="Prabha Varma" loading="lazy">
    <h3>{b("Press kit", "പ്രസ് കിറ്റ്")}</h3>
    <p>{b("Short and long biographical notes in English and Malayalam, high-resolution photographs and book covers.", "ഇംഗ്ലീഷിലും മലയാളത്തിലും ഹ്രസ്വ-ദീർഘ ജീവചരിത്രക്കുറിപ്പുകൾ, ഉയർന്ന റെസല്യൂഷൻ ചിത്രങ്ങൾ, പുസ്തക കവറുകൾ.")}</p>
    <a class="btn ghost" href="#">{b("Download (coming soon)", "ഡൗൺലോഡ് (ഉടൻ)")}</a>
  </div>
  <div>
    <h3>{b("Publishers", "പ്രസാധകർ")}</h3>
    <p>DC Books · Mathrubhumi Books · Sahitya Pravarthaka Co-operative Society · Kerala Bhasha Institute</p>
  </div>
</section>
"""

PAGES = [
    ("index.html", "Poet, Lyricist, Journalist", "കവി", home, "Prabha Varma — Malayalam poet, lyricist and journalist. Saraswati Samman, Sahitya Akademi Award and National Film Award recipient; author of Shyama Madhavam, Kanal Chilambu, Roudra Sathwikam."),
    ("works.html", "Works", "കൃതികൾ", works, "Complete bibliography of Prabha Varma: novels in verse, poetry collections, novels, criticism, memoir and translations."),
    ("honours.html", "Honours", "പുരസ്കാരങ്ങൾ", honours, "Awards and honours received by Prabha Varma, including the Saraswati Samman, Sahitya Akademi Award and Rajat Kamal."),
    ("stage.html", "On Stage & Screen", "രംഗവേദി", stage, "Prabha Varma's film songs, Carnatic kritis, Mohiniyattam padams and theatre adaptations."),
    ("writings.html", "Readings", "വായന", writings, "Excerpts from Prabha Varma's verse novels in English translation, critical essays and speeches."),
    ("about.html", "Life", "ജീവിതം", about, "Biography of Prabha Varma — poet, journalist and public figure from Kerala."),
    ("contact.html", "Contact", "ബന്ധപ്പെടുക", contact, "Contact the office of poet Prabha Varma for invitations, press and permissions."),
]
for f, te, tm, body, d in PAGES:
    with open(os.path.join(OUT, f), "w", encoding="utf-8") as fh:
        fh.write(page(f, te, tm, body, d))
print("built", len(PAGES), "pages")
