from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Olá usuário {}.
Bem vindo ao {}

Eu sou o Mestre dos Sussurradores (como Varys em Game of Thron). 👻🤨 Maconha doida pow tlgd? Kjjkk, brinks!

Você pode me usar para mandar mensagem secretamente para alguém! Com id ou username em grupos e canais.


Para ver como funciona, aperte 'Como usar' abaixo..

By 『♚•꣣𝑻⃯̭꣣𝒉⃯̭꣣𝒆⃯̭꣣ ┼ ͓꣣𝑷⃯̭͓꣣𝒂⃯̭꣣𝒏⃯̭꣣𝒅⃯̭͓꣣𝒂⃯̭꣣•♚』〖⭟ ˢ͢ᵗ͢ᵃ͢ᶠ͢ᶠ ⃪ 〗
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 Envie um sussurro 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 Voltar ao inicial 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 Envie um sussurro 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("Como usar ❔", callback_data="help"),
            InlineKeyboardButton("🎪 Sobre 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("⨣ Criador pae ⨣", url="https://t.me/xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx")],
        [InlineKeyboardButton("⚙ Grupo de Suporte ⚙", url="https://t.me/blazer808_Stay")],
    ]

    # Help Message
    HELP = """
Basta digitar a mensagem abaixo do formato em qualquer bate-papo..

`@panbbot Sua Mensagem Username da pessoa ou/id`
    """

    # About Message
    ABOUT = """
**Sobre esse bot** 

Bot criado pelo @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx

Inspirado pelo : nnbbot ( Rei das mensagens secretas ) 

Estrutura : [Pyrogram](docs.pyrogram.org)

Linguagem : [Python](www.python.org)

Desenvolvedor : @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx
    """
