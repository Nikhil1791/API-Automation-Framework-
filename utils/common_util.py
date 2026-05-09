from faker import Faker

fake = Faker()


class CommonUtil:

    @staticmethod
    def generate_random_name():
        return fake.name()
    
    