#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:47:01 2019

@author: Steven
Automatización de tweets con python 
"""

def create_tweet(tweet_text, myData = False):
    """
    Parameters
    ----------
    tweet_text : string
        Texto a colocar en un tweet
    myData: bool
        Bandera para imprimir o no los datos de la cuenta
    Returns
    -------
    None.

    """
    #Importamos las librerias
    import pandas
    import tweepy

    #Leemos un CSV con las Keys para evitar tenerlas en el codigo
    df = pandas.read_csv('Keys.csv')
    CK = df['Key'][0]
    AT = df['Key'][1]
    CS = df['Secret'][0]
    ATS = df['Secret'][1]
    
    # Autenticacion con Twitter
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)
    
    # Create API object
    api = tweepy.API(auth)
    
    #Verificamos que nos pudimos autenticar
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
     
    #Resumen de la informacion de la cuenta
    user = api.me()
    if(myData):
        print('Name: ' + user.name)
        print('Location: ' + user.location)
        print('Friends: ' + str(user.friends_count))
        print('Followers: ' + str(user.followers_count))

    # Creando un tweet
    api.update_status(tweet_text)

def create_tweet_media(filenames,tweet_text, myData = False):
    """

    Parameters
    ----------
    filenames : media
        Lista con Imagen, gift o video a publicar.
        Ejemplo =>  ['1.png', '2.png', ...]
    myData: boole
        Bandera para imprimir o no los datos de la cuenta
    tweet_text : string
        Texto a colocar en tweet

    Returns
    -------
    None.

    """
    #Importamos las librerias
    import pandas
    import tweepy

    #Leemos un CSV con las Keys para evitar tenerlas en el codigo
    df = pandas.read_csv('Data/Keys.csv')
    CK = df['Key'][0]
    AT = df['Key'][1]
    CS = df['Secret'][0]
    ATS = df['Secret'][1]
    
    # Autenticacion con Twitter
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)
    
    # Create API object
    api = tweepy.API(auth)
    
    #Verificamos que nos pudimos autenticar
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
     
    #Resumen de la informacion de la cuenta
    user = api.me()
    if(myData):
        print('Name: ' + user.name)
        print('Location: ' + user.location)
        print('Friends: ' + str(user.friends_count))
        print('Followers: ' + str(user.followers_count))
  
    # Upload images and get media_ids
    media_ids = []
    for filename in filenames:
        res = api.media_upload(filename)
        media_ids.append(res.media_id)
     
    #Creando tweet con media_ids
    api.update_status(media_ids=media_ids, status=tweet_text)

