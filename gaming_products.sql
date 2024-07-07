-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-07-2024 a las 06:27:43
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gaming_products`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `category` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` varchar(255) NOT NULL,
  `amount` varchar(255) NOT NULL,
  `photo` varchar(5000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`id`, `category`, `name`, `price`, `amount`, `photo`) VALUES
(17, 'Tarjeta grafica', 'Geforce GTX 1060 6GB', '280000', '5', 'imagen_gtx.png'),
(18, 'Consola', 'Nintendo switch old 64gb ', '645000', '3', 'switch.webp'),
(19, 'Motherboards', 'Gigabyte a520m', '135900', '8', 'asus_a520m.webp'),
(20, 'Auricular', 'Logitech G332', '129000', '6', 'auricular_logitech.webp'),
(21, 'Consola', 'Sony playstation 4 slim 500gb ', '715000', '3', 'ps4.webp'),
(22, 'Memoria', 'Ram 8gb DDR4 3200 Mhz', '39000', '10', 'corsair_ram.webp'),
(23, 'Mouse', 'Logitech G403', '70000', '8', 'mouse_logitech.webp'),
(24, 'Teclado', 'T-dagger tipo mecanico rgb', '55800', '12', 'teclado_gamer.webp'),
(27, 'Smart watch', 'Ion box azul ', '40000', '6', 'smartwatch.webp'),
(39, 'Computadora personal ', 'Asus vivo intel i3 N-305 ', '750000', '6', 'notebook_asus.webp');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
