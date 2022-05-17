from .item import Item, ItemCreate, ItemInDB, ItemUpdate
from .msg import Msg
from .token import Token, TokenPayload
from .user import User, UserCreate, UserInDB, UserUpdate
from .istanza import Istanza, IstanzaCreate, IstanzaInDB, IstanzaUpdate
from .richiedente import Richiedente, RichiedenteBase, RichiedenteCreate


'''
Base - all shared attributes of a resource
Create - attributes required to create a new resource - used at POST requests
Update - attributes that can be updated - used at PUT requests
InDB - attributes present on any resource coming out of the database
Public - attributes present on public facing resources being returned from GET, POST, and PUT requests
'''