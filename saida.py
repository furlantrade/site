<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SpaceX-Token - A memecoin que te leva à lua e além!</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        spacex: {
                            dark: '#0B0E17',
                            blue: '#005288',
                            light: '#D4F1F9',
                            accent: '#FFD700',
                        }
                    },
                    fontFamily: {
                        orbitron: ['Orbitron', 'sans-serif'],
                        space: ['"Space Grotesk"', 'sans-serif'],
                    },
                    animation: {
                        'float': 'float 6s ease-in-out infinite',
                        'pulse-slow': 'pulse 5s ease-in-out infinite',
                    }
                }
            }
        }
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Space+Grotesk:wght@300;400;600;700&display=swap');
        
        body {
            font-family: 'Space Grotesk', sans-serif;
            background-color: #0B0E17;
            color: white;
            overflow-x: hidden;
        }
        
        .hero-bg {
            background: radial-gradient(circle at center, #00528820, #0B0E17 70%);
        }
        
        .space-bg {
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><circle cx="10" cy="10" r="1" fill="white" opacity="0.8"/><circle cx="30" cy="25" r="0.8" fill="white" opacity="0.6"/><circle cx="70" cy="15" r="0.6" fill="white" opacity="0.7"/><circle cx="85" cy="40" r="0.7" fill="white" opacity="0.5"/><circle cx="20" cy="60" r="0.5" fill="white" opacity="0.9"/><circle cx="50" cy="70" r="0.4" fill="white" opacity="0.6"/><circle cx="75" cy="85" r="0.9" fill="white" opacity="0.5"/><circle cx="90" cy="65" r="0.3" fill="white" opacity="0.7"/></svg>');
            background-size: 200px;
        }
        
        .rocket-trail {
            position: relative;
        }
        
        .rocket-trail::after {
            content: '';
            position: absolute;
            bottom: -20px;
            left: 50%;
            transform: translateX(-50%);
            width: 4px;
            height: 80px;
            background: linear-gradient(to top, #005288, transparent);
            border-radius: 50%;
            filter: blur(2px);
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        
        .token-card {
            background: linear-gradient(145deg, #0B0E17, #00528830);
            border: 1px solid #00528880;
            box-shadow: 0 10px 30px #00528820;
            transition: all 0.3s ease;
        }
        
        .token-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px #00528840;
        }
        
        .btn-spacex {
            background: linear-gradient(45deg, #005288, #003366);
            border: 1px solid #D4F1F950;
            transition: all 0.3s ease;
        }
        
        .btn-spacex:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px #00528880;
        }
        
        .btn-accent {
            background: linear-gradient(45deg, #FFD700, #FFA500);
            color: #0B0E17;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .btn-accent:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px #FFD70080;
        }
        
        .roadmap-item::before {
            content: '';
            position: absolute;
            left: -30px;
            top: 0;
            height: 100%;
            width: 2px;
            background: linear-gradient(to bottom, #005288, #D4F1F9, #005288);
        }
        
        .roadmap-item:last-child::before {
            height: 50%;
        }
    </style>
</head>
<body class="space-bg">
    <!-- Navigation -->
    <nav class="bg-spacex-dark/90 backdrop-blur-md border-b border-spacex-blue/30 fixed w-full z-50">
        <div class="container mx-auto px-6 py-4">
            <div class="flex justify-between items-center">
                <div class="flex items-center space-x-2">
                    <div class="rocket-trail">
                        <i class="fas fa-rocket text-spacex-accent text-2xl animate-float"></i>
                    </div>
                    <span class="font-orbitron text-xl font-bold bg-gradient-to-r from-spacex-light to-spacex-accent bg-clip-text text-transparent">SPACEX-TOKEN</span>
                </div>
                <div class="hidden md:flex space-x-8">
                    <a href="#about" class="text-spacex-light hover:text-spacex-accent transition">Sobre</a>
                    <a href="#tokenomics" class="text-spacex-light hover:text-spacex-accent transition">Tokenomics</a>
                    <a href="#roadmap" class="text-spacex-light hover:text-spacex-accent transition">Roadmap</a>
                    <a href="#whitepaper" class="text-spacex-light hover:text-spacex-accent transition">Whitepaper</a>
                </div>
                <div class="flex items-center space-x-4">
                    <button class="btn-spacex px-4 py-2 rounded-full text-sm font-bold flex items-center space-x-2">
                        <i class="fas fa-wallet"></i>
                        <span>Conectar Carteira</span>
                    </button>
                    <button class="md:hidden text-spacex-light">
                        <i class="fas fa-bars text-xl"></i>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-bg min-h-screen flex items-center pt-20">
        <div class="container mx-auto px-6 py-20">
            <div class="flex flex-col md:flex-row items-center">
                <div class="md:w-1/2 mb-12 md:mb-0">
                    <h1 class="font-orbitron text-4xl md:text-6xl font-bold mb-6">
                        <span class="bg-gradient-to-r from-spacex-accent to-spacex-light bg-clip-text text-transparent">SPACEX-TOKEN</span>
                    </h1>
                    <h2 class="text-xl md:text-2xl text-spacex-light mb-8">
                        A memecoin que te leva direto à lua <span class="text-spacex-accent font-bold">— e além!</span>
                    </h2>
                    <p class="text-spacex-light/80 mb-8 max-w-lg">
                        Inspirada na inovação espacial e no espírito ousado de exploração. 
                        Uma memecoin com utilidade real que promove a adoção divertida de criptoativos.
                    </p>
                    <div class="flex flex-wrap gap-4">
                        <button class="btn-accent px-6 py-3 rounded-full font-bold flex items-center space-x-2">
                            <i class="fas fa-shopping-cart"></i>
                            <span>Comprar na Jupiter DEX</span>
                        </button>
                        <button class="btn-spacex px-6 py-3 rounded-full font-bold flex items-center space-x-2">
                            <i class="fas fa-plus"></i>
                            <span>Adicionar à carteira Phantom</span>
                        </button>
                    </div>
                </div>
                <div class="md:w-1/2 flex justify-center">
                    <div class="relative">
                        <img src="xspace.png" alt="SpaceX-Token" class="w-64 h-64 md:w-80 md:h-80 animate-float">
                        <div class="absolute -bottom-10 -left-10 w-32 h-32 bg-spacex-blue/20 rounded-full filter blur-xl"></div>
                        <div class="absolute -top-10 -right-10 w-40 h-40 bg-spacex-accent/10 rounded-full filter blur-xl"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-20 bg-gradient-to-b from-spacex-dark to-spacex-blue/10">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="font-orbitron text-3xl md:text-4xl font-bold mb-4">
                    <span class="bg-gradient-to-r from-spacex-light to-spacex-accent bg-clip-text text-transparent">Sobre o SpaceX-Token</span>
                </h2>
                <div class="w-24 h-1 bg-gradient-to-r from-spacex-blue to-spacex-accent mx-auto"></div>
            </div>
            
            <div class="flex flex-col md:flex-row gap-8">
                <div class="md:w-1/2">
                    <div class="token-card p-8 rounded-2xl mb-8">
                        <h3 class="font-orbitron text-xl text-spacex-accent mb-4">🚀 Visão Espacial</h3>
                        <p class="text-spacex-light/80 mb-4">
                            O SpaceX-Token é uma criptomoeda inspirada na inovação espacial e no espírito ousado de exploração. 
                            Criado como uma memecoin com utilidade real, o SPX Token promove a adoção divertida de criptoativos 
                            com foco em comunidade, parcerias e impacto cultural.
                        </p>
                        <p class="text-spacex-light/80">
                            Nosso objetivo é combinar o melhor dos dois mundos: o engajamento viral das memecoins com a 
                            utilidade prática de projetos blockchain sérios.
                        </p>
                    </div>
                    
                    <div class="grid grid-cols-2 gap-4">
                        <div class="token-card p-6 rounded-xl">
                            <div class="text-spacex-accent text-2xl mb-2">
                                <i class="fas fa-coins"></i>
                            </div>
                            <h4 class="font-bold mb-2">Suprimento Total</h4>
                            <p class="text-spacex-light/80 text-sm">1 bilhão de tokens</p>
                        </div>
                        <div class="token-card p-6 rounded-xl">
                            <div class="text-spacex-accent text-2xl mb-2">
                                <i class="fas fa-network-wired"></i>
                            </div>
                            <h4 class="font-bold mb-2">Rede</h4>
                            <p class="text-spacex-light/80 text-sm">Solana</p>
                        </div>
                        <div class="token-card p-6 rounded-xl">
                            <div class="text-spacex-accent text-2xl mb-2">
                                <i class="fas fa-bolt"></i>
                            </div>
                            <h4 class="font-bold mb-2">Taxas</h4>
                            <p class="text-spacex-light/80 text-sm">Zero taxas de compra</p>
                        </div>
                        <div class="token-card p-6 rounded-xl">
                            <div class="text-spacex-accent text-2xl mb-2">
                                <i class="fas fa-cogs"></i>
                            </div>
                            <h4 class="font-bold mb-2">Utilidade</h4>
                            <p class="text-spacex-light/80 text-sm">Pagamentos, NFTs, Staking</p>
                        </div>
                    </div>
                </div>
                
                <div class="md:w-1/2">
                    <div class="token-card p-8 rounded-2xl h-full">
                        <h3 class="font-orbitron text-xl text-spacex-accent mb-4">🪐 Utilidade do Token</h3>
                        <div class="space-y-6">
                            <div class="flex items-start">
                                <div class="text-spacex-accent mr-4 mt-1">
                                    <i class="fas fa-ticket-alt"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold mb-1">Pagamentos em Eventos</h4>
                                    <p class="text-spacex-light/80 text-sm">
                                        Use SPX para comprar ingressos, merch e experiências exclusivas em eventos espaciais e de cripto.
                                    </p>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <div class="text-spacex-accent mr-4 mt-1">
                                    <i class="fas fa-image"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold mb-1">Colecionáveis NFT</h4>
                                    <p class="text-spacex-light/80 text-sm">
                                        Colecione NFTs exclusivos da SpaceX-Token com diferentes níveis de raridade e benefícios.
                                    </p>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <div class="text-spacex-accent mr-4 mt-1">
                                    <i class="fas fa-lock"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold mb-1">Staking Rewards</h4>
                                    <p class="text-spacex-light/80 text-sm">
                                        Bloqueie seus tokens e ganhe recompensas passivas enquanto apoia a rede.
                                    </p>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <div class="text-spacex-accent mr-4 mt-1">
                                    <i class="fas fa-users"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold mb-1">Comunidades Exclusivas</h4>
                                    <p class="text-spacex-light/80 text-sm">
                                        Acesse grupos VIP, AMAs com especialistas e conteúdos premium com base em seu saldo de SPX.
                                    </p>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <div class="text-spacex-accent mr-4 mt-1">
                                    <i class="fas fa-gamepad"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold mb-1">Jogos e Metaverso</h4>
                                    <p class="text-spacex-light/80 text-sm">
                                        Use SPX em nosso futuro ecossistema de jogos espaciais e experiências no metaverso.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Tokenomics Section -->
    <section id="tokenomics" class="py-20 bg-spacex-dark">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="font-orbitron text-3xl md:text-4xl font-bold mb-4">
                    <span class="bg-gradient-to-r from-spacex-light to-spacex-accent bg-clip-text text-transparent">Tokenomics</span>
                </h2>
                <div class="w-24 h-1 bg-gradient-to-r from-spacex-blue to-spacex-accent mx-auto"></div>
            </div>
            
            <div class="flex flex-col lg:flex-row gap-12 items-center">
                <div class="lg:w-1/2">
                    <div class="token-card p-8 rounded-2xl">
                        <h3 class="font-orbitron text-xl text-spacex-accent mb-6">Distribuição de Tokens</h3>
                        
                        <div class="mb-8">
                            <div class="flex justify-between mb-2">
                                <span class="text-spacex-light">Liquidez</span>
                                <span class="text-spacex-accent font-bold">40%</span>
                            </div>
                            <div class="w-full bg-spacex-blue/20 rounded-full h-2.5">
                                <div class="bg-spacex-accent h-2.5 rounded-full" style="width: 40%"></div>
                            </div>
                        </div>
                        
                        <div class="mb-8">
                            <div class="flex justify-between mb-2">
                                <span class="text-spacex-light">Comunidade & Marketing</span>
                                <span class="text-spacex-accent font-bold">25%</span>
                            </div>
                            <div class="w-full bg-spacex-blue/20 rounded-full h-2.5">
                                <div class="bg-spacex-light h-2.5 rounded-full" style="width: 25%"></div>
                            </div>
                        </div>
                        
                        <div class="mb-8">
                            <div class="flex justify-between mb-2">
                                <span class="text-spacex-light">Desenvolvimento</span>
                                <span class="text-spacex-accent font-bold">20%</span>
                            </div>
                            <div class="w-full bg-spacex-blue/20 rounded-full h-2.5">
                                <div class="bg-spacex-blue h-2.5 rounded-full" style="width: 20%"></div>
                            </div>
                        </div>
                        
                        <div class="mb-8">
                            <div class="flex justify-between mb-2">
                                <span class="text-spacex-light">Equipe</span>
                                <span class="text-spacex-accent font-bold">10%</span>
                            </div>
                            <div class="w-full bg-spacex-blue/20 rounded-full h-2.5">
                                <div class="bg-gradient-to-r from-spacex-blue to-spacex-accent h-2.5 rounded-full" style="width: 10%"></div>
                            </div>
                        </div>
                        
                        <div>
                            <div class="flex justify-between mb-2">
                                <span class="text-spacex-light">Parcerias</span>
                                <span class="text-spacex-accent font-bold">5%</span>
                            </div>
                            <div class="w-full bg-spacex-blue/20 rounded-full h-2.5">
                                <div class="bg-gradient-to-r from-spacex-accent to-spacex-light h-2.5 rounded-full" style="width: 5%"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="lg:w-1/2">
                    <div class="token-card p-8 rounded-2xl">
                        <h3 class="font-orbitron text-xl text-spacex-accent mb-6">Detalhes Técnicos</h3>
                        
                        <div class="space-y-6">
                            <div class="flex justify-between items-center">
                                <div class="flex items-center">
                                    <div class="text-spacex-accent mr-4">
                                        <i class="fas fa-tag"></i>
                                    </div>
                                    <span class="font-bold">Nome do Token</span>
                                </div>
                                <span class="text-spacex-light/80">SpaceX-Token</span>
                            </div>
                            
                            <div class="flex justify-between items-center">
                                <div class="flex items-center">
                                    <div class="text-spacex-accent mr-4">
                                        <i class="fas fa-code"></i>
                                    </div>
                                    <span class="font-bold">Símbolo</span>
                                </div>
                                <span class="text-spacex-light/80">SPX</span>
                            </div>
                            
                            <div class="flex justify-between items-center">
                                <div class="flex items-center">
                                    <div class="text-spacex-accent mr-4">
                                        <i class="fas fa-project-diagram"></i>
                                    </div>
                                    <span class="font-bold">Rede Blockchain</span>
                                </div>
                                <span class="text-spacex-light/80">Solana (SPL Token)</span>
                            </div>
                            
                            <div class="flex justify-between items-center">
                                <div class="flex items-center">
                                    <div class="text-spacex-accent mr-4">
                                        <i class="fas fa-coins"></i>
                                    </div>
                                    <span class="font-bold">Suprimento Total</span>
                                </div>
                                <span class="text-spacex-light/80">1,000,000,000 SPX</span>
                            </div>
                            
                            <div class="flex justify-between items-center">
                                <div class="flex items-center">
                                    <div class="text-spacex-accent mr-4">
                                        <i class="fas fa-burn"></i>
                                    </div>
                                    <span class="font-bold">Mecanismo de Queima</span>
                                </div>
                                <span class="text-spacex-light/80">Queimadas periódicas</span>
                            </div>
                            
                            <div class="flex justify-between items-center">
                                <div class="flex items-center">
                                    <div class="text-spacex-accent mr-4">
                                        <i class="fas fa-percentage"></i>
                                    </div>
                                    <span class="font-bold">Taxas de Transação</span>
                                </div>
                                <span class="text-spacex-light/80">0% (apenas taxas da rede Solana)</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Roadmap Section -->
    <section id="roadmap" class="py-20 bg-gradient-to-b from-spacex-dark to-spacex-blue/10">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="font-orbitron text-3xl md:text-4xl font-bold mb-4">
                    <span class="bg-gradient-to-r from-spacex-light to-spacex-accent bg-clip-text text-transparent">Roadmap Galáctico</span>
                </h2>
                <div class="w-24 h-1 bg-gradient-to-r from-spacex-blue to-spacex-accent mx-auto"></div>
            </div>
            
            <div class="relative max-w-3xl mx-auto">
                <!-- Vertical line -->
                <div class="absolute left-1/2 h-full w-0.5 bg-gradient-to-b from-spacex-blue via-spacex-accent to-spacex-blue transform -translate-x-1/2"></div>
                
                <!-- Roadmap items -->
                <div class="space-y-12">
                    <!-- Phase 1 -->
                    <div class="relative flex items-center">
                        <div class="absolute left-1/2 -ml-4 w-8 h-8 rounded-full bg-spacex-accent border-4 border-spacex-dark flex items-center justify-center transform -translate-x-1/2">
                            <span class="font-orbitron text-spacex-dark font-bold">1</span>
                        </div>
                        <div class="ml-auto w-5/12 px-6 py-4 bg-spacex-blue/20 backdrop-blur-sm rounded-xl border border-spacex-blue/30">
                            <h3 class="font-orbitron text-spacex-accent mb-2">Fase 1: Decolagem</h3>
                            <ul class="text-spacex-light/80 text-sm space-y-2 list-disc pl-5">
                                <li>Lançamento do token na Solana</li>
                                <li>Listagem em DEXs (Jupiter, Raydium)</li>
                                <li>Site oficial e redes sociais</li>
                                <li>Primeira campanha de marketing</li>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- Phase 2 -->
                    <div class="relative flex items-center">
                        <div class="absolute left-1/2 -ml-4 w-8 h-8 rounded-full bg-spacex-accent border-4 border-spacex-dark flex items-center justify-center transform -translate-x-1/2">
                            <span class="font-orbitron text-spacex-dark font-bold">2</span>
                        </div>
                        <div class="mr-auto w-5/12 px-6 py-4 bg-spacex-blue/20 backdrop-blur-sm rounded-xl border border-spacex-blue/30">
                            <h3 class="font-orbitron text-spacex-accent mb-2">Fase 2: Órbita Estável</h3>
                            <ul class="text-spacex-light/80 text-sm space-y-2 list-disc pl-5">
                                <li>Parcerias estratégicas anunciadas</li>
                                <li>Programa de staking lançado</li>
                                <li>Primeira coleção de NFTs</li>
                                <li>Listagem em CEXs menores</li>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- Phase 3 -->
                    <div class="relative flex items-center">
                        <div class="absolute left-1/2 -ml-4 w-8 h-8 rounded-full bg-spacex-accent border-4 border-spacex-dark flex items-center justify-center transform -translate-x-1/2">
                            <span class="font-orbitron text-spacex-dark font-bold">3</span>
                        </div>
                        <div class="ml-auto w-5/12 px-6 py-4 bg-spacex-blue/20 backdrop-blur-sm rounded-xl border border-spacex-blue/30">
                            <h3 class="font-orbitron text-spacex-accent mb-2">Fase 3: Rumo à Lua</h3>
                            <ul class="text-spacex-light/80 text-sm space-y-2 list-disc pl-5">
                                <li>Listagem em grandes CEXs</li>
                                <li>Utilidade em eventos reais</li>
                                <li>Plataforma de jogos beta</li>
                                <li>Comunidade atinge 50k membros</li>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- Phase 4 -->
                    <div class="relative flex items-center">
                        <div class="absolute left-1/2 -ml-4 w-8 h-8 rounded-full bg-spacex-accent border-4 border-spacex-dark flex items-center justify-center transform -translate-x-1/2">
                            <span class="font-orbitron text-spacex-dark font-bold">4</span>
                        </div>
                        <div class="mr-auto w-5/12 px-6 py-4 bg-spacex-blue/20 backdrop-blur-sm rounded-xl border border-spacex-blue/30">
                            <h3 class="font-orbitron text-spacex-accent mb-2">Fase 4: Além da Lua</h3>
                            <ul class="text-spacex-light/80 text-sm space-y-2 list-disc pl-5">
                                <li>Ecossistema de metaverso</li>
                                <li>Integração com projetos espaciais</li>
                                <li>Governança descentralizada</li>
                                <li>Expansão para outras blockchains</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Whitepaper Section -->
    <section id="whitepaper" class="py-20 bg-spacex-dark">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="font-orbitron text-3xl md:text-4xl font-bold mb-4">
                    <span class="bg-gradient-to-r from-spacex-light to-spacex-accent bg-clip-text text-transparent">Whitepaper</span>
                </h2>
                <div class="w-24 h-1 bg-gradient-to-r from-spacex-blue to-spacex-accent mx-auto"></div>
            </div>
            
            <div class="max-w-4xl mx-auto">
                <div class="token-card p-8 md:p-12 rounded-2xl">
                    <div class="flex flex-col md:flex-row gap-8 items-center">
                        <div class="md:w-1/3 flex justify-center">
                            <div class="relative">
                                <div class="w-48 h-64 bg-gradient-to-br from-spacex-blue to-spacex-accent rounded-lg shadow-xl flex items-center justify-center">
                                    <i class="fas fa-file-alt text-6xl text-spacex-dark"></i>
                                </div>
                                <div class="absolute -bottom-4 -right-4 w-32 h-10 bg-spacex-accent/80 rounded-lg flex items-center justify-center shadow-lg">
                                    <span class="font-orbitron text-spacex-dark text-sm font-bold">v1.0.0</span>
                                </div>
                            </div>
                        </div>
                        <div class="md:w-2/3">
                            <h3 class="font-orbitron text-2xl text-spacex-accent mb-4">O plano para a memecoin mais lendária da galáxia</h3>
                            <p class="text-spacex-light/80 mb-6">
                                O whitepaper do SpaceX-Token detalha nossa visão completa, tokenomics avançada, roadmap estratégico, 
                                equipe por trás do projeto e valores fundamentais. Conheça em profundidade o que nos torna únicos 
                                e como planejamos conquistar o espaço cripto.
                            </p>
                            <div class="space-y-4 mb-8">
                                <div class="flex items-start">
                                    <div class="text-spacex-accent mr-3 mt-1">
                                        <i class="fas fa-check"></i>
                                    </div>
                                    <p class="text-spacex-light/80 flex-1">
                                        <span class="font-bold text-spacex-light">Visão e Missão:</span> Nossa abordagem única para combinar memes e utilidade real.
                                    </p>
                                </div>
                                <div class="flex items-start">
                                    <div class="text-spacex-accent mr-3 mt-1">
                                        <i class="fas fa-check"></i>
                                    </div>
                                    <p class="text-spacex-light/80 flex-1">
                                        <span class="font-bold text-spacex-light">Tokenomics Detalhada:</span> Distribuição, incentivos e mecanismos de valorização.
                                    </p>
                                </div>
                                <div class="flex items-start">
                                    <div class="text-spacex-accent mr-3 mt-1">
                                        <i class="fas fa-check"></i>
                                    </div>
                                    <p class="text-spacex-light/80 flex-1">
                                        <span class="font-bold text-spacex-light">Roadmap Expandido:</span> Metas e marcos para os próximos 3 anos.
                                    </p>
                                </div>
                                <div class="flex items-start">
                                    <div class="text-spacex-accent mr-3 mt-1">
                                        <i class="fas fa-check"></i>
                                    </div>
                                    <p class="text-spacex-light/80 flex-1">
                                        <span class="font-bold text-spacex-light">Equipe e Parceiros:</span> Conheça os astronautas por trás deste foguete.
                                    </p>
                                </div>
                            </div>
                            <button class="btn-accent px-6 py-3 rounded-full font-bold flex items-center space-x-2 mx-auto md:mx-0">
                                <i class="fas fa-download"></i>
                                <span><a href="whitepaper.pdf" target="_blank" rel="noopener noreferrer">
  Baixar Whitepaper (PDF)
</a>
</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Community Section -->
    <section class="py-20 bg-gradient-to-b from-spacex-blue/10 to-spacex-dark">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="font-orbitron text-3xl md:text-4xl font-bold mb-4">
                    <span class="bg-gradient-to-r from-spacex-light to-spacex-accent bg-clip-text text-transparent">Junte-se à Nossa Comunidade</span>
                </h2>
                <div class="w-24 h-1 bg-gradient-to-r from-spacex-blue to-spacex-accent mx-auto"></div>
            </div>
            
            <div class="max-w-4xl mx-auto">
                <div class="flex flex-wrap justify-center gap-6">
                    <a href="#" class="token-card w-16 h-16 rounded-full flex items-center justify-center text-2xl hover:text-spacex-accent transition">
                        <i class="fab fa-telegram"></i>
                    </a>
                    <a href="#" class="token-card w-16 h-16 rounded-full flex items-center justify-center text-2xl hover:text-spacex-accent transition">
                        <i class="fab fa-twitter"></i>
                    </a>
                    <a href="#" class="token-card w-16 h-16 rounded-full flex items-center justify-center text-2xl hover:text-spacex-accent transition">
                        <i class="fab fa-discord"></i>
                    </a>
                    <a href="#" class="token-card w-16 h-16 rounded-full flex items-center justify-center text-2xl hover:text-spacex-accent transition">
                        <i class="fab fa-reddit"></i>
                    </a>
                    <a href="#" class="token-card w-16 h-16 rounded-full flex items-center justify-center text-2xl hover:text-spacex-accent transition">
                        <i class="fab fa-medium"></i>
                    </a>
                    <a href="#" class="token-card w-16 h-16 rounded-full flex items-center justify-center text-2xl hover:text-spacex-accent transition">
                        <i class="fab fa-github"></i>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-spacex-dark/90 backdrop-blur-md border-t border-spacex-blue/30 py-12">
        <div class="container mx-auto px-6">
            <div class="flex flex-col md:flex-row justify-between items-center">
                <div class="flex items-center space-x-2 mb-6 md:mb-0">
                    <div class="rocket-trail">
                        <i class="fas fa-rocket text-spacex-accent text-2xl animate-float"></i>
                    </div>
                    <span class="font-orbitron text-xl font-bold bg-gradient-to-r from-spacex-light to-spacex-accent bg-clip-text text-transparent">SPACEX-TOKEN</span>
                </div>
                
                <div class="flex flex-wrap justify-center gap-6 mb-6 md:mb-0">
                    <a href="#about" class="text-spacex-light/80 hover:text-spacex-accent transition">Sobre</a>
                    <a href="#tokenomics" class="text-spacex-light/80 hover:text-spacex-accent transition">Tokenomics</a>
                    <a href="#roadmap" class="text-spacex-light/80 hover:text-spacex-accent transition">Roadmap</a>
                    <a href="#whitepaper" class="text-spacex-light/80 hover:text-spacex-accent transition">Whitepaper</a>
                    <a href="#" class="text-spacex-light/80 hover:text-spacex-accent transition">FAQ</a>
                </div>
                
                <div class="flex space-x-4">
                    <button class="btn-spacex px-4 py-2 rounded-full text-sm font-bold flex items-center space-x-2">
                        <i class="fas fa-shopping-cart"></i>
                        <span>Comprar SPX</span>
                    </button>
                </div>
            </div>
            
            <div class="border-t border-spacex-blue/30 mt-8 pt-8 text-center text-spacex-light/60 text-sm">
                <p>© 2025 SpaceX-Token. Todos os direitos reservados.</p>
                <p class="mt-2">Este projeto não tem afiliação com SpaceX ou Elon Musk. É apenas uma memecoin divertida na blockchain Solana.</p>
            </div>
        </div>
    </footer>

    <!-- Back to Top Button -->
    <button id="backToTop" class="fixed bottom-8 right-8 w-12 h-12 bg-spacex-blue/80 backdrop-blur-md rounded-full flex items-center justify-center text-spacex-accent text-xl opacity-0 invisible transition-all duration-300">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script>
        // Back to Top Button
        const backToTopButton = document.getElementById('backToTop');
        
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.remove('opacity-0', 'invisible');
                backToTopButton.classList.add('opacity-100', 'visible');
            } else {
                backToTopButton.classList.remove('opacity-100', 'visible');
                backToTopButton.classList.add('opacity-0', 'invisible');
            }
        });
        
        backToTopButton.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
        
        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
        
        // Animate elements when they come into view
        const animateOnScroll = () => {
            const elements = document.querySelectorAll('.token-card, .roadmap-item');
            
            elements.forEach(element => {
                const elementPosition = element.getBoundingClientRect().top;
                const screenPosition = window.innerHeight / 1.3;
                
                if (elementPosition < screenPosition) {
                    element.classList.add('animate-fadeIn');
                }
            });
        };
        
        window.addEventListener('scroll', animateOnScroll);
        animateOnScroll(); // Run once on page load
    </script>
</body>
</html>
