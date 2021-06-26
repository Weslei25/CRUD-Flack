from app import db


class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	name = db.Column(db.String)
	email = db.Column(db.String, unique=True)

	def __init__(self, username, password, name, email):
		self.username = username
		self.password = password
		self.name = name
		self.email = email


	def __repr__(self):
		return "<User %r>" % self.username
		# retorna os usarios de forma ordenada


class Post(db.Model):
	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	user_id = db.Column(db,Integer, db.ForeignKey('users_id'))

	user = db.relationship('User', foreign_keys=user_id)
	# Ha uma relação entre a tabema uses e a tabela posts

	def __init__(self, content, user_id):
		self.content = content
		self.user_id = user_id


	def __repr__(self):
		return "<Post %r>" % self.id
		# Retorno somente o id no lugar do post


class Follow(db.Model):
	__tablename__ = "follow"

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users_id'))
	follower_id = db.Column(db.Integer, db.ForeignKey('users_id'))

	user = db.relationship('User', foreign_keys=user_id)
	follower = db.relationship('User', foreign_keys=user_id)
		