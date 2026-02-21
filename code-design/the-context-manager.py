# The Scenario: You are building a system that fetches "Chunks" of text from a vector database and feeds them to an LLM. The LLM has a Strict Token Limit. If you send too much text, the API calls will fail.
# Your Goal: Create a DocumentChunk class to manage these pieces of text.

class DocumentChunk:
    _total_tokens: int = 0
    _loaded_chunks: list[str] = []
    MAX_TOKENS: int = 1000

# --- Creation functions ---
    @classmethod
    def from_raw_text(cls, text: str) -> 'DocumentChunk':
        token_count: int = len(text.split(' '))
        return DocumentChunk(text, token_count)

    def __init__(self, content: str, token_count: int) -> None:
        if self._has_valid_number_of_tokens(token_count):
            self.token_count = token_count
            self.content = content
            self._add_document_chunk(content, token_count)
        else:
            raise MemoryError('LLM Context Window Full!')
        
    def __del__(self) -> None:
        if hasattr(self, 'token_count'):
            DocumentChunk._total_tokens -= self.token_count
            DocumentChunk._loaded_chunks.remove(self.content)

# --- Gatekeeper functions ---
    @classmethod
    def _has_valid_number_of_tokens(cls, token_count: int) -> bool:
        total: int = token_count + cls._total_tokens
        if total <= cls.MAX_TOKENS:
            return True
        else:
            return False

# --- Helper Functions ---
    @classmethod
    def _add_document_chunk(cls, content: str, token_count: int) -> None:
        cls._total_tokens += token_count
        cls._loaded_chunks.append(content)

# --- Utility Functions ---
    @staticmethod
    def estimate_cost(price_per_token: float, number_of_token: int):
        return price_per_token * number_of_token


d1 = DocumentChunk.from_raw_text('Testando se esse texto funcionara direito')
d2 = DocumentChunk.from_raw_text(""""
                                 The "RAG Context Manager" Challenge
                                The Scenario: You are building a system that fetches "Chunks" of text from a vector database and feeds them to an LLM. The LLM has a Strict Token Limit. If you send too much text, the API calls will fail.

                                Your Goal: Create a DocumentChunk class to manage these pieces of text.

                                1. Shared State (The "Buffer")
                                _total_tokens: A class variable (int) tracking the sum of tokens currently loaded.

                                _loaded_chunks: A class variable (list) storing the content of all chunks currently in memory.

                                MAX_TOKENS = 1000: A class-level constant representing the limit.

                                2. The Factory Method: from_raw_text
                                Create a classmethod from_raw_text(cls, text).

                                Inside this method, simulate a tokenizer by calculating the token count (for this challenge, let's just say 1 word = 1 token).

                                It should then return a new instance of DocumentChunk.

                                3. The Constructor (__init__)
                                Takes content and token_count.

                                The Guard: Before adding the chunk, check if _total_tokens + current_tokens exceeds MAX_TOKENS.

                                If it exceeds the limit, raise a MemoryError("LLM Context Window Full!").

                                If safe, update the class-level total tokens and append the content to the class-level list.

                                4. The Utility: estimate_cost
                                Create a staticmethod estimate_cost(tokens).

                                RAG engineers always track spend! Assume the price is $0.0002 per token. Return the calculated price.

                                5. The Cleanup (__del__)
                                When a chunk is "popped" or deleted from the context, subtract its tokens from the total and remove its text from the list.

                                This is a "real-world" architecture for a local context cache. Show me how you'd build this AI-ready management system!
                                 """)
del d2
print(d1)