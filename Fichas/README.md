Indice: ➭ ⭢ ⇨ ⬇ ⬎ ↴ ➥➦ ▼
Ctrl J: Terminal
Crtl S: Salva o arquivo
Crtl Z: Salvar tudo
Crtl P: Acesso a pesquisa
Print: Crtl + Shift + S ou Win + PrtSc
Py: python –-version ou -v

Crie uma pasta no Desktop “Repositório”
VsC: File ➥ Open Folder ➥ “Repositório” ➥ New File
Idioma: Crtl P ➦ Configure Display Language ➦ PT-BR

Terminal ➥ git init ➥ git clone ▼ 
<> Code ➥ Https ➥ Url ▼
https://github.com/codartz/Senac.git ▼
cd Senac ➥ git add PP.py ▼
git commit -m "Primeiro commit: add PP.py" ▼
git branch -M main ▼
git push -u origin main 


No terminal, estando na raiz do repositório e com os ficheiros já salvos:
# adiciona tudo que mudou (novos, modificados, removidos)
git add .            # ou `git add -A`

# cria um commit com uma mensagem descritiva
git commit -m "Minha mensagem de commit"

# envia a branch actual para o remoto (origin/main por exemplo)
git push -u origin main


ou, se as alterações forem apenas em ficheiros já rastreados, dá para
combinar add+commit em:
git commit -am "mensagem"   # atalho: adiciona+commita modificações
git push

Se o seu repositório usa a branch main
# ir para o diretório do clone local
cd "c:\Users\Taís\OneDrive - SENAC-SC\Senac\Senac"

# buscar e mesclar as alterações da branch 'main' no GitHub
git pull origin main

Caso sua branch principal se chame master substitua main por master nos comandos.

git pull origin <nome-da-branch>
cd caminho/do/seu/repositorio
git pull origin main