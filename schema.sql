
CREATE TABLE `categories` (
  category_id     INT NOT NULL AUTO_INCREMENT,
  category_name   VARCHAR(45) NOT NULL UNIQUE,
  PRIMARY KEY (category_id)
);


CREATE TABLE `transactions` (
  transaction_id    INT NOT NULL AUTO_INCREMENT,
  amount            DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
  description       VARCHAR(45) NOT NULL,
  entry_date        DATE NOT NULL,
  type              ENUM('expense', 'income') NOT NULL,
  category_id       INT NOT NULL,
PRIMARY KEY (transaction_id),
FOREIGN KEY (category_id) REFERENCES categories(category_id)
  ON DELETE RESTRICT
);


insert into `categories` (category_id, category_name)
values
  (1, 'Personal'),
  (2, 'Housing'),
  (3, 'Food'),
  (4, 'Transport'),
  (5, 'Subscriptions');
