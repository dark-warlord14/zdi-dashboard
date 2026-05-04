const App = {
    published: [],
    upcoming: [],
    index: [],
    stats: null,
    md: null,
    currentSort: { field: 'published_date', dir: 'desc' },
    currentPage: 1,
    pageSize: 50,
    filters: { search: '', vendor: '', cvss: '', cve: '', deadline: '' },
    debounceTimer: null,

    async init() {
        this.md = window.markdownit({ html: false, linkify: true, breaks: true });
        document.documentElement.dataset.theme = localStorage.getItem('theme') || 'dark';
        await this.loadData();
        window.addEventListener('hashchange', () => this.route());
        this.route();
    },

    async loadData() {
        const [published, upcoming, index, stats] = await Promise.all([
            fetch('/data/published.json').then(r => r.ok ? r.json() : []),
            fetch('/data/upcoming.json').then(r => r.ok ? r.json() : []),
            fetch('/data/index.json').then(r => r.ok ? r.json() : []),
            fetch('/data/stats.json').then(r => r.ok ? r.json() : null),
        ]);
        this.published = published;
        this.upcoming = upcoming;
        this.index = index;
        this.stats = stats;
    },

    toggleTheme() {
        const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
        document.documentElement.dataset.theme = next;
        localStorage.setItem('theme', next);
    },

    route() {
        const hash = location.hash || '#/published';
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.toggle('active', hash.startsWith(`#/${link.dataset.nav}`));
        });
        if (hash.startsWith('#/advisory/')) return this.showDetail(hash.split('/')[2]);
        if (hash.startsWith('#/stats')) return this.showStats();
        if (hash.startsWith('#/upcoming')) return this.showList('upcoming');
        return this.showList('published');
    },

    resetListStateIfNeeded(kind) {
        const defaultSort = kind === 'published' ? 'published_date' : 'deadline';
        if (this.activeKind !== kind) {
            this.activeKind = kind;
            this.currentSort = { field: defaultSort, dir: 'desc' };
            this.currentPage = 1;
            this.filters = { search: '', vendor: '', cvss: '', cve: '', deadline: '' };
        }
    },

    showList(kind) {
        this.resetListStateIfNeeded(kind);
        const records = kind === 'published' ? this.published : this.upcoming;
        const filtered = this.filterRecords(records, kind);
        const sorted = this.sortRecords(filtered);
        const totalPages = Math.max(1, Math.ceil(sorted.length / this.pageSize));
        this.currentPage = Math.min(this.currentPage, totalPages);
        const page = sorted.slice((this.currentPage - 1) * this.pageSize, this.currentPage * this.pageSize);
        const vendors = [...new Set(records.map(r => r.vendor).filter(Boolean))].sort();

        document.getElementById('app').innerHTML = `
            <div class="tabs-title">
                <h1>${kind === 'published' ? 'Published Advisories' : 'Upcoming Advisories'}</h1>
            </div>
            <div class="stats-bar">
                ${Components.statCard('Published', this.published.length)}
                ${Components.statCard('Upcoming', this.upcoming.length)}
                ${Components.statCard('High CVSS', (this.index || []).filter(r => Number(r.cvss) >= 7).length)}
                ${Components.statCard('Vendors', vendors.length)}
            </div>
            ${this.filtersHtml(kind, vendors)}
            <div class="result-count">Showing ${page.length} of ${filtered.length} records</div>
            <div class="table-wrapper">${kind === 'published' ? this.publishedTable(page) : this.upcomingTable(page)}</div>
            <div id="pagination"></div>
        `;
        if (totalPages > 1) {
            document.getElementById('pagination').appendChild(Components.pagination(this.currentPage, totalPages, p => {
                this.currentPage = p;
                this.showList(kind);
            }));
        }
    },

    filtersHtml(kind, vendors) {
        return `
            <div class="filters">
                <input class="search-box" type="search" placeholder="Search IDs, title, vendor, CVE, detail text..." value="${Components.escapeHtml(this.filters.search)}" oninput="App.onFilterDebounced('search', this.value)">
                <select onchange="App.onFilter('vendor', this.value)">
                    <option value="">All Vendors</option>
                    ${vendors.map(v => `<option value="${Components.escapeHtml(v)}" ${this.filters.vendor === v ? 'selected' : ''}>${Components.escapeHtml(v)}</option>`).join('')}
                </select>
                <select onchange="App.onFilter('cvss', this.value)">
                    <option value="">All CVSS</option>
                    ${['critical', 'high', 'medium', 'low'].map(v => `<option value="${v}" ${this.filters.cvss === v ? 'selected' : ''}>${v}</option>`).join('')}
                </select>
                ${kind === 'published' ? `
                    <select onchange="App.onFilter('cve', this.value)">
                        <option value="">All CVE States</option>
                        <option value="present" ${this.filters.cve === 'present' ? 'selected' : ''}>CVE present</option>
                        <option value="missing" ${this.filters.cve === 'missing' ? 'selected' : ''}>CVE missing</option>
                    </select>` : `
                    <select onchange="App.onFilter('deadline', this.value)">
                        <option value="">All Deadlines</option>
                        <option value="past_due" ${this.filters.deadline === 'past_due' ? 'selected' : ''}>Past due</option>
                        <option value="due_soon" ${this.filters.deadline === 'due_soon' ? 'selected' : ''}>Due soon</option>
                        <option value="future" ${this.filters.deadline === 'future' ? 'selected' : ''}>Future</option>
                    </select>`}
                <button class="outline" onclick="App.clearFilters()">Clear</button>
            </div>
        `;
    },

    publishedTable(records) {
        return `<table><thead><tr>
            ${this.th('zdi_id', 'ZDI ID')} ${this.th('vendor', 'Vendor')} ${this.th('cve', 'CVE')} ${this.th('cvss', 'CVSS')}
            ${this.th('published_date', 'Published')} ${this.th('updated_date', 'Updated')} ${this.th('title', 'Title')}
        </tr></thead><tbody>${records.map(r => `
            <tr onclick="location.hash='#/advisory/${r.zdi_id}'">
                <td class="id-cell">${Components.escapeHtml(r.zdi_id)}</td>
                <td>${Components.escapeHtml(r.vendor || 'N/A')}</td>
                <td>${Components.escapeHtml(r.cve || 'N/A')}</td>
                <td>${Components.cvssBadge(r.cvss)}</td>
                <td>${Components.formatDate(r.published_date)}</td>
                <td>${Components.formatDate(r.updated_date)}</td>
                <td class="title-cell">
                    <div>${Components.escapeHtml(r.title)}</div>
                    ${r.description_snippet ? `<p class="description-snippet">${Components.escapeHtml(r.description_snippet)}</p>` : ''}
                </td>
            </tr>`).join('')}</tbody></table>`;
    },

    upcomingTable(records) {
        return `<table><thead><tr>
            ${this.th('zdi_can', 'ZDI-CAN')} ${this.th('vendor', 'Vendor')} ${this.th('cvss', 'CVSS')}
            ${this.th('reported_date', 'Reported')} ${this.th('deadline', 'Deadline')} ${this.th('discoverer', 'Discoverer')}
        </tr></thead><tbody>${records.map(r => `
            <tr>
                <td class="id-cell">${Components.escapeHtml(r.zdi_can)}</td>
                <td>${Components.escapeHtml(r.vendor || 'N/A')}</td>
                <td>${Components.cvssBadge(r.cvss)}</td>
                <td>${Components.formatDate(r.reported_date)}</td>
                <td>${Components.formatDate(r.deadline)}</td>
                <td class="title-cell">${Components.escapeHtml(r.discoverer || 'N/A')}</td>
            </tr>`).join('')}</tbody></table>`;
    },

    th(field, label) {
        const arrow = this.currentSort.field === field ? (this.currentSort.dir === 'asc' ? ' ▲' : ' ▼') : '';
        return `<th class="sortable" onclick="App.onSort('${field}')">${label}${arrow}</th>`;
    },

    filterRecords(records, kind) {
        return records.filter(r => {
            const haystack = Object.values(r).join(' ').toLowerCase();
            if (this.filters.search && !haystack.includes(this.filters.search.toLowerCase())) return false;
            if (this.filters.vendor && r.vendor !== this.filters.vendor) return false;
            if (this.filters.cvss && Components.cvssBand(r.cvss) !== this.filters.cvss) return false;
            if (kind === 'published' && this.filters.cve === 'present' && !r.cve) return false;
            if (kind === 'published' && this.filters.cve === 'missing' && r.cve) return false;
            if (kind === 'upcoming' && this.filters.deadline && this.deadlineState(r.deadline) !== this.filters.deadline) return false;
            return true;
        });
    },

    sortRecords(records) {
        const { field, dir } = this.currentSort;
        return [...records].sort((a, b) => {
            const av = a[field] ?? '';
            const bv = b[field] ?? '';
            const result = typeof av === 'number' && typeof bv === 'number'
                ? av - bv
                : String(av).localeCompare(String(bv));
            return dir === 'asc' ? result : -result;
        });
    },

    deadlineState(deadline) {
        if (!deadline) return 'unknown';
        const days = (new Date(deadline) - new Date()) / 86400000;
        if (days < 0) return 'past_due';
        if (days <= 30) return 'due_soon';
        return 'future';
    },

    onSort(field) {
        this.currentSort = this.currentSort.field === field
            ? { field, dir: this.currentSort.dir === 'asc' ? 'desc' : 'asc' }
            : { field, dir: 'asc' };
        this.currentPage = 1;
        this.showList(this.activeKind || 'published');
    },

    onFilter(key, value) {
        this.filters[key] = value;
        this.currentPage = 1;
        this.showList(this.activeKind || 'published');
    },

    onFilterDebounced(key, value) {
        clearTimeout(this.debounceTimer);
        this.debounceTimer = setTimeout(() => this.onFilter(key, value), 120);
    },

    clearFilters() {
        this.filters = { search: '', vendor: '', cvss: '', cve: '', deadline: '' };
        this.currentPage = 1;
        this.showList(this.activeKind || 'published');
    },

    async showDetail(id) {
        const app = document.getElementById('app');
        app.innerHTML = '<p class="loading-initial">Loading advisory...</p>';
        const [jsonRes, mdRes] = await Promise.all([
            fetch(`/data/advisories/${id}/advisory.json`),
            fetch(`/data/advisories/${id}/advisory.md`),
        ]);
        if (!jsonRes.ok || !mdRes.ok) {
            app.innerHTML = '<div class="panel">Advisory detail not found.</div>';
            return;
        }
        const detail = await jsonRes.json();
        const markdown = await mdRes.text();
        app.innerHTML = `
            <div class="detail-layout">
                <article class="panel markdown">${this.md.render(markdown)}</article>
                <aside class="panel meta-list">
                    ${this.meta('ZDI ID', detail.zdi_id)}
                    ${this.meta('ZDI-CAN', detail.zdi_can)}
                    ${this.meta('CVE', detail.cve)}
                    ${this.meta('CVSS', detail.cvss)}
                    ${this.meta('Vendor', (detail.affected_vendors || []).join(', '))}
                    <a class="outline" href="${detail.source_url}" target="_blank" rel="noopener">Source</a>
                    <a class="outline" href="/data/advisories/${id}/advisory.json">JSON</a>
                    <a class="outline" href="/data/advisories/${id}/advisory.md">Markdown</a>
                </aside>
            </div>
        `;
    },

    meta(label, value) {
        return `<div><span class="meta-label">${Components.escapeHtml(label)}</span><span class="meta-value">${Components.escapeHtml(value || 'N/A')}</span></div>`;
    },

    showStats() {
        const stats = this.stats || {};
        document.getElementById('app').innerHTML = `
            <div class="tabs-title"><h1>Stats</h1></div>
            <div class="stats-bar">
                ${Components.statCard('Published', stats.total_published || this.published.length)}
                ${Components.statCard('Upcoming', stats.total_upcoming || this.upcoming.length)}
                ${Components.statCard('High CVSS', stats.high_cvss || 0)}
                ${Components.statCard('With CVE', stats.cve_coverage || 0)}
            </div>
            <div class="chart-grid">
                <div class="panel"><canvas id="vendorsChart"></canvas></div>
                <div class="panel"><canvas id="yearsChart"></canvas></div>
            </div>
        `;
        this.renderBarChart('vendorsChart', stats.by_vendor || {}, 'Top vendors');
        this.renderBarChart('yearsChart', stats.by_year || {}, 'Published by year');
    },

    renderBarChart(id, data, label) {
        const ctx = document.getElementById(id);
        if (!ctx || !window.Chart) return;
        const entries = Object.entries(data).slice(0, 12);
        new Chart(ctx, {
            type: 'bar',
            data: { labels: entries.map(e => e[0]), datasets: [{ label, data: entries.map(e => e[1]) }] },
            options: { responsive: true, plugins: { legend: { display: false } } }
        });
    }
};

document.addEventListener('DOMContentLoaded', () => App.init());
