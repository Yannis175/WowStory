/* 单词故事本 · PWA Service Worker 离线缓存系统 */
const CACHE_NAME = 'wowstory-cache-v1';

// 初次安装预缓存的核心应用文件
const PRECACHE_ASSETS = [
  './',
  './index.html',
  './_app.js',
  './_units_manifest.js',
  './manifest.json',
  // 预缓存 26 个单元 HTML
  ...Array.from({ length: 26 }, (_, i) => `./Unit${String(i + 1).padStart(2, '0')}.html`)
];

// 1. 安装 (Install)：预缓存核心静态代码
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] 预缓存核心静态代码资源');
      return cache.addAll(PRECACHE_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// 2. 激活 (Activate)：清理旧版本的 Cache
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[ServiceWorker] 正在清除旧缓存:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// 3. 拦截请求 (Fetch)：网络优先 -> 本地 Cache 降级 (静态资源优先 Cache)
self.addEventListener('fetch', (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // 不拦截非 GET 请求或 API 请求
  if (request.method !== 'GET' || url.pathname.startsWith('/api/')) {
    return;
  }

  // 资源拦截策略：Cache 第一，Network 降级，同时自动更新 Cache
  event.respondWith(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.match(request).then((cachedResponse) => {
        // 网络请求（后台拉取最新版）
        const fetchPromise = fetch(request).then((networkResponse) => {
          // 仅在成功响应时写入缓存
          if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
            cache.put(request, networkResponse.clone());
          }
          return networkResponse;
        }).catch((err) => {
          console.log('[ServiceWorker] 网络不可用，使用纯离线模式:', err);
          return cachedResponse;
        });

        // 如果本地缓存已有该资源（如 HTML、JS、音频），则直接返回缓存（实现秒开和离线运行）
        // 否则等待网络请求
        return cachedResponse || fetchPromise;
      });
    })
  );
});
