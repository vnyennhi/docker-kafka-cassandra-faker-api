USE kafkapipeline;
CREATE TABLE IF NOT EXISTS fakerdata (
  name TEXT,
  address TEXT,
  year INT,
  PRIMARY KEY (name, address)
);