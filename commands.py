import click
from faker import Faker

from app import db
from app.models import Message 


fake = Faker()

@click.command()
@click.option('--count', default=30, help='Number of forge posts, default is 30.')
def forge_data(count):
    """Simple program to forge post data"""
    click.echo('forging data')
    for _ in range(count):
        name = fake.name()
        time = fake.date_time()
        msg = fake.text()
        post = Message(author=name, created_at=time, content=msg)
        db.session.add(post)
    db.session.commit()
    click.echo('forged {} posts'.format(count))

if __name__ == '__main__':
    forge_data()