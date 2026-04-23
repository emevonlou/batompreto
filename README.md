# BatomPreto

Lightweight OCR + clipboard utility for fast text capture and translation (PT-BR ↔ EN), with on-screen overlay support.  
Ferramenta leve de OCR + clipboard para capturar e traduzir textos na tela (PT-BR ↔ EN), com suporte a sobreposição na tela.

---

## Important / Importante

In some multiplayer servers (such as Hypixel), features like OCR and AutoCopy may not behave as expected.

This happens because these environments often handle inputs, overlays and automated interactions differently, which can interfere with how the app reads, copies or processes text.

For a smoother experience, it is recommended to disable these features while playing online.  

Em alguns servidores multiplayer (como o Hypixel), funcionalidades como OCR e AutoCopy podem não se comportar como esperado.

Isso acontece porque esses ambientes lidam de forma diferente com inputs, overlays e interações automáticas, o que pode interferir na leitura, cópia ou processamento de texto pelo app.

Para uma experiência mais estável, é recomendado desativar essas funções durante o uso em servidores online.

---

## Features / Funcionalidades

- Real-time translation (Portuguese ↔ English) / Tradução em tempo real (Português ↔ Inglês)
- Bilingual quick phrases system (Portuguese and English) / Sistema de frases rápidas bilíngue (Português e Inglês)
- Double-click to insert English phrases / Duplo clique para inserir frases em inglês
- Right-click to insert Portuguese phrases / Clique com botão direito para inserir frases em português
- Smart clipboard system with anti-spam protection / Sistema inteligente de cópia com proteção anti-spam
- OCR-based chat detection and translation / Detecção e tradução de chat via OCR
- Always-on-top window for in-game usage / Janela sempre visível para uso em jogo
- Lightweight and responsive interface / Interface leve e responsiva

---

## Usage / Uso

Recommended / Recomendado  
- Singleplayer / servidores privados  
- Quick text capture and translation / captura e tradução rápida  
- Live communication (games, calls, work) / comunicação em tempo real (jogos, calls, trabalho)  

Avoid / Evite  
- Competitive multiplayer environments when using automation features  
- Ambientes multiplayer competitivos ao utilizar funcionalidades automatizadas  

---

## Installation / Instalação

### Fedora (Recommended) / Fedora (Recomendado)

#### Dependencies / Dependências

Before installing, make sure you have the required dependencies installed:

Antes de instalar, certifique-se de ter as dependências necessárias:

```bash
sudo dnf install python3 python3-tkinter crow-translate
```
- Install using RPM / Instale usando RPM:
```bash
sudo dnf install ./batompreto-1.1.0-1.fc42.x86_64.rpm
```
This is the recommended and fully tested installation method.
Este é o método recomendado e totalmente testado.

- Linux Portable (Experimental) / Linux Portátil (Experimental)

A portable .zip version is available, but it may depend on system libraries and is not fully validated yet.
Uma versão portátil em .zip está disponível, mas pode depender de bibliotecas do sistema e ainda não está totalmente validada.

If you choose to use it / Se você optar por usar:
```bash
unzip batompreto-linux-portable.zip
cd dist/batompreto
./batompreto
```
If it does not work on your system, please use the RPM version instead.
Se não funcionar no seu sistema, utilize a versão RPM.

---

About / Sobre

BatomPreto is currently under active development.
BatomPreto está atualmente em fase de desenvolvimento.
It was originally created for personal use, focused on improving real-time communication while gaming and working.
Inicialmente foi criado para uso pessoal, com foco em melhorar a comunicação em tempo real durante jogos e trabalho.
I decided to continue developing and sharing it because I believe in open source and collaborative improvement.
Decidi continuar desenvolvendo e compartilhar o projeto porque acredito no open source e na evolução colaborativa.

---

## Note

Not made to automate gameplay — only to assist communication and understanding.  
Não foi feito para automatizar gameplay — apenas auxiliar na comunicação e compreensão.
