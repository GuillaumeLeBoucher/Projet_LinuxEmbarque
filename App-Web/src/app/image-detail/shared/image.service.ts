import {Injectable} from '@angular/core'
import { Component, OnInit } from '@angular/core';
import * as data from "./data.json";


// Avec ce service on va récupérer les données des images qui sont situées dans le JSON data.json. Ce Json est dans le 
// même directory. On récupère en particulier le path des images ainsi que l'état de la caméra. On peut donc trouver les images
// et les afficher dans l'application. De meme pour l'état.
@Injectable()
export class ImageService{
    
    
    visibleImages =[];
    visibleEtat="";
    getImages(){
        return this.visibleImages = IMAGES.slice(0)
    }

    getImageById( id: number){
        return IMAGES.slice(0).find(image => image.id ==id)
    } 
    getEtat(){
        console.log(ETAT);
        return this.visibleEtat= ETAT
    }
} 
console.log(data);
// Fiare une pop up de demande de nom et de légende lors de la prise de photo
const IMAGES = data['PhotoPath'];
const ETAT = data['Etat']; // Etat est de type string
