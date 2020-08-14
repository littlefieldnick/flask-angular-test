import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { take, map } from 'rxjs/operators';

// @ts-ignore
import {DataService} from "./data.service";
import { Observable } from 'rxjs';
import {ResourceService} from "../service/resource.service";
@Injectable({
  providedIn: 'root'
})
export class ResourceResolver implements Resolve <Observable<any>>{

  constructor(private resourceDs: ResourceService) { }

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot){
    return this.resourceDs.getAllResources().pipe(
      take(1),
      map(data => data)
    )
  }
}
