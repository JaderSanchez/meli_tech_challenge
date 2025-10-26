-- Setup

CREATE DATABASE meli;
USE meli;

CREATE TABLE customers (
  id SMALLINT PRIMARY KEY,
  first_name VARCHAR(64),
  last_name VARCHAR(64)
);

CREATE TABLE campaigns (
  id SMALLINT PRIMARY KEY,
  customer_id SMALLINT,
  name VARCHAR(64),
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE events (
  dt VARCHAR(19),
  campaign_id SMALLINT,
  status VARCHAR(64),
  FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
);

INSERT INTO customers (id, first_name, last_name) VALUES
(1, 'Whitney', 'Ferrero'),
(2, 'Dickie', 'Romera');

INSERT INTO campaigns (id, customer_id, name) VALUES
(1, 1, 'Upton Group'),
(2, 1, 'Roob, Hudson and Rippin'),
(3, 1, 'Mccullough, Rempel and Larson'),
(4, 1, 'Lang and Sons'),
(5, 2, 'Ruecker, Hand and Haley');

INSERT INTO events (dt, campaign_id, status) VALUES
('2021-12-02 13:52:00', 1, 'failure'),
('2021-12-02 08:17:48', 2, 'failure'),
('2021-12-02 08:18:17', 2, 'failure'),
('2021-12-01 11:55:32', 3, 'failure'),
('2021-12-01 06:53:16', 4, 'failure'),
('2021-12-02 04:51:09', 4, 'failure'),
('2021-12-01 06:34:04', 5, 'failure'),
('2021-12-02 03:21:18', 5, 'failure'),
('2021-12-01 03:18:24', 5, 'failure'),
('2021-12-02 15:32:37', 1, 'success'),
('2021-12-01 04:23:20', 1, 'success'),
('2021-12-02 06:53:24', 1, 'success'),
('2021-12-02 08:01:02', 2, 'success'),
('2021-12-01 15:57:19', 2, 'success'),
('2021-12-02 16:14:34', 3, 'success'),
('2021-12-02 21:56:38', 3, 'success'),
('2021-12-01 05:54:43', 4, 'success'),
('2021-12-02 17:56:45', 4, 'success'),
('2021-12-02 11:56:50', 4, 'success'),
('2021-12-02 06:08:20', 5, 'success');