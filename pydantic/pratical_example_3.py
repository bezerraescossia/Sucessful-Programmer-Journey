from typing import Literal, List, Optional
from pydantic import BaseModel, Field, model_validator

def run_guardrail(query: str) -> Literal["allow", "block"]:
    return "block" if "senha" in query.lower() else "allow"

def get_rag_context(query: str) -> str:
    return "Conteúdo recuperado sobre as normas da ANBIMA..."

def generate_llm_response(query: str, context: str) -> str:
    return f"Baseado na ANBIMA: {query} é permitido conforme o manual."

class RAGFlow(BaseModel):
    user_query: str
    
    # Campos que serão preenchidos durante a validação
    guardrail_status: Optional[Literal["allow", "block"]] = None
    final_answer: Optional[str] = None
    sources: List[str] = Field(default_factory=list)

    @model_validator(mode='after')
    def execute_rag_pipeline(self) -> 'RAGFlow':
        self.guardrail_status = run_guardrail(self.user_query)
        
        if self.guardrail_status == "block":
            self.final_answer = "Sua consulta viola as políticas de segurança."
            self.sources = []
            return self

        context = get_rag_context(self.user_query)
        self.final_answer = generate_llm_response(self.user_query, context)
        self.sources = ["Normativo_ANBIMA_V1.pdf"]
        
        return self

# Execução
fluxo = RAGFlow(user_query="Como funciona a certificação CPA-20?")
print(f"Status: {fluxo.guardrail_status}")
print(f"Resposta: {fluxo.final_answer}")