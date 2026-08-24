import { registerSW } from 'virtual:pwa-register';

if (typeof window !== 'undefined') {
  registerSW({
    immediate: true,
    onRegistered(r) {
      console.log('SW Registered:', r);
    },
    onRegisterError(error) {
      console.error('SW Registration error', error);
    }
  });
}
