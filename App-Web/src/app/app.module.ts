import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { appRoutes} from '../routes'
import {NgbModule, NgbAlertModule} from '@ng-bootstrap/ng-bootstrap';
import { NavbarComponent } from './navbar/navbar.component';
import { GalleryComponent } from './gallery/gallery.component';
import { ImageDetailComponent } from './image-detail/image-detail.component';
import { ImageService } from './image-detail/shared/image.service';
import {ImageFilterPipe} from './image-detail/shared/filter.pipe'
import { RouterModule } from '@angular/router';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import {MatButtonModule} from '@angular/material'
import {MatTooltipModule} from '@angular/material'

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    GalleryComponent,
    ImageDetailComponent,
    ImageFilterPipe
  ],
  imports: [
    BrowserModule,
    NgbModule,
    NgbAlertModule,
    RouterModule.forRoot(appRoutes),
    NoopAnimationsModule,
    MatButtonModule,
    MatTooltipModule
  ],
  exports: [
    MatButtonModule,
    MatTooltipModule
  ],
  providers: [ImageService, ImageFilterPipe],
  bootstrap: [AppComponent]
})
export class AppModule { }
