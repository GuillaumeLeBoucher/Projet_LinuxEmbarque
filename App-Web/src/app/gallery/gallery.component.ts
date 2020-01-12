import { Component, OnInit, OnChanges, Input } from '@angular/core';
import {ImageService} from '../image-detail/shared/image.service'

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss']
})
export class GalleryComponent implements OnInit {
  title ="Recent Photos";
  visibleImages: any[] = [];
  @Input() filterBy?: string = 'all'
  constructor(private imageService: ImageService) { 
    this.visibleImages = this.imageService.getImages();
  }

  ngOnChange(){
    this.visibleImages = this.imageService.getImages()
  }
  ngOnInit() {
  }
  TakePicFonction(){
    console.log("coucou")
  }
}
