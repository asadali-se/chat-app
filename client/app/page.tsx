import Link from "next/link";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export default function Home() {
  return (
    <div className="min-h-screen bg-white dark:bg-black">
      {/* Header matching the auth layout header */}
      <div className="bg-black dark:bg-white h-16 flex items-center justify-center shadow-md">
        <h1 className="text-white dark:text-black text-3xl font-bold tracking-tight">
          ChatApp
        </h1>
      </div>

      {/* Centered content */}
      <div className="flex items-center justify-center min-h-[calc(100vh-4rem)] p-4">
        <Card className="w-full max-w-md text-center">
          <CardHeader className="space-y-3">
            <CardTitle className="text-3xl font-bold text-black dark:text-white">
              Welcome to ChatApp
            </CardTitle>
            <CardDescription className="text-gray-600 dark:text-gray-400 text-lg">
              Real‑time messaging, simple and fast.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <Link href="/login" className="block">
              <Button
                className="w-full bg-black hover:bg-gray-800 dark:bg-white dark:text-black dark:hover:bg-gray-200 font-semibold text-lg py-6"
                size="lg"
              >
                Get Started → Login
              </Button>
            </Link>
            <p className="text-gray-500 dark:text-gray-400 text-sm">
              Don’t have an account?{" "}
              <Link
                href="/register"
                className="text-black dark:text-white font-medium underline"
              >
                Sign up
              </Link>
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
