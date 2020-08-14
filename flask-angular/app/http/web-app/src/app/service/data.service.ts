import {Observable} from "rxjs";

export abstract class DataService {
  abstract getData(): Observable<any[]>
}
