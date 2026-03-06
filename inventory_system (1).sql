-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 06, 2026 at 04:11 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `category` varchar(50) NOT NULL,
  `stock` int(11) DEFAULT 0,
  `min_stock` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `status` enum('Available','Low Stock','Out of Stock') DEFAULT 'Available',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `item_name`, `category`, `stock`, `min_stock`, `price`, `status`, `created_at`) VALUES
(1, 'Kingston 16GB DDR4 3200MHz', 'RAM', 0, 5, 1500.00, 'Available', '2024-01-05 00:30:00'),
(2, 'Corsair Vengeance 8GB DDR4', 'RAM', 30, 8, 900.00, 'Available', '2024-01-12 01:15:00'),
(3, 'G.Skill Ripjaws 32GB DDR4', 'RAM', 15, 5, 2800.00, 'Available', '2024-02-03 02:00:00'),
(4, 'HyperX Fury 16GB DDR5', 'RAM', 20, 5, 3200.00, 'Available', '2024-02-20 03:30:00'),
(5, 'Samsung 8GB DDR4 2666MHz', 'RAM', 40, 10, 850.00, 'Available', '2024-03-08 00:45:00'),
(6, 'Intel Core i3-12100F', 'CPU (Processor)', 18, 5, 5500.00, 'Available', '2024-03-15 01:00:00'),
(7, 'Intel Core i5-12400F', 'CPU (Processor)', 15, 5, 8500.00, 'Available', '2024-04-02 02:30:00'),
(8, 'Intel Core i7-12700K', 'CPU (Processor)', 10, 3, 15000.00, 'Available', '2024-04-18 03:00:00'),
(9, 'AMD Ryzen 5 5600X', 'CPU (Processor)', 12, 5, 9500.00, 'Available', '2024-05-07 00:15:00'),
(10, 'AMD Ryzen 7 5800X', 'CPU (Processor)', 8, 3, 14000.00, 'Available', '2024-05-22 01:45:00'),
(11, 'AMD Ryzen 9 5900X', 'CPU (Processor)', 5, 2, 22000.00, 'Available', '2024-06-10 02:00:00'),
(12, 'Intel Core i9-12900K', 'CPU (Processor)', 1, 2, 28000.00, 'Available', '2024-06-25 03:30:00'),
(13, 'NVIDIA GTX 1650 4GB', 'GPU (Graphics Card)', 10, 3, 8000.00, 'Available', '2024-07-03 00:30:00'),
(14, 'NVIDIA RTX 3060 12GB', 'GPU (Graphics Card)', 8, 3, 18000.00, 'Available', '2024-07-19 01:00:00'),
(15, 'NVIDIA RTX 3070 8GB', 'GPU (Graphics Card)', 5, 2, 28000.00, 'Available', '2024-08-05 02:15:00'),
(16, 'AMD RX 6600 8GB', 'GPU (Graphics Card)', 7, 3, 15000.00, 'Available', '2024-08-21 03:00:00'),
(17, 'AMD RX 6700 XT 12GB', 'GPU (Graphics Card)', 4, 2, 25000.00, 'Available', '2024-09-09 00:45:00'),
(18, 'NVIDIA RTX 4060 8GB', 'GPU (Graphics Card)', 6, 2, 22000.00, 'Available', '2024-09-24 01:30:00'),
(19, 'Seagate 1TB HDD 7200RPM', 'Storage (SSD/HDD)', 30, 8, 1800.00, 'Available', '2024-10-01 00:00:00'),
(20, 'Western Digital 2TB HDD', 'Storage (SSD/HDD)', 25, 8, 2500.00, 'Available', '2024-10-14 01:15:00'),
(21, 'Samsung 970 EVO 500GB NVMe', 'Storage (SSD/HDD)', 20, 5, 3500.00, 'Available', '2024-10-28 02:30:00'),
(22, 'Kingston A2000 1TB NVMe', 'Storage (SSD/HDD)', 15, 5, 4500.00, 'Available', '2024-11-06 03:00:00'),
(23, 'Crucial MX500 500GB SSD', 'Storage (SSD/HDD)', 22, 5, 2800.00, 'Available', '2024-11-19 00:30:00'),
(24, 'WD Blue 1TB SSD', 'Storage (SSD/HDD)', 18, 5, 3800.00, 'Available', '2024-12-02 01:00:00'),
(25, 'Seagate Barracuda 4TB HDD', 'Storage (SSD/HDD)', 10, 3, 4200.00, 'Available', '2024-12-16 02:15:00'),
(26, 'ASUS Prime B550M-A', 'Motherboard', 12, 3, 5500.00, 'Available', '2024-12-20 03:30:00'),
(27, 'MSI B450 Tomahawk MAX', 'Motherboard', 10, 3, 6000.00, 'Available', '2025-01-08 00:00:00'),
(28, 'Gigabyte B660M DS3H', 'Motherboard', 8, 3, 5800.00, 'Available', '2025-01-20 01:15:00'),
(29, 'ASRock B550M Pro4', 'Motherboard', 9, 3, 5200.00, 'Available', '2025-02-03 02:00:00'),
(30, 'ASUS ROG Strix B550-F', 'Motherboard', 6, 2, 9500.00, 'Available', '2025-02-17 03:30:00'),
(31, 'Corsair CV550 550W 80+', 'Power Supply', 15, 5, 2800.00, 'Available', '2025-03-01 00:30:00'),
(32, 'Seasonic Focus GX-650W', 'Power Supply', 12, 4, 4500.00, 'Available', '2025-03-14 01:00:00'),
(33, 'EVGA 600W 80+ Bronze', 'Power Supply', 18, 5, 2500.00, 'Available', '2025-04-02 02:15:00'),
(34, 'Cooler Master MWE 750W', 'Power Supply', 10, 3, 3800.00, 'Available', '2025-04-18 03:00:00'),
(35, 'Thermaltake Smart 500W', 'Power Supply', 20, 5, 2200.00, 'Available', '2025-05-05 00:45:00'),
(36, 'Logitech MK270 Keyboard+Mouse', 'Accessories', 25, 8, 1200.00, 'Available', '2025-05-20 01:30:00'),
(37, 'Redragon K552 Mech Keyboard', 'Accessories', 15, 5, 2500.00, 'Available', '2025-06-03 02:00:00'),
(38, 'Logitech G502 Gaming Mouse', 'Accessories', 20, 5, 3200.00, 'Available', '2025-06-17 03:15:00'),
(39, 'Generic USB Hub 4-Port', 'Accessories', 35, 10, 350.00, 'Available', '2025-07-01 00:00:00'),
(40, 'HDMI Cable 1.8m', 'Accessories', 50, 15, 250.00, 'Available', '2025-07-15 01:30:00'),
(41, 'DisplayPort Cable 2m', 'Accessories', 30, 10, 350.00, 'Available', '2025-08-02 02:00:00'),
(42, 'Thermal Paste Arctic MX-4', 'Accessories', 40, 10, 280.00, 'Available', '2025-08-18 03:30:00'),
(43, 'Cable Ties Pack 100pcs', 'Accessories', 60, 20, 120.00, 'Available', '2025-09-05 00:15:00'),
(44, 'Cooler Master Hyper 212', 'Accessories', 12, 4, 1800.00, 'Available', '2025-09-19 01:00:00'),
(45, 'DeepCool GAMMAXX 400', 'Accessories', 10, 3, 1500.00, 'Available', '2025-10-07 02:30:00'),
(46, 'Noctua NH-U12S CPU Cooler', 'Accessories', 6, 2, 4500.00, 'Available', '2025-10-21 03:00:00'),
(47, 'Tecware Nexus M MicroATX', 'Accessories', 8, 3, 2200.00, 'Available', '2025-11-04 00:30:00'),
(48, 'Phanteks P300A Mesh', 'Accessories', 3, 2, 3500.00, 'Available', '2025-11-18 01:15:00'),
(49, 'NZXT H510 Mid Tower', 'Accessories', 5, 2, 5500.00, 'Available', '2025-12-02 02:00:00'),
(50, 'Cooler Master MB311L', 'Accessories', 7, 2, 2800.00, 'Available', '2025-12-16 03:30:00'),
(51, 'Intel core i5', 'RAM (Memory)', 9, 5, 150.00, 'Available', '2026-03-02 07:47:46'),
(52, 'core i 5', 'CPU (Processor)', 15, 10, 500.00, 'Available', '2026-03-06 10:48:57');

