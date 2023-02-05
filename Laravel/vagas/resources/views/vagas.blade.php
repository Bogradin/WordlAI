<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="{{ URL::asset('css/vagas.css') }}" rel="stylesheet">
    <title>Vagas</title>
</head>
<body>
    <div class="container">
        <div class="center-div border">
            <div class="menu-header">
                <h3>Menu</h3>
            </div>
            <div class="content topBorder">
                @foreach ( $vagas as $indice => $vaga)
                    @if ($vaga['status'] == 'ON')
                        <div class="vaga border">
                            Nome da Vaga: {{ $vaga['nome'] }}
                            <br>
                            Breve Descrição: {{ $vaga['descrição'] }}
                            <br>
                            Data da Inscrição: {{ $vaga['data'] }}
                            <br>
                            Status: {{ $vaga['status'] }}
                            <br>
                        </div>
                    @endif
                @endforeach
            </div>
            <div class="paginate">
                <a href="/teste?page={{ $vagas->currentPage() - 1 }}">&lt;</a>
                <div style="width:20px;display:inline-block;"></div>
                <a href="/teste?page={{ $vagas->currentPage() + 1 }}">&gt;</a>
            </div>
        </div>
    </div>
</body>
</html>