
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    font-family: 'Inter', sans-serif;
    color: #1e293b;
    background: #f1f5f9;
    font-synthesis: none;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-width: 320px;
    background: #f1f5f9;
}

button, input {
    font: inherit;
}

.header {
    background: #101d32;
    color: white;
    padding: 28px max(calc((100% - 1100px) / 2), 5%);
}

.header-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.brand-icon {
    display: grid;
    place-items: center;
    width: 48px;
    height: 48px;
    background: #173d5c;
    color: #55c7f4;
    border-radius: 12px;
}

.brand h2 {
    font-size: 19px;
    letter-spacing: 1px;
}

.brand span {
    font-size: 10px;
    color: #a9bed5;
    letter-spacing: 1px;
}

.online {
    display: flex;
    align-items: center;
    gap: 7px;
    color: #4ade80;
    font-size: 12px;
    font-weight: 700;
}

.header-title {
    margin-top: 42px;
    padding-bottom: 12px;
}

.header-title > span {
    color: #55c7f4;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.header-title h1 {
    font-size: clamp(25px, 4vw, 36px);
    margin: 12px 0;
}

.header-title p {
    color: #a9bed5;
    font-size: 14px;
}

.container {
    max-width: 1100px;
    margin: 30px auto;
    padding: 0 20px;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-bottom: 25px;
}

.stat-card {
    display: flex;
    align-items: center;
    gap: 15px;
    background: white;
    border-radius: 12px;
    padding: 22px;
    box-shadow: 0 3px 12px #00000008;
}

.stat-icon {
    width: 45px;
    height: 45px;
    border-radius: 10px;
    display: grid;
    place-items: center;
}

.blue {
    background: #e0f2fe;
    color: #0284c7;
}

.purple {
    background: #ede9fe;
    color: #7c3aed;
}

.orange {
    background: #ffedd5;
    color: #ea580c;
}

.stat-card h2 {
    font-size: 25px;
}

.stat-card p {
    font-size: 12px;
    color: #64748b;
    margin-top: 5px;
}

.panel {
    background: white;
    border-radius: 14px;
    padding: 27px;
    margin-bottom: 25px;
    box-shadow: 0 3px 15px #00000008;
}

.section-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
    margin-bottom: 25px;
}

.section-heading h2 {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 19px;
}

.section-heading h2 svg {
    color: #168bc1;
}

.section-heading p {
    color: #64748b;
    font-size: 12px;
    margin-top: 7px;
}

.badge {
    background: #e0f2fe;
    color: #0369a1;
    padding: 7px 11px;
    border-radius: 20px;
    font-size: 10px;
    font-weight: 700;
    white-space: nowrap;
}

.success-badge {
    background: #dcfce7;
    color: #15803d;
}

.progress-info {
    display: flex;
    justify-content: space-between;
    color: #64748b;
    font-size: 12px;
    margin-bottom: 9px;
}

.progress-info strong {
    color: #168bc1;
}

.progress-bar {
    width: 100%;
    height: 7px;
    background: #e2e8f0;
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 25px;
}

.progress-fill {
    height: 100%;
    background: #168bc1;
    border-radius: 20px;
    transition: width 0.3s;
}

.racks-grid {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.rack-card {
    padding: 20px;
    border: 1px solid #e2e8f0;
    border-radius: 11px;
}

.rack-heading {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.rack-title {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #168bc1;
}

.rack-title h3 {
    color: #1e293b;
    font-size: 15px;
}

.rack-heading > span {
    font-size: 10px;
    color: #64748b;
    background: #f1f5f9;
    padding: 6px 10px;
    border-radius: 20px;
}

.sensor-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
}

.sensor-field label {
    display: block;
    font-size: 12px;
    color: #64748b;
    margin-bottom: 8px;
}

.input-wrapper {
    display: flex;
    align-items: center;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding-right: 12px;
    transition: border 0.2s;
}

.input-wrapper:focus-within {
    border-color: #168bc1;
    box-shadow: 0 0 0 3px #168bc11a;
}

.input-wrapper input {
    width: 100%;
    min-width: 0;
    border: none;
    outline: none;
    padding: 12px;
    background: transparent;
    color: #1e293b;
    font-size: 15px;
}

.input-wrapper span {
    font-size: 12px;
    color: #64748b;
}

.actions {
    display: flex;
    gap: 12px;
    margin-top: 25px;
    flex-wrap: wrap;
}

.actions button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 9px;
    border: none;
    padding: 13px 19px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 13px;
    cursor: pointer;
    transition: 0.2s;
}

