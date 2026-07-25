@echo off
REM ============================================================
REM setup_depot.bat
REM Prepare le depot local video_cours (git, git LFS, arborescence,
REM .gitignore) selon la procedure decrite dans CLAUDE.md.
REM
REM A PLACER A LA RACINE DU PROJET video_cours (a cote de 1ereC/,
REM 1ereD/, CLAUDE.md, etc.) puis a lancer par double-clic OU
REM depuis une invite de commandes : setup_depot.bat
REM
REM Si les fichiers livres par Claude (constants.py, boxes.py,
REM render-manim.yml, detect_scenes.py) se trouvent dans le MEME
REM dossier que ce script au moment de l'execution, le script les
REM deplace automatiquement au bon endroit.
REM ============================================================

setlocal enabledelayedexpansion
set "REPO_URL=https://github.com/ibif/video_cours.git"
set "SCRIPT_DIR=%~dp0"

echo.
echo ============================================================
echo   Preparation du depot local video_cours
echo ============================================================
echo.

REM ------------------------------------------------------------
REM 1. Verifier que git est installe
REM ------------------------------------------------------------
where git >nul 2>nul
if errorlevel 1 (
    echo [ERREUR] git n'est pas trouve dans le PATH.
    echo Installe Git pour Windows avant de relancer ce script :
    echo https://git-scm.com/download/win
    pause
    exit /b 1
)
echo [OK] git detecte.

REM ------------------------------------------------------------
REM 2. Initialiser le depot git si necessaire
REM ------------------------------------------------------------
if exist ".git" (
    echo [OK] Depot git deja initialise, on ne touche pas a .git
) else (
    echo [ETAPE] git init...
    git init
    if errorlevel 1 (
        echo [ERREUR] echec de git init.
        pause
        exit /b 1
    )
)

REM ------------------------------------------------------------
REM 3. Configurer le remote origin si absent
REM ------------------------------------------------------------
git remote get-url origin >nul 2>nul
if errorlevel 1 (
    echo [ETAPE] Ajout du remote origin : %REPO_URL%
    git remote add origin %REPO_URL%
) else (
    echo [OK] Remote origin deja configure :
    git remote get-url origin
)

REM ------------------------------------------------------------
REM 4. Git LFS (PDF et videos)
REM ------------------------------------------------------------
where git-lfs >nul 2>nul
if errorlevel 1 (
    echo [ATTENTION] git-lfs n'est pas trouve dans le PATH.
    echo Installe Git LFS avant de continuer : https://git-lfs.com
    echo Le script continue sans LFS pour l'instant, a corriger plus tard.
) else (
    echo [ETAPE] git lfs install...
    git lfs install
    echo [ETAPE] Suivi LFS pour *.pdf et *.mp4...
    git lfs track "*.pdf"
    git lfs track "*.mp4"
)

REM ------------------------------------------------------------
REM 5. Creation de l'arborescence attendue
REM ------------------------------------------------------------
echo.
echo [ETAPE] Creation des repertoires...

if not exist "1ereC" mkdir "1ereC"
if not exist "1ereD" mkdir "1ereD"
if not exist "shapes" mkdir "shapes"
if not exist "scenes" mkdir "scenes"
if not exist "media" mkdir "media"
if not exist "chapters" mkdir "chapters"
if not exist ".github" mkdir ".github"
if not exist ".github\workflows" mkdir ".github\workflows"
if not exist ".github\scripts" mkdir ".github\scripts"

echo [OK] Arborescence creee :
echo   1ereC\  1ereD\  shapes\  scenes\  media\  chapters\
echo   .github\workflows\  .github\scripts\

REM ------------------------------------------------------------
REM 6. .gitignore (uniquement s'il n'existe pas deja)
REM ------------------------------------------------------------
if exist ".gitignore" (
    echo [OK] .gitignore deja present, non modifie.
) else (
    echo [ETAPE] Creation de .gitignore...
    (
        echo media/
        echo media_test_*/
        echo .venv/
    ) > .gitignore
    echo [OK] .gitignore cree.
)

REM ------------------------------------------------------------
REM 7. Deplacer les fichiers livres s'ils sont a cote du script
REM ------------------------------------------------------------
echo.
echo [ETAPE] Recherche des fichiers livres a cote du script...

if exist "%SCRIPT_DIR%constants.py" (
    move /Y "%SCRIPT_DIR%constants.py" "constants.py" >nul
    echo   - constants.py place a la racine.
)

if exist "%SCRIPT_DIR%boxes.py" (
    move /Y "%SCRIPT_DIR%boxes.py" "shapes\boxes.py" >nul
    echo   - boxes.py place dans shapes\
)

if exist "%SCRIPT_DIR%render-manim.yml" (
    move /Y "%SCRIPT_DIR%render-manim.yml" ".github\workflows\render-manim.yml" >nul
    echo   - render-manim.yml place dans .github\workflows\
)

if exist "%SCRIPT_DIR%detect_scenes.py" (
    move /Y "%SCRIPT_DIR%detect_scenes.py" ".github\scripts\detect_scenes.py" >nul
    echo   - detect_scenes.py place dans .github\scripts\
)

REM ------------------------------------------------------------
REM 8. git add + commit (demande confirmation avant, pas de push auto)
REM ------------------------------------------------------------
echo.
echo ============================================================
echo   Preparation terminee.
echo ============================================================
echo.
set /p CONFIRM="Veux-tu faire 'git add' + 'git commit' maintenant ? (o/n) : "
if /i "%CONFIRM%"=="o" (
    git add 1ereC 1ereD constants.py shapes scenes .github .gitignore .gitattributes CLAUDE.md 2>nul
    git commit -m "Setup pipeline autonome (arborescence + git LFS + workflow)"
    echo.
    echo [OK] Commit effectue. Pour pousser vers GitHub :
    echo   git push -u origin main
) else (
    echo [INFO] Rien commite. Verifie le contenu avec 'git status' puis :
    echo   git add ...
    echo   git commit -m "..."
    echo   git push -u origin main
)

echo.
echo N'oublie pas, cote GitHub (une seule fois) :
echo   - Settings - Actions - General - Workflow permissions
echo     - "Read and write permissions"
echo.
pause
endlocal
