from random import choice

from app import db
from .resource_category import ResourceCategory


class Resource(db.Model):
    """
    Basic schema for a resource

    TODO: Add descriptors and associations
    """

    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('resource_categories.id'))
    address = db.Column(db.String(500))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    description = db.Column(db.String(500))
    website = db.Column(db.String(500))

    def __repr__(self):
        return '<Resource: {resource}>'.format(resource=self.name)

    @staticmethod
    def get_resources_as_dict():
        resources = Resource.query.all()
        resources_as_dicts = []
        for resource in resources:
            resource = resource.__dict__
            resource["category"] = ResourceCategory.query.get(resource["category_id"]).name
            if '_sa_instance_state' in resource:
                del resource['_sa_instance_state']
            resources_as_dicts.append(resource)
        return resources_as_dicts

    @staticmethod
    def get_single_resource_as_dict(id):
        resource = Resource.query.get(id)
        print(resource)
        if resource is not None:
            resource = resource.__dict__

            if '_sa_instance_state' in resource:
                del resource['_sa_instance_state']

        return resource

    @staticmethod
    def generate_fake(count=15, center_lat=43.6591, center_long=-70.2568):
        """
        Generate a number of fake resources for testing

        :param count: number of fake resources to make
        :param center_lat: center latitude for state
        :param center_long: center longitude for state
        :return: None
        """

        from sqlalchemy.exc import IntegrityError
        from faker import Faker
        from geopy.geocoders import Nominatim

        fake = Faker()
        geolocater = Nominatim(user_agent="place-matters")
        categories = ResourceCategory.query.all()
        for i in range(count):
            name = fake.name()

            # Generate places around Cumberland County, Maine
            latitude = str(fake.coordinate(
                center=center_lat,
                radius=0.20
            ))
            longitude = str(fake.coordinate(
                center=center_long,
                radius=0.20
            ))

            location = geolocater.reverse(latitude + ', ' + longitude)
            # Check to make sure a valid location is found
            if location.address is None:
                continue

            resource = Resource(name = name,
                                address = location.address,
                                category_id=choice(categories).id,
                                latitude = latitude,
                                longitude = longitude,
                                website=fake.url(),
                                description=fake.text())

            db.session.add(resource)

            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

    @staticmethod
    def print_resources():
        """
        Print list of all resources

        :return: None
        """
        resources = Resource.query.all()
        for resource in resources:
            print(resource)
            print((resource.address))
            print(('(%s , %s)' % (resource.latitude, resource.longitude)))
