import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000',
});

export const getKpiDefinitions = () => api.get('/kpis/definitions').then(res => res.data);
export const getKpiTimeseries = (key: string) => api.get(`/kpis/${key}/timeseries`).then(res => res.data);
export const triggerSync = (provider: string) => api.post(`/ingest/pull/${provider}`).then(res => res.data);
export const computeKpis = () => api.post('/kpis/compute').then(res => res.data);
export const getIntegrations = () => api.get('/integrations/').then(res => res.data);
export const getAlertEvents = () => api.get('/alerts/events').then(res => res.data);
export const getEvents = (source?: string) => api.get('/ingest/events', { params: { source } }).then(res => res.data);

export default api;
