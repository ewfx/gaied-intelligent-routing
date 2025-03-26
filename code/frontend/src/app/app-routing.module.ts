import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UploadFileComponent } from './components/upload-file.component';
import { EmailListComponent } from './components/email-list.component';

const routes: Routes = [
  { path: '', component: UploadFileComponent },
  { path: 'results', component: EmailListComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}