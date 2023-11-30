from flask_restful import Resource
from api import api
from ..schemas import formacao_schema
from flask import request, make_response, jsonify
from ..entidades import formacao
from ..services import formacao_service

class FormacaoList(Resource):
    def get(self):
        formacao = formacao_service.listar_formacoes()
        cs = formacao_schema.FormacaoSchema(many=True)
        return make_response(cs.jsonify(formacao), 200)
    
    def post(self):
        cs = formacao_schema.FormacaoSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
        
        novo_formacao = formacao.Formacao(nome=nome, descricao=descricao)
        resultado = formacao_service.cadastrar_formacao(novo_formacao)
        x = cs.jsonify(resultado)
        return make_response(x, 201)



class FormacaoDetail(Resource):
    def get(self, id):
        formacao = formacao_service.listar_formacao(id)
        if formacao is None:
            return make_response(jsonify("formacao não encontrado"), 404)
        else:
            cs = formacao_schema.FormacaoSchema()
            return make_response(cs.jsonify(formacao), 200)

    def put(self, id):
        formacao_bd = formacao_service.listar_formacao(id)
        if formacao_bd is None:
            return make_response(jsonify("formacao não encontrado"), 404)
        
        cs = formacao_schema.FormacaoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(cs.jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            novo_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            formacao_service.atualiza_formacao(formacao_bd, novo_formacao)
            formacao_atualizado = formacao_service.listar_formacao(id)
            return make_response(cs.jsonify(formacao_atualizado), 200)


    def delete(self, id):
        formacao_bd = formacao_service.listar_formacao(id)
        if formacao_bd is None:
            return make_response(jsonify("formacao não encontrado"), 404)
        
        formacao_service.remove_formacao(formacao_bd)
        return make_response(jsonify("formacao deletado com sucesso"), 200)


api.add_resource(FormacaoList, "/formacoes")
api.add_resource(FormacaoDetail, "/formacoes/<int:id>")