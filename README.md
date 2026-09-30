# Agata Medical Aesthetics

Site da nova marca da Agata Soldato. A fonte da verdade é o documento que ela
mandou em 18/09 (`Agata_Medical_Aesthetics_Website.pdf`, "Website Content Master"),
que substitui o `..._WITH_PACKAGES.docx`. A única mudança de texto entre os dois foi
a saída da Lanie. **O site segue o documento seção por seção, na mesma ordem.**

A marca **não** é mais "Agata Soldato". É **Agata Medical Aesthetics**, selo AMA,
assinatura "Cosmetic & Paramedical Tattooing". A Agata aparece sozinha como
fundadora e master artist. A Lanie Stein saiu do documento e do site.

- HTML/CSS/JS puro, arquivo único, sem framework
- Idiomas EN (principal) / PT-BR / ES por bandeirinha, guardado no localStorage
- Fontes self-hosted (Cormorant Garamond + Montserrat, subset latin)
- Deploy estático na Vercel

## Para onde vão os botões

**Todo CTA do site liga para (512) 502-5022.** São 16, e cada um é um
`<a href="tel:+15125025022">` escrito no HTML, sem JavaScript no meio.
Trocar o número é um find and replace em `5125025022`.

Nada de `preventDefault`, nada de ponte: uma ligação tem que disparar no
primeiro toque, e o navegador tem que mostrar o número de verdade ao passar o
mouse ou segurar o dedo. O `data-cta` sobrou só como etiqueta, para um gerenciador
de tags conseguir separar o botão do hero do botão do FAQ no dia em que entrar um.

O **PatientNow saiu em 23/09**, a pedido da cliente: ela quis que o botão ligasse.
O link era `https://book.mypatientnow.com/practice/47U2Ts`, guardado aqui caso volte.
O `thank-you.html` ficou órfão, apontando para o `tel:`, porque é o lugar pronto
para medir a ligação se um GTM entrar. Hoje não existe nenhuma tag no site.

Além dos botões, o número aparece escrito em três lugares: segundo botão do hero,
último item do menu no celular (`.nav__tel`, porque o botão do topo some nessa
largura) e sob a marca no rodapé.

**Não há seção de contato nem formulário.** Saíram em 18/09 a pedido do Leonardo,
e o bloco de contato só mostrava "To be confirmed". As seções 15 (Contact Page) e
16 (Contact Form Consent Copy) do documento ficam de fora por isso. Quando ela
confirmar endereço, horário e Instagram, o lugar natural é o rodapé.

O próprio documento dela avisa, e vale repetir: **não reaproveitar o telefone,
o endereço nem o e-mail da Posh** (11719 RM 2244 #101, Bee Cave, TX 78738,
+1 512 251-4170, info@poshpermanentmakeup.com) a menos que continuem válidos
para a empresa nova.

## Confirmar com a Agata

1. **Financiamento.** A seção existe e explica o processo, mas sem provedor. O
   documento dela manda só publicar provedor, link, APR promocional, compra
   mínima e disclosures depois de confirmar a conta merchant da empresa nova, e
   proíbe herdar a conta de financiamento da Posh. Hoje o CTA leva ao agendamento.
2. **Histórico.** O site diz 12 anos e mais de 10 mil procedimentos, números que
   vieram do documento dela. Como parte desse histórico foi construída sob a
   marca Posh, **confirmar se o acordo do divórcio permite reivindicá-lo**,
   principalmente cláusula de não concorrência ou de não solicitação.
3. **Preços dos pacotes.** Estão publicados exatamente como no documento: economia
   de US$ 500 no Complete Look, US$ 500 no PMU Reset, US$ 749 no Tummy, US$ 949
   no Breast. Conferir antes de ir ao ar, preço em página pública é promessa.
4. **Política de privacidade e termos.** O documento pede revisão jurídica da
   política de privacidade, do texto de SMS e dos termos de uso antes do
   lançamento. Sem formulário no site, quem coleta telefone é o PatientNow, nos
   termos dele. Se um formulário voltar, o texto de consentimento está no documento.

## Fotos dos serviços (30/09)

Ela mandou o acervo pelo WhatsApp e **9 dos 10 cartões têm foto real**. Só falta
**camuflagem de estrias**, que continua em `.svc__soon`.

**Uma foto por cartão, não duas.** Era para ser um par lado a lado, mas o material
dela já vem montado: antes e depois empilhados no mesmo enquadramento, distância e
luz, exatamente como o documento pede. As metades são deitadas (proporção de 1,1 a
2,5), então cortar cada uma para um retrato 4:5 jogava fora justamente a comparação,
sobrava um olho ou o dorso do nariz. O cartão mostra o composto inteiro num slot
4:5, com a legenda "antes e depois" por cima. `.svc__ph` e `.svc__orn` saíram.

