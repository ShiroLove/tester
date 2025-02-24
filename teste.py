#!/usr/bin/env bash

# TPUT :-:

BLACK=$(tput setaf 0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
BLUE=$(tput setaf 4)
MAGENTA=$(tput setaf 5)
CYAN=$(tput setaf 6)
WHITE=$(tput setaf 7)
BOLD=$(tput bold)
REDBG=$(tput setab 1)
SUBRI=$(tput smul)
RESET=$(tput sgr0)

#######################

banner()
{
        clear
        echo "${WHITE}
┌───────────────────────────────────────────────────────────────┐
│░█████╗░███╗░░░███╗██████╗░░█████╗░██╗███╗░░██╗███████╗██╗░░░░░│
│██╔══██╗████╗░████║██╔══██╗██╔══██╗██║████╗░██║██╔════╝██║░░░░░│
│██║░░╚═╝██╔████╔██║██████╔╝███████║██║██╔██╗██║█████╗░░██║░░░░░│
│██║░░██╗██║╚██╔╝██║██╔═══╝░██╔══██║██║██║╚████║██╔══╝░░██║░░░░░│
│╚█████╔╝██║░╚═╝░██║██║░░░░░██║░░██║██║██║░╚███║███████╗███████╗│
│░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚══════╝│
├───────────────────────────────────────────────────────────────┤
│                       ${BOLD}[ @Krannos - TKNMX ] ${RESET}${WHITE}                │
└───────────────────────────────────────────────────────────────┘${RESET}"
}

menu()
{
        banner
        echo -e "\n${MAGENTA}[${RESET}1${MAGENTA}]${RESET} - Seu ip"
        echo -e "\n${MAGENTA}[${RESET}2${MAGENTA}]${RESET} - Consulta IP."
        echo -e "\n${MAGENTA}[${RESET}3${MAGENTA}]${RESET} - Consulta CNPJ."
        echo -e "\n${MAGENTA}[${RESET}4${MAGENTA}]${RESET} - Consulta CEP."

        echo -e "\n${MAGENTA}[${RESET}5${MAGENTA}]${RESET} - Consulta PLACA."
        echo -e "\n${MAGENTA}[${RESET}6${MAGENTA}]${RESET} - Consulta BANCO."
        echo -e "\n${MAGENTA}[${RESET}7${MAGENTA}]${RESET} - Consulta NÚMERO."
        echo -e "\n${MAGENTA}[${RESET}8${MAGENTA}]${RESET} - Apks Premium."
        echo -e "\n${MAGENTA}[${RESET}99${MAGENTA}]${RESET} - Contact Me.\n"
        echo -ne "${WHITE}➜${RESET} ";
        read opcao
        case $opcao in
                1|01)
                        clear
                        SeuIp
                        ;;
                2|02)
                        clear
                        consulta_ip
                        ;;
                3|03)
                        clear
                        consulta_cnpj
                        ;;
                4|04)
                        clear
                        consulta_cep
                        ;;
                5|05)
                        clear
                        consulta_placa
                        ;;
                6|06)
                        clear
                        consulta_banco
                        ;;
                7|07)
                        clear
                        consulta_ddd
                        ;;
                8|08)
                        clear
                        apks_premium
                        ;;
                99)
                        clear
                        contact_me
                        ;;
                *)
                        echo -e "\n${RED}Opção Invalida.${RESET}"
                        exit 1
        esac
}

SeuIp()
{
        youip=`curl -s ifconfig.me`
        echo -e "\n${WHITE}SEU IP É ${SUBRI}$youip${RESET}\n"
}

consulta_ip()
{
        echo -e "${WHITE}┏━━━━[INFORME O IP]${RESET}"
        echo -e "${WHITE}┃${RESET}"
        echo -ne "${WHITE}┗━━➤ ${RESET}"${BOLD}
        read -r ip
        curl -s http://ipwhois.app/json/$ip | jq > .ip.json
        continent=`cat .ip.json | jq -r '.continent'`
        country=`cat .ip.json | jq -r '.country'`
        region=`cat .ip.json | jq -r '.region'`
        city=`cat .ip.json | jq -r '.city'`
        lat=`cat .ip.json | jq -r '.latitude'`
        lon=`cat .ip.json | jq -r '.longitude'`
        asn=`cat .ip.json | jq -r '.asn'`
        org=`cat .ip.json | jq -r '.org'`
        echo -e "${RESET}\nCONTINENTE: ${GREEN}$continent${RESET}"
        echo -e "\nPAÍS: ${GREEN}$country${RESET}"
        echo -e "\nREGIÃO: ${GREEN}$region${RESET}"
        echo -e "\nCIDADE: ${GREEN}$city${RESET}"
        echo -e "\nLATITUDE: ${GREEN}$lat${RESET}"
        echo -e "\nLONGITUDE: ${GREEN}$lon${RESET}"
        echo -e "\nASN: ${GREEN}$asn${RESET}"
        echo -e "\nORG: ${GREEN}$org${RESET}\n"

        if [[ -e .ip.json ]]; then
                rm .ip.json
        fi
}

