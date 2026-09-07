# Agata Medical Aesthetics

Site da nova marca da Agata Soldato, montado a partir do documento de conteúdo e
de marca que ela enviou (`Agata_Medical_Aesthetics_Website_Content_WITH_PACKAGES.docx`).

A marca **não** é mais "Agata Soldato". É **Agata Medical Aesthetics**, selo AMA,
assinatura "Cosmetic & Paramedical Tattooing". A Agata aparece como fundadora e
master artist, ao lado da Lanie Stein, artista sênior.

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
const BOOKING = '';   // link do sistema de agendamento (opcional)
```

`PHONE` e `BOOKING` também precisam ser repetidos no topo do `thank-you.html`.

Enquanto os dois estiverem vazios, todo CTA rola até o formulário em vez de sair
da página, então o site não quebra se for ao ar incompleto. Os campos vazios
aparecem como "To be confirmed" na seção de contato.

O próprio documento dela avisa, e vale repetir: **não reaproveitar o telefone,
o endereço nem o e-mail da Posh** (11719 RM 2244 #101, Bee Cave, TX 78738,
+1 512 251-4170, info@poshpermanentmakeup.com) a menos que continuem válidos
para a empresa nova.

## Confirmar com a Agata

1. **Financiamento.** A seção existe e explica o processo, mas sem provedor. O
   documento dela manda só publicar provedor, link, APR promocional, compra
   mínima e disclosures depois de confirmar a conta merchant da empresa nova, e
   proíbe herdar a conta de financiamento da Posh. Hoje o CTA leva ao formulário.
2. **Retrato da Lanie.** Os dois arquivos vieram nomeados `ChatGPT Image`, um com
   jaleco branco e outro preto, mesma pose e mesma luz. Parece retoque de
   guarda-roupa sobre uma foto real, o que é normal. Se for imagem gerada, não
   pode ir ao ar como foto de uma pessoa nomeada. Confirmar com ela.
3. **Histórico.** O site diz 12 anos e mais de 10 mil procedimentos, números que
   vieram do documento dela. Como parte desse histórico foi construída sob a
   marca Posh, **confirmar se o acordo do divórcio permite reivindicá-lo**,
   principalmente cláusula de não concorrência ou de não solicitação.
4. **Preços dos pacotes.** Estão publicados exatamente como no documento: economia
   de US$ 500 no Complete Look, US$ 500 no PMU Reset, US$ 749 no Tummy, US$ 949
   no Breast. Conferir antes de ir ao ar, preço em página pública é promessa.
5. **Sessões e tempo de cadeira** na tabela de serviços usam faixas padrão do
   setor. Estão no array `SERVICES` do script, um por idioma. Ela precisa
   confirmar ou corrigir.
6. **Consentimento de SMS.** O texto do formulário é o que ela mandou. O próprio
   documento pede revisão jurídica da política de privacidade, do texto de SMS e
   dos termos de uso antes do lançamento.

## Fotos que faltam

A seção de resultados é um carrossel arrastável. Só o par de sobrancelha é real,
os outros quatro cartões estão marcados como "photo coming soon" e são só trocar:

| Onde | O que pedir |
|---|---|
| Resultados | Antes/depois de **lip blush**, **eyeliner**, **aréola** e **camuflagem de cicatriz**, já cicatrizados |
| Resultados | Pares no **mesmo enquadramento, distância e luz**, como o próprio documento dela pede |
| Serviços | Foto do **estúdio novo** |
| Artistas | Uma foto de cada uma **trabalhando**, não posada |
| Hero | O hero hoje é só tipografia. Se entrar foto ali, tem que casar o fundo com `--hero` `#F1E7DA` |

## Assets, e a armadilha do fundo

Os retratos **não** têm fundo recortado. O fundo foi casado com a cor da seção em
que a foto aparece, o que evita halo no cabelo:

| Arquivo | Fundo casado com |
|---|---|
| `agata-editorial.webp` (bloco Artistas) | `--ivory` `#F8F3EB` |
| `lanie.webp` (bloco Artistas) | `--ivory` `#F8F3EB` |

Se trocar qualquer uma dessas fotos, ou mudar a cor da seção, refazer o
casamento, senão volta a aparecer o retângulo da foto. A técnica está nos
scripts: máscara do fundo cinza do estúdio por distância de cor mais teste de
temperatura (o fundo é frio, o jaleco creme é quente), blur de 1.5px na borda, e
balanço quente aplicado só ao sujeito.

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
| 100 | 100 | 100 | 100 |

LCP 1,0s · CLS 0,004 · TBT 0ms

## Decisões de layout que não devem ser desfeitas

**Sem tag acima de título.** Nenhuma seção tem kicker em caixa alta. Foi removido
de propósito, é o que dá cara de template.

**Hero sem foto.** Só tipografia centrada, título em duas linhas. O `max-width`
do H1 é `41ch` e **não pode levar `text-wrap:balance`**: com balance o navegador
reequilibra e devolve a terceira linha.

**Pacotes em linhas horizontais, não em cards.** Quatro linhas de
`nome | descrição e itens | preço | CTA`. Os itens de cada pacote são uma lista
inline separada por losango, não uma lista vertical. Isso cortou a seção de
1.759px para 1.572px e alinhou os preços numa coluna, que é o que permite
comparar. Sticky stack foi considerado e descartado: o efeito é bonito mas cada
card passa a exigir uma tela de rolagem, ou seja, faz o oposto de compactar.

**Artistas sem cargo abaixo do nome** e sem "Master" antes de Agata Soldato. Os
anos de experiência continuam no primeiro parágrafo de cada uma.

**Não devolver o hero para `flex-wrap`.** Os dois botões do hero e o bloco de
números ficavam exatamente no limite de caber lado a lado em 412px. Qualquer
mudança de largura do texto, inclusive a troca da fonte de fallback para a real,
desempilhava a linha e puxava 66px de tudo abaixo. Isso sozinho valia CLS 0,12.
Hoje os botões empilham em largura total abaixo de 560px e as métricas são grid
de colunas fixas, as duas coisas deterministas.