**A foto de aréola nasce desfocada** e só abre no clique, em `.svc__ba--med`. É
foto clínica de reconstrução pós-mastectomia: o desfoque protege quem está rolando
a página em público e mantém o domínio seguro para anúncio, sem esconder o trabalho
dela. Sem JS o desfoque fica e nada quebra.

**Piercing não é antes e depois**, a legenda dele diz "resultado".

| Cartão | Foto | Observação |
|---|---|---|
| Nano brows | `svc-nano-brows` | trocou o par antigo, que era um recorte esticado com adesivo de medição no quadro |
| Ombre brows | `svc-ombre-brows` | pele negra; corte em `cx 0,62` para a **mesma** sobrancelha aparecer nas duas metades |
| Lip blush | `svc-lip-blush` | |
| Reconstrução de lábio | `svc-lip-reconstruction` | ela chama de *Lip Shape Reconstruction* |
| Delineado | `svc-eyeliner` | correção: traço falhado em cima, gatinho limpo embaixo |
| Aréola | `svc-areola` | desfocada até o clique |
| Estrias | — | **única que falta** |
| Cicatriz | `svc-scar-camouflage` | abdominoplastia; a versão com a marca "posh" foi descartada |
| Remoção a laser | `svc-laser-removal` | laser na sobrancelha tatuada em cima, pigmento levantado embaixo |
| Piercing | `svc-piercing` | resultado, sem par |

Para refazer um corte: `_tools/cortar-fotos.py`, que tem o ponto focal de cada
foto e o porquê. Os originais são de paciente e ficam **fora do repositório**,
em `_tools/originais/` (no `.gitignore`).

### Sobrou material que não entrou

Ela mandou serviços que o documento de 18/09 não lista como cartão, e fotos boas
que não couberam. **Nada disso foi para o site sem ela pedir:**

- **Brow Restoration / Brow Regrowth** — ela nomeou como serviço próprio e mandou
  três pares. Hoje some dentro de nano e ombre brows. Se vira cartão, é decisão dela.
- **Lip Neutralization**, **Smokey Eyeliner**, **Winged Eyeliner**, **Lash Liner**,
  **Eyeliner Correction** — estão cobertos pela descrição dos cartões de lábio e
  delineado, mas cada um tem foto própria.
- Uma arte de **6 quadros da remoção a laser** (antes, laser, 1, 2, 3 e 4+ sessões),
  pronta e legendada. Não cabe num slot 4:5, mas é o melhor material do acervo.
- Fotos de bastidor do estúdio: pigmentos, máquina, paquímetro, luva.

Se esse acervo for usar, o lugar é uma galeria de resultados própria, não o trilho.

## O que a cliente mudou depois do documento (21/09)

O documento de 18/09 continua sendo a fonte da copy, com estas exceções pedidas
por ela no WhatsApp:

| Mudança | Onde |
|---|---|
| Saiu o segundo parágrafo do intro ("From brows, lips, and eyeliner...") | seção INTRO |
| "Nano Brows & Ombre Brows" viraram **dois** serviços; "Lip Blush & Cleft Lip Reconstruction" também. São 10 cartões, não 8 | seção SERVICES |
| Saíram o botão e o aviso "Results vary..." do bloco "Not Sure Which Package" | `.pkg__end` |
| Saiu o box inteiro "Important Financing Policy", com o botão Explore Payment Options | seção FINANCING |
| A foto dela passou a vir **acima** do texto no celular | `.art` na media query de 1040px |
| O logo entrou acima do H1 do hero | `.hero__logo` |
| Telefone **(512) 502-5022** entrou como segundo botão do hero e no rodapé | `a[href^="tel:"]` |
| **23/09:** o PatientNow saiu e os 16 CTAs passaram a ligar direto | ver "Para onde vão os botões" |
| **23/09:** Featured Services virou trilho horizontal no desktop | `.svcrail`, ver abaixo |
| **30/09:** chegaram as fotos de resultado, 9 dos 10 cartões preenchidos | ver "Fotos dos serviços" |

As descrições dos quatro serviços separados não existem no documento: foram
quebradas a partir da descrição combinada que ele traz, sem palavra nova.

**Ainda combinado num cartão só, de propósito:** "Laser Tattoo Removal & Permanent
Makeup Removal". Ela não apontou esse, então fica como está.

## Featured Services: o trilho

De **1041px para cima** a seção segura a tela e os 10 cartões deslizam para o lado
enquanto a pessoa rola para baixo. Abaixo disso nada muda: continua grade de 2
colunas, e no celular a fileira de arrastar de sempre.

