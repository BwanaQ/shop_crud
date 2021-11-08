import { Component, OnInit } from '@angular/core';
import { UnitService } from 'src/app/_services/unit.service';
import { Unit } from 'src/app/models/unit';

@Component({
  selector: 'app-unit-list',
  templateUrl: './unit-list.component.html',
  styleUrls: ['./unit-list.component.css'],
})
export class UnitListComponent implements OnInit {
  units: Unit[];
  constructor(private uService: UnitService) {}

  ngOnInit(): void {
    this.getUnits();
  }

  getUnits(): any {
    this.uService.getUnits().subscribe((units) => {
      this.units = units;
      console.log('units: ' + JSON.stringify(this.units));
    });
  }
}
