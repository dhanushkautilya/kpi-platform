import React, { useState, useEffect } from 'react';
import { getEvents } from '../api/client';

const Events: React.FC = () => {
    const [events, setEvents] = useState<any[]>([]);

    useEffect(() => {
        loadEvents();
    }, []);

    const loadEvents = async () => {
        const data = await getEvents();
        setEvents(data);
    };

    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold text-gray-900 tracking-tight">Event Feed</h1>
                <p className="text-gray-500 mt-1">Real-time stream of normalized events from all sources</p>
            </div>

            <div className="bg-white rounded-xl border border-gray-100 shadow-sm overflow-hidden">
                <table className="min-w-full divide-y divide-gray-200">
                    <thead className="bg-gray-50">
                        <tr>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Source</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Timestamp</th>
                        </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                        {events.map((event) => (
                            <tr key={event.id} className="hover:bg-gray-50 transition">
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <span className="text-sm font-medium text-gray-900">{event.event_type}</span>
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <span className={`px-2 py-1 rounded-full text-xs font-semibold ${event.source === 'stripe' ? 'bg-blue-100 text-blue-700' :
                                            event.source === 'ga4' ? 'bg-orange-100 text-orange-700' : 'bg-green-100 text-green-700'
                                        }`}>
                                        {event.source}
                                    </span>
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {event.amount ? `$${event.amount.toFixed(2)}` : '-'}
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {new Date(event.timestamp).toLocaleString()}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default Events;
