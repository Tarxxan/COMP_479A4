from afinn import Afinn

afinn = Afinn(language='en', emoticons=True)

score = afinn.score('join')
print(score)