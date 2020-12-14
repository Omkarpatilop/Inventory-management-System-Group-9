-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 14, 2020 at 03:52 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `oid` int(30) NOT NULL,
  `email` varchar(100) NOT NULL,
  `passcode` varchar(100) NOT NULL,
  `otp` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`oid`, `email`, `passcode`, `otp`) VALUES
(1, 'lokhanderobal19ce@student.mes.ac.in', '12345678', 3333),
(2, 'nairvarav19ce@student.mes.ac.in', '12345678', 1245),
(3, 'khedkarniman19ce@student.mes.ac.in', '12345678', 7842),
(4, 'patilomsan19ce@student.mes.ac.in', '12345678', 1348);

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `mail_id` varchar(100) NOT NULL,
  `product_id` int(50) NOT NULL,
  `product_name` varchar(150) NOT NULL,
  `product_qty` int(100) NOT NULL,
  `product_price` bigint(100) NOT NULL,
  `total` bigint(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`mail_id`, `product_id`, `product_name`, `product_qty`, `product_price`, `total`) VALUES
('niranjan@gmail.com', 9348, 'strawberry', 100, 43, 4300),
('rohan@gmail.com', 8564, 'choclate', 90, 20, 2000),
('rohan@gmail.com', 1692, 'oil', 100, 20, 2000);

-- --------------------------------------------------------

--
-- Table structure for table `sales_bill`
--

CREATE TABLE `sales_bill` (
  `inv_id` int(11) NOT NULL,
  `date` varchar(10) CHARACTER SET latin1 NOT NULL,
  `amount` int(11) NOT NULL,
  `mail_id` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sales_stocks`
--

CREATE TABLE `sales_stocks` (
  `inv_id` int(11) NOT NULL,
  `item_no` int(11) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales_stocks`
--

INSERT INTO `sales_stocks` (`inv_id`, `item_no`, `qty`) VALUES
(8889, 2248, 10),
(4368, 12, 90),
(9507, 2248, 8),
(7111, 11, 10),
(8505, 58, 1),
(8505, 12, 2),
(8505, 2248, 2),
(8505, 2248, 3),
(2295, 58, 1),
(2295, 12, 1),
(5451, 12, 6),
(6029, 2248, 1),
(3800, 12, 10),
(3800, 2248, 10),
(6043, 9348, 10),
(9822, 9348, 10),
(9822, 9348, 10),
(5108, 9348, 10),
(9360, 9348, 1),
(9891, 9348, 10),
(9936, 9348, 1),
(9691, 9348, 10),
(2502, 9348, 10),
(3620, 9348, 1),
(6988, 8564, 10);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` bigint(10) NOT NULL,
  `f_name` varchar(50) NOT NULL,
  `l_name` varchar(50) NOT NULL,
  `mail_id` varchar(100) NOT NULL,
  `que` varchar(50) NOT NULL,
  `answer` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `f_name`, `l_name`, `mail_id`, `que`, `answer`, `password`) VALUES
(2, 'Rohan', 'Lokhande', 'rohan@gmail.com', 'Your favourite book', 'GOT', '12345678'),
(5, 'Varun', 'Nair', 'varun@gmail.com', 'Your best friend', 'myself', 'Varun@123'),
(6, 'NIRANJAN ', 'KHEDKAR', 'niranjan@gmail.com', 'Your favourite book', 'harrry potter', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `oid` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` bigint(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
