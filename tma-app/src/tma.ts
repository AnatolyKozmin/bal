export function initializeTelegramWebApp(): void {
  const tg = (window as any)?.Telegram?.WebApp;
  if (!tg) return;
  try {
    tg.expand?.();
    tg.ready?.();
    const bg = tg.themeParams?.bg_color as string | undefined;
    if (bg) {
      document.documentElement.style.backgroundColor = bg;
      document.body.style.backgroundColor = bg;
    }
  } catch {}
}

export function closeTelegramWebApp(): void {
  const tg = (window as any)?.Telegram?.WebApp;
  try { tg?.close?.(); } catch {}
}

export function getTelegramUser(): { id: number | null; username: string | null } {
  const tg = (window as any)?.Telegram?.WebApp;
  const user = tg?.initDataUnsafe?.user;
  return {
    id: user?.id ?? null,
    username: user?.username ?? null,
  };
}


