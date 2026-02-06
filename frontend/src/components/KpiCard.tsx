import React from 'react';

interface KpiCardProps {
    title: string;
    value: string | number;
    description?: string;
    trend?: {
        value: number;
        isUp: boolean;
    };
}

const KpiCard: React.FC<KpiCardProps> = ({ title, value, description, trend }) => {
    return (
        <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
            <h3 className="text-sm font-medium text-gray-500 uppercase tracking-wider">{title}</h3>
            <div className="mt-2 flex items-baseline">
                <span className="text-3xl font-bold text-gray-900">{value}</span>
                {trend && (
                    <span className={`ml-2 text-sm font-semibold ${trend.isUp ? 'text-green-600' : 'text-red-600'}`}>
                        {trend.isUp ? '↑' : '↓'} {trend.value}%
                    </span>
                )}
            </div>
            {description && <p className="mt-1 text-sm text-gray-500">{description}</p>}
        </div>
    );
};

export default KpiCard;
