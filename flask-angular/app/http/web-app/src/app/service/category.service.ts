import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import {DataService} from "./data.service";
import {Observable} from "rxjs";
import {ResourceCategory} from "../models/resource_category";


@Injectable({
  providedIn: 'root'
})
export class CategoryService{
  constructor(public http: HttpClient) {

  }

  getAllResourceCategories(): Observable<any>{
    const headers = new HttpHeaders().set('Content-Type', 'application-json')
    return this.http.get<ResourceCategory>('http://localhost:5000/api/categories/', {headers})
  }


}
