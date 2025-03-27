import { Component } from '@angular/core';
import { EmailListComponent } from './components/email-list/email-list.component';
import { UploadFileComponent } from './components/upload-file/upload-file.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [EmailListComponent, UploadFileComponent], // 👈 Import the components here
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  classifiedEmails = [
    { subject: 'Hello', sender: 'user@example.com', content: 'Test email' }
  ];
}
