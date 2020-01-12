import { Component, OnInit } from '@angular/core';
import {ImageService} from './shared/image.service';
import {ActivatedRoute} from '@angular/router'
@Component({
  selector: 'app-image-detail',
  templateUrl: './image-detail.component.html',
  styleUrls: ['./image-detail.component.scss']
})
export class ImageDetailComponent implements OnInit {
  image:any;

  constructor(private ImageService: ImageService, private route:ActivatedRoute) { }

  ngOnInit() {
    this.image = this.ImageService.getImageById(
      +this.route.snapshot.params['id']
    )
  }

}