Como funciona, em três peças:

| Peça | Papel |
|---|---|
| `.svcrail` | o espaço vertical. Altura = uma tela + a distância que o trilho precisa andar, e quem calcula isso é o JS |
| `.svcrail__vp` | o quadro que gruda (`position:sticky`), uma tela de altura, com `padding-top` para os cartões não passarem por baixo do header fixo |
| `.svcrail__pad` | sangra para a largura da tela inteira e recoloca o início do trilho na margem da página |

O JS só põe a classe `.is-rail` na seção quando a tela é larga **e** o sistema não
está em `prefers-reduced-motion`. Sem a classe, todo o CSS do trilho é inerte e a
grade original aparece. Sem JS nenhum, idem. É o mesmo motivo de `.svcrail` e
`.svcrail__vp` serem `div`s sem estilo fora do trilho: o HTML funciona sozinho.

Duas armadilhas que custaram tempo:

- `overflow` na seção tem que ser **`clip`**, não `hidden`. `hidden` transforma o
  elemento em container de rolagem e o `sticky` de dentro para de grudar.
- a sangria é `margin-inline:calc(50% - 50vw)`. Com barra de rolagem visível o
  `100vw` passa alguns pixels da largura útil, e é o `overflow-x:clip` que apara
  essa sobra. Sem ele nasce uma barra horizontal no site inteiro.

O aviso "continue rolando" apaga sozinho no último quarto do percurso: o JS
escreve `--rail-done` (0 a 1) na seção e o CSS liga a opacidade nisso.


## Assets, e a armadilha do fundo

O retrato da Agata **não** tem fundo recortado. O fundo cinza do estúdio foi
trocado pela cor exata da seção, então a foto não tem borda visível e ela parece
estar dentro da seção:

| Arquivo | Fundo casado com |
|---|---|
| `agata-portrait.webp` (1100w) e `agata-portrait-700.webp` | `--artist-bg` `#EDE2CF` |

O `#EDE2CF` não é o `--sand-soft` (`#EDE1CE`): é a cor que o webp devolve depois
de comprimido, medida pixel a pixel. Usar a cor do CSS deixava 1 ponto de
diferença, o suficiente para o retângulo aparecer em algumas telas. O areia foi
escolhido porque o jaleco é creme e sumiria no marfim.

Se trocar a foto ou a cor da seção, refazer o casamento. Como foi feito: máscara
de pessoa do Apple Vision (`VNGenerateForegroundInstanceMaskRequest`) sobre o
original de 4000x6000 (`Downloads/Agata Soldato/Agata Soldato.jpg`), fundo do
estúdio modelado por ajuste quadrático, troca de cor com descontaminação das
bordas (`saída = foto + (1 - alfa) x (cor nova - fundo)`, que tira o cinza dos
fios de cabelo) e um balanço quente leve só no sujeito. Os lados da imagem são
cor chapada de propósito: no celular a foto fica 128% mais larga que a coluna e
entre 1041 e 1240px usa `cover`, e em ambos os casos só a cor chapada é cortada.

As duas logos (`logo-ama.webp` vinho e `logo-ama-white.webp` branca) mantêm alpha
de verdade e podem ir sobre qualquer fundo.

## Marca

Do documento da cliente, resumido:

| Papel | Cor |
|---|---|
| Pomegranate | `#751D32` |
| Desert Rose | `#B86F78` |
| Warm Blush | `#E5C4BF` |
| Antique Gold | `#B58A52` |
| Warm Sand | `#D8C4A8` |
| Ivory | `#F8F3EB` |
| Espresso | `#30231F` |

Equilíbrio pedido: 50% marfim, 20% vinho, 10% rosa, 10% blush e areia, 5%
espresso, 5% dourado. **Dourado é detalhe, nunca cor dominante.**

O dourado dos rótulos pequenos é `--gold-ink` `#7A5A30`, não o `#B58A52` do
documento: o tom original dá 4,1:1 sobre o fundo areia e reprova em contraste.
O `#B58A52` continua em uso onde é só traço e ícone, que não precisam passar.

Cormorant Garamond nos títulos, em peso 500 e 600, nunca nos pesos finos, como o
documento pede. Montserrat em navegação, corpo, botões, preço e FAQ.
Sem fonte manuscrita em lugar nenhum.

O motivo do arco (moldura das fotos das artistas, losango dourado dos separadores)
é a leitura discreta da influência que ela descreve. Sem lanterna, sem mosaico.

## Rastreio de conversão

Nenhum CTA aponta direto para fora. Todos passam por `thank-you.html?c=<contexto>`,
que dispara `dataLayer.push({event:'booking_conversion', contexto, idioma})` e só
depois redireciona. Quando `BOOKING` e `PHONE` estiverem preenchidos, o link de
agendamento ganha do WhatsApp.

