const Components = {
    escapeHtml(value) {
        return String(value ?? '').replace(/[&<>"']/g, ch => ({
            '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
        }[ch]));
    },

    statCard(label, value) {
        return `<div class="stat-card"><span class="stat-label">${this.escapeHtml(label)}</span><span class="stat-value">${this.escapeHtml(value)}</span></div>`;
    },

    cvssBand(score) {
        const value = Number(score);
        if (Number.isNaN(value)) return 'unknown';
        if (value >= 9) return 'critical';
        if (value >= 7) return 'high';
        if (value >= 4) return 'medium';
        return 'low';
    },

    cvssBadge(score) {
        if (score === null || score === undefined || score === '') return '<span class="badge">N/A</span>';
        const band = this.cvssBand(score);
        return `<span class="badge ${band}">${this.escapeHtml(score)} ${band}</span>`;
    },

    formatDate(value) {
        return value || 'N/A';
    },

    pagination(current, total, onClick) {
        const wrap = document.createElement('div');
        wrap.className = 'pagination';
        const start = Math.max(1, current - 2);
        const end = Math.min(total, current + 2);
        for (let page = start; page <= end; page++) {
            const button = document.createElement('button');
            button.textContent = String(page);
            button.className = page === current ? 'active' : '';
            button.onclick = () => onClick(page);
            wrap.appendChild(button);
        }
        return wrap;
    }
};
