
# TrebolSoft (MVP)

Stack:
- Backend: FastAPI (Python)
- DB/Auth/Storage: Supabase (PostgreSQL)
- Hosting API: Render
- App móvil: React Native (Expo, TypeScript)
- Mapas: Mapbox

## Requisitos
- Python 3.11+
- Node.js 18+
- Docker (opcional para dev)
- Cuenta en Supabase y Render

## Variables de entorno
Copia `.env.example` a `.env` dentro de `api/` y `app/` ajustando valores.

### API (`api/.env`)
```env
ENV=dev
API_V1_STR=/api/v1
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:PORT/DB
SUPABASE_PROJECT_URL=https://mogxabnsjjcqapqcdtxp.supabase.co
SUPABASE_JWKS_URL=https://mogxabnsjjcqapqcdtxp.supabase.co/auth/v1/keys
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1vZ3hhYm5zampjcWFwY3FkdHhwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MDUzNjAwOCwiZXhwIjoyMDc2MTEyMDA4fQ.UaA4jhGbqhURDXBWhyRH2wgs-p3ItsbvNkmrVMdzS6w
CORS_ORIGINS=http://localhost:8081,https://app.trebolsoft.com
MAPBOX_TOKEN=pk.eyJ1IjoidHJlYm9sc29mdCIsImEiOiJjbWdzNG50Y2QwYnMzMmxvam84dXB6ZTdoIn0.voaAD-TqnriYg0vyL768og
```

### APP (`app/.env`)
```env
EXPO_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1
EXPO_PUBLIC_SUPABASE_URL=https://<project>.supabase.co
EXPO_PUBLIC_SUPABASE_ANON_KEY=CHANGE_ME
EXPO_PUBLIC_MAPBOX_TOKEN=CHANGE_ME
```

## Desarrollo local (opción Docker)
```bash
docker compose up --build
```
- API: http://localhost:8000
- Swagger: http://localhost:8000/docs

## Desarrollo móvil
```bash
cd app
npm i
npx expo start
```

## Despliegue a Render (API)
- Usa `infra/render/render.yaml` o crea un Web Service y configura `Build Command` y `Start Command`:
  - Build: `pip install -r api/requirements.txt && alembic -c api/alembic.ini upgrade head`
  - Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## Supabase
- Crea proyecto, habilita Storage y Auth.
- Ejecuta `infra/supabase/init.sql` en el SQL editor para crear tablas iniciales.

## Licencia
Propietario: TrebolSoft.

