import { Component, OnInit, Input } from '@angular/core';
import { Unit } from 'src/app/models/unit';
@Component({
  selector: 'app-unit-item',
  templateUrl: './unit-item.component.html',
  styleUrls: ['./unit-item.component.css'],
})
export class UnitItemComponent implements OnInit {
  @Input() unit: Unit;
  constructor() {}

  ngOnInit(): void {}
}
