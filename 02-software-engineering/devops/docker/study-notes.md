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