#!/usr/bin/env python3
"""
Recorta as fotos de resultado que a Agata mandou para o formato do cartao de servico.

Cada foto dela JA e um antes/depois composto, empilhado no mesmo enquadramento,
distancia e luz. Entao nao se divide: o cartao mostra o composto inteiro, e o
recorte so ajusta a proporcao para 4:5.

focal = (cx, cy) em 0..1, o ponto que tem que sobreviver ao corte. Fica no centro
por padrao; onde o assunto esta fora do meio, o numero esta anotado ao lado.

Saida: assets/svc-<slug>.webp (620x775) e assets/svc-<slug>-420.webp (420x525).
O teto e 620 e nao 700 porque o cartao tem no maximo 331 px: em tela retina o
navegador pede ~662 px, e 700 so adicionava peso que ninguem ve.

As fotos de origem sao de paciente e NAO entram no repositorio. Coloque os
originais em _tools/originais/ com os numeros da coluna "origem" (001.jpg,
002.jpg...) na ordem alfabetica dos arquivos que a cliente mandou, ou troque o
numero pelo nome real do arquivo dela. Rode com: python3 _tools/cortar-fotos.py
"""
from PIL import Image
import pathlib, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ORIG = RAIZ / "_tools" / "originais"
DEST = RAIZ / "assets"
RATIO = 4 / 5          # a proporcao do slot no cartao
SIZES = [(620, 775), (420, 525)]

# slug                    origem  focal       o que e
FOTOS = [
    # sobrancelha
    ("nano-brows",          "010", (0.47, 0.50)),  # rala -> fio a fio
    ("ombre-brows",         "029", (0.62, 0.50)),  # pele negra; 0.62 enquadra a MESMA sobrancelha
                                                   # nas duas metades, centro cortava a de cima
    ("brow-restoration",    "007", (0.50, 0.50)),  # quase sem pelo -> desenho cheio
    # labios
    ("lip-blush",           "033", (0.50, 0.50)),
    ("ombre-lip-blush",     "036", (0.50, 0.50)),  # esfumado do contorno para dentro
    ("lip-neutralization",  "065", (0.50, 0.50)),  # ja nasce 4:5, nao corta nada
    ("lip-reconstruction",  "051", (0.50, 0.50)),  # labio leporino reconstruido
    # olhos
    ("lash-liner",          "016", (0.50, 0.50)),  # resultado, nao antes/depois
    ("winged-eyeliner",     "049", (0.50, 0.50)),  # resultado, olho aberto e fechado
    ("smokey-eyeliner",     "047", (0.50, 0.47)),  # resultado; 0.47 centra no olho
    ("eyeliner-correction", "035", (0.50, 0.50)),  # traco falhado -> gatinho limpo
    # paramedico e corpo
    ("areola",              "030", (0.50, 0.50)),  # restauracao pos-mastectomia
    ("scar-camouflage",     "027", (0.50, 0.50)),  # cicatriz de abdominoplastia
    ("laser-removal",       "009", (0.48, 0.50)),  # laser na sobrancelha tatuada
    ("piercing",            "045", (0.50, 0.50)),  # resultado, nao antes/depois
]


def recortar(im, focal):
    w, h = im.size
    alvo = w / h
    if alvo > RATIO:                      # larga demais: tira das laterais
        nw, nh = int(round(h * RATIO)), h
    else:                                 # alta demais: tira de cima e de baixo
        nw, nh = w, int(round(w / RATIO))
    cx, cy = focal
    x = min(max(int(round(cx * w - nw / 2)), 0), w - nw)
    y = min(max(int(round(cy * h - nh / 2)), 0), h - nh)
    return im.crop((x, y, x + nw, y + nh))


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for slug, num, focal in FOTOS:
        src = ORIG / f"{num}.jpg"
        if not src.exists():
            sys.exit(f"faltou {src}")
        im = Image.open(src).convert("RGB")
        corte = recortar(im, focal)
        for w, h in SIZES:
            nome = f"svc-{slug}.webp" if w == 620 else f"svc-{slug}-{w}.webp"
            corte.resize((w, h), Image.LANCZOS).save(
                DEST / nome, "WEBP", quality=72, method=6
            )
        print(f"{slug:20s} {num}  {im.size} -> {corte.size}")


if __name__ == "__main__":
    main()
