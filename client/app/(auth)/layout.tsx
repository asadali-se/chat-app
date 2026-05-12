export default function AuthLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <div className="min-h-screen bg-white dark:bg-black">
            {/* Header Bar */}
            <div className="bg-black dark:bg-white h-16 flex items-center justify-center shadow-md">
                <h1 className="text-white dark:text-black text-3xl font-bold tracking-tight">
                    ChatApp
                </h1>
            </div>

            {/* Page Content */}
            <div className="flex items-center justify-center min-h-[calc(100vh-4rem)] p-4">
                {children}
            </div>
        </div>
    );
}
