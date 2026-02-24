---
author: bzescossia
created: 2026-02-22
---

# Docker

- A construção de uma imagem em docker `docker build .` é baseada em camadas (*layered-based*). Portanto, a ordem na qual uma *Dockerfile* é escrito faz diferença, no exemplo abaixo é demonstrado como podemos usar as camadas para otimizar a construção de imagens. Note que na situação anterior qualquer alteração na pasta indicará executar o requirements.txt, enquanto que depois da otimização esse comando só será executado se o requirements.txt alterar.

    **Antes**:

    ```bash
    FROM python

    WORKDIR /app

    COPY . /app

    RUN pip install -r requirements.txt
    ```

    **Depois**:

    ```bash
    FROM python

    WORKDIR /app

    COPY requirements.txt /app

    RUN pip install -r requirements.txt

    COPY . /app
    ```

- `RUN` e `CMD` parecem semelhantes, porém existe uma diferença crucial! Enquanto que `RUN` é utilizado na construção da imagem, o comando `CMD` é um comando executado no lançamento do *container*. Portanto, é necessário prestar atenção se o comando que você quer passar é de construção de imagem ou de execução de *container*.
- Por padrão `docker run` inicia um novo container, mesmo que já exista um container associado a imagem.
- Por padrão `docker run` executa em *attach* mode, enquanto que `docker start` executa em *dettach*
- Uma imagem somente poderá ser removida por `docker rmi image_name` se não houver nenhum container dessa imagem, mesmo que pausado (stop). Portanto, para remover essa imagem é preciso primeiro remover os containers a ele associado e depois remover a imagem.