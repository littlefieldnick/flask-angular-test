import {Component, HostListener, OnInit} from '@angular/core';
import {SearchForm} from "../forms/search-form";
import {Resource} from "../models/resource";
import {ResourceCategory} from "../models/resource_category";
import {ActivatedRoute} from "@angular/router";
import {ResourceService} from "../service/resource.service";

@Component({
  selector: 'map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  title = 'Place Matters Maine';
  mapOpen = false;
  searchForm: SearchForm
  resources: Array<Resource>
  categories: Array<ResourceCategory>

  zoom=15;
  constructor(private route: ActivatedRoute, private resourceService: ResourceService) {
    this.searchForm = new SearchForm()
  }

  ngOnInit(): void {
    this.categories = this.route.snapshot.data.categories;
    this.resources = this.route.snapshot.data.resources;
  }

  //Load hidden map (when screen size is smaller than md device)
  toggleMap(){
    this.mapOpen = !this.mapOpen
  }

  search(){
    let category = this.searchForm.get("category").value;
    let resourceName = this.searchForm.get("name").value;
    if(category.length == 0){
      category = ''
    }

    if(resourceName.length == null){
      resourceName = ''
    }
    this.resourceService.searchResources(category, resourceName).subscribe((data: Resource[]) =>{
      this.resources = data;
    })

  }

  resetSearchForm(){
    this.searchForm.reset()

    this.resourceService.getAllResources().subscribe((data: Resource[]) =>{
      this.resources = data;
    })
  }

  @HostListener('window:resize', ['$event'])
  onResize(event) {
    console.log("Resize event fired!")
    if (this.mapOpen){
      this.mapOpen = false;
    }
  }
}