## Rodar local

```bash
npx serve -l 8877 .
```

## Performance

Lighthouse mobile, throttling real (`--throttling-method=devtools`):

| Performance | Acessibilidade | Boas práticas | SEO |
|---|---|---|---|
| 99 | 100 | 100 | 100 |

LCP 1,9s · CLS 0 · TBT 0ms (medido em 18/09, depois da reestruturação)

O LCP subiu de 0,8s para 1,9s quando a foto entrou no hero, porque ela passou a
ser o maior elemento visível. Continua na faixa verde e o CLS zerou.

## Decisões de layout que não devem ser desfeitas

**Sem tag acima de título.** Nenhuma seção tem kicker em caixa alta. Foi removido
de propósito, é o que dá cara de template.

**Hero com foto e texto à esquerda.** A foto do lip blush é fundo full-bleed e o
texto ocupa a metade esquerda, onde a própria foto já tem área vazia. O véu são
três degradês empilhados em `.hero__veil`: um de cima para baixo, que segura a
legibilidade da navegação sobre a luva escura; um da esquerda para a direita, que
sustenta o texto; e um diagonal fraco no canto inferior esquerdo, que disfarça a
luva de baixo. Nenhum tem parada dura, é isso que evita a emenda visível entre o
véu e a foto.

**No mobile a foto não fica atrás do texto.** Vira uma faixa no pé do hero
(`.hero__bg` e `.hero__veil` com `top:auto;bottom:0`). Cobrir um bloco alto e
estreito com a mesma foto dava zoom absurdo, só aparecia um lábio gigante.

O mobile usa o mesmo recorte horizontal (`hero-lips-1000.webp`, 25KB), não o
retrato: na faixa larga ele entra sem zoom e pesa menos. O retrato que a cliente
mandou continua disponível, mas fora do repositório.

**O título do hero é o nome da marca.** A seção "Hero Section" do documento pede
`AGATA MEDICAL AESTHETICS`, a frase e `BOOK NOW`, e é isso que está lá, em duas
linhas ("Agata" / "Medical Aesthetics"). O H1 sugerido para SEO ("Permanent
Makeup & Cosmetic Tattooing in Austin, TX") ficou de fora do visual porque não
cabe no hero sem virar texto que ela não pediu. O `<title>` e a meta description
seguem o texto de SEO do documento, que é onde pesa mais.

**Ordem das seções igual à do documento.** Hero, intro, serviços, artista,
processo, pacotes, dúvidas, parcelamento, "Ready for your next look?" (só título,
texto e botão) e cursos. As seções 15 e 16 do documento (contato e texto de
consentimento do formulário) foram tiradas a pedido do Leonardo, ver acima.

**Pacotes em linhas horizontais, não em cards.** Quatro linhas de
`nome | descrição e itens | preço em cima do CTA`. O preço e o botão dividem a
mesma coluna, um sobre o outro: lado a lado, os preços longos ("3-Session Removal
Package: $500") passavam por baixo do botão em qualquer tela acima de 900px.
Abaixo de 900px a linha empilha. Os itens de cada pacote são uma lista
inline separada por losango, não uma lista vertical. Isso cortou a seção de
1.759px para 1.572px e alinhou os preços numa coluna, que é o que permite
comparar. Sticky stack foi considerado e descartado: o efeito é bonito mas cada
card passa a exigir uma tela de rolagem, ou seja, faz o oposto de compactar.

**Toda seção termina com um CTA.** `Book Your Consultation`, classe `.sec__cta`,
em intro, serviços, artista, processo e dúvidas. Pacotes, cursos e
parcelamento têm CTA próprio e específico, e o "Ready for your next look?" leva o
`Request a Consultation` do documento. Todos passam pela ponte de conversão, então quando o link de
agendamento definitivo chegar é só preencher `BOOKING` e todos apontam para lá.

**Seção da artista em duas colunas, foto de cima a baixo.** Foto à esquerda,
apoiada na borda de baixo da seção (a cintura encontra o fim da seção), texto à
direita com os negritos do documento. No celular o texto vem primeiro e a foto
fecha a seção, pelo mesmo motivo.

**Não devolver o hero para `flex-wrap`.** Os dois botões do hero e o bloco de
números ficavam exatamente no limite de caber lado a lado em 412px. Qualquer
mudança de largura do texto, inclusive a troca da fonte de fallback para a real,
desempilhava a linha e puxava 66px de tudo abaixo. Isso sozinho valia CLS 0,12.
Hoje os botões empilham em largura total abaixo de 560px e as métricas são grid
de colunas fixas, as duas coisas deterministas.
