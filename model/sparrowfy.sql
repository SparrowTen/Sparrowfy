-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： db
-- 產生時間： 2023 年 06 月 12 日 19:01
-- 伺服器版本： 8.0.33
-- PHP 版本： 8.1.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `sparrowfy`
--

-- --------------------------------------------------------

--
-- 資料表結構 `playlist`
--

CREATE TABLE `playlist` (
  `id` int NOT NULL,
  `name` text NOT NULL,
  `user_id` int NOT NULL,
  `song_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `song`
--

CREATE TABLE `song` (
  `id` int NOT NULL,
  `name` text NOT NULL,
  `artist` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 傾印資料表的資料 `song`
--

INSERT INTO `song` (`id`, `name`, `artist`) VALUES
(1, 'アイドル', 'Ayase / YOASOBI'),
(2, 'セブンティーン', 'Ayase / YOASOBI'),
(3, '海のまにまに', 'Ayase / YOASOBI'),
(4, 'アドベンチャー', 'Ayase / YOASOBI'),
(5, '好きだ', 'Ayase / YOASOBI'),
(6, '祝福', 'Ayase / YOASOBI'),
(7, 'ミスター', 'Ayase / YOASOBI'),
(8, 'あの夢をなぞって (Ballade Ver.)', 'Ayase / YOASOBI'),
(9, 'もしも命が描けたら', 'Ayase / YOASOBI'),
(10, 'ツバメ', 'Ayase / YOASOBI'),
(11, 'いばら', 'Ado'),
(12, 'アタシは問題作', 'Ado'),
(13, 'FREEDOM', 'Ado'),
(14, '行方知れず', 'Ado'),
(15, 'リベリオン', 'Ado'),
(16, '風のゆくえ（ウタ from ONE PIECE FILM RED）', 'Ado'),
(17, 'Tot Musica（ウタ from ONE PIECE FILM RED）', 'Ado'),
(18, '世界のつづき（ウタ from ONE PIECE FILM RED）', 'Ado'),
(19, 'ウタカタララバイ（ウタ from ONE PIECE FILM RED）', 'Ado'),
(20, '逆光（ウタ from ONE PIECE FILM RED）', 'Ado');

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `name` text NOT NULL,
  `password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `song`
--
ALTER TABLE `song`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `song`
--
ALTER TABLE `song`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
