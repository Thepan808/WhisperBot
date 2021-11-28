from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Olá usuário {}.
Bem vindo ao {}

Eu sou o " Mini Mestre dos Sussurradores ". 👻🤨 Maconha doida pow tlgd? Kjjkk, brinks!

Você pode me usar para mandar mensagem secretamente para alguém! Com id ou username em grupos e canais.


Para ver como funciona, aperte 'Como usar' abaixo..

By 『♚•꣣𝑻⃯̭꣣𝒉⃯̭꣣𝒆⃯̭꣣ ┼ ͓꣣𝑷⃯̭͓꣣𝒂⃯̭꣣𝒏⃯̭꣣𝒅⃯̭͓꣣𝒂⃯̭꣣•♚』〖⭟ ˢ͢ᵗ͢ᵃ͢ᶠ͢ᶠ ⃪ 〗
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 Envie um sussurro 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="♦ Voltar ao inicial ♦", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 Envie uma mensagem privada 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("Como usar ❔", callback_data="help"),
            InlineKeyboardButton("🤨 Sobre 🤨", callback_data="about")
        ],
        [InlineKeyboardButton("♦ Criador ♦", url="https://t.me/The_Panda_Ofc")],
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

Bot criado pelo @The_Panda_Ofc

Inspirado pelo : nnbbot ( Rei das mensagens secretas ) 

Estrutura : [Pyrogram](docs.pyrogram.org)

Linguagem : [Python](www.python.org)

Desenvolvedor : @The_Panda_Ofc
    """
