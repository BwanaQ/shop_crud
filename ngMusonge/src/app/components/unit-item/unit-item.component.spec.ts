import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UnitItemComponent } from './unit-item.component';

describe('UnitItemComponent', () => {
  let component: UnitItemComponent;
  let fixture: ComponentFixture<UnitItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UnitItemComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UnitItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
