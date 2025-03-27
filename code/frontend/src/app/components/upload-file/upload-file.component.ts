import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';  // ✅ Import CommonModule
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-upload-file',
  standalone: true,  // ✅ Ensure it's standalone
  imports: [CommonModule],  // ✅ Import CommonModule for *ngIf and | json
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.css']
})
export class UploadFileComponent {
  selectedFile: File | null = null;
  classificationResult: any = null;

  constructor(private apiService: ApiService) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  uploadFile() {
    if (!this.selectedFile) {
      alert('Please select a file first.');
      return;
    }
    this.apiService.uploadFile(this.selectedFile).subscribe(response => {
      this.classificationResult = response;
    }, error => {
      console.error('Error uploading file:', error);
    });
  }
}
