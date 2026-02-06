import React, { useState, useEffect } from 'react';
import { getIntegrations, triggerSync } from '../api/client';
import { Power, RefreshCcw, CheckCircle, XCircle } from 'lucide-react';

const Integrations: React.FC = () => {
    const [integrations, setIntegrations] = useState<any[]>([]);
    const [loading, setLoading] = useState<Record<string, boolean>>({});

    useEffect(() => {
        loadIntegrations();
    }, []);

    const loadIntegrations = async () => {
        const data = await getIntegrations();
        setIntegrations(data);
    };

    const handleSync = async (provider: string) => {
        setLoading(prev => ({ ...prev, [provider]: true }));
        try {
            await triggerSync(provider);
            await loadIntegrations();
        } finally {
            setLoading(prev => ({ ...prev, [provider]: false }));
        }
    };

    const providers = [
        { id: 'stripe', name: 'Stripe', icon: '💳', desc: 'Revenue & Payments' },
        { id: 'ga4', name: 'Google Analytics 4', icon: '📊', desc: 'Traffic & Conversion' },
        { id: 'hubspot', name: 'HubSpot', icon: '🤝', desc: 'Sales & CRM' },
    ];

    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold text-gray-900 tracking-tight">Integrations</h1>
                <p className="text-gray-500 mt-1">Connect your data sources to start monitoring KPIs</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {providers.map((p) => {
                    const connected = integrations.find(i => i.provider === p.id && i.is_active);
                    return (
                        <div key={p.id} className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-all">
                            <div className="flex justify-between items-start">
                                <span className="text-4xl">{p.icon}</span>
                                <span className={`px-2 py-1 rounded-full text-xs font-semibold ${connected ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-400'}`}>
                                    {connected ? 'Connected' : 'Disconnected'}
                                </span>
                            </div>
                            <h3 className="mt-4 text-xl font-bold text-gray-900">{p.name}</h3>
                            <p className="mt-1 text-sm text-gray-500">{p.desc}</p>

                            <div className="mt-6 flex gap-3">
                                {connected ? (
                                    <button
                                        onClick={() => handleSync(p.id)}
                                        disabled={loading[p.id]}
                                        className="flex-1 bg-gray-50 text-gray-700 px-4 py-2 rounded-lg font-medium hover:bg-gray-100 transition flex items-center justify-center gap-2"
                                    >
                                        <RefreshCcw size={16} className={loading[p.id] ? 'animate-spin' : ''} />
                                        Sync Now
                                    </button>
                                ) : (
                                    <button
                                        className="flex-1 bg-indigo-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-indigo-700 transition"
                                    >
                                        Connect
                                    </button>
                                )}
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
};

export default Integrations;
