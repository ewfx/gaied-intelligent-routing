import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';  // ✅ Import CommonModule

@Component({
  selector: 'app-email-list',
  standalone: true,  // ✅ Ensure it's standalone
  imports: [CommonModule],  // ✅ Import CommonModule for *ngFor
  templateUrl: './email-list.component.html',
  styleUrls: ['./email-list.component.css']
})
export class EmailListComponent {
  @Input() emails: any[] = [];  // Ensure emails array exists
}
