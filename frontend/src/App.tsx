import React, { useState } from 'react';
import Dashboard from './pages/Dashboard';
import Integrations from './pages/Integrations';
import Events from './pages/Events';
import { LayoutDashboard, Link, Activity, Bell, Menu, X } from 'lucide-react';

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'dashboard' | 'integrations' | 'events'>('dashboard');
  const [isSidebarOpen, setSidebarOpen] = useState(true);

  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'integrations', label: 'Integrations', icon: Link },
    { id: 'events', label: 'Events Feed', icon: Activity },
  ];

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {/* Sidebar */}
      <div className={`fixed inset-y-0 left-0 z-50 w-64 bg-white border-r border-gray-100 transform transition-transform ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'} lg:relative lg:translate-x-0`}>
        <div className="h-full flex flex-col p-6">
          <div className="flex items-center gap-3 mb-10">
            <div className="w-10 h-10 bg-indigo-600 rounded-xl flex items-center justify-center text-white font-bold text-xl">
              G
            </div>
            <span className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-indigo-600 to-purple-600">
              GrownIntelligence
            </span>
          </div>

          <nav className="flex-1 space-y-2">
            {navItems.map((item) => (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id as any)}
                className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-medium transition-all ${activeTab === item.id
                    ? 'bg-indigo-50 text-indigo-600 shadow-sm'
                    : 'text-gray-500 hover:bg-gray-50 hover:text-gray-900'
                  }`}
              >
                <item.icon size={20} />
                {item.label}
              </button>
            ))}
          </nav>

          <div className="mt-auto p-4 bg-indigo-600 rounded-2xl text-white">
            <h4 className="font-bold">Next Pro</h4>
            <p className="text-xs text-indigo-100 mt-1">Upgrade for advanced AI alerts</p>
            <button className="mt-3 w-full bg-white text-indigo-600 py-2 rounded-lg text-sm font-bold hover:bg-indigo-50 transition">
              Upgrade
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col">
        <header className="h-16 bg-white border-b border-gray-100 flex items-center justify-between px-8">
          <button onClick={() => setSidebarOpen(!isSidebarOpen)} className="lg:hidden text-gray-500">
            <Menu size={24} />
          </button>
          <div className="flex items-center gap-4 ml-auto">
            <button className="p-2 text-gray-400 hover:text-gray-600 transition">
              <Bell size={20} />
            </button>
            <div className="w-8 h-8 rounded-full bg-gray-200 border border-gray-300"></div>
          </div>
        </header>

        <main className="p-8 max-w-7xl mx-auto w-full">
          {activeTab === 'dashboard' && <Dashboard />}
          {activeTab === 'integrations' && <Integrations />}
          {activeTab === 'events' && <Events />}
        </main>
      </div>
    </div>
  );
};

export default App;
