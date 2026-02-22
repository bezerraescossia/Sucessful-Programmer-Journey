from pydantic import BaseModel
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

logging.debug('Creating instances for the class...')

galois = Person(first_name="Evariste", last_name="Galois", age=20)
newton = Person(first_name="Isaac", last_name="Newton", age=84)

logging.debug(f'Calling __dict__ method of the class to output in a dictionary format...')
logging.debug(f'{newton.__dict__}')

logging.debug(f'Serializing via pydantic method model_dump()')
logging.debug(f'{galois.model_dump()}')
logging.debug(f'Type: {type(galois.model_dump())}')

logging.debug(f'Serializing via pydantic method model_dump_json()')
logging.debug(f'{newton.model_dump_json()}')
logging.debug(f'Type: {type(newton.model_dump_json())}')

logging.debug(f'Testing different arguments for dump functions')
logging.debug(f'{newton.model_dump_json(indent=2)}')
logging.debug(f'{newton.model_dump_json(indent= 2, exclude={"first_name", "last_name"})}')
logging.debug(f'{newton.model_dump(include={"first_name"})}')