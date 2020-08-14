import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpErrorResponse, HttpParams} from '@angular/common/http';
import {DataService} from "./data.service";
import {Observable} from "rxjs";
import {Resource} from "../models/resource";

@Injectable({
  providedIn: 'root'
})
export class ResourceService{
  constructor(public http: HttpClient) {

  }

  getAllResources(): Observable<any>{
    const headers = new HttpHeaders().set('Content-Type', 'application-json')
    return this.http.get<Resource>('http://localhost:5000/api/resources/', {headers})
  }

  searchResources(category:string, resourceName:string): Observable<any>{
    const header = new HttpHeaders().set('Content-Type', 'application-json')

    return this.http.get<Resource>('http://localhost:5000/api/resources/search/',
      {headers: header, params: {category: category, resource: resourceName}})
  }

}
