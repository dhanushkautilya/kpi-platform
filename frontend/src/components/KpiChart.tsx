import React from 'react';
import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

interface KpiChartProps {
    data: any[];
    title: string;
}

const KpiChart: React.FC<KpiChartProps> = ({ data, title }) => {
    return (
        <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm h-80">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">{title}</h3>
            <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={data}>
                    <defs>
                        <linearGradient id="colorValue" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor="#6366f1" stopOpacity={0.1} />
                            <stop offset="95%" stopColor="#6366f1" stopOpacity={0} />
                        </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f3f4f6" />
                    <XAxis
                        dataKey="timestamp"
                        tickFormatter={(str) => new Date(str).toLocaleDateString()}
                        tick={{ fontSize: 12, fill: '#9ca3af' }}
                        axisLine={false}
                        tickLine={false}
                    />
                    <YAxis
                        tick={{ fontSize: 12, fill: '#9ca3af' }}
                        axisLine={false}
                        tickLine={false}
                    />
                    <Tooltip
                        contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }}
                        labelFormatter={(label) => new Date(label).toLocaleString()}
                    />
                    <Area
                        type="monotone"
                        dataKey="value"
                        stroke="#6366f1"
                        strokeWidth={3}
                        fillOpacity={1}
                        fill="url(#colorValue)"
                    />
                </AreaChart>
            </ResponsiveContainer>
        </div>
    );
};

export default KpiChart;
