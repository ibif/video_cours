@echo off
REM ============================================================
REM pousser_tag_test.bat
REM Recupere la branche claude/maths-test-scene-setup-5mx8sq,
REM cree le tag chapitre__1ereC__Maths__Test et le pousse vers
REM GitHub pour declencher le rendu HD complet (voir CLAUDE.md,
REM section "Pipeline autonome").
REM
REM A LANCER depuis un dossier qui est DEJA un clone du depot
REM video_cours (celui ou tu executes normalement tes commandes
REM git). Si ce n'est pas le cas, le script propose de cloner le
REM depot dans un nouveau dossier "video_cours".
REM ============================================================

setlocal enabledelayedexpansion
set "REPO_URL=https://github.com/ibif/video_cours.git"
set "BRANCH=claude/maths-test-scene-setup-5mx8sq"
set "TAG=chapitre__1ereC__Maths__Test"

echo.
echo ============================================================
echo   Declenchement du rendu HD - %TAG%
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
REM 2. Se placer dans le depot (clone si absent)
REM ------------------------------------------------------------
git rev-parse --is-inside-work-tree >nul 2>nul
if errorlevel 1 (
    echo.
    echo [INFO] Ce dossier n'est pas un depot git.
    if exist "video_cours" (
        echo [OK] Dossier video_cours deja present, on y entre.
        cd video_cours
    ) else (
        echo [ETAPE] Clonage de %REPO_URL% ...
        git clone %REPO_URL%
        if errorlevel 1 (
            echo [ERREUR] echec du clonage.
            pause
            exit /b 1
        )
        cd video_cours
    )
)

REM ------------------------------------------------------------
REM 3. Recuperer et basculer sur la branche
REM ------------------------------------------------------------
echo.
echo [ETAPE] git fetch origin %BRANCH% ...
git fetch origin %BRANCH%
if errorlevel 1 (
    echo [ERREUR] echec du fetch. Verifie ta connexion / tes droits d'acces.
    pause
    exit /b 1
)

echo [ETAPE] git checkout %BRANCH% ...
git checkout %BRANCH%
if errorlevel 1 (
    echo [ERREUR] echec du checkout.
    pause
    exit /b 1
)

echo [ETAPE] git pull origin %BRANCH% ...
git pull origin %BRANCH%

echo.
echo [OK] Derniers commits sur %BRANCH% :
git log --oneline -5
echo.

REM ------------------------------------------------------------
REM 4. Verifier si le tag existe deja (local ou distant)
REM ------------------------------------------------------------
git rev-parse %TAG% >nul 2>nul
if not errorlevel 1 (
    echo [ATTENTION] Le tag %TAG% existe deja localement.
    set /p CONFIRM="Le supprimer et le recreer ? (o/n) : "
    if /i "!CONFIRM!"=="o" (
        git tag -d %TAG%
    ) else (
        echo [INFO] Script interrompu, tag non touche.
        pause
        exit /b 0
    )
)

REM ------------------------------------------------------------
REM 5. Creer et pousser le tag
REM ------------------------------------------------------------
echo.
echo [ETAPE] Creation du tag %TAG% ...
git tag %TAG%
if errorlevel 1 (
    echo [ERREUR] echec de la creation du tag.
    pause
    exit /b 1
)

echo [ETAPE] git push origin %TAG% ...
git push origin %TAG%
if errorlevel 1 (
    echo.
    echo [ERREUR] echec du push du tag.
    echo Verifie ton authentification GitHub ^(token / SSH^).
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   Tag pousse avec succes !
echo ============================================================
echo.
echo Le rendu HD se declenche automatiquement sur GitHub Actions.
echo Suis l'avancement ici :
echo   https://github.com/ibif/video_cours/actions
echo.
echo A la fin, la video sera disponible dans :
echo   1ereC\Maths\Chapitre_Test.mp4
echo et publiee en Release :
echo   https://github.com/ibif/video_cours/releases/tag/%TAG%
echo.
pause
endlocal
