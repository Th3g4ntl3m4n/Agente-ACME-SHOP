# pyrefly: ignore [missing-import]
import agentplatform

client = agentplatform.Client(project="agent-platform-platzi-510322", location="us-central1")


def consultar_conocimiento_empresa(query: str) -> str:
    """Consulta la base de conocimiento general de la compañía para responder preguntas corporativas, 
    sobre la empresa o políticas generales.

    Args:
        query: La consulta o término a buscar en la base de conocimiento.

    Returns:
        Información obtenida de la base de conocimiento.
    """
    try:
        response = client.rag.retrieve_contexts(
            vertex_rag_store={
                "rag_resources": [
                    {
                        "rag_corpus": (
                            "projects/agent-platform-platzi-510322/locations/us-central1/ragCorpora/2226036057223200768"
                        )
                    }
                ]
            },
            query={"text": query},
        )
        if not response.contexts or not response.contexts.contexts:
            return "No se encontró información relevante en la base de conocimiento de la empresa."

        return "\n\n".join([ctx.text for ctx in response.contexts.contexts])
    except Exception as e:
        return f"Error al consultar el RAG Corpus: {str(e)}"


conocimiento_empresa_rag = consultar_conocimiento_empresa