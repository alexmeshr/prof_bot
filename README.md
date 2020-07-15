# profbot
models.py
	-class BaseModel(Model)
	-class User(BaseModel)
		-username
		-join_date
		-score	
		-current_chat_id																																																																									
	-class Point(BaseModel)
		-score
		-question
		-wr_answer
		-r_answer
utils.py
	-def parsing(message) - получает сообщение и обрабатывает
	-def generate_markup(answers, i) и def next_markup() служебные функции для встроенных клавиатур
views.py 
	-def get_points() - выдает кп
	-def register(id) - /проверяет, есть ли пользователь в базе/(еще не сделано) и добавляет, если нужно
    -def clear_users() - удаляет всех пользователей
	-def create_tables() - создает бд



