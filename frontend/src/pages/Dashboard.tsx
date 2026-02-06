import React, { useState, useEffect } from 'react';
import KpiCard from '../components/KpiCard';
import KpiChart from '../components/KpiChart';
import { getKpiDefinitions, getKpiTimeseries, computeKpis } from '../api/client';

const Dashboard: React.FC = () => {
    const [kpis, setKpis] = useState<any[]>([]);
    const [timeseriesData, setTimeseriesData] = useState<Record<string, any[]>>({});

    useEffect(() => {
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const defs = await getKpiDefinitions();
            setKpis(defs);

            const ts: Record<string, any[]> = {};
            for (const kpi of defs) {
                const data = await getKpiTimeseries(kpi.key);
                ts[kpi.key] = data;
            }
            setTimeseriesData(ts);
        } catch (err) {
            console.error(err);
        }
    };

    const handleCompute = async () => {
        await computeKpis();
        loadData();
    };

    return (
        <div className="space-y-8">
            <div className="flex justify-between items-center">
                <div>
                    <h1 className="text-3xl font-bold text-gray-900 tracking-tight">Growth Dashboard</h1>
                    <p className="text-gray-500 mt-1">Real-time monitoring of your business KPIs</p>
                </div>
                <button
                    onClick={handleCompute}
                    className="bg-indigo-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-indigo-700 transition shadow-sm"
                >
                    Re-compute KPIs
                </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                {kpis.map((kpi) => (
                    <KpiCard
                        key={kpi.id}
                        title={kpi.name}
                        value={timeseriesData[kpi.key]?.length > 0 ? timeseriesData[kpi.key][timeseriesData[kpi.key].length - 1].value : "N/A"}
                        description={kpi.description}
                    />
                ))}
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                {kpis.map((kpi) => (
                    <KpiChart
                        key={kpi.id}
                        title={kpi.name}
                        data={timeseriesData[kpi.key] || []}
                    />
                ))}
            </div>
        </div>
    );
};

export default Dashboard;