.primary-button {
    background: #168bc1;
    color: white;
}

.primary-button:hover {
    background: #0879a9;
}

.primary-button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.secondary-button {
    background: #f1f5f9;
    color: #475569;
}

.secondary-button:hover {
    background: #e2e8f0;
}

.error-message {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #fee2e2;
    color: #b91c1c;
    padding: 13px;
    border-radius: 8px;
    margin-top: 20px;
    font-size: 13px;
}

.results {
    animation: appear 0.3s ease;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.alert-box, .success-box {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 18px;
    border-radius: 10px;
    margin-bottom: 20px;
}

.alert-box {
    background: #fee2e2;
    color: #b91c1c;
}

.success-box {
    background: #dcfce7;
    color: #166534;
}

.alert-box h3, .success-box h3 {
    font-size: 14px;
    margin-bottom: 5px;
}

.alert-box p, .success-box p {
    font-size: 12px;
}

.critical-card {
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 25px;
}

.critical-card > span {
    font-size: 11px;
    font-weight: 700;
    color: #64748b;
    letter-spacing: 1px;
}

.critical-card h1 {
    color: #0284c7;
    font-size: 38px;
    margin: 12px 0;
}

.critical-card h1.danger {
    color: #dc2626;
}

.critical-card p {
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 13px;
    color: #475569;
}

.result-title {
    font-size: 16px;
    margin: 25px 0 15px;
}

.mean-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}

.mean-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 17px;
}

.mean-card span {
    font-size: 11px;
    color: #64748b;
    font-weight: 700;
}

.mean-card h2 {
    font-size: 22px;
    margin: 12px 0;
}

.mean-bar {
    height: 7px;
    background: #e2e8f0;
    border-radius: 20px;
    overflow: hidden;
}

.mean-bar div {
    height: 100%;
    background: #168bc1;
    border-radius: 20px;
}

.table-container {
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
    text-align: center;
}

th, td {
    padding: 15px;
    border-bottom: 1px solid #e2e8f0;
    font-size: 13px;
}

th {
    background: #101d32;
    color: white;
}

.hot-cell {
    color: #dc2626;
    font-weight: 800;
    background: #fee2e2;
}

footer {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 25px;
    color: #64748b;
    font-size: 11px;
}

@media (max-width: 650px) {
    .header {
        padding: 25px 20px;
    }

    .container {
        padding: 0 12px;
        margin-top: 18px;
    }

    .stats-grid {
        gap: 8px;
    }

    .stat-card {
        padding: 13px 8px;
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }

    .stat-card h2 {
        font-size: 19px;
    }

    .stat-card p {
        font-size: 10px;
    }

    .stat-icon {
        width: 35px;
        height: 35px;
    }

    .panel {
        padding: 17px;
    }

    .sensor-grid {
        gap: 8px;
    }

    .input-wrapper input {
        padding: 10px 5px;
        font-size: 13px;
    }

    .mean-grid {
        grid-template-columns: 1fr;
    }

    .section-heading {
        align-items: flex-start;
    }

    .header-title {
        margin-top: 30px;
    }

    .header-title p {
        line-height: 1.6;
    }
}

@media (max-width: 380px) {
    .section-heading h2 {
        font-size: 15px;
    }

    .badge {
        font-size: 9px;
        padding: 6px;
    }

    .actions button {
        width: 100%;
    }
}
