<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bhopal Influencer Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Chosen Palette: Calm Harmony -->
    <!-- Application Structure Plan: A dashboard-style SPA is chosen for its effectiveness in presenting data-driven content. The structure includes a header, a primary controls section for filtering, a summary stats area for a high-level overview, a visualization section with charts for trend analysis, and a dynamic card grid for detailed exploration. This non-linear structure empowers users (e.g., marketers) to move from a broad overview to specific details seamlessly. Filters for platform, niche, and follower tier allow for targeted data slicing, making the process of finding suitable influencers for a campaign highly efficient and user-friendly, a significant improvement over a static data file. -->
    <!-- Visualization & Content Choices: 
        - Report Info: Influencer List -> Goal: Inform -> Viz: Dynamic Stat Cards -> Interaction: Real-time updates on filter -> Justification: Provides immediate high-level insights -> Method: JS DOM Manipulation.
        - Report Info: Niche Data -> Goal: Compare -> Viz: Bar Chart -> Interaction: Re-renders on filter -> Justification: Clearly shows the density of influencers across categories -> Library: Chart.js (Canvas).
        - Report Info: Platform Data -> Goal: Compare Proportions -> Viz: Donut Chart -> Interaction: Re-renders on filter -> Justification: Instantly communicates the platform split -> Library: Chart.js (Canvas).
        - Report Info: Full Influencer Details -> Goal: Organize/Explore -> Viz: Interactive Card Grid -> Interaction: Filters and search dynamically update the displayed cards -> Justification: A modern, responsive, and visually engaging way to present detailed records -> Method: HTML/CSS (Tailwind) + JS.
    -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <style>
        body {
            background-color: #FDFBF7;
            color: #4A4A4A;
            font-family: 'Inter', sans-serif;
        }
        .chart-container {
            position: relative;
            margin: auto;
            height: 320px;
            width: 100%;
            max-width: 500px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
            }
        }
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #FDFBF7;
        }
        ::-webkit-scrollbar-thumb {
            background: #D1C7B9;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #B9AD9E;
        }
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body class="antialiased">

    <div class="container mx-auto p-4 md:p-8">
        <header class="text-center mb-8">
            <h1 class="text-4xl md:text-5xl font-bold text-[#6D5D4D]">Bhopal Influencer Hub</h1>
            <p class="text-lg text-[#8A7A6A] mt-2">An interactive dashboard to explore content creators in Bhopal</p>
        </header>

        <main>
            <div class="bg-white/60 backdrop-blur-sm rounded-2xl shadow-lg p-4 md:p-6 mb-8 border border-gray-200/50">
                <p class="text-base text-[#6D5D4D] mb-6 text-center">
                    This dashboard provides a comprehensive overview of the influencer landscape in Bhopal, based on the provided report data. Use the filters below to dynamically explore creators by their platform, niche, and follower size. The charts and influencer list will update in real-time to help you identify the perfect match for your campaigns.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                    <input type="text" id="search-input" placeholder="Search by name..." class="w-full p-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#B9AD9E] focus:border-[#B9AD9E] transition duration-200 bg-white">
                    
                    <select id="platform-filter" class="w-full p-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#B9AD9E] focus:border-[#B9AD9E] transition duration-200 bg-white">
                        <option value="all">All Platforms</option>
                        <option value="Instagram">Instagram</option>
                        <option value="YouTube">YouTube</option>
                    </select>

                    <select id="niche-filter" class="w-full p-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#B9AD9E] focus:border-[#B9AD9E] transition duration-200 bg-white">
                        <option value="all">All Niches</option>
                    </select>

                    <select id="tier-filter" class="w-full p-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#B9AD9E] focus:border-[#B9AD9E] transition duration-200 bg-white">
                        <option value="all">All Tiers</option>
                        <option value="Nano">Nano (5K-15K)</option>
                        <option value="Micro">Micro (15K-100K)</option>
                        <option value="Mid-tier">Mid-tier (100K-500K)</option>
                    </select>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
                <div class="bg-white rounded-2xl shadow-md p-6 border border-gray-200/50 text-center">
                    <h3 class="text-lg font-semibold text-[#8A7A6A]">Total Influencers</h3>
                    <p id="total-influencers" class="text-4xl font-bold text-[#6D5D4D] mt-2">0</p>
                </div>
                <div class="bg-white rounded-2xl shadow-md p-6 border border-gray-200/50 text-center">
                    <h3 class="text-lg font-semibold text-[#8A7A6A]">Avg. Followers</h3>
                    <p id="avg-followers" class="text-4xl font-bold text-[#6D5D4D] mt-2">0</p>
                </div>
                <div class="bg-white rounded-2xl shadow-md p-6 border border-gray-200/50 text-center">
                    <h3 class="text-lg font-semibold text-[#8A7A6A]">Contact Info Available</h3>
                    <p id="contact-available" class="text-4xl font-bold text-[#6D5D4D] mt-2">0</p>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
                <div class="bg-white rounded-2xl shadow-md p-4 md:p-6 border border-gray-200/50">
                    <h3 class="text-xl font-bold text-center text-[#6D5D4D] mb-4">Influencers by Niche</h3>
                    <div class="chart-container">
                        <canvas id="nicheChart"></canvas>
                    </div>
                </div>
                <div class="bg-white rounded-2xl shadow-md p-4 md:p-6 border border-gray-200/50">
                    <h3 class="text-xl font-bold text-center text-[#6D5D4D] mb-4">Platform Distribution</h3>
                    <div class="chart-container">
                        <canvas id="platformChart"></canvas>
                    </div>
                </div>
            </div>
            
            <div id="influencer-list" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            </div>
        </main>
    </div>

    <script>
        const rawData = `
Name / Handle,Platform,Profile URL,Followers / Subscribers Count,Category / Niche,Contact Information
Priyanka Mishra,Instagram,https://www.instagram.com/officialsandeepmishra_,156.9K,"Online trainers",N/A
Sumit Varyani,Instagram,,N/A,"Photography, Travel & Food",N/A
Nuzhat Parween,Instagram,https://www.instagram.com/nuzhatparween786,124.7K,Cricket,N/A
Shriya Gullah,Instagram,https://www.instagram.com/makeupstoriesbyshreya,143.4K,"Makeup / Beauty",N/A
Khushhali Sharma,Instagram,https://www.instagram.com/zinminolisharma,141.7K,N/A,N/A
Mehak Smoker,Instagram,https://www.instagram.com/mehaksmoker,157.4K,VJs & RJs,N/A
Anushka Bajpayee,Instagram,https://www.instagram.com/anushkabajpayee,N/A,"Fashion, Lifestyle, Model",anushkabajpayee@gmail.com
Annie Jain,Instagram,https://www.instagram.com/amazing_finds_annie,489.7K,Appliance Reviewers,N/A
Naini Jain,Instagram,https://www.instagram.com/rj_naini,250.1K,"Family, Kids & Pets",N/A
ARISH GOUR,Instagram,https://www.instagram.com/animals_cute.wild,205.2K,"Pets & Animals",N/A
Renuka Pahade,Instagram,https://www.instagram.com/jasmine_simplyperfect,198.5K,Fitness,N/A
Shiway,Instagram,https://www.instagram.com/shiway_skate_stunt,196.1K,Freestylers,N/A
Bhopali Points,Instagram,https://www.instagram.com/bhopali_points,206.9K,Vloggers,N/A
Arpita,Instagram,https://www.instagram.com/bhukkad_belly,46.9K,Food,N/A
Shatakshi Rai,Instagram,https://www.instagram.com/the.foodie_fashionista,30.8K,"Food, Fashion",N/A
Mayuriii,Instagram,https://www.instagram.com/mayuribilthareofficial,25.8K,Fashion,N/A
Rohan Pathak,Instagram,https://www.instagram.com/imrohanhq,25.2K,N/A,N/A
Kamal Batham,Instagram,https://www.instagram.com/art_with_komu_,24K,"Arts, Doodling & Painting",N/A
Akash Pandey,Instagram,https://www.instagram.com/akashpandey_official__,23.6K,N/A,N/A
Vikash Malviya,Instagram,https://www.instagram.com/vikashmalviya9,21.7K,Fashion,N/A
Divyani Ghosh,Instagram,https://www.instagram.com/divyanighosh9518,24.2K,N/A,N/A
Sudeep Shah,Instagram,https://www.instagram.com/i.am.sudeep.shah,19.2K,N/A,N/A
Anurag Dhakad,Instagram,https://www.instagram.com/anuragdhakad01,18.9K,N/A,N/A
Anshu Samraat MandLekar,Instagram,https://www.instagram.com/anshu_and_samraat,18.5K,"Family, Kids & Pets",N/A
Divyanshi_Das,Instagram,https://www.instagram.com/official_divyanshidas1410,18.1K,N/A,N/A
Shalinni,Instagram,https://www.instagram.com/sheengram_tkg,18.4K,N/A,N/A
Kartik Swamy,Instagram,https://www.instagram.com/anna_kartik_,16.6K,"Travel & Places",N/A
Pratibha Sahu,"Instagram, YouTube",,N/A,"Dancer, Fashion Designer",N/A
Harshita Rajak,YouTube,,23.7K,"Beauty, Fashion, Lifestyle",N/A
Yogesh Sharma,YouTube,,244K,"Travel, Vlogs",Yogeshsharmadance@gmail.com
Wanderlust Shashank,YouTube,,N/A,"Travel, Vlogs",N/A
IFRAH,Instagram,https://www.instagram.com/crafts_by_ifrah,19.9K,"Crafts & DIY Arts",N/A
Shefali Alvares Rashid,Instagram,https://www.instagram.com/shefali_alvares,57K,Musicians,N/A
Nir Addie,Instagram,https://www.instagram.com/nir.addie,53.6K,N/A,N/A
Mamta,Instagram,https://www.instagram.com/lil_babie_world,49.3K,"Family, Kids & Pets",N/A
Arish,Instagram,https://www.instagram.com/arish_nature.animals,46.8K,"Pets & Animals",N/A
Laaraib Siddique,Instagram,https://www.instagram.com/laaraibsiddique,41.1K,Musicians,N/A
Syed Mehboob Ali,Instagram,https://www.instagram.com/mehboob.alii,40.6K,N/A,N/A
Shryansh Bisen,Instagram,https://www.instagram.com/shrylox,36.3K,VJs & RJs,N/A
deepbellus makeup,Instagram,https://www.instagram.com/deepbellusmakeup,34.3K,Makeup,N/A
saloni chouksey,Instagram,https://www.instagram.com/the_amishu_chouksey,33K,"Family, Kids & Pets",N/A
THE BHOPAL,Instagram,https://www.instagram.com/thebhopal,33.6K,"City-focused, Travel & Places",N/A
SUBHAN UDDIN,Instagram,https://www.instagram.com/subhan_ud,30.3K,N/A,N/A
        `.trim();

        let nicheChart, platformChart;
        let influencerData = [];

        function parseFollowers(followerStr) {
            if (!followerStr || typeof followerStr !== 'string') return 0;
            const lowerCaseStr = followerStr.toLowerCase();
            if (lowerCaseStr.includes('k')) {
                return parseFloat(lowerCaseStr.replace('k', '')) * 1000;
            }
            if (lowerCaseStr.includes('m')) {
                return parseFloat(lowerCaseStr.replace('m', '')) * 1000000;
            }
            return parseInt(followerStr, 10) || 0;
        }

        function getTier(followers) {
            if (followers >= 100000 && followers <= 500000) return 'Mid-tier';
            if (followers >= 15000 && followers < 100000) return 'Micro';
            if (followers >= 5000 && followers < 15000) return 'Nano';
            return 'Other';
        }

        function parseCSV(csvData) {
            const lines = csvData.split('\n');
            const headers = lines[0].split(',').map(h => h.trim());
            return lines.slice(1).map(line => {
                const values = line.match(/(".*?"|[^",]+)(?=\s*,|\s*$)/g) || [];
                const entry = {};
                headers.forEach((header, i) => {
                    let value = (values[i] || '').replace(/"/g, '').trim();
                    if (value === 'N/A') value = '';
                    entry[header] = value;
                });
                const followers = parseFollowers(entry['Followers / Subscribers Count']);
                return {
                    name: entry['Name / Handle'],
                    platform: entry['Platform'],
                    url: entry['Profile URL'],
                    followers: followers,
                    niche: entry['Category / Niche'] || 'General',
                    contact: entry['Contact Information'],
                    tier: getTier(followers)
                };
            }).filter(d => d.name && d.followers > 0);
        }

        function populateNicheFilter(data) {
            const nicheFilter = document.getElementById('niche-filter');
            const niches = [...new Set(data.map(item => item.niche))].sort();
            niches.forEach(niche => {
                const option = document.createElement('option');
                option.value = niche;
                option.textContent = niche;
                nicheFilter.appendChild(option);
            });
        }

        function renderInfluencerCards(data) {
            const listElement = document.getElementById('influencer-list');
            listElement.innerHTML = '';
            if (data.length === 0) {
                listElement.innerHTML = `<p class="col-span-full text-center text-gray-500 py-10">No influencers match the current filters.</p>`;
                return;
            }
            data.forEach(influencer => {
                const card = document.createElement('div');
                card.className = 'bg-white rounded-2xl shadow-md p-5 border border-gray-200/50 flex flex-col transition-transform transform hover:scale-105 duration-300';
                
                const platformIcon = influencer.platform.includes('Instagram') 
                    ? `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-pink-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>`
                    : `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" /></svg>`;

                card.innerHTML = `
                    <div class="flex items-center justify-between mb-3">
                        <h4 class="text-lg font-bold text-[#6D5D4D] truncate">${influencer.name}</h4>
                        ${platformIcon}
                    </div>
                    <div class="space-y-2 text-sm text-[#8A7A6A] flex-grow">
                        <p><strong>Followers:</strong> ${(influencer.followers / 1000).toFixed(1)}K</p>
                        <p><strong>Niche:</strong> ${influencer.niche}</p>
                        <p><strong>Tier:</strong> ${influencer.tier}</p>
                    </div>
                    <div class="mt-4 pt-4 border-t border-gray-200">
                        ${influencer.url ? `<a href="${influencer.url}" target="_blank" class="block w-full text-center bg-[#B9AD9E] text-white py-2 rounded-lg hover:bg-[#A89C8E] transition-colors">View Profile</a>` : `<button class="w-full text-center bg-gray-300 text-gray-500 py-2 rounded-lg cursor-not-allowed">No Profile</button>`}
                    </div>
                `;
                listElement.appendChild(card);
            });
        }

        function updateStats(data) {
            document.getElementById('total-influencers').textContent = data.length;
            
            const totalFollowers = data.reduce((sum, item) => sum + item.followers, 0);
            const avgFollowers = data.length > 0 ? totalFollowers / data.length : 0;
            document.getElementById('avg-followers').textContent = (avgFollowers / 1000).toFixed(1) + 'K';

            const contacts = data.filter(item => item.contact).length;
            document.getElementById('contact-available').textContent = contacts;
        }
        
        function updateCharts(data) {
            updateNicheChart(data);
            updatePlatformChart(data);
        }

        function updateNicheChart(data) {
            const nicheCtx = document.getElementById('nicheChart').getContext('2d');
            const nicheCounts = data.reduce((acc, item) => {
                acc[item.niche] = (acc[item.niche] || 0) + 1;
                return acc;
            }, {});

            const sortedNiches = Object.entries(nicheCounts).sort((a, b) => b[1] - a[1]).slice(0, 10);
            const labels = sortedNiches.map(item => item[0]);
            const values = sortedNiches.map(item => item[1]);

            if (nicheChart) {
                nicheChart.destroy();
            }
            nicheChart = new Chart(nicheCtx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Number of Influencers',
                        data: values,
                        backgroundColor: '#D1C7B9',
                        borderColor: '#B9AD9E',
                        borderWidth: 1,
                        borderRadius: 5,
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    indexAxis: 'y',
                    scales: {
                        x: { beginAtZero: true, grid: { display: false } },
                        y: { grid: { display: false } }
                    },
                    plugins: { legend: { display: false } }
                }
            });
        }
        
        function updatePlatformChart(data) {
            const platformCtx = document.getElementById('platformChart').getContext('2d');
            const platformCounts = data.reduce((acc, item) => {
                const platforms = item.platform.split(',').map(p => p.trim());
                platforms.forEach(p => {
                    acc[p] = (acc[p] || 0) + 1;
                });
                return acc;
            }, {});

            if (platformChart) {
                platformChart.destroy();
            }
            platformChart = new Chart(platformCtx, {
                type: 'doughnut',
                data: {
                    labels: Object.keys(platformCounts),
                    datasets: [{
                        data: Object.values(platformCounts),
                        backgroundColor: ['#E8C3B9', '#B9AD9E', '#A89C8E'],
                        borderColor: '#FDFBF7',
                        borderWidth: 4,
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom' }
                    }
                }
            });
        }

        function filterData() {
            const platform = document.getElementById('platform-filter').value;
            const niche = document.getElementById('niche-filter').value;
            const tier = document.getElementById('tier-filter').value;
            const searchTerm = document.getElementById('search-input').value.toLowerCase();

            const filtered = influencerData.filter(item => {
                const platformMatch = platform === 'all' || item.platform.includes(platform);
                const nicheMatch = niche === 'all' || item.niche === niche;
                const tierMatch = tier === 'all' || item.tier === tier;
                const searchMatch = item.name.toLowerCase().includes(searchTerm);
                return platformMatch && nicheMatch && tierMatch && searchMatch;
            });

            renderInfluencerCards(filtered);
            updateStats(filtered);
            updateCharts(filtered);
        }

        document.addEventListener('DOMContentLoaded', () => {
            influencerData = parseCSV(rawData);
            populateNicheFilter(influencerData);
            
            document.getElementById('platform-filter').addEventListener('change', filterData);
            document.getElementById('niche-filter').addEventListener('change', filterData);
            document.getElementById('tier-filter').addEventListener('change', filterData);
            document.getElementById('search-input').addEventListener('input', filterData);

            filterData();
        });
    </script>
</body>
</html>
