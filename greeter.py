from translate import Translator
# make sur that file name isn't the same as the package we're trying to import from
# translator = Translator(to_lang="es")
# translation = translator.translate("Hello, Hope you have a good day")
# output -> Hola, Espero que tengas un buen día
translator = Translator(to_lang="fr")
translation = translator.translate("Hello, I love you")
print(translation)
# output -> Bonjour je t'aime
