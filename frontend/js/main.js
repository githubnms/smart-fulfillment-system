// js/main.js

// Wait for DOM fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // ------------------------------
    // 1. ACTIVE SIDEBAR HIGHLIGHTING (simulate page)
    // ------------------------------
    const navItems = document.querySelectorAll('.nav-item');
    function setActive(navId) {
        navItems.forEach(item => {
            const itemNav = item.getAttribute('data-nav');
            if (itemNav === navId) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
    }
    // Highlight Dashboard as default (current)
    setActive('dashboard');
    
    // Add click simulation (just for UI consistency)
    navItems.forEach(item => {
        item.addEventListener('click', function(e) {
            const navTarget = this.getAttribute('data-nav');
            setActive(navTarget);
            // Optional: show toast in console / alert? We'll just mimic.
            if (navTarget !== 'dashboard') {
                // keep UI feel but do not break charts / counters
                console.log(`Navigation: ${navTarget} (simulated)`);
            } else {
                // Dashboard stays
            }
        });
    });
    
    // ------------------------------
    // 2. ANIMATED COUNTERS FOR STATS CARDS
    // ------------------------------
    function animateCounter(element, targetValue, isFloat = false) {
        let start = 0;
        const duration = 1000; // ms
        const stepTime = 16;
        let steps = duration / stepTime;
        let increment = targetValue / steps;
        let current = 0;
        const timer = setInterval(() => {
            current += increment;
            if (current >= targetValue) {
                if (isFloat) {
                    element.innerText = targetValue.toFixed(1);
                } else {
                    element.innerText = Math.floor(targetValue);
                }
                clearInterval(timer);
            } else {
                if (isFloat) {
                    element.innerText = current.toFixed(1);
                } else {
                    element.innerText = Math.floor(current);
                }
            }
        }, stepTime);
    }
    
    const totalOrdersEl = document.getElementById('totalOrdersValue');
    const warehousesEl = document.getElementById('warehousesValue');
    const inventoryEl = document.getElementById('inventoryValue');
    const deliveryEl = document.getElementById('deliveryValue');
    
    if (totalOrdersEl) {
        const targetTotal = parseInt(totalOrdersEl.getAttribute('data-target'), 10);
        animateCounter(totalOrdersEl, targetTotal, false);
    }
    if (warehousesEl) {
        const targetWare = parseInt(warehousesEl.getAttribute('data-target'), 10);
        animateCounter(warehousesEl, targetWare, false);
    }
    if (inventoryEl) {
        const targetInv = parseInt(inventoryEl.getAttribute('data-target'), 10);
        animateCounter(inventoryEl, targetInv, false);
    }
    if (deliveryEl) {
        const targetDel = parseFloat(deliveryEl.getAttribute('data-target'));
        animateCounter(deliveryEl, targetDel, true);
    }
    
    // ------------------------------
    // 3. CHARTS.JS INITIALIZATION (Line + Bar)
    // ------------------------------
    // Line Chart: Orders Trend
    const ctxLine = document.getElementById('ordersLineChart')?.getContext('2d');
    let ordersChart = null;
    if (ctxLine) {
        ordersChart = new Chart(ctxLine, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Orders Processed',
                    data: [1240, 1580, 1920, 2100, 2430, 2847],
                    borderColor: '#ff9900',
                    backgroundColor: 'rgba(255,153,0,0.05)',
                    borderWidth: 3,
                    pointBackgroundColor: '#006ce0',
                    pointBorderColor: '#6842ff',
                    pointRadius: 4,
                    pointHoverRadius: 7,
                    tension: 0.3,
                    fill: true,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: { labels: { color: '#cbd5e6', font: { size: 11 } } },
                    tooltip: { mode: 'index', intersect: false }
                },
                scales: {
                    y: { grid: { color: 'rgba(255,255,255,0.08)' }, ticks: { color: '#b9c7d9' } },
                    x: { grid: { display: false }, ticks: { color: '#b9c7d9' } }
                }
            }
        });
    }
    
    // Bar Chart: Warehouse Distribution
    const ctxBar = document.getElementById('warehouseBarChart')?.getContext('2d');
    let warehouseChart = null;
    if (ctxBar) {
        warehouseChart = new Chart(ctxBar, {
            type: 'bar',
            data: {
                labels: ['NA DC', 'EU Hub', 'APAC', 'LATAM', 'MEA'],
                datasets: [{
                    label: 'Units (K)',
                    data: [324, 287, 196, 112, 78],
                    backgroundColor: 'rgba(0,108,224,0.7)',
                    borderColor: '#ff9900',
                    borderWidth: 1,
                    borderRadius: 8,
                    hoverBackgroundColor: '#6842ff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: { labels: { color: '#cbd5e6', font: { size: 11 } } }
                },
                scales: {
                    y: { grid: { color: 'rgba(255,255,255,0.08)' }, ticks: { color: '#b9c7d9' } },
                    x: { ticks: { color: '#b9c7d9' } }
                }
            }
        });
    }
    
    // ------------------------------
    // 4. LIVE ACTIVITY AUTO-UPDATE (every 3 sec)
    // ------------------------------
    const activityContainer = document.getElementById('activityLogList');
    // Initial predefined logs (6-8 entries)
    const initialLogs = [
        { time: "10:23:45", msg: "Order #SFP-2381 shipped to destination" },
        { time: "10:18:22", msg: "Warehouse A restocked 420 units" },
        { time: "10:12:07", msg: "Smart Routing simulation completed" },
        { time: "10:05:33", msg: "Inventory sync: +189 items added" },
        { time: "09:58:11", msg: "Order #SFP-2379 delivered (on-time)" },
        { time: "09:47:29", msg: "Warehouse B temperature alert resolved" },
        { time: "09:34:50", msg: "New order created via API" },
        { time: "09:21:03", msg: "Fulfillment batch optimized" }
    ];
    
    function formatTime() {
        const now = new Date();
        return now.toLocaleTimeString('en-US', { hour: '2-digit', minute:'2-digit', second:'2-digit' });
    }
    
    function addActivityLog(message) {
        if (!activityContainer) return;
        const logDiv = document.createElement('div');
        logDiv.className = 'log-entry';
        const timeSpan = document.createElement('span');
        timeSpan.className = 'time';
        timeSpan.innerText = formatTime();
        const msgSpan = document.createElement('span');
        msgSpan.className = 'message';
        msgSpan.innerText = message;
        logDiv.appendChild(timeSpan);
        logDiv.appendChild(msgSpan);
        activityContainer.appendChild(logDiv);
        // Auto-scroll to bottom
        activityContainer.scrollTop = activityContainer.scrollHeight;
        // Keep max 30 logs to avoid overflow
        while (activityContainer.children.length > 30) {
            activityContainer.removeChild(activityContainer.firstChild);
        }
    }
    
    // Populate initial logs
    if (activityContainer) {
        activityContainer.innerHTML = '';
        initialLogs.forEach(log => {
            const logDiv = document.createElement('div');
            logDiv.className = 'log-entry';
            const timeSpan = document.createElement('span');
            timeSpan.className = 'time';
            timeSpan.innerText = log.time;
            const msgSpan = document.createElement('span');
            msgSpan.className = 'message';
            msgSpan.innerText = log.msg;
            logDiv.appendChild(timeSpan);
            logDiv.appendChild(msgSpan);
            activityContainer.appendChild(logDiv);
        });
        // scroll to bottom after init
        activityContainer.scrollTop = activityContainer.scrollHeight;
    }
    
    // Possible random events pool
    const activityMessages = [
        "Order #SFP-" + Math.floor(Math.random()*900+1000) + " shipped via express",
        "Warehouse C inventory count updated",
        "New simulation run: pick density improved by 5%",
        "Fulfillment engine recalculated routes",
        "Alert: low stock for item B-420 (reordering)",
        "Smart Fulfillment sync completed",
        "Order #ORD" + Math.floor(Math.random()*4000) + " dispatched",
        "Integration webhook received",
        "Dashboard metrics refreshed",
        "Cross-dock operation started"
    ];
    
    let intervalId = setInterval(() => {
        // pick random message
        const randomMsg = activityMessages[Math.floor(Math.random() * activityMessages.length)];
        addActivityLog(randomMsg);
    }, 3000);
    
    // ------------------------------
    // 5. SMOOTH PAGE LOAD ANIMATION (CSS already handles fadeSlideUp)
    //    Additionally ensure cards have subtle entrance
    // ------------------------------
    const allCards = document.querySelectorAll('.stat-card, .action-card, .chart-card');
    allCards.forEach((card, idx) => {
        card.style.animation = `fadeSlideUp 0.3s ease forwards`;
        card.style.animationDelay = `${idx * 0.02}s`;
        card.style.opacity = '0';
        // override after animation fill
        card.addEventListener('animationend', () => {
            card.style.opacity = '1';
        });
    });
    
    // ------------------------------
    // Quick actions click handlers (soft interaction, console logs)
    // ------------------------------
    const actionCards = document.querySelectorAll('.action-card');
    actionCards.forEach(action => {
        action.addEventListener('click', (e) => {
            const actionType = action.getAttribute('data-action') || action.innerText.trim();
            console.log(`[SmartFulfill] Quick action triggered: ${actionType}`);
            // In a full app you would navigate or open modals. For demo we add a temporary activity log as feedback
            addActivityLog(`⚡ Action: ${actionType} clicked (simulated)`);
        });
    });
    
    // ------------------------------
    // Mobile Sidebar Toggle (responsiveness)
    // ------------------------------
    const mobileToggle = document.getElementById('mobileMenuToggle');
    const sidebar = document.querySelector('.sidebar');
    if (mobileToggle && sidebar) {
        mobileToggle.addEventListener('click', function(e) {
            sidebar.classList.toggle('open');
        });
        // Close sidebar when clicking outside on mobile if needed? optional
        document.addEventListener('click', function(event) {
            const isSidebar = sidebar.contains(event.target);
            const isToggle = mobileToggle.contains(event.target);
            if (window.innerWidth <= 768 && sidebar.classList.contains('open') && !isSidebar && !isToggle) {
                sidebar.classList.remove('open');
            }
        });
    }
    
    // adjust chart resize on window orientation change (optional)
    window.addEventListener('resize', () => {
        if (ordersChart) ordersChart.resize();
        if (warehouseChart) warehouseChart.resize();
    });
    
    // prevent memory leaks, but keep interval healthy (just for demo, not needed to clear on unload but good practice)
    window.addEventListener('beforeunload', () => {
        if (intervalId) clearInterval(intervalId);
    });
    
    // Additional: Simulate operational status badge (dynamic pulse ok)
    console.log('Smart Fulfillment System — Dashboard fully operational');
});