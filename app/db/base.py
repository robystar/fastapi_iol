# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.user import User  # noqa
from app.models.recipe import Recipe  # noqa

from app.models.istanza import Istanza

from app.models.soggetti import Fisica, Giuridica, Recapito, Tecnico, Esecutore, Condominio, Richiedenti, Tecnici, Esecutori

from app.models.ubicazione import Civici, Nct, Uiu