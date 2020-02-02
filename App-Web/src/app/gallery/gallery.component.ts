import { Component, OnInit, OnChanges, Input } from '@angular/core';
import {ImageService} from '../image-detail/shared/image.service';
import { BrowserModule }    from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import openSocket from 'socket.io-client';


declare var require: any;
@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss']
})
export class GalleryComponent implements OnInit {
  title ="Photos took by the PI camera";
  visibleImages: any[] = [];
  visibleEtat:any ="";
  @Input() filterBy?: string = 'all'
  constructor(private imageService: ImageService) { 
    this.visibleImages = this.imageService.getImages();
    this.visibleEtat = this.imageService.getEtat();
  }

  ngOnChange(){
    this.visibleImages = this.imageService.getImages();
    this.visibleEtat = this.imageService.getEtat();
  }
  ngOnInit() {
  }

 
  
  test(){
    console.log("coucou")
  }
}