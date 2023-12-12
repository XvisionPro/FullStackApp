nav_list = [{'title': "Главная", 'url_name': 'main'},
            {'title': "Обо мне", 'url_name': 'about'},
            {'title': 'Портфолио', 'url_name': 'portfolio'},
            {'title': 'Войти', 'url_name': 'login'},]


class DataMixin:
   paginate_by = 2
   def get_user_context(self, **kwargs):
      context = kwargs
      context['nav_list'] = nav_list
      return context
