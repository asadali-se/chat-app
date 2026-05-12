"use client";

import { useEffect, useState } from "react";
import { authAPI, clearTokens, type User } from "@/lib/api";
import { useRouter } from "next/navigation";

export default function ChatPage() {
    const router = useRouter();
    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        authAPI
            .getMe()
            .then((userData) => {
                setUser(userData);
                setLoading(false);
            })
            .catch(() => {
                clearTokens();
                router.push("/login");
            });
    }, [router]);

    const handleLogout = () => {
        clearTokens();
        router.push("/login");
    };

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-white dark:bg-black">
                <div className="text-black dark:text-white">Loading...</div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-white dark:bg-black">
            <div className="bg-black dark:bg-white h-16 flex items-center justify-between px-6 shadow-md">
                <h1 className="text-white dark:text-black text-2xl font-bold">
                    ChatApp
                </h1>
                <button
                    onClick={handleLogout}
                    className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded transition"
                >
                    Logout
                </button>
            </div>
            <div className="p-6">
                <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-100">
                    Welcome, {user?.username}!
                </h2>
                <p className="text-gray-600 dark:text-gray-400 mt-2">
                    Chat interface coming soon...
                </p>
            </div>
        </div>
    );
}
