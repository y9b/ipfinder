import requests
import os
import json
import time

#IMPORTS

os.system('cls')
os.system('title ɪᴘ ꜰɪɴᴅᴇʀ :)')

#INICIO 


#CRIAR UM LOOP 
while True:
  print("""
                                          
     %%%%%%%%%%%%%%#########(((((//#(/.   
   ..&(((/((((((((((((((((((((#((((##(*   
    .&%%%%%%&%%%%%%&&%%%%%&/#%%%%%%&&&&   
     /(((######&&&####@@&&%%&&&&%%&&(*,   
      .......,,,%*,,,&&##&@&@&&&%%&@.     
               .&%&&&@@@*#&&&%%%%%%&@.    
                ,,...,,,..,%&&&&%%%%%&/   
                           ,%&%&&&%%&&&&  
                            ,%&&&&&&&%&&, 
                             ,&@&@@@&%#/. 
                              ((((////.   
                                 ...      
                                                                   
                                                   """)
  ip = input("[IP] > ")
  time.sleep(1)
  os.system('cls')
  print("finding . . .")
  time.sleep(2)

  #FAZER AQUELE TEMPINHO PRA DAR SUSPENSE MAS É INSTANTANEO O RESULTADO

  r = requests.get(f'http://ip-api.com/json/{ip}?fields=continent,region,regionName,city,timezone,isp,query')
  asteck = r.json()

  #API QUE USEI :)


  #AQUI ELE VERIFICA SE O IP REALMENTE FUNCIONA
  #VENDO SE "city" DENTRO DO JSON DA API EXISTE :)
  if "city" in asteck:
    os.system('cls')
    print("found!\n")
    #AQUI SÓ DEFINE AS VARIAVEIS PARA DEPOIS USAR NO RESULTADO
    regionName = asteck.get('regionName')
    timezone = asteck.get('timezone')
    city = asteck.get('city')
    query = asteck.get('query')
    continent = asteck.get('continent')
    isp = asteck.get('isp')
    region = asteck.get('region')
    print(f"IP : {query} \nCity: {city} - Region: {regionName} / {region} - Continent: {continent} \nISP: {isp} - Timezone: {timezone}")
    q = input("\nQuit? (y/n)")
    if q == "y":
      quit()
    else:
      os.system('cls')
      continue    
  else:
    os.system('cls')
    print("not found!")
    time.sleep(2)
    os.system('cls')
