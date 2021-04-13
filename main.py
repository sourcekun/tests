from gtts import gTTS

text = 'я вас всех взорву нахуй пидарасы, аллахом клянусь, АУЕ ФАРТУ МАСТИ'

obj = gTTS(text, lang='ru')

obj.save('mw.mp3')
123