def simular_ia_analise(redes, sites, interesses=""):
    texto = f"{redes} {sites} {interesses}".lower()

    analise = []
    score = 0
    recomendacoes = []

    if "furia" in texto:
        analise.append("Fã engajado com a organização FURIA.")
        score += 20
        recomendacoes.append("Acompanhe os bastidores da FURIA no YouTube e Twitch.")

    if "valorant" in texto:
        analise.append("Provável fã de Valorant.")
        score += 15
        recomendacoes.append("Confira os torneios VCT no canal oficial da Riot.")

    if "csgo" in texto or "cs:go" in texto:
        analise.append("Fã de FPS competitivo como CS:GO.")
        score += 15
        recomendacoes.append("Participe de comunidades no Discord voltadas para CS.")

    if "lol" in texto or "league" in texto:
        analise.append("Interessado em MOBAs como League of Legends.")
        score += 15
        recomendacoes.append("Explore conteúdos do CBLOL e Worlds.")

    if "dota" in texto:
        analise.append("Possível fã de Dota 2.")
        score += 10
        recomendacoes.append("Siga os torneios The International.")

    if "bet" in texto or "gg" in texto:
        analise.append("Acompanha sites de apostas ou estatísticas de eSports.")
        score += 10
        recomendacoes.append("Use plataformas como HLTV ou EsportsCharts para estatísticas.")

    if "twitch" in texto or "youtube" in texto:
        analise.append("Consome conteúdo ao vivo e vídeos sobre eSports.")
        score += 10
        recomendacoes.append("Assine canais oficiais das equipes e jogos.")

    if "twitter" in texto or "instagram" in texto:
        analise.append("Ativo em redes sociais populares.")
        score += 5
        recomendacoes.append("Siga jogadores profissionais e comentaristas de eSports.")

    if not analise:
        analise.append("Perfil geral de fã de eSports.")
        score += 5

    if not recomendacoes:
        recomendacoes.append("Explore novas modalidades e acompanhe campeonatos ao vivo.")

    resultado = " | ".join(analise)
    pontuacao = f"Pontuação de engajamento: {score}/100"
    sugestoes = "Recomendações: " + " | ".join(recomendacoes)

    return f"{resultado}\n{pontuacao}\n{sugestoes}"
