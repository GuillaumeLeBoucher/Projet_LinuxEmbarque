import {Injectable} from '@angular/core'
import { Component, OnInit } from '@angular/core';
import * as data from "./data.json";

@Injectable()
export class ImageService{
    
    
    visibleImages =[];
    getImages(){
        return this.visibleImages = IMAGES.slice(0)
    }

    getImageById( id: number){
        return IMAGES.slice(0).find(image => image.id ==id)
    } 
} 
console.log(data)
const IMAGES2 = data['PhotoPath']
console.log("imPath" , IMAGES2)
const IMAGES = [
    {"id": 1, "category": "boats", "caption": "View from a boat", "url": "assets/img/boat_01.jpg"},
    {"id": 2, "category": "boats", "caption": "This boat is beautifull", "url": "assets/img/boat_02.jpg"},
    {"id": 3, "category": "camping", "caption": "Camping view", "url": "assets/img/camping_01.jpg"},
    {"id": 4, "category": "library", "caption": "All my books are in this picture", "url": "assets/img/library_01.jpg"},
    {"id": 5, "category": "selfie", "caption": "Belle brochette de PD", "url": "assets/img/image.jpg"}

]