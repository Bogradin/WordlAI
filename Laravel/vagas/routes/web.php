<?php

use Illuminate\Support\Facades\Route;

Route::get('/', 'PrincipalController@principal')->name('index');

Route::get('/teste', 'TesteController@teste')->name('teste');