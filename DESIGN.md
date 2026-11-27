# DESIGN.md — ulil-abshor.my.id

Design system in force. Read before changing any surface. Every rule here exists
because a detector or a real contrast measurement demanded it, not because it looked nice.

## Mode
Experience. The work leads; the interface recedes. No decorative chrome that competes
with a project screenshot.

## Palette
```
--bg          #07090d    page ground
--bg-soft     #0b0f16    raised surface (cards, terminal)
--line        rgba(255,255,255,.08)   hairline
--line-strong rgba(255,255,255,.18)   focus / active border
--text        #e9eef6    primary text
--muted       #93a1b3    secondary text (never below 4.5:1 on --bg)
--accent      #5fe08a    available status, one CTA only
--accent-2    #37c8ff    gradient partner, never a text color
--warn        #f5a623    reserved
```

Two accents, one job each: green means "available", cyan exists only as the second
stop of the primary button gradient. Nothing else may use them.

## Type
```
--font-display  "Instrument Serif"   h1, h2, h3 only
--font          "Inter"              body, UI
--mono          ui-monospace         labels, metrics, terminal
```

Floor is **13px**. Nothing readable sits at 11.5px or below — that was the single
largest defect on this site (42 instances). Labels may be 11px uppercase with
letter-spacing, never lowercase body copy.

## Space
```
--radius  16px    cards, buttons are pills (100px)
section padding   5.5rem block
card padding      16px minimum — content never touches a border
```

## Motion
One easing family: `cubic-bezier(.2,.7,.2,1)`. No bounce, no elastic, no overshoot.
No infinite loops on decorative elements (the pulsing scroll dot is gone).
Hero content fades in on a 0.9s stagger, CSS only.

## Contrast floor
Body text ≥ 4.5:1 against its actual background. Primary button: dark text
`#04120a` on the green→cyan gradient (measured ≈ 12:1 at the green stop).
Hover states never reduce contrast below the resting state.

## Forbidden
These are the tells that made the site read as AI-generated. Do not reintroduce:

- Gradient text (`background-clip: text`)
- Colored glow shadows (`box-shadow` with an accent hue)
- Pulsing / blinking dots
- Hero eyebrow chips above the name ("OPEN FOR WORK" in tracked uppercase)
- Heading level jumps (h2 → h4)
- Em-dash chains in prose (use a colon, comma or full stop)
- More than two typefaces plus mono

## Verification
```
~/.hermes-assistant/skills/creative/impeccable/scripts/impeccable detect index.html
```
Target: zero findings except `overused-font` (a taste call, accepted).
Baseline when this system was adopted: **55 findings**. Current: **2**.

## Cards
Two card families, deliberately different — do not merge them.

**Project card** (`#posts .item`): full-bleed screenshot cover on top, title, tech
line, description, metric row, live link. Grid is Isotope `fitRows`; every card is the
same width. One card was once double-wide (`kartu-lebar`) — removed, because a wider
card reads as "more important" and the work is not ranked that way.

**Certificate plate** (`.cert-plate`): a document, not a screenshot. Media sits in a
padded frame with `object-fit: contain` (never crop a certificate), a year badge in the
corner, and a body separated by a hairline rule — mono kicker, serif title, meta, link.
No hover overlay; text never covers the certificate. The featured international
certificate spans full width with media left / body right on desktop.

## Scroll reveal
`js/reveal.js` — IntersectionObserver, not AOS, because Isotope owns the transform on
`.item` and AOS would fight it. Animate the inner `.portfolio-item` / `.cert-plate`
only, never `.item`.

Use a **keyframe animation** (`kartuMasuk`), not a transition: `#posts .portfolio-item`
sets `transition: transform .4s …` with ID-level specificity, so a transition-based
reveal loses and the card appears instantly. The animation also uses
`fill-mode: backwards` — never `forwards`/`both` — so the final `transform` is released
and the card's own hover lift still works.

Rhythm matches AOS elsewhere on the site: **800ms, `ease`, 100px rise**. Project cards
stagger 100ms per column; certificate plates do not stagger (each sits in its own row
wrapper), and they must not also carry `data-aos` — two systems moving the same card
doubles the travel to 200px and flashes an empty card. Filtering force-reveals visible cards after 120ms so nothing stays
invisible. `prefers-reduced-motion` disables it entirely.

## Known false positive
The detector reports the primary button as `#04120a on #d63447` (4.1:1). The red is the
GSAP reveal cover sitting behind the button, not its background. Measured live, the
button is dark text on a green→cyan gradient at ≈ 12:1. Ignore that finding; do not
"fix" it by darkening the button.
