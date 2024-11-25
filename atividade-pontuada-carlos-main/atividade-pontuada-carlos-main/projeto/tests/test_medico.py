import pytest

from projeto.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo


@pytest.fixture
def cadastro_medico_valido():
    medico = Medico(7,"Silvestre", "378218312", "dwqdwq", 
                Endereco("Rua A", 77, "Casa", "8888","Salvador", Unidade_Federativa.BAHIA), Sexo.MASCULINO,
                Estado_Civil.CASADO,"08/07/2000", "321312", "321321", "321321", Setor.ENGENHARIA, 32133, "A04")
    return medico

def validando_id_do_medico(cadastro_medico_valido):
    assert cadastro_medico_valido.id == 7