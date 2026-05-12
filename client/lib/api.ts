const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export interface User {
    id: number;
    username: string;
    email: string;
    avatar_url: string | null;
    status: string;
    is_online: boolean;
    created_at: string;
}

interface LoginResponse {
    access_token: string;
    refresh_token: string;
    token_type: string;
}

const getToken = (): string | null => {
    if (typeof window !== "undefined") {
        return localStorage.getItem("access_token");
    }
    return null;
};

async function fetchAPI<T>(
    endpoint: string,
    options: RequestInit = {}
): Promise<T> {
    const url = `${API_BASE_URL}${endpoint}`;

    // Create Headers object safely
    const headers = new Headers();

    // Set default content type
    headers.set("Content-Type", "application/json");

    // If there are custom headers in options, add them
    if (options.headers) {
        const customHeaders = new Headers(options.headers);
        customHeaders.forEach((value, key) => {
            headers.set(key, value);
        });
    }

    // Add Authorization header if token exists
    const token = getToken();
    if (token) {
        headers.set("Authorization", `Bearer ${token}`);
    }

    const response = await fetch(url, {
        ...options,
        headers,
    });

    if (!response.ok) {
        const error = await response.json().catch(() => ({}));
        throw new Error(error.detail || `HTTP error ${response.status}`);
    }

    return response.json();
}

export const authAPI = {
    register: (username: string, email: string, password: string): Promise<User> =>
        fetchAPI<User>("/auth/register", {
            method: "POST",
            body: JSON.stringify({ username, email, password }),
        }),

    login: (username: string, password: string): Promise<LoginResponse> =>
        fetchAPI<LoginResponse>("/auth/login", {
            method: "POST",
            body: JSON.stringify({ username, password }),
        }),

    getMe: (): Promise<User> => fetchAPI<User>("/auth/me"),

    logout: (): Promise<{ message: string }> =>
        fetchAPI("/auth/logout", { method: "POST" }),
};

export const setTokens = (accessToken: string, refreshToken: string): void => {
    localStorage.setItem("access_token", accessToken);
    localStorage.setItem("refresh_token", refreshToken);
};

export const clearTokens = (): void => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
};