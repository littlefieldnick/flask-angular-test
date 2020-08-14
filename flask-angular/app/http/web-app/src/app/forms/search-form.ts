import {FormControl, FormGroup, Validators} from '@angular/forms'

export class SearchFormControl extends FormControl{
  label: string
  modelProperty: string
  constructor(label: string, property: string, value:any, validator:any, disabled?: boolean) {
    super({value: value, disabled: disabled}, validator);
    this.label = label
    this.modelProperty = property
  }
}

export class SearchForm extends FormGroup{
  constructor() {
    super({
      name: new SearchFormControl('Name', 'name', '', [], false),
      category: new SearchFormControl('Category', 'category', '', [], false )
    })
  }

  get formControls(): SearchFormControl[] {
    return Object.keys(this.controls)
      .map(k => this.controls[k] as SearchFormControl);
  }
}
