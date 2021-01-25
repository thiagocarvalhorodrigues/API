import requests

resultado_get = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(resultado_get.json())
#
resultado_get_com_id = requests.get('https://jsonplaceholder.typicode.com/posts/5')
# print(resultado_get_com_id.json())

postagem = {'userId': 1, 'title': 'Uma nova postagem', 'body': 'Olá eu sou uma nova postagem'}

# resultado_post = requests.post('https://jsonplaceholder.typicode.com/posts', postagem)
# print(resultado_post.json())


postagem_atualizada = {'userId': 1, 'title': 'Uma nova postagem', 'body': 'Olá eu sou uma nova postagem 2021'}
resultado_put = requests.put('https://jsonplaceholder.typicode.com/posts/1', postagem_atualizada)
# print(resultado_put.json())

resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(resultado_delete.json())
