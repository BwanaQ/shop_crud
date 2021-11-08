import { Unit } from '../models/unit';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class UnitService {
  baseURL = 'http://localhost:8000/';
  apiLink = `${this.baseURL}api/v1/`;

  constructor(private http: HttpClient) {}
  getUnits(): Observable<Unit[]> {
    return this.http.get<Unit[]>(`${this.apiLink}units/available-units/`);
  }
}
