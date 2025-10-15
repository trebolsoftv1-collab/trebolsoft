
create extension if not exists pgcrypto;

CREATE TABLE if not exists customers (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  full_name text NOT NULL,
  document text,
  phone text,
  status text NOT NULL DEFAULT 'activo',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  deleted_at timestamptz
);

CREATE TABLE if not exists addresses (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  customer_id uuid NOT NULL REFERENCES customers(id),
  address_line text,
  lat decimal(10,6),
  lng decimal(10,6),
  zone text,
  primary boolean DEFAULT false
);

CREATE TABLE if not exists loans (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  customer_id uuid NOT NULL REFERENCES customers(id),
  principal numeric(14,2) NOT NULL,
  rate_daily numeric(6,4) NOT NULL,
  insurance numeric(14,2) DEFAULT 0,
  term_days int NOT NULL,
  start_date date NOT NULL,
  status text NOT NULL DEFAULT 'vigente',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  deleted_at timestamptz
);

CREATE TABLE if not exists schedules (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  loan_id uuid NOT NULL REFERENCES loans(id),
  due_date date NOT NULL,
  amount_due numeric(14,2) NOT NULL,
  paid boolean DEFAULT false
);

CREATE TABLE if not exists payments (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  loan_id uuid NOT NULL REFERENCES loans(id),
  schedule_id uuid REFERENCES schedules(id),
  collector_id uuid,
  pay_date timestamptz NOT NULL DEFAULT now(),
  amount_paid numeric(14,2) NOT NULL,
  method text,
  receipt_number text,
  metadata jsonb
);

CREATE TABLE if not exists routes (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text,
  zone text,
  date date,
  status text DEFAULT 'planificada'
);

CREATE TABLE if not exists route_stops (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  route_id uuid NOT NULL REFERENCES routes(id),
  customer_id uuid NOT NULL REFERENCES customers(id),
  sequence int,
  planned_lat decimal(10,6),
  planned_lng decimal(10,6),
  notes text,
  visited boolean DEFAULT false,
  visited_at timestamptz
);

CREATE TABLE if not exists assignments (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  route_id uuid NOT NULL REFERENCES routes(id),
  user_id uuid NOT NULL,
  assigned_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE if not exists cash_sessions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL,
  opened_at timestamptz NOT NULL DEFAULT now(),
  closed_at timestamptz,
  opening_cash numeric(14,2),
  closing_cash numeric(14,2),
  difference numeric(14,2)
);

CREATE TABLE if not exists audit_logs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity text NOT NULL,
  entity_id uuid NOT NULL,
  action text NOT NULL,
  user_id uuid,
  at timestamptz NOT NULL DEFAULT now(),
  before jsonb,
  after jsonb
);
