# Agata Soldato — Permanent Makeup

Landing da nova marca pessoal da Agata Soldato, que sai da Posh Permanent Makeup e passa a
atender com o próprio nome. Mesmos serviços, marca nova.

- HTML/CSS/JS puro, arquivo único, sem framework
- Idiomas EN (principal) / PT-BR / ES por bandeirinha, guardado no localStorage
- Fontes self-hosted (Cormorant Garamond + Poppins, subset latin)
- Deploy estático na Vercel

## Antes de publicar: o que falta preencher

Tudo o que é dado real da Agata está concentrado no topo do `<script>` do `index.html`.
Preencha as quatro constantes e o site inteiro passa a funcionar (CTAs, WhatsApp, formulário):

```js
const PHONE   = '';   // só dígitos com código do país, ex: '15125550100'
const IG      = '';   // handle sem o @, ex: 'agatasoldato'
const STUDIO  = '';   // endereço do novo estúdio
const MAPS    = '';   // link do Google Maps (opcional)
```

O mesmo `PHONE` precisa ser repetido no topo do `thank-you.html`.
Enquanto `PHONE` estiver vazio, todo CTA rola até o formulário em vez de abrir o WhatsApp,
então o site não quebra se for ao ar incompleto. Os campos ainda não preenchidos aparecem
como `[A PREENCHER: ...]` na seção de contato.

## Confirmar com a Agata

1. **Nome da marca.** Assumi `AGATA SOLDATO` como marca, com a assinatura `Ael` dela
   (extraída do material de treinamento) como selo. É o movimento natural de quem perde a
   marca compartilhada: a marca passa a ser a pessoa. Se ela já tem outro nome em mente, o
   wordmark está em um único lugar no HTML (`.brand`).
2. **Números do histórico.** O site diz "desde 2015", "mais de dez mil clientes" e cita
   formação com James Olaya e Branko Babic. Isso vem de fontes públicas ligadas à Posh
   (Yelp, Nextdoor, LinkedIn). **Verificar se o acordo do divórcio permite reivindicar esse
   histórico**, principalmente cláusula de não concorrência ou de não solicitação de
   clientes. Se houver restrição, é só cortar os três números do hero e o bloco de
   credenciais, o resto da página se sustenta sozinho.
3. **Duração e sessões por procedimento.** O painel lateral da seção de serviços mostra
   tempo de cadeira, número de sessões e durabilidade. Usei faixas padrão do setor, estão
   no array `SPECS` do script. Ela precisa confirmar ou corrigir os valores dela.
4. **Endereço, horário e telefone novos.** Os que estão no site antigo são da Posh.
5. **Piercing.** O site antigo oferecia piercing. Mantive só na linha de "também
   disponível", sem destaque, porque piercing não sustenta o tom premium do resto. Se ela
   quiser vender piercing de verdade, vale uma seção própria.

## Fotos que faltam

Trabalhei com o material que veio na pasta: o retrato dela, a peça de treinamento e um par
antes/depois de sobrancelha. A seção de resultados já está montada em carrossel arrastável,
então é só trocar os cartões marcados como "photo coming soon" por pares reais:

| Onde | O que pedir |
|---|---|
| Resultados | Antes/depois de **lip blush**, **eyeliner** e **areola**, já cicatrizados |
| Resultados | Se possível, pares no **mesmo enquadramento e mesma luz**, aí dá pra ligar um comparador com arraste em cima da foto |
| Serviços | Uma foto do **estúdio novo** (ambiente, cadeira, luz) |
| Sobre | Uma segunda foto dela **trabalhando**, não posada, para não repetir o retrato do hero |

Os assets atuais estão em `assets/` já otimizados em WebP. O retrato do hero teve o fundo
ajustado para `#E3DED4`, que é a cor de fundo da seção hero, para a foto parecer sem
moldura. Se trocar a foto do hero, casar a cor de fundo de novo (`--hero` no CSS).

## Rastreio de conversão

Nenhum CTA aponta direto para o `wa.me`. Todos passam por `thank-you.html?c=<contexto>`,
que dispara `dataLayer.push({event:'whatsapp_conversion', contexto, idioma})` e só depois
redireciona. Basta pendurar a tag de conversão no GTM em cima desse evento. O formulário
leva a mensagem montada por `sessionStorage`, nunca pela URL.

## Rodar local

```bash
npx serve -l 8877 .
```

## Performance

Lighthouse local, throttling real (`--throttling-method=devtools`):

| | Performance | Acessibilidade | Boas práticas | SEO |
|---|---|---|---|---|
| Mobile | 99 | 100 | 100 | 100 |
| Desktop | 85–92 | 100 | 100 | 100 |

O desktop oscila por causa do servidor local sem compressão. Vale remedir na URL da Vercel
depois do deploy, que é onde entra brotli e CDN.