consulta_cnpj()
{
        echo -e "${WHITE}┏━━━━[INFORME A CNPJ]${RESET}"
        echo -e "${WHITE}┃${RESET}"
        echo -ne "${WHITE}┗━━➤ ${RESET}"${BOLD}
        read -r cnpj
        curl -s https://www.receitaws.com.br/v1/cnpj/$cnpj | jq > .cnpj.json
        nome=`cat .cnpj.json | jq -r '.nome'`
        tipo=`cat .cnpj.json | jq -r '.tipo'`
        cep=`cat .cnpj.json | jq -r '.cep'`
        numero=`cat .cnpj.json | jq -r '.telefone'`
        cnpj=`cat .cnpj.json | jq -r '.cnpj'`
        email=`cat .cnpj.json | jq -r '.email'`
        status=`cat .cnpj.json | jq -r '.status'`
        porte=`cat .cnpj.json | jq -r '.porte'`
        situacao=`cat .cnpj.json | jq -r '.situacao'`
        municipio=`cat .cnpj.json | jq -r '.municipio'`
        bairro=`cat .cnpj.json | jq -r '.bairro'`
        logradouro=`cat .cnpj.json | jq -r '.logradouro'`
        numero=`cat .cnpj.json | jq -r '.numero'`
        echo -e "${RESET}\nCNPJ: ${GREEN}$cnpj${RESET}"
        echo -e "\nNOME: ${GREEN}$nome${RESET}"
        echo -e "\nTIPO: ${GREEN}$tipo${RESET}"
        echo -e "\nCEP: ${GREEN}$cep${RESET}"
        echo -e "\nTELEFONE: ${GREEN}$numero${RESET}"
        echo -e "\nEMAIL: ${GREEN}$email${RESET}"
        echo -e "\nSTATUS: ${GREEN}$status${RESET}"
        echo -e "\nPORTE: ${GREEN}$porte${RESET}"
        echo -e "\nSITUAÇÃO: ${GREEN}$situacao${RESET}"
        echo -e "\nMUNICIPIO: ${GREEN}$municipio${RESET}"
        echo -e "\nBAIRRO: ${GREEN}$bairro${RESET}"
        echo -e "\nLOGRADOURO: ${GREEN}$logradouro${RESET}"
        echo -e "\nNUMERO: ${GREEN}$numero${RESET}\n"

        if [[ -e .cnpj.json ]]; then
                rm .cnpj.json
        fi

}

consulta_cep()
{
        echo -e "${WHITE}┏━━━━[INFORME O CEP]${RESET}"
        echo -e "${WHITE}┃${RESET}"
        echo -ne "${WHITE}┗━━➤ ${RESET}"${BOLD}
        read -r cep_a
        cep=`echo "$cep_a" | tr -d '[:punct:]'`
        curl -s https://ws.apicep.com/cep.json?code=$cep | jq > .cep.json
        code=`cat .cep.json | jq -r '.code'`
        cidade=`cat .cep.json | jq -r '.city'`
        bairro_cep=`cat .cep.json | jq -r '.district'`
        endereco=`cat .cep.json | jq -r '.address'`
        echo -e "${RESET}\nCEP: ${GREEN}$code${RESET}"
        echo -e "\nCIDADE: ${GREEN}$cidade${RESET}"
        echo -e "\nBAIRRO: ${GREEN}$bairro_cep${RESET}"
        echo -e "\nENDEREÇO: ${GREEN}$endereco${RESET}\n"

        if [[ -e .cep.json ]]; then
                rm .cep.json
        fi
}

