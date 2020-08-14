import {Component, HostListener, OnInit} from '@angular/core';
import {FormGroup} from "@angular/forms";
import {SearchForm} from "./forms/search-form";
import {ResourceService} from "./service/resource.service";
import {Resource} from "./models/resource";
import {ResourceCategory} from "./models/resource_category";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{
  title: 'app-root';

}
