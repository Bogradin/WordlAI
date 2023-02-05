<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Pagination\Paginator;
use Illuminate\Support\Collection;
use Illuminate\Pagination\LengthAwarePaginator;

class TesteController extends Controller
{
    function teste() {
        $vagasArray = [
            0 => [
                'nome' => 'Ally',
                'descrição' => 'Data Entry',
                'data' => '20/09',
                'status' => 'ON'
            ],
            1 => [
                'nome' => 'Hub',
                'descrição' => 'Programador',
                'data' => '12/08',
                'status' => 'ON'
            ],
            2 => [
                'nome' => 'Teste',
                'descrição' => 'Teste',
                'data' => 'Teste',
                'status' => 'ON'
            ],
            3 => [
                'nome' => 'Teste',
                'descrição' => 'Teste',
                'data' => 'Teste',
                'status' => 'ON'
            ],
            4 => [
                'nome' => 'Teste',
                'descrição' => 'Teste',
                'data' => 'Teste',
                'status' => 'ON'
            ],
            5 => [
                'nome' => 'Teste',
                'descrição' => 'Teste',
                'data' => 'Teste',
                'status' => 'ON'
            ],
            6 => [
                'nome' => 'Teste',
                'descrição' => 'Teste',
                'data' => 'Teste',
                'status' => 'ON'
            ],
            7 => [
                'nome' => 'Teste',
                'descrição' => 'Teste',
                'data' => 'Teste',
                'status' => 'ON'
            ],
            8 => [
                'nome' => 'Teste',
                'descrição' => 'Teste',
                'data' => 'Teste',
                'status' => 'ON'
            ],
            9 => [
                'nome' => 'Teste',
                'descrição' => 'Teste',
                'data' => 'Teste',
                'status' => 'ON'
            ]
        ];
        $vagas = $this->paginate($vagasArray);
        return view('vagas', ['vagas' => $vagas]);
    }

    public function paginate($items, $perPage = 6, $page = null, $options = [])
    {
        $page = $page ?: (Paginator::resolveCurrentPage() ?: 1);
        $items = $items instanceof Collection ? $items : Collection::make($items);
        return new LengthAwarePaginator($items->forPage($page, $perPage), $items->count(), $perPage, $page, $options);
    }
}
