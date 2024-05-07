import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatIconModule } from '@angular/material/icon';

import { AppRoutingModule } from './app/app-routing.module';
import { MatInputModule } from '@angular/material/input';
import { AuthService } from './app/services/auth.service';
import { AppComponent } from './app/app.component';
import { LoginComponent } from './app/components/auth/login/login.component';
// import { ProductListComponent } from './components/products/product-list/product-list.component';
// import { ProductDetailComponent } from './components/products/product-detail/product-detail.component';
// import { ProductEditComponent } from './components/products/product-edit/product-edit.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    // ProductListComponent,
    // ProductDetailComponent,
    // ProductEditComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    MatInputModule,
    BrowserAnimationsModule,
    MatIconModule,
  ],
  providers: [AuthService],
  bootstrap: [AppComponent],
})
export class AppModule {}
