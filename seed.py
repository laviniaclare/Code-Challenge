import os
import csv
from datetime import datetime
from app_settings import app, db
from models import Host, Appartment


def create_tables():
	db.reflect()
	db.drop_all()
	db.create_all()
	db.session.commit()

def load_data():
	with open('data/AB_NYC_2019.csv', mode='r') as csv_data:
		csv_reader = csv.reader(csv_data, delimiter=',')
		line_count=0
		skipped = []
		hosts_seen = set()
		appartments_seen = set()
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
				continue
			if len(row) < 16:
				# skip rows that are too short because we don't know
				# which columns are missing
				skipped.append(row)
				continue
			line_count += 1
			print(line_count)
			last_review_date = datetime.strptime(row[12],'%Y-%m-%d') if row[12] else None
			appartment_id=int(row[0])
			name=row[1]
			neighbourhood_group=row[4]
			neighbourhood=row[5]
			try:
				latitude=float(row[6])
				longitude=float(row[7])
			except ValueError:
				skipped.append(row)
				continue
			room_type=row[8]
			price=float(row[9])
			minimum_nights=int(row[10])
			number_of_reviews=int(row[11])
			reviews_per_month=float(row[13]) if row[13] else None
			calculated_host_listings_count=int(row[14])
			availability_365=int(row[15])
			host_id=int(row[2])

			new_host = Host(host_id=host_id, name=row[3])
			new_appartment = Appartment(
				appartment_id=int(row[0]),
				name=row[1],
				neighbourhood_group=row[4],
				neighbourhood=row[5],
				latitude=float(row[6]),
				longitude=float(row[7]),
				room_type=row[8],
				price=float(row[9]),
				minimum_nights=int(row[10]),
				number_of_reviews=int(row[11]),
				last_review=last_review_date,
				reviews_per_month=float(row[13]) if row[13] else None,
				calculated_host_listings_count=int(row[14]),
				availability_365=int(row[15]),
				host_id=int(row[2]),
			)
			print(new_appartment)
			print(new_host)

			if new_host.host_id in hosts_seen:
				print("Host {} already added".format(new_host))
			else:
				db.session.add(new_host)
				hosts_seen.add(new_host.host_id)

			if new_appartment.appartment_id in appartments_seen:
				print("Duplicate entry: {}".format(new_appartment))
			else:
				db.session.add(new_appartment)
				appartments_seen.add(new_appartment.appartment_id)

		db.session.flush()

		print(f'Processed {line_count} lines.')
		print(f'Skipped {len(skipped)} lines')


def main():
	create_tables()
	load_data()

if __name__ == '__main__':
	main()
