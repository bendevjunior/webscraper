from bs4 import BeautifulSoup, NavigableString, Tag
import codecs
import requests

html = requests.get("http://agrofit.agricultura.gov.br/agrofit_cons/!ap_produto_form_detalhe_cons?p_id_produto=&p_nm_marca_comercial=abamex&p_id_registrante_empresa=&p_id_ingrediente_ativo=&p_nm_comum_portugues=&p_id_tecnica_aplicacao=&p_id_classe=&p_nr_registro=&p_id_classificacao_tox=&p_id_classificacao_amb=&p_tipo_aplicacao=C&p_id_cultura=&p_id_praga_inseto=&p_id_cultura_planta=&p_id_planta_daninha=&p_id_cultura_praga=&p_id_cultura_inseto=&p_id_praga=&p_nm_sort=nm_marca_comercial&p_linha_inicial=0&p_id_produto_formulado_tecnico=5422").content

#soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(html, 'html5lib')
table = soup.find("table", {"id": "doses"})
trbody = table.find('tbody')

file = codecs.open("arquivos/cultura.txt", "w", "utf-8")
titulos_documentos = ''
collum = 0
for tr in table.findAll(class_='labelCampo'): 
    for td in tr.findAll('td'):
        titulos_documentos += '\n'
        titulos_documentos += 'cabeçalho'
        titulos_documentos += '\n'
        if isinstance(td, NavigableString):
            continue
        if isinstance(td, Tag):
            for t in td.children: 
                if isinstance(t, NavigableString):
                    continue
                if isinstance(t, Tag): 
                   for a in t.children:
                       print(a)
                       titulos_documentos += a + ' - '
file.writelines(titulos_documentos)