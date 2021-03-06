from app_settings import app, db


class Host(db.Model):
	__tablename__ = 'hosts'
	host_id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(80), nullable=False)

	def __repr__(self):
		return '<Host {name} {host_id}>'.format(name=self.name, host_id=self.host_id)

class Appartment(db.Model):
	__tablename__ = 'appartments'
	appartment_id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	neighbourhood_group = db.Column(db.String(80), nullable=False)
	neighbourhood = db.Column(db.String(80), nullable=False)
	latitude = db.Column(db.Numeric(), nullable=False)
	longitude = db.Column(db.Numeric(), nullable=False)
	room_type = db.Column(db.String(80), nullable=True)
	price = db.Column(db.Numeric(), nullable=False)
	minimum_nights = db.Column(db.Numeric(), nullable=True)
	number_of_reviews = db.Column(db.Numeric(), nullable=False, default=0)
	last_review = db.Column(db.DateTime(), nullable=True)
	reviews_per_month = db.Column(db.Numeric(), nullable=True)
	calculated_host_listings_count = db.Column(db.Numeric(), nullable=True)
	availability_365 = db.Column(db.Numeric(), nullable=True)

	host_id = db.Column(db.Integer(), nullable=False)


	def __repr__(self):
		return '<Appartment {name} {neighbourhood} {neighbourhood_group}>'.format(
			name=self.name,
			neighbourhood=self.neighbourhood,
			neighbourhood_group=self.neighbourhood_group
		)

