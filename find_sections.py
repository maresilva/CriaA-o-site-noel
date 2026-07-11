import re
import os

with open("solucoes.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 6985: <section class="sol-section sol-hero">
# 7007: <section class="sol-section sol-section-alt">  (Soluções)
# 7214: <section class="sol-section sol-segments-section"> (Segmentos)
# 7299: <section class="sol-section sol-section-alt"> (Processo)
# 7346: <section class="sol-section sol-included-section"> (Diferenciais)
# 7416: <section class="sol-cta"> (CTA)
# 7689: <section id="institucional-contato" class="inst-contact-section ca-section"> (Contato)

# I can just use line numbers, but let's confirm them first by searching the lines

sections = []
for i, line in enumerate(lines):
    if line.strip().startswith("<section") or line.strip().startswith("<!-- 7. CTA FINAL -->") or line.strip().startswith("<!-- START INSTITUTIONAL CONTACT SECTION -->"):
        sections.append((i, line.strip()))

# Print the discovered sections
for idx, line in sections:
    print(f"{idx}: {line[:60]}")