-- --------------------------------------------------------

--
-- Table structure for table `stock_logs`
--

CREATE TABLE `stock_logs` (
  `log_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `movement_type` enum('IN','OUT') NOT NULL,
  `reason` text DEFAULT NULL,
  `notes` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stock_logs`
--

INSERT INTO `stock_logs` (`log_id`, `product_id`, `user_id`, `quantity`, `movement_type`, `reason`, `notes`, `created_at`) VALUES
(1, 50, 2, 10, 'IN', 'Stocking more', '', '2026-02-27 13:45:49'),
(2, 1, 2, 20, 'IN', 'Stocking more', 'Initial restock', '2024-01-06 01:15:00'),
(3, 2, 2, 15, 'IN', 'Stocking more', 'Initial restock', '2024-01-06 01:30:00'),
(4, 3, 2, 10, 'IN', 'Stocking more', 'Initial restock', '2024-01-06 01:45:00'),
(5, 4, 2, 5, 'OUT', 'Sold', 'Sold to customer', '2024-01-10 02:00:00'),
(6, 5, 2, 8, 'OUT', 'Sold', 'Bulk order', '2024-01-15 03:00:00'),
(7, 6, 2, 3, 'OUT', 'Sold', 'Walk-in customer', '2024-01-20 06:00:00'),
(8, 7, 2, 10, 'IN', 'Stocking more', 'Supplier delivery', '2024-02-03 00:30:00'),
(9, 8, 2, 12, 'IN', 'Stocking more', 'Supplier delivery', '2024-02-03 00:45:00'),
(10, 9, 2, 5, 'OUT', 'Sold', 'Online order', '2024-02-10 02:30:00'),
(11, 10, 2, 3, 'OUT', 'Sold', 'Walk-in customer', '2024-02-14 05:00:00'),
(12, 11, 2, 8, 'IN', 'Stocking more', 'Restock', '2024-02-20 01:00:00'),
(13, 12, 2, 2, 'OUT', 'Damaged', 'Defective unit returned', '2024-02-25 07:00:00'),
(14, 1, 2, 10, 'IN', 'Stocking more', 'Monthly restock', '2024-03-01 00:00:00'),
(15, 13, 2, 5, 'OUT', 'Sold', 'Corporate client', '2024-03-05 02:00:00'),
(16, 14, 2, 3, 'OUT', 'Sold', 'Walk-in customer', '2024-03-10 03:30:00'),
(17, 15, 2, 15, 'IN', 'Stocking more', 'Supplier delivery', '2024-03-15 01:00:00'),
(18, 16, 2, 4, 'OUT', 'Sold', 'Online order', '2024-03-20 06:00:00'),
(19, 17, 2, 2, 'OUT', 'Used for Repair', 'Service repair job', '2024-03-25 08:00:00'),
(20, 2, 2, 20, 'IN', 'Stocking more', 'Bulk purchase', '2024-04-02 00:30:00'),
(21, 3, 2, 8, 'OUT', 'Sold', 'Walk-in customer', '2024-04-08 02:00:00'),
(22, 18, 2, 10, 'IN', 'Stocking more', 'Supplier delivery', '2024-04-10 01:00:00'),
(23, 19, 2, 5, 'OUT', 'Sold', 'Online order', '2024-04-15 05:00:00'),
(24, 20, 2, 3, 'OUT', 'Damaged', 'Dropped during delivery', '2024-04-20 06:30:00'),
(25, 21, 2, 12, 'IN', 'Stocking more', 'Restock', '2024-04-25 00:00:00'),
(26, 22, 2, 6, 'OUT', 'Sold', 'Corporate client', '2024-05-03 02:00:00'),
(27, 23, 2, 15, 'IN', 'Stocking more', 'Supplier delivery', '2024-05-07 01:00:00'),
(28, 24, 2, 4, 'OUT', 'Sold', 'Walk-in customer', '2024-05-12 03:30:00'),
(29, 25, 2, 2, 'OUT', 'Defective/RMA', 'RMA return to supplier', '2024-05-18 06:00:00'),
(30, 26, 2, 10, 'IN', 'Stocking more', 'Restock', '2024-05-22 00:30:00'),
(31, 5, 2, 5, 'OUT', 'Sold', 'Online order', '2024-05-28 07:00:00'),
(32, 27, 2, 8, 'IN', 'Stocking more', 'Supplier delivery', '2024-06-04 01:00:00'),
(33, 28, 2, 3, 'OUT', 'Sold', 'Walk-in customer', '2024-06-10 02:30:00'),
(34, 29, 2, 10, 'IN', 'Stocking more', 'Monthly restock', '2024-06-15 00:00:00'),
(35, 30, 2, 5, 'OUT', 'Sold', 'Corporate client', '2024-06-20 05:00:00'),
(36, 6, 2, 4, 'OUT', 'Sold', 'Online order', '2024-06-25 06:00:00'),
(37, 31, 2, 20, 'IN', 'Stocking more', 'Bulk purchase', '2024-07-02 00:00:00'),
(38, 32, 2, 6, 'OUT', 'Sold', 'Walk-in customer', '2024-07-08 02:00:00'),
(39, 33, 2, 3, 'OUT', 'Damaged', 'Damaged in storage', '2024-07-12 06:00:00'),
(40, 34, 2, 15, 'IN', 'Stocking more', 'Supplier delivery', '2024-07-18 01:00:00'),
(41, 7, 2, 5, 'OUT', 'Sold', 'Online order', '2024-07-25 03:00:00'),
(42, 35, 2, 10, 'IN', 'Stocking more', 'Monthly restock', '2024-08-05 00:30:00'),
(43, 36, 2, 4, 'OUT', 'Sold', 'Walk-in customer', '2024-08-10 02:00:00'),
(44, 37, 2, 8, 'IN', 'Stocking more', 'Supplier delivery', '2024-08-15 01:00:00'),
(45, 38, 2, 3, 'OUT', 'Sold', 'Corporate client', '2024-08-20 05:30:00'),
(46, 8, 2, 10, 'IN', 'Stocking more', 'Restock', '2024-08-28 00:00:00'),
(47, 39, 2, 5, 'OUT', 'Sold', 'Online order', '2024-09-03 02:00:00'),
(48, 40, 2, 12, 'IN', 'Stocking more', 'Supplier delivery', '2024-09-08 01:00:00'),
(49, 41, 2, 4, 'OUT', 'Sold', 'Walk-in customer', '2024-09-14 03:00:00'),
(50, 42, 2, 2, 'OUT', 'Defective/RMA', 'RMA return', '2024-09-20 06:00:00'),
(51, 9, 2, 8, 'IN', 'Stocking more', 'Monthly restock', '2024-09-25 00:30:00'),
(52, 43, 2, 10, 'IN', 'Stocking more', 'Bulk purchase', '2024-10-02 00:00:00'),
(53, 44, 2, 5, 'OUT', 'Sold', 'Corporate client', '2024-10-08 02:30:00'),
(54, 45, 2, 3, 'OUT', 'Sold', 'Walk-in customer', '2024-10-15 03:00:00'),
(55, 10, 2, 6, 'IN', 'Stocking more', 'Supplier delivery', '2024-10-20 01:00:00'),
(56, 46, 2, 4, 'OUT', 'Sold', 'Online order', '2024-10-28 06:00:00'),
(57, 47, 2, 8, 'IN', 'Stocking more', 'Monthly restock', '2024-11-04 00:30:00'),
(58, 48, 2, 3, 'OUT', 'Sold', 'Walk-in customer', '2024-11-10 02:00:00'),
(59, 49, 2, 10, 'IN', 'Stocking more', 'Supplier delivery', '2024-11-15 01:00:00'),
(60, 50, 2, 2, 'OUT', 'Damaged', 'Damaged in transit', '2024-11-20 05:00:00'),
(61, 11, 2, 5, 'OUT', 'Sold', 'Online order', '2024-11-25 07:00:00'),
(62, 1, 2, 15, 'IN', 'Stocking more', 'Year-end restock', '2024-12-02 00:00:00'),
(63, 2, 2, 8, 'OUT', 'Sold', 'Christmas season sale', '2024-12-10 02:00:00'),
(64, 3, 2, 10, 'OUT', 'Sold', 'Christmas season sale', '2024-12-15 03:30:00'),
(65, 12, 2, 20, 'IN', 'Stocking more', 'Year-end restock', '2024-12-18 01:00:00'),
(66, 4, 2, 5, 'OUT', 'Sold', 'New Year sale', '2024-12-28 06:00:00'),
(67, 13, 2, 10, 'IN', 'Stocking more', 'New year restock', '2025-01-03 00:00:00'),
(68, 14, 2, 4, 'OUT', 'Sold', 'Walk-in customer', '2025-01-08 02:30:00'),
(69, 15, 2, 12, 'IN', 'Stocking more', 'Supplier delivery', '2025-01-14 01:00:00'),
(70, 5, 2, 3, 'OUT', 'Sold', 'Online order', '2025-01-20 05:00:00'),
(71, 16, 2, 5, 'OUT', 'Sold', 'Corporate client', '2025-01-28 07:00:00'),
(72, 17, 2, 8, 'IN', 'Stocking more', 'Supplier delivery', '2025-02-04 00:30:00'),
(73, 18, 2, 4, 'OUT', 'Sold', 'Walk-in customer', '2025-02-10 02:00:00'),
(74, 19, 2, 10, 'IN', 'Stocking more', 'Monthly restock', '2025-02-14 01:00:00'),
(75, 20, 2, 3, 'OUT', 'Damaged', 'Defective unit', '2025-02-20 06:00:00'),
(76, 6, 2, 6, 'OUT', 'Sold', 'Online order', '2025-02-25 03:00:00'),
(77, 21, 2, 15, 'IN', 'Stocking more', 'Supplier delivery', '2025-03-03 00:00:00'),
(78, 22, 2, 5, 'OUT', 'Sold', 'Walk-in customer', '2025-03-08 02:30:00'),
(79, 23, 2, 3, 'OUT', 'Sold', 'Corporate client', '2025-03-14 05:00:00'),
(80, 7, 2, 8, 'IN', 'Stocking more', 'Restock', '2025-03-20 01:00:00'),
(81, 24, 2, 4, 'OUT', 'Sold', 'Online order', '2025-03-27 06:00:00'),
(82, 25, 2, 10, 'IN', 'Stocking more', 'Supplier delivery', '2025-04-02 00:30:00'),
(83, 26, 2, 3, 'OUT', 'Sold', 'Walk-in customer', '2025-04-08 02:00:00'),
(84, 27, 2, 5, 'OUT', 'Sold', 'Online order', '2025-04-14 05:30:00'),
(85, 8, 2, 12, 'IN', 'Stocking more', 'Monthly restock', '2025-04-20 01:00:00'),
(86, 28, 2, 2, 'OUT', 'Defective/RMA', 'RMA return', '2025-04-28 07:00:00'),
(87, 29, 2, 8, 'IN', 'Stocking more', 'Supplier delivery', '2025-05-05 00:00:00'),
(88, 30, 2, 4, 'OUT', 'Sold', 'Corporate client', '2025-05-12 02:30:00'),
(89, 31, 2, 10, 'IN', 'Stocking more', 'Bulk purchase', '2025-05-18 01:00:00'),
(90, 9, 2, 5, 'OUT', 'Sold', 'Walk-in customer', '2025-05-24 05:00:00'),
(91, 32, 2, 3, 'OUT', 'Sold', 'Online order', '2025-05-30 06:00:00'),
(92, 33, 2, 15, 'IN', 'Stocking more', 'Supplier delivery', '2025-06-04 00:30:00'),
(93, 34, 2, 6, 'OUT', 'Sold', 'Walk-in customer', '2025-06-10 02:00:00'),
(94, 35, 2, 4, 'OUT', 'Sold', 'Corporate client', '2025-06-16 05:00:00'),
(95, 10, 2, 10, 'IN', 'Stocking more', 'Monthly restock', '2025-06-22 01:00:00'),
(96, 36, 2, 5, 'OUT', 'Sold', 'Online order', '2025-06-28 07:00:00'),
(97, 37, 2, 8, 'IN', 'Stocking more', 'Supplier delivery', '2025-07-03 00:00:00'),
(98, 38, 2, 3, 'OUT', 'Sold', 'Walk-in customer', '2025-07-09 02:30:00'),
(99, 39, 2, 10, 'IN', 'Stocking more', 'Bulk purchase', '2025-07-15 01:00:00'),
(100, 11, 2, 4, 'OUT', 'Sold', 'Online order', '2025-07-21 05:00:00'),
(101, 40, 2, 2, 'OUT', 'Damaged', 'Damaged in storage', '2025-07-28 06:00:00'),
(102, 41, 2, 12, 'IN', 'Stocking more', 'Supplier delivery', '2025-08-04 00:30:00'),
(103, 42, 2, 5, 'OUT', 'Sold', 'Corporate client', '2025-08-11 02:00:00'),
(104, 43, 2, 8, 'IN', 'Stocking more', 'Monthly restock', '2025-08-18 01:00:00'),
(105, 12, 2, 4, 'OUT', 'Sold', 'Walk-in customer', '2025-08-25 05:30:00'),
(106, 44, 2, 3, 'OUT', 'Sold', 'Online order', '2025-08-30 07:00:00'),
(107, 45, 2, 10, 'IN', 'Stocking more', 'Supplier delivery', '2025-09-03 00:00:00'),
(108, 46, 2, 4, 'OUT', 'Sold', 'Corporate client', '2025-09-10 02:30:00'),
(109, 47, 2, 6, 'IN', 'Stocking more', 'Restock', '2025-09-16 01:00:00'),
(110, 13, 2, 3, 'OUT', 'Sold', 'Walk-in customer', '2025-09-22 05:00:00'),
(111, 48, 2, 5, 'OUT', 'Sold', 'Online order', '2025-09-28 06:00:00'),
(112, 49, 2, 15, 'IN', 'Stocking more', 'Supplier delivery', '2025-10-04 00:30:00'),
(113, 50, 2, 4, 'OUT', 'Sold', 'Walk-in customer', '2025-10-10 02:00:00'),
(114, 14, 2, 8, 'IN', 'Stocking more', 'Monthly restock', '2025-10-16 01:00:00'),
(115, 1, 2, 3, 'OUT', 'Sold', 'Online order', '2025-10-22 05:30:00'),
(116, 15, 2, 5, 'OUT', 'Sold', 'Corporate client', '2025-10-28 07:00:00'),
(117, 16, 2, 10, 'IN', 'Stocking more', 'Supplier delivery', '2025-11-04 00:00:00'),
(118, 17, 2, 4, 'OUT', 'Sold', 'Walk-in customer', '2025-11-10 02:30:00'),
(119, 18, 2, 12, 'IN', 'Stocking more', 'Bulk purchase', '2025-11-16 01:00:00'),
(120, 2, 2, 6, 'OUT', 'Sold', 'Online order', '2025-11-22 05:00:00'),
(121, 19, 2, 3, 'OUT', 'Sold', 'Corporate client', '2025-11-28 06:00:00'),
(122, 20, 2, 15, 'IN', 'Stocking more', 'Year-end restock', '2025-12-02 00:30:00'),
(123, 3, 2, 8, 'OUT', 'Sold', 'Christmas sale', '2025-12-10 02:00:00'),
(124, 21, 2, 5, 'OUT', 'Sold', 'Christmas sale', '2025-12-15 03:30:00'),
(125, 22, 2, 20, 'IN', 'Stocking more', 'Year-end restock', '2025-12-18 01:00:00'),
(126, 4, 2, 6, 'OUT', 'Sold', 'New Year sale', '2025-12-28 06:00:00'),
(127, 1, 2, 15, 'OUT', 'Sold', '', '2026-02-27 14:04:18'),
(128, 1, 2, 10, 'OUT', 'Sold', '', '2026-02-27 14:04:37'),
(129, 50, 2, 11, 'OUT', 'Used for Repair', '', '2026-02-27 14:09:18'),
(130, 50, 2, 3, 'OUT', 'Used for Repair', '', '2026-02-27 14:09:35'),
(131, 48, 2, 4, 'OUT', 'Damaged', '', '2026-02-27 14:13:44'),
(132, 12, 2, 3, 'OUT', 'Damaged', '', '2026-02-27 14:14:47'),
(133, 50, 2, 5, 'IN', 'Stocking more', '', '2026-02-28 14:28:50'),
(134, 51, 2, 6, 'OUT', 'Sold', '', '2026-03-02 07:48:08'),
(135, 51, 2, 5, 'IN', 'Stocking more', '', '2026-03-02 07:48:50'),
(136, 52, 2, 10, 'IN', 'Stocking more', '', '2026-03-06 10:49:23'),
(137, 52, 2, 10, 'OUT', 'Sold', '', '2026-03-06 10:57:27');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `PasswordHash` varchar(255) NOT NULL,
  `FullName` varchar(30) NOT NULL,
  `role` enum('Admin','Staff') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `PasswordHash`, `FullName`, `role`, `created_at`) VALUES
(1, 'admin', '$2b$12$acHUmCrdalc4F9uXE9uNhe06okgTQsDrdnkgsO7VbKjKK1qJReWui', 'Jamaillah Santi', 'Admin', '2026-02-10 11:25:42'),
(2, 'staff', '$2b$12$mHfolWALoaaRK7zVpGDn1u3vIUH2UaXcAvkjVlX.OFhTgxo6LDxua', 'Germaine Joy Incinda', 'Staff', '2026-02-10 11:25:42');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `stock_logs`
--
ALTER TABLE `stock_logs`
  ADD PRIMARY KEY (`log_id`),
  ADD KEY `fk_product` (`product_id`),
  ADD KEY `fk_user` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `stock_logs`
--
ALTER TABLE `stock_logs`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=138;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `stock_logs`
--
ALTER TABLE `stock_logs`
  ADD CONSTRAINT `fk_product` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
