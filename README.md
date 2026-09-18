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

## Antes de publicar: o que falta preencher

Tudo o que é dado real está no topo do `<script>` do `index.html`:

```js
const PHONE   = '';   // só dígitos com código do país, ex: '15125550100'
const IG      = '';   // handle sem o @
const EMAIL   = '';   // e-mail da empresa nova
const STUDIO  = '';   // endereço do estúdio novo
const MAPS    = '';   // link do Google Maps (opcional)
const HOURS   = '';   // ex: 'Mon to Fri, 9am to 6pm'
const BOOKING = 'https://book.mypatientnow.com/practice/47U2Ts';  // PREENCHIDO
```

`PHONE` e `BOOKING` também precisam ser repetidos no topo do `thank-you.html`.

`BOOKING` já está preenchido com o link do PatientNow, então os 15 CTAs e o
formulário saem da página pela ponte de conversão e caem no agendamento. O que a
pessoa digita no formulário não viaja junto, porque o site não tem backend.

Enquanto `PHONE` e `BOOKING` estiverem os dois vazios, todo CTA rola até o
formulário em vez de sair da página, então o site não quebra se for ao ar
incompleto. Os campos vazios aparecem como "To be confirmed" na seção de contato.

O próprio documento dela avisa, e vale repetir: **não reaproveitar o telefone,
o endereço nem o e-mail da Posh** (11719 RM 2244 #101, Bee Cave, TX 78738,
+1 512 251-4170, info@poshpermanentmakeup.com) a menos que continuem válidos
para a empresa nova.

## Confirmar com a Agata

1. **Financiamento.** A seção existe e explica o processo, mas sem provedor. O
   documento dela manda só publicar provedor, link, APR promocional, compra
   mínima e disclosures depois de confirmar a conta merchant da empresa nova, e
   proíbe herdar a conta de financiamento da Posh. Hoje o CTA leva ao formulário.
2. **Histórico.** O site diz 12 anos e mais de 10 mil procedimentos, números que
   vieram do documento dela. Como parte desse histórico foi construída sob a
   marca Posh, **confirmar se o acordo do divórcio permite reivindicá-lo**,
   principalmente cláusula de não concorrência ou de não solicitação.
3. **Preços dos pacotes.** Estão publicados exatamente como no documento: economia
   de US$ 500 no Complete Look, US$ 500 no PMU Reset, US$ 749 no Tummy, US$ 949
   no Breast. Conferir antes de ir ao ar, preço em página pública é promessa.
4. **Consentimento de SMS.** O texto do formulário é o que ela mandou. O próprio
   documento pede revisão jurídica da política de privacidade, do texto de SMS e
   dos termos de uso antes do lançamento.

## Fotos que faltam

Cada serviço em destaque é um cartão com o slot de antes e depois em cima, porque
o documento marca "(before and after picture)" em sete dos oito serviços. Só o par
de sobrancelha é real. Os outros seis estão como "photo coming soon", e é só trocar
o `.svc__soon` por um `.svc__ba` igual ao da sobrancelha (duas fotos 4:5).

O **Eyeliner Tattoo** não tem foto no documento, então o slot dele leva o motivo
do arco em vez de prometer uma foto. Se ela mandar um par de delineado, vira `.svc__ba`.

| Onde | O que pedir |
|---|---|
| Serviços | Antes/depois de **lip blush**, **aréola**, **estrias**, **cicatriz**, **remoção** e **piercing**, já cicatrizados |
| Serviços | Pares no **mesmo enquadramento, distância e luz**, como o próprio documento dela pede |


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
documento pede. Montserrat em navegação, corpo, botões, preço, formulário e FAQ.
Sem fonte manuscrita em lugar nenhum.

O motivo do arco (moldura das fotos das artistas, losango dourado dos separadores)
é a leitura discreta da influência que ela descreve. Sem lanterna, sem mosaico.

## Rastreio de conversão

Nenhum CTA aponta direto para fora. Todos passam por `thank-you.html?c=<contexto>`,
que dispara `dataLayer.push({event:'booking_conversion', contexto, idioma})` e só
depois redireciona. Quando `BOOKING` e `PHONE` estiverem preenchidos, o link de
agendamento ganha do WhatsApp. O formulário leva a mensagem montada por
`sessionStorage`, nunca pela URL.

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
texto e botão), cursos e, por último, contato com o formulário e o texto de
consentimento. O formulário mora em `#contact`, e é para lá que os CTAs caem
quando não há link de agendamento.

**Pacotes em linhas horizontais, não em cards.** Quatro linhas de
`nome | descrição e itens | preço | CTA`. Os itens de cada pacote são uma lista
inline separada por losango, não uma lista vertical. Isso cortou a seção de
1.759px para 1.572px e alinhou os preços numa coluna, que é o que permite
comparar. Sticky stack foi considerado e descartado: o efeito é bonito mas cada
card passa a exigir uma tela de rolagem, ou seja, faz o oposto de compactar.

**Toda seção termina com um CTA.** `Book Your Consultation`, classe `.sec__cta`,
em intro, serviços, resultados, artistas, processo e dúvidas. Pacotes, cursos e
parcelamento têm CTA próprio e específico, o "Ready for your next look?" leva o
`Request a Consultation` do documento e o contato é o próprio formulário. Todos passam pela ponte de conversão, então quando o link de
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
