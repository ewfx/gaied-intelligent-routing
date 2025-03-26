import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { UploadFileComponent } from './components/upload-file.component';
import { EmailListComponent } from './components/email-list.component';

@NgModule({
  declarations: [
    AppComponent,
    UploadFileComponent,
    EmailListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}