consulta_placa()
{
        echo -e "${WHITE}┏━━━━[INFORME A PLACA]${RESET}"
        echo -e "${WHITE}┃${RESET}"
        echo -ne "${WHITE}┗━━➤ ${RESET}"${BOLD}
        read -r placa_a
        placa=`echo "$placa_a" | tr -d '[:punct:]'`
        wget --no-check-certificate https://apicarros.com/v1/consulta/$placa/json -O .placa.json &> /dev/null
        ano=`cat .placa.json | jq -r '.ano'`
        modelo=`cat .placa.json | jq -r '.modelo'`
        cor=`cat .placa.json | jq -r '.cor'`
        chassi=`cat .placa.json | jq -r '.chassi'`
        municipio=`cat .placa.json | jq -r '.municipio'`
        echo -e "${RESET}\nPLACA: ${GREEN}$placa${RESET}"
        echo -e "\nANO: ${GREEN}$ano${RESET}"
        echo -e "\nMODELO: ${GREEN}$modelo${RESET}"
        echo -e "\nCOR: ${GREEN}$cor${RESET}"
        echo -e "\nCHASSI: ${GREEN}$chassi${RESET}"
        echo -e "\nMUNICIPIO: ${GREEN}$municipio${RESET}\n"

        if [[ -e .placa.json ]]; then
                rm .placa.json
        fi
}

consulta_banco()
{
        echo -e "${WHITE}┏━━━━[INFORME O CODIGO BANCARIO]${RESET}"
        echo -e "${WHITE}┃${RESET}"
        echo -ne "${WHITE}┗━━➤ ${RESET}"${BOLD}
        read -r banco_a
        banco=`echo "$banco_a" | tr -d '[:punct:]'`
        curl -s https://brasilapi.com.br/api/banks/v1/$banco | jq > .banco.json
        code=`cat .banco.json | jq -r '.code'`
        ispb=`cat .banco.json | jq -r '.ispb'`
        fullname=`cat .banco.json | jq -r '.fullName'`
        echo -e "${RESET}\nCÓDIGO: ${GREEN}$code${RESET}"
        echo -e "\nNOME: ${GREEN}$fullname${RESET}"
        echo -e "\nISPB: ${GREEN}$ispb${RESET}\n"

        if [[ -e .banco.json ]]; then
                rm .banco.json
        fi
}

consulta_ddd()
{
        echo -e "${WHITE}┏━━━━[INFORME O DDD]${RESET}"
        echo -e "${WHITE}┃${RESET}"
        echo -ne "${WHITE}┗━━➤ ${RESET}"${BOLD}
        read -r ddd
        curl -s https://brasilapi.com.br/api/ddd/v1/$ddd | jq > .ddd.json
        estado=`cat .ddd.json | jq -r '.state'`
        cidades=`cat .ddd.json | jq -r '.cities' | tr -d '",[]'`
        echo -e "${RESET}\nESTADO: ${GREEN}$estado${RESET}"
        echo -e "\nCIDADES: ${GREEN}$cidades${RESET}"

        if [[ -e .ddd.json ]]; then
                rm .ddd.json
        fi
}

apks_premium()
{
        clear 
        echo -e "\n${WHITE}1 - Spotify Premium.${RESET}\n"
        echo -e "${WHITE}Link:${RESET} ${BOLD}${SUBRI}https://www.mediafire.com/file/fv9f62ecff97f5i/Spotify_8.5.74.834.apk/file${RESET}"
        echo -e "\n${WHITE}2 - KineMaster Premium.${RESET}\n"
        echo -e "${WHITE}Link:${RESET} ${BOLD}${SUBRI}https://www.mediafire.com/file/kn4gtxibwaj3ct7/KineMaster_v4.15.5.17370.apk/file${RESET}"
        echo -e "\n${WHITE}3 - Youtube Music e Youtube (Sem Anúncios).${RESET}\n"
        echo -e "${WHITE}Link:${RESET} ${BOLD}${SUBRI}https://github.com/YTVanced/VancedManager/releases/latest/download/manager.apk${RESET}"
        echo -e "\n${WHITE}4 - CapCut Premium.${RESET}\n"
        echo -e "${WHITE}Link:${RESET} ${BOLD}${SUBRI}https://www.mediafire.com/file/v958n3acx372hs1/CapCut_v2.9.1.apk/file${RESET}"
        echo -e "\n${WHITE}5 - PicsArt Premium.${RESET}\n"
        echo -e "${WHITE}Link:${RESET} ${BOLD}${SUBRI}https://www.mediafire.com/file/qsnln0cuub4aylz/PicsArt_v17.2.4_GOLD_Android_11.apk/file${RESET}"
}
menu