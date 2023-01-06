
class Facebook:

    def __init__(self, codigo_facebook):

        self.codigo_facebook = codigo_facebook
        self.url_com_id = []


# função que insere o código do perfil nas urls informativas do Facebook

    def inserir_id_na_url(self):
        lista_de_urls = ['https://facebook.com/search/%s/photos-of',
                         'https://facebook.com/search/%s/photos-tagged',
                         'https://facebook.com/search/%s/photos-commented',
                         'https://facebook.com/search/%s/photos-liked',
                         'https://facebook.com/search/%s/stories',
                         'https://facebook.com/search/%s/stories-commented',
                         'https://facebook.com/search/%s/stories-liked',
                         'https://facebook.com/search/%s/videos-tagged',
                         'https://facebook.com/search/%s/videos-commented',
                         'https://facebook.com/search/%s/videos-liked',
                         'https://facebook.com/search/%s/groups']

        for url in lista_de_urls:
            self.url_com_id.append(url % (self.codigo_facebook))

        self.resultado()

    # Função que exibe as URLs prontas informando o que retornam
    def resultado(self):
        descricao = ['Verificar fotos bloqueadas do perfil',
                     'Verificar fotos que foram marcadas pelo perfil',
                     'Fotos que o perfil comentou',
                     'Fotos em perfil curtiu',
                     'Histórico de postagens do perfil',
                     'Postagens que o perfil comentou',
                     'Postagens que o perfil curtiu',
                     'VÍdeos que foi marcado',
                     'Vídeos que o perfil comentou',
                     'vídeos que o perfil curtiu',
                     'Grupos que pertence']

        print('######################################################')
        for x in range(11):
            print(descricao[x])
            print('<a>' + self.url_com_id[x] + '</a>')
            print('')

        print('######################################################')
