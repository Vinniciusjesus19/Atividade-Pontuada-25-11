import pytest

from projeto.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo


@pytest.fixture
def cadastro_medico_valido():
    medico = Medico(7,"Vinnicius", "378218312", "abcdee", 
                Endereco("Rua A", 75, "Casa", "9754","Salvador", Unidade_Federativa.BAHIA), Sexo.MASCULINO,
                Estado_Civil.CASADO,"08/12/2025", "321312", "321321", "321321", Setor.ENGENHARIA, 32133, "A06")
    return medico

def validando_id_do_medico(cadastro_medico_valido):
    assert cadastro_medico_valido.id == 7