-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 28, 2020 at 05:17 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `komputer`
--

-- --------------------------------------------------------

--
-- Table structure for table `cpu`
--

CREATE TABLE `cpu` (
  `id_cpu` varchar(50) NOT NULL,
  `warna` varchar(50) NOT NULL,
  `id_mobo` varchar(50) NOT NULL,
  `id_prosessor` varchar(50) NOT NULL,
  `id_ram` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cpu`
--

INSERT INTO `cpu` (`id_cpu`, `warna`, `id_mobo`, `id_prosessor`, `id_ram`) VALUES
('C01', 'hijau', 'M01', 'P01', 'R1');

-- --------------------------------------------------------

--
-- Table structure for table `mobo`
--

CREATE TABLE `mobo` (
  `id_mobo` varchar(50) NOT NULL,
  `jumlah_slot_memory` varchar(50) NOT NULL,
  `jumlah_slot_harddisk` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mobo`
--

INSERT INTO `mobo` (`id_mobo`, `jumlah_slot_memory`, `jumlah_slot_harddisk`) VALUES
('M01', '4', '5');

-- --------------------------------------------------------

--
-- Table structure for table `prosessor`
--

CREATE TABLE `prosessor` (
  `id_prosessor` varchar(50) NOT NULL,
  `core` varchar(50) NOT NULL,
  `kecepatan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prosessor`
--

INSERT INTO `prosessor` (`id_prosessor`, `core`, `kecepatan`) VALUES
('P01', 'i3', '5Mz');

-- --------------------------------------------------------

--
-- Table structure for table `ram`
--

CREATE TABLE `ram` (
  `id_ram` varchar(50) NOT NULL,
  `kapasitas` varchar(50) NOT NULL,
  `kecepatan_ram` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ram`
--

INSERT INTO `ram` (`id_ram`, `kapasitas`, `kecepatan_ram`) VALUES
('R1', '5', '4mz');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cpu`
--
ALTER TABLE `cpu`
  ADD PRIMARY KEY (`id_cpu`),
  ADD KEY `id_mobo` (`id_mobo`),
  ADD KEY `id_prosesor` (`id_prosessor`),
  ADD KEY `id_ram` (`id_ram`);

--
-- Indexes for table `mobo`
--
ALTER TABLE `mobo`
  ADD PRIMARY KEY (`id_mobo`);

--
-- Indexes for table `prosessor`
--
ALTER TABLE `prosessor`
  ADD PRIMARY KEY (`id_prosessor`);

--
-- Indexes for table `ram`
--
ALTER TABLE `ram`
  ADD PRIMARY KEY (`id_ram`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
