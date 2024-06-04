import numpy as np
import pandas as pd
import plotly.graph_objects as go
import json



def plot1(df):
    p = df.sort_values(by="Pessoas_afetadas", ascending=False).iloc[:10,:][["NM_MUN","Pessoas_afetadas"]].sort_values(by="Pessoas_afetadas", ascending=True)
    p["label"] = p.apply(lambda x: "{} ({:,} mil)".format(x["NM_MUN"], x["Pessoas_afetadas"]), axis=1).values
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=p["Pessoas_afetadas"], y=p["NM_MUN"], orientation='h', text=p["label"], marker_color="#e9c545"))
    fig.update_layout(barcornerradius=15)
    json_output = json.loads(fig.to_json())
    json_output["title"] = "Valor Absoluto da População Afetada Pelas Cheias no Rio Grande do Sul"
    json_output["text"] = """
        Das regiões mais afetadas encontramos em primeiro a cidade de Canoas, em seguida Porto Alegre, São Leopoldo,
        Eldorado do Sul, Guaíba, Santa Cruz do Sul, Lajeado, Novo Hamburgo, Estrela e Montenegro. Estão as dez cidades
        mais afetadas pelas cheias no Rio Grande do Sul, em termos de população afetada.
        """
    return json_output


def plot2(df):
    p = df.sort_values(by="Domicilios_2022", ascending=False).iloc[:10,:][["NM_MUN","Domicilios_2022"]].sort_values(by="Domicilios_2022", ascending=True)
    p["label"] = p.apply(lambda x: "{} ({:,} mil)".format(x["NM_MUN"], x["Domicilios_2022"]), axis=1).values
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=p["Domicilios_2022"], y=p["NM_MUN"], orientation='h', text=p["label"], marker_color="#e9c545"))
    fig.update_layout(barcornerradius=15)
    json_output = json.loads(fig.to_json())
    json_output["title"] = "Quantidade de domicílios Afetada Pelas Cheias no Rio Grande do Sul"
    json_output["text"] = """
        Em Porto Alegre, quase 700 mil domicílios foram afetados pelas enchentes. Essa quantidade é três 
        vezes maior do que o município que vem em seguida, Caxias do Sul. Além disso, outros cinco 
        municípios tiveram mais de cem mil domicílios afetados: Canoas, Santa Maria, Gravataí, Viamão e Novo Hamburgo.
        """
    return json_output


def plot3(df):
    p = df.sort_values(by="Pessoas_%", ascending=False).iloc[:10,:][["NM_MUN","Pessoas_%"]].sort_values(by="Pessoas_%", ascending=True)
    p["label"] = p.apply(lambda x: "{} ({:,}%)".format(x["NM_MUN"], x["Pessoas_%"]), axis=1).values
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=p["Pessoas_%"], y=p["NM_MUN"], orientation='h', text=p["label"], marker_color="#e9c545"))
    fig.update_layout(barcornerradius=15)

    json_output = json.loads(fig.to_json())
    json_output["title"] = "Porporção de pessoas afetadas Pelas Cheias no Rio Grande do Sul"
    json_output["text"] = """
        Das regiões mais afetadas encontra-se em primeiro a cidade de Eudorado do Sul. Em seguida Estrela, Canoas,
        São Leopoldo, Roca Sales, Muásum, Arroio do Meio, Dona Francisca, Encantado e Cerro Branco. Estas são as dez cidades
        mais afetadas pelas cheias no Rio Grande do Sul.
        """
    return json_output


def plot4(df):
    p = df.sort_values(by="Domicilios_2022", ascending=False).iloc[:10,:][["NM_MUN","Domicilios_2022"]].sort_values(by="Domicilios_2022", ascending=True)
    p["label"] = p.apply(lambda x: "{} ({:,} mil)".format(x["NM_MUN"], x["Domicilios_2022"]), axis=1).values
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=p["Domicilios_2022"], y=p["NM_MUN"], orientation='h', text=p["label"], marker_color="#e9c545"))
    fig.update_layout(barcornerradius=15)
    json_output = json.loads(fig.to_json())
    
    json_output["title"] = "Outro Titulo"
    json_output["text"] = """
        Das regiões mais afetadas encontramos em primeiro a cidade de eudorado do sul, em seguida Estrela, Canoas,
        São Leopoldo, Roca Sales, Muásum, Arroio do Meio, Dona Francisca, Encantado e Cerro Branco. Estão as dez cidades
        mais afetadas pelas cheias no Rio Grande do Sul.
        """
    return json_output


def plot5(df):
    p = df.sort_values(by="Domicilios_2022", ascending=False).iloc[:10,:][["NM_MUN","Domicilios_2022"]].sort_values(by="Domicilios_2022", ascending=True)
    p["label"] = p.apply(lambda x: "{} ({:,} mil)".format(x["NM_MUN"], x["Domicilios_2022"]), axis=1).values
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=p["Domicilios_2022"], y=p["NM_MUN"], orientation='h', text=p["label"], marker_color="#e9c545"))
    fig.update_layout(barcornerradius=15)
    json_output = json.loads(fig.to_json())
    
    json_output["title"] = "Outro Titulo"
    json_output["text"] = """
        Das regiões mais afetadas encontramos em primeiro a cidade de eudorado do sul, em seguida Estrela, Canoas,
        São Leopoldo, Roca Sales, Muásum, Arroio do Meio, Dona Francisca, Encantado e Cerro Branco. Estão as dez cidades
        mais afetadas pelas cheias no Rio Grande do Sul.
        """
    return json_output