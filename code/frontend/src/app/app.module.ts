import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { EmailListComponent } from './components/email-list/email-list.component';
import { UploadFileComponent } from './components/upload-file/upload-file.component';
import { ApiService } from './services/api.service';

@NgModule({
  declarations: [
    AppComponent,
    UploadFileComponent,
    EmailListComponent
  ],
  imports: [
    BrowserModule,  // ✅ Includes CommonModule by default
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [ApiService], 
  bootstrap: [AppComponent]
})
export class AppModule {}
