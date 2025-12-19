/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `project`;

/*Table structure for table `appointment` */

DROP TABLE IF EXISTS `appointment`;

CREATE TABLE `appointment` (
  `appointment_id` int(11) NOT NULL AUTO_INCREMENT,
  `health_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `appointment` */

insert  into `appointment`(`appointment_id`,`health_id`,`staff_id`,`date`,`status`) values 
(3,1,1,'2023-11-08','Not Attended'),
(6,2,2,'2023-11-03','Not Attended');

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `attendance_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

insert  into `attendance`(`attendance_id`,`staff_id`,`date`,`attendance_status`) values 
(1,2,'2023-11-02','present'),
(2,2,'2023-11-01','absent'),
(3,2,'2023-10-31','absent'),
(4,2,'2023-10-30','absent'),
(5,2,'2023-10-29','absent'),
(6,2,'2023-10-28','absent'),
(7,2,'2023-10-27','absent'),
(8,2,'2023-10-26','absent'),
(9,2,'2023-11-03','present'),
(10,2,'2023-11-04','present'),
(11,2,'2023-11-08','present'),
(12,2,'2023-11-07','absent'),
(13,2,'2023-11-06','absent'),
(14,2,'2023-11-05','absent'),
(15,1,'2023-11-08','present'),
(16,1,'2023-11-07','absent'),
(17,1,'2023-11-06','absent'),
(18,1,'2023-11-05','absent'),
(19,1,'2023-11-04','absent'),
(20,1,'2023-11-03','absent'),
(21,1,'2023-11-02','absent'),
(22,1,'2023-11-01','absent'),
(23,2,'2023-11-09','present'),
(24,2,'2023-11-10','present'),
(25,2,'2023-11-21','present'),
(26,2,'2023-11-20','absent'),
(27,2,'2023-11-19','absent'),
(28,2,'2023-11-18','absent'),
(29,2,'2023-11-17','absent'),
(30,2,'2023-11-16','absent'),
(31,2,'2023-11-15','absent'),
(32,2,'2023-11-14','absent'),
(33,2,'2023-11-22','present'),
(34,2,'2023-11-23','present');

/*Table structure for table `c_address` */

DROP TABLE IF EXISTS `c_address`;

CREATE TABLE `c_address` (
  `c_address_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `c_address_line1` varchar(100) DEFAULT NULL,
  `c_address_line2` varchar(100) DEFAULT NULL,
  `c_landmark` varchar(50) DEFAULT NULL,
  `c_pincode` varchar(50) DEFAULT NULL,
  `c_city` varchar(50) DEFAULT NULL,
  `c_state` varchar(50) DEFAULT NULL,
  `c_country` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`c_address_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `c_address` */

insert  into `c_address`(`c_address_id`,`username`,`c_address_line1`,`c_address_line2`,`c_landmark`,`c_pincode`,`c_city`,`c_state`,`c_country`) values 
(1,'psdevika95@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(2,'liya@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(3,'anu@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(4,'athira@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `complaint_des` varchar(255) DEFAULT NULL,
  `reply` varchar(255) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`username`,`complaint_des`,`reply`,`date`) values 
(1,'psdevika95@gmail.com','goooooooooooooooooooooood','ddddd','23-05-2023'),
(2,'anu@gmail.com','hello','Please wait for the Response','31-10-2023');

/*Table structure for table `designation` */

DROP TABLE IF EXISTS `designation`;

CREATE TABLE `designation` (
  `designation_id` int(11) NOT NULL AUTO_INCREMENT,
  `designation_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`designation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `designation` */

insert  into `designation`(`designation_id`,`designation_name`) values 
(1,'software engineer'),
(2,'Tester'),
(3,'Designer'),
(4,'Physiatrists');

/*Table structure for table `emotions` */

DROP TABLE IF EXISTS `emotions`;

CREATE TABLE `emotions` (
  `emotions_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `emotions` varchar(50) DEFAULT NULL,
  `emotions_score` int(11) DEFAULT NULL,
  `date` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`emotions_id`)
) ENGINE=InnoDB AUTO_INCREMENT=642 DEFAULT CHARSET=latin1;

/*Data for the table `emotions` */

insert  into `emotions`(`emotions_id`,`staff_id`,`emotions`,`emotions_score`,`date`) values 
(1,2,'neutral',6,'2023-11-02'),
(2,2,'neutral',6,'2023-11-02'),
(3,2,'neutral',6,'2023-11-02'),
(4,2,'neutral',6,'2023-11-02'),
(5,2,'neutral',6,'2023-11-02'),
(6,2,'neutral',6,'2023-11-02'),
(7,2,'neutral',6,'2023-11-02'),
(8,2,'neutral',6,'2023-11-02'),
(9,2,'neutral',6,'2023-11-02'),
(10,2,'neutral',6,'2023-11-02'),
(11,2,'neutral',6,'2023-11-02'),
(12,2,'neutral',6,'2023-11-02'),
(13,2,'neutral',6,'2023-11-02'),
(14,2,'neutral',6,'2023-11-02'),
(15,2,'neutral',6,'2023-11-02'),
(16,2,'neutral',6,'2023-11-02'),
(17,2,'neutral',6,'2023-11-02'),
(18,2,'neutral',6,'2023-11-02'),
(19,2,'neutral',6,'2023-11-02'),
(20,2,'neutral',6,'2023-11-02'),
(21,2,'neutral',6,'2023-11-02'),
(22,2,'neutral',6,'2023-11-02'),
(23,2,'neutral',6,'2023-11-02'),
(24,2,'neutral',6,'2023-11-02'),
(25,2,'neutral',6,'2023-11-02'),
(26,2,'neutral',6,'2023-11-02'),
(27,2,'neutral',6,'2023-11-02'),
(28,2,'neutral',6,'2023-11-02'),
(29,2,'neutral',6,'2023-11-02'),
(30,2,'neutral',6,'2023-11-02'),
(31,2,'neutral',6,'2023-11-02'),
(32,2,'neutral',6,'2023-11-02'),
(33,2,'neutral',6,'2023-11-02'),
(34,2,'neutral',6,'2023-11-02'),
(35,2,'neutral',6,'2023-11-02'),
(36,2,'neutral',6,'2023-11-02'),
(37,2,'neutral',6,'2023-11-02'),
(38,2,'neutral',6,'2023-11-02'),
(39,2,'neutral',6,'2023-11-02'),
(40,2,'neutral',6,'2023-11-02'),
(41,2,'neutral',6,'2023-11-02'),
(42,2,'sad',4,'2023-11-02'),
(43,2,'neutral',6,'2023-11-02'),
(44,2,'neutral',6,'2023-11-02'),
(45,2,'neutral',6,'2023-11-02'),
(46,2,'neutral',6,'2023-11-02'),
(47,2,'fear',2,'2023-11-02'),
(48,2,'sad',4,'2023-11-02'),
(49,2,'sad',4,'2023-11-02'),
(50,2,'neutral',6,'2023-11-02'),
(51,2,'sad',4,'2023-11-02'),
(52,2,'sad',4,'2023-11-02'),
(53,2,'sad',4,'2023-11-02'),
(54,2,'sad',4,'2023-11-02'),
(55,2,'sad',4,'2023-11-02'),
(56,2,'neutral',6,'2023-11-02'),
(57,2,'sad',4,'2023-11-02'),
(58,2,'neutral',6,'2023-11-02'),
(59,2,'sad',4,'2023-11-02'),
(60,2,'sad',4,'2023-11-02'),
(61,2,'neutral',6,'2023-11-02'),
(62,2,'happy',3,'2023-11-02'),
(63,2,'happy',3,'2023-11-02'),
(64,2,'happy',3,'2023-11-02'),
(65,2,'sad',4,'2023-11-02'),
(66,2,'neutral',6,'2023-11-02'),
(67,2,'neutral',6,'2023-11-02'),
(68,2,'happy',3,'2023-11-02'),
(69,2,'fear',2,'2023-11-02'),
(70,2,'angry',0,'2023-11-02'),
(71,2,'angry',0,'2023-11-02'),
(72,2,'angry',0,'2023-11-02'),
(73,2,'neutral',6,'2023-11-02'),
(74,2,'angry',0,'2023-11-02'),
(75,2,'neutral',6,'2023-11-02'),
(76,2,'neutral',6,'2023-11-02'),
(77,2,'neutral',6,'2023-11-02'),
(78,2,'neutral',6,'2023-11-02'),
(79,2,'neutral',6,'2023-11-02'),
(80,2,'sad',4,'2023-11-02'),
(81,2,'neutral',6,'2023-11-02'),
(82,2,'sad',4,'2023-11-02'),
(83,2,'sad',4,'2023-11-02'),
(84,2,'neutral',6,'2023-11-02'),
(85,2,'neutral',6,'2023-11-02'),
(86,2,'sad',4,'2023-11-02'),
(87,2,'neutral',6,'2023-11-02'),
(88,2,'sad',4,'2023-11-02'),
(89,2,'neutral',6,'2023-11-02'),
(90,2,'sad',4,'2023-11-02'),
(91,2,'neutral',6,'2023-11-02'),
(92,2,'neutral',6,'2023-11-02'),
(93,2,'neutral',6,'2023-11-02'),
(94,2,'neutral',6,'2023-11-02'),
(95,2,'neutral',6,'2023-11-02'),
(96,2,'neutral',6,'2023-11-02'),
(97,2,'neutral',6,'2023-11-02'),
(98,2,'sad',4,'2023-11-02'),
(99,2,'neutral',6,'2023-11-02'),
(100,2,'sad',4,'2023-11-02'),
(101,2,'sad',4,'2023-11-02'),
(102,2,'sad',4,'2023-11-02'),
(103,2,'neutral',6,'2023-11-02'),
(104,2,'neutral',6,'2023-11-02'),
(105,2,'fear',2,'2023-11-02'),
(106,2,'fear',2,'2023-11-02'),
(107,2,'neutral',6,'2023-11-02'),
(108,2,'neutral',6,'2023-11-02'),
(109,2,'neutral',6,'2023-11-02'),
(110,2,'neutral',6,'2023-11-02'),
(111,2,'neutral',6,'2023-11-02'),
(112,2,'neutral',6,'2023-11-02'),
(113,2,'neutral',6,'2023-11-02'),
(114,2,'neutral',6,'2023-11-02'),
(115,2,'neutral',6,'2023-11-02'),
(116,2,'neutral',6,'2023-11-02'),
(117,2,'neutral',6,'2023-11-02'),
(118,2,'neutral',6,'2023-11-02'),
(119,2,'neutral',6,'2023-11-02'),
(120,2,'neutral',6,'2023-11-02'),
(121,2,'neutral',6,'2023-11-02'),
(122,2,'neutral',6,'2023-11-02'),
(123,2,'neutral',6,'2023-11-02'),
(124,2,'neutral',6,'2023-11-02'),
(125,2,'neutral',6,'2023-11-02'),
(126,2,'neutral',6,'2023-11-02'),
(127,2,'neutral',6,'2023-11-02'),
(128,2,'neutral',6,'2023-11-02'),
(129,2,'neutral',6,'2023-11-02'),
(130,2,'neutral',6,'2023-11-02'),
(131,2,'neutral',6,'2023-11-02'),
(132,2,'neutral',6,'2023-11-02'),
(133,2,'neutral',6,'2023-11-02'),
(134,2,'neutral',6,'2023-11-02'),
(135,2,'neutral',6,'2023-11-02'),
(136,2,'neutral',6,'2023-11-02'),
(137,2,'neutral',6,'2023-11-02'),
(138,2,'neutral',6,'2023-11-02'),
(139,2,'neutral',6,'2023-11-02'),
(140,2,'neutral',6,'2023-11-02'),
(141,2,'neutral',6,'2023-11-02'),
(142,2,'neutral',6,'2023-11-02'),
(143,2,'neutral',6,'2023-11-02'),
(144,2,'neutral',6,'2023-11-02'),
(145,2,'neutral',6,'2023-11-02'),
(146,2,'neutral',6,'2023-11-02'),
(147,2,'neutral',6,'2023-11-02'),
(148,2,'neutral',6,'2023-11-02'),
(149,2,'neutral',6,'2023-11-02'),
(150,2,'neutral',6,'2023-11-02'),
(151,2,'neutral',6,'2023-11-02'),
(152,2,'neutral',6,'2023-11-02'),
(153,2,'neutral',6,'2023-11-02'),
(154,2,'neutral',6,'2023-11-02'),
(155,2,'neutral',6,'2023-11-02'),
(156,2,'neutral',6,'2023-11-02'),
(157,2,'neutral',6,'2023-11-02'),
(158,2,'neutral',6,'2023-11-02'),
(159,2,'neutral',6,'2023-11-02'),
(160,2,'neutral',6,'2023-11-02'),
(161,2,'neutral',6,'2023-11-02'),
(162,2,'neutral',6,'2023-11-02'),
(163,2,'neutral',6,'2023-11-02'),
(164,2,'neutral',6,'2023-11-02'),
(165,2,'neutral',6,'2023-11-02'),
(166,2,'neutral',6,'2023-11-02'),
(167,2,'neutral',6,'2023-11-02'),
(168,2,'neutral',6,'2023-11-02'),
(169,2,'neutral',6,'2023-11-02'),
(170,2,'neutral',6,'2023-11-02'),
(171,2,'neutral',6,'2023-11-02'),
(172,2,'neutral',6,'2023-11-02'),
(173,2,'neutral',6,'2023-11-02'),
(174,2,'neutral',6,'2023-11-02'),
(175,2,'neutral',6,'2023-11-02'),
(176,2,'neutral',6,'2023-11-02'),
(177,2,'neutral',6,'2023-11-02'),
(178,2,'neutral',6,'2023-11-02'),
(179,2,'neutral',6,'2023-11-02'),
(180,2,'neutral',6,'2023-11-02'),
(181,2,'neutral',6,'2023-11-02'),
(182,2,'neutral',6,'2023-11-02'),
(183,2,'neutral',6,'2023-11-02'),
(184,2,'neutral',6,'2023-11-02'),
(185,2,'neutral',6,'2023-11-02'),
(186,2,'neutral',6,'2023-11-02'),
(187,2,'neutral',6,'2023-11-02'),
(188,2,'neutral',6,'2023-11-02'),
(189,2,'neutral',6,'2023-11-02'),
(190,2,'neutral',6,'2023-11-02'),
(191,2,'neutral',6,'2023-11-02'),
(192,2,'neutral',6,'2023-11-02'),
(193,2,'neutral',6,'2023-11-02'),
(194,2,'sad',4,'2023-11-02'),
(195,2,'neutral',6,'2023-11-02'),
(196,2,'neutral',6,'2023-11-02'),
(197,2,'neutral',6,'2023-11-02'),
(198,2,'neutral',6,'2023-11-02'),
(199,2,'neutral',6,'2023-11-02'),
(200,2,'sad',4,'2023-11-02'),
(201,2,'neutral',6,'2023-11-02'),
(202,2,'neutral',6,'2023-11-02'),
(203,2,'neutral',6,'2023-11-02'),
(204,2,'neutral',6,'2023-11-03'),
(205,2,'sad',4,'2023-11-03'),
(206,2,'sad',4,'2023-11-03'),
(207,2,'sad',4,'2023-11-03'),
(208,2,'sad',4,'2023-11-03'),
(209,2,'sad',4,'2023-11-03'),
(210,2,'neutral',6,'2023-11-03'),
(211,2,'neutral',6,'2023-11-03'),
(212,2,'neutral',6,'2023-11-03'),
(213,2,'neutral',6,'2023-11-03'),
(214,2,'sad',4,'2023-11-03'),
(215,2,'sad',4,'2023-11-03'),
(216,2,'neutral',6,'2023-11-03'),
(217,2,'neutral',6,'2023-11-03'),
(218,2,'neutral',6,'2023-11-03'),
(219,2,'neutral',6,'2023-11-03'),
(220,2,'neutral',6,'2023-11-03'),
(221,2,'sad',4,'2023-11-03'),
(222,2,'neutral',6,'2023-11-03'),
(223,2,'neutral',6,'2023-11-03'),
(224,2,'neutral',6,'2023-11-03'),
(225,2,'neutral',6,'2023-11-03'),
(226,2,'neutral',6,'2023-11-03'),
(227,2,'neutral',6,'2023-11-03'),
(228,2,'sad',4,'2023-11-03'),
(229,2,'neutral',6,'2023-11-03'),
(230,2,'neutral',6,'2023-11-03'),
(231,2,'neutral',6,'2023-11-03'),
(232,2,'neutral',6,'2023-11-03'),
(233,2,'neutral',6,'2023-11-03'),
(234,2,'sad',4,'2023-11-03'),
(235,2,'neutral',6,'2023-11-03'),
(236,2,'neutral',6,'2023-11-03'),
(237,2,'neutral',6,'2023-11-03'),
(238,2,'neutral',6,'2023-11-03'),
(239,2,'neutral',6,'2023-11-03'),
(240,2,'neutral',6,'2023-11-03'),
(241,2,'neutral',6,'2023-11-03'),
(242,2,'neutral',6,'2023-11-03'),
(243,2,'neutral',6,'2023-11-03'),
(244,2,'neutral',6,'2023-11-03'),
(245,2,'neutral',6,'2023-11-03'),
(246,2,'neutral',6,'2023-11-03'),
(247,2,'neutral',6,'2023-11-03'),
(248,2,'neutral',6,'2023-11-03'),
(249,2,'neutral',6,'2023-11-03'),
(250,2,'neutral',6,'2023-11-03'),
(251,2,'neutral',6,'2023-11-03'),
(252,2,'sad',4,'2023-11-03'),
(253,2,'neutral',6,'2023-11-03'),
(254,2,'sad',4,'2023-11-03'),
(255,2,'sad',4,'2023-11-03'),
(256,2,'sad',4,'2023-11-03'),
(257,2,'neutral',6,'2023-11-03'),
(258,2,'sad',4,'2023-11-03'),
(259,2,'sad',4,'2023-11-03'),
(260,2,'sad',4,'2023-11-03'),
(261,2,'sad',4,'2023-11-03'),
(262,2,'sad',4,'2023-11-03'),
(263,2,'neutral',6,'2023-11-03'),
(264,2,'neutral',6,'2023-11-03'),
(265,2,'sad',4,'2023-11-03'),
(266,2,'neutral',6,'2023-11-03'),
(267,2,'sad',4,'2023-11-03'),
(268,2,'sad',4,'2023-11-03'),
(269,2,'sad',4,'2023-11-03'),
(270,2,'neutral',6,'2023-11-03'),
(271,2,'sad',4,'2023-11-03'),
(272,2,'sad',4,'2023-11-03'),
(273,2,'sad',4,'2023-11-03'),
(274,2,'sad',4,'2023-11-03'),
(275,2,'sad',4,'2023-11-03'),
(276,2,'sad',4,'2023-11-03'),
(277,2,'sad',4,'2023-11-03'),
(278,2,'sad',4,'2023-11-03'),
(279,2,'sad',4,'2023-11-03'),
(280,2,'sad',4,'2023-11-03'),
(281,2,'sad',4,'2023-11-03'),
(282,2,'sad',4,'2023-11-03'),
(283,2,'sad',4,'2023-11-03'),
(284,2,'neutral',6,'2023-11-03'),
(285,2,'neutral',6,'2023-11-03'),
(286,2,'sad',4,'2023-11-03'),
(287,2,'neutral',6,'2023-11-03'),
(288,2,'neutral',6,'2023-11-03'),
(289,2,'sad',4,'2023-11-03'),
(290,2,'sad',4,'2023-11-03'),
(291,2,'neutral',6,'2023-11-03'),
(292,2,'neutral',6,'2023-11-03'),
(293,2,'neutral',6,'2023-11-03'),
(294,2,'sad',4,'2023-11-03'),
(295,2,'sad',4,'2023-11-03'),
(296,2,'sad',4,'2023-11-03'),
(297,2,'neutral',6,'2023-11-03'),
(298,2,'neutral',6,'2023-11-03'),
(299,2,'neutral',6,'2023-11-03'),
(300,2,'neutral',6,'2023-11-03'),
(301,2,'sad',4,'2023-11-03'),
(302,2,'neutral',6,'2023-11-03'),
(303,2,'sad',4,'2023-11-03'),
(304,2,'sad',4,'2023-11-03'),
(305,2,'sad',4,'2023-11-03'),
(306,2,'sad',4,'2023-11-03'),
(307,2,'neutral',6,'2023-11-03'),
(308,2,'neutral',6,'2023-11-03'),
(309,2,'sad',4,'2023-11-03'),
(310,2,'neutral',6,'2023-11-03'),
(311,2,'neutral',6,'2023-11-03'),
(312,2,'sad',4,'2023-11-03'),
(313,2,'sad',4,'2023-11-03'),
(314,2,'sad',4,'2023-11-03'),
(315,2,'sad',4,'2023-11-03'),
(316,2,'sad',4,'2023-11-03'),
(317,2,'sad',4,'2023-11-03'),
(318,2,'sad',4,'2023-11-03'),
(319,2,'sad',4,'2023-11-03'),
(320,2,'fear',2,'2023-11-03'),
(321,2,'fear',2,'2023-11-03'),
(322,2,'fear',2,'2023-11-03'),
(323,2,'neutral',6,'2023-11-03'),
(324,2,'neutral',6,'2023-11-03'),
(325,2,'neutral',6,'2023-11-03'),
(326,2,'neutral',6,'2023-11-03'),
(327,2,'neutral',6,'2023-11-03'),
(328,2,'sad',4,'2023-11-03'),
(329,2,'sad',4,'2023-11-03'),
(330,2,'sad',4,'2023-11-03'),
(331,2,'neutral',6,'2023-11-03'),
(332,2,'sad',4,'2023-11-03'),
(333,2,'neutral',6,'2023-11-03'),
(334,2,'fear',2,'2023-11-03'),
(335,2,'sad',4,'2023-11-03'),
(336,2,'neutral',6,'2023-11-03'),
(337,2,'neutral',6,'2023-11-03'),
(338,2,'neutral',6,'2023-11-03'),
(339,2,'neutral',6,'2023-11-03'),
(340,2,'neutral',6,'2023-11-03'),
(341,2,'neutral',6,'2023-11-03'),
(342,2,'neutral',6,'2023-11-03'),
(343,2,'neutral',6,'2023-11-03'),
(344,2,'neutral',6,'2023-11-03'),
(345,2,'neutral',6,'2023-11-03'),
(346,2,'neutral',6,'2023-11-03'),
(347,2,'neutral',6,'2023-11-03'),
(348,2,'neutral',6,'2023-11-03'),
(349,2,'sad',4,'2023-11-03'),
(350,2,'neutral',6,'2023-11-03'),
(351,2,'sad',4,'2023-11-03'),
(352,2,'sad',4,'2023-11-03'),
(353,2,'sad',4,'2023-11-03'),
(354,2,'sad',4,'2023-11-03'),
(355,2,'sad',4,'2023-11-03'),
(356,2,'sad',4,'2023-11-03'),
(357,2,'sad',4,'2023-11-03'),
(358,2,'sad',4,'2023-11-03'),
(359,2,'sad',4,'2023-11-03'),
(360,2,'neutral',6,'2023-11-03'),
(361,2,'neutral',6,'2023-11-03'),
(362,2,'neutral',6,'2023-11-03'),
(363,2,'neutral',6,'2023-11-03'),
(364,2,'neutral',6,'2023-11-03'),
(365,2,'neutral',6,'2023-11-03'),
(366,2,'neutral',6,'2023-11-03'),
(367,2,'neutral',6,'2023-11-03'),
(368,2,'neutral',6,'2023-11-03'),
(369,2,'neutral',6,'2023-11-03'),
(370,2,'neutral',6,'2023-11-03'),
(371,2,'neutral',6,'2023-11-03'),
(372,2,'disgust',1,'2023-11-03'),
(373,2,'disgust',1,'2023-11-03'),
(374,2,'neutral',6,'2023-11-03'),
(375,2,'fear',2,'2023-11-03'),
(376,2,'neutral',6,'2023-11-03'),
(377,2,'fear',2,'2023-11-03'),
(378,2,'sad',4,'2023-11-03'),
(379,2,'sad',4,'2023-11-03'),
(380,2,'sad',4,'2023-11-03'),
(381,2,'sad',4,'2023-11-03'),
(382,2,'fear',2,'2023-11-03'),
(383,2,'sad',4,'2023-11-03'),
(384,2,'fear',2,'2023-11-03'),
(385,2,'fear',2,'2023-11-03'),
(386,2,'sad',4,'2023-11-03'),
(387,2,'happy',3,'2023-11-03'),
(388,2,'neutral',6,'2023-11-03'),
(389,2,'neutral',6,'2023-11-03'),
(390,2,'neutral',6,'2023-11-03'),
(391,2,'neutral',6,'2023-11-03'),
(392,2,'neutral',6,'2023-11-03'),
(393,2,'neutral',6,'2023-11-03'),
(394,2,'neutral',6,'2023-11-03'),
(395,2,'sad',4,'2023-11-03'),
(396,2,'neutral',6,'2023-11-03'),
(397,2,'neutral',6,'2023-11-03'),
(398,2,'neutral',6,'2023-11-03'),
(399,2,'neutral',6,'2023-11-03'),
(400,2,'neutral',6,'2023-11-03'),
(401,2,'neutral',6,'2023-11-03'),
(402,2,'neutral',6,'2023-11-03'),
(403,2,'neutral',6,'2023-11-03'),
(404,2,'neutral',6,'2023-11-03'),
(405,2,'neutral',6,'2023-11-03'),
(406,2,'neutral',6,'2023-11-03'),
(407,2,'neutral',6,'2023-11-03'),
(408,2,'sad',4,'2023-11-03'),
(409,2,'neutral',6,'2023-11-03'),
(410,2,'neutral',6,'2023-11-03'),
(411,2,'sad',4,'2023-11-03'),
(412,2,'neutral',6,'2023-11-03'),
(413,2,'neutral',6,'2023-11-03'),
(414,2,'neutral',6,'2023-11-03'),
(415,2,'neutral',6,'2023-11-03'),
(416,2,'happy',3,'2023-11-03'),
(417,2,'happy',3,'2023-11-03'),
(418,2,'happy',3,'2023-11-03'),
(419,2,'happy',3,'2023-11-03'),
(420,2,'fear',2,'2023-11-03'),
(421,2,'sad',4,'2023-11-03'),
(422,2,'sad',4,'2023-11-03'),
(423,2,'sad',4,'2023-11-03'),
(424,2,'neutral',6,'2023-11-03'),
(425,2,'sad',4,'2023-11-03'),
(426,2,'sad',4,'2023-11-03'),
(427,2,'neutral',6,'2023-11-03'),
(428,2,'sad',4,'2023-11-03'),
(429,2,'fear',2,'2023-11-03'),
(430,2,'sad',4,'2023-11-03'),
(431,2,'sad',4,'2023-11-03'),
(432,2,'sad',4,'2023-11-03'),
(433,2,'sad',4,'2023-11-03'),
(434,2,'sad',4,'2023-11-03'),
(435,2,'sad',4,'2023-11-03'),
(436,2,'sad',4,'2023-11-03'),
(437,2,'happy',3,'2023-11-03'),
(438,2,'happy',3,'2023-11-03'),
(439,2,'angry',0,'2023-11-03'),
(440,2,'happy',3,'2023-11-03'),
(441,2,'fear',2,'2023-11-03'),
(442,2,'neutral',6,'2023-11-03'),
(443,2,'neutral',6,'2023-11-03'),
(444,2,'neutral',6,'2023-11-03'),
(445,2,'sad',4,'2023-11-03'),
(446,2,'fear',2,'2023-11-03'),
(447,2,'neutral',6,'2023-11-03'),
(448,2,'neutral',6,'2023-11-03'),
(449,2,'neutral',6,'2023-11-03'),
(450,2,'neutral',6,'2023-11-03'),
(451,2,'sad',4,'2023-11-03'),
(452,2,'sad',4,'2023-11-03'),
(453,2,'neutral',6,'2023-11-03'),
(454,2,'sad',4,'2023-11-03'),
(455,2,'neutral',6,'2023-11-03'),
(456,2,'neutral',6,'2023-11-03'),
(457,2,'sad',4,'2023-11-03'),
(458,2,'angry',0,'2023-11-03'),
(459,2,'sad',4,'2023-11-03'),
(460,2,'sad',4,'2023-11-03'),
(461,2,'sad',4,'2023-11-03'),
(462,2,'sad',4,'2023-11-03'),
(463,2,'neutral',6,'2023-11-03'),
(464,2,'neutral',6,'2023-11-03'),
(465,2,'neutral',6,'2023-11-03'),
(466,2,'neutral',6,'2023-11-03'),
(467,2,'fear',2,'2023-11-03'),
(468,2,'sad',4,'2023-11-03'),
(469,2,'sad',4,'2023-11-03'),
(470,2,'neutral',6,'2023-11-03'),
(471,2,'neutral',6,'2023-11-03'),
(472,1,'sad',4,'2023-11-08'),
(473,1,'sad',4,'2023-11-08'),
(474,1,'sad',4,'2023-11-08'),
(475,1,'fear',2,'2023-11-08'),
(476,1,'angry',0,'2023-11-08'),
(477,1,'neutral',6,'2023-11-08'),
(478,1,'fear',2,'2023-11-08'),
(479,1,'neutral',6,'2023-11-08'),
(480,1,'neutral',6,'2023-11-08'),
(481,1,'neutral',6,'2023-11-08'),
(482,1,'happy',3,'2023-11-08'),
(483,1,'neutral',6,'2023-11-08'),
(484,1,'neutral',6,'2023-11-08'),
(485,1,'neutral',6,'2023-11-08'),
(486,1,'neutral',6,'2023-11-08'),
(487,1,'neutral',6,'2023-11-08'),
(488,1,'neutral',6,'2023-11-08'),
(489,1,'neutral',6,'2023-11-08'),
(490,1,'neutral',6,'2023-11-08'),
(491,1,'neutral',6,'2023-11-08'),
(492,1,'neutral',6,'2023-11-08'),
(493,1,'neutral',6,'2023-11-08'),
(494,1,'neutral',6,'2023-11-08'),
(495,1,'neutral',6,'2023-11-08'),
(496,1,'neutral',6,'2023-11-08'),
(497,1,'neutral',6,'2023-11-08'),
(498,1,'neutral',6,'2023-11-08'),
(499,1,'neutral',6,'2023-11-08'),
(500,1,'neutral',6,'2023-11-08'),
(501,1,'neutral',6,'2023-11-08'),
(502,1,'neutral',6,'2023-11-08'),
(503,1,'neutral',6,'2023-11-08'),
(504,1,'neutral',6,'2023-11-08'),
(505,1,'neutral',6,'2023-11-08'),
(506,1,'neutral',6,'2023-11-08'),
(507,1,'neutral',6,'2023-11-08'),
(508,1,'neutral',6,'2023-11-08'),
(509,1,'neutral',6,'2023-11-08'),
(510,1,'neutral',6,'2023-11-08'),
(511,1,'neutral',6,'2023-11-08'),
(512,1,'neutral',6,'2023-11-08'),
(513,1,'neutral',6,'2023-11-08'),
(514,1,'sad',4,'2023-11-08'),
(515,1,'neutral',6,'2023-11-08'),
(516,1,'neutral',6,'2023-11-08'),
(517,1,'neutral',6,'2023-11-08'),
(518,1,'neutral',6,'2023-11-08'),
(519,1,'neutral',6,'2023-11-08'),
(520,1,'neutral',6,'2023-11-08'),
(521,1,'neutral',6,'2023-11-08'),
(522,1,'neutral',6,'2023-11-08'),
(523,1,'neutral',6,'2023-11-08'),
(524,1,'neutral',6,'2023-11-08'),
(525,1,'neutral',6,'2023-11-08'),
(526,1,'neutral',6,'2023-11-08'),
(527,1,'neutral',6,'2023-11-08'),
(528,1,'neutral',6,'2023-11-08'),
(529,1,'neutral',6,'2023-11-08'),
(530,1,'neutral',6,'2023-11-08'),
(531,1,'neutral',6,'2023-11-08'),
(532,1,'neutral',6,'2023-11-08'),
(533,1,'neutral',6,'2023-11-08'),
(534,1,'neutral',6,'2023-11-08'),
(535,1,'neutral',6,'2023-11-08'),
(536,1,'neutral',6,'2023-11-08'),
(537,1,'sad',4,'2023-11-08'),
(538,1,'neutral',6,'2023-11-08'),
(539,1,'neutral',6,'2023-11-08'),
(540,1,'neutral',6,'2023-11-08'),
(541,1,'sad',4,'2023-11-08'),
(542,1,'neutral',6,'2023-11-08'),
(543,1,'neutral',6,'2023-11-08'),
(544,1,'neutral',6,'2023-11-08'),
(545,1,'neutral',6,'2023-11-08'),
(546,1,'neutral',6,'2023-11-08'),
(547,1,'neutral',6,'2023-11-08'),
(548,1,'neutral',6,'2023-11-08'),
(549,1,'neutral',6,'2023-11-08'),
(550,1,'neutral',6,'2023-11-08'),
(551,1,'neutral',6,'2023-11-08'),
(552,1,'neutral',6,'2023-11-08'),
(553,1,'sad',4,'2023-11-08'),
(554,1,'sad',4,'2023-11-08'),
(555,1,'sad',4,'2023-11-08'),
(556,1,'happy',3,'2023-11-08'),
(557,1,'fear',2,'2023-11-08'),
(558,1,'sad',4,'2023-11-08'),
(559,1,'sad',4,'2023-11-08'),
(560,1,'sad',4,'2023-11-08'),
(561,1,'angry',0,'2023-11-08'),
(562,1,'angry',0,'2023-11-08'),
(563,1,'angry',0,'2023-11-08'),
(564,1,'fear',2,'2023-11-08'),
(565,1,'sad',4,'2023-11-08'),
(566,1,'sad',4,'2023-11-08'),
(567,1,'sad',4,'2023-11-08'),
(568,1,'sad',4,'2023-11-08'),
(569,1,'sad',4,'2023-11-08'),
(570,1,'sad',4,'2023-11-08'),
(571,1,'sad',4,'2023-11-08'),
(572,1,'sad',4,'2023-11-08'),
(573,1,'happy',3,'2023-11-08'),
(574,1,'neutral',6,'2023-11-08'),
(575,1,'happy',3,'2023-11-08'),
(576,1,'happy',3,'2023-11-08'),
(577,1,'happy',3,'2023-11-08'),
(578,1,'happy',3,'2023-11-08'),
(579,1,'neutral',6,'2023-11-08'),
(580,1,'neutral',6,'2023-11-08'),
(581,1,'sad',4,'2023-11-08'),
(582,1,'sad',4,'2023-11-08'),
(583,1,'neutral',6,'2023-11-08'),
(584,1,'sad',4,'2023-11-08'),
(585,1,'neutral',6,'2023-11-08'),
(586,1,'neutral',6,'2023-11-08'),
(587,1,'sad',4,'2023-11-08'),
(588,1,'sad',4,'2023-11-08'),
(589,1,'sad',4,'2023-11-08'),
(590,1,'fear',2,'2023-11-08'),
(591,1,'neutral',6,'2023-11-08'),
(592,1,'neutral',6,'2023-11-08'),
(593,1,'neutral',6,'2023-11-08'),
(594,1,'neutral',6,'2023-11-08'),
(595,1,'neutral',6,'2023-11-08'),
(596,1,'neutral',6,'2023-11-08'),
(597,1,'neutral',6,'2023-11-08'),
(598,1,'neutral',6,'2023-11-08'),
(599,1,'neutral',6,'2023-11-08'),
(600,1,'neutral',6,'2023-11-08'),
(601,1,'neutral',6,'2023-11-08'),
(602,1,'neutral',6,'2023-11-08'),
(603,1,'neutral',6,'2023-11-08'),
(604,1,'neutral',6,'2023-11-08'),
(605,1,'neutral',6,'2023-11-08'),
(606,1,'neutral',6,'2023-11-08'),
(607,1,'neutral',6,'2023-11-08'),
(608,1,'neutral',6,'2023-11-08'),
(609,1,'happy',3,'2023-11-08'),
(610,1,'happy',3,'2023-11-08'),
(611,1,'happy',3,'2023-11-08'),
(612,1,'angry',0,'2023-11-08'),
(613,1,'sad',4,'2023-11-08'),
(614,1,'angry',0,'2023-11-08'),
(615,1,'angry',0,'2023-11-08'),
(616,2,'fear',2,'2023-11-22'),
(617,2,'sad',4,'2023-11-22'),
(618,2,'neutral',6,'2023-11-22'),
(619,2,'sad',4,'2023-11-22'),
(620,2,'neutral',6,'2023-11-22'),
(621,2,'sad',4,'2023-11-22'),
(622,2,'neutral',6,'2023-11-22'),
(623,2,'sad',4,'2023-11-22'),
(624,2,'neutral',6,'2023-11-22'),
(625,2,'neutral',6,'2023-11-22'),
(626,2,'neutral',6,'2023-11-22'),
(627,2,'neutral',6,'2023-11-22'),
(628,2,'neutral',6,'2023-11-22'),
(629,2,'neutral',6,'2023-11-22'),
(630,2,'neutral',6,'2023-11-22'),
(631,2,'neutral',6,'2023-11-22'),
(632,2,'neutral',6,'2023-11-22'),
(633,2,'neutral',6,'2023-11-22'),
(634,2,'neutral',6,'2023-11-22'),
(635,2,'neutral',6,'2023-11-22'),
(636,2,'neutral',6,'2023-11-22'),
(637,2,'neutral',6,'2023-11-22'),
(638,2,'neutral',6,'2023-11-22'),
(639,2,'neutral',6,'2023-11-22'),
(640,2,'neutral',6,'2023-11-22'),
(641,2,'sad',4,'2023-11-22');

/*Table structure for table `fares` */

DROP TABLE IF EXISTS `fares`;

CREATE TABLE `fares` (
  `fare_id` int(11) NOT NULL AUTO_INCREMENT,
  `starting_stop_id` int(11) DEFAULT NULL,
  `ending_stop_id` int(11) DEFAULT NULL,
  `amount_per_seat` varchar(20) DEFAULT NULL,
  `pass_amount` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`fare_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `fares` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback_desc` varchar(50) DEFAULT NULL,
  `date_time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `health_care_team` */

DROP TABLE IF EXISTS `health_care_team`;

CREATE TABLE `health_care_team` (
  `health_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `h_fname` varchar(50) DEFAULT NULL,
  `h_lname` varchar(50) DEFAULT NULL,
  `h_qualification` varchar(50) DEFAULT NULL,
  `h_phone_no` varchar(50) DEFAULT NULL,
  `h_email_id` varchar(50) DEFAULT NULL,
  `h_dob` varchar(50) DEFAULT NULL,
  `h_gender` varchar(50) DEFAULT NULL,
  `h_resume` varchar(255) DEFAULT NULL,
  `h_credential` varchar(255) DEFAULT NULL,
  `h_photo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`health_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `health_care_team` */

insert  into `health_care_team`(`health_id`,`username`,`h_fname`,`h_lname`,`h_qualification`,`h_phone_no`,`h_email_id`,`h_dob`,`h_gender`,`h_resume`,`h_credential`,`h_photo`) values 
(1,'liya@gmail.com','liya','a','mma','8987675645','liya@gmail.com','1995-05-04','Female',NULL,NULL,NULL),
(2,'athira@gmail.com','Athira','Murali','gggg','9895392501','athira@gmail.com','1996-10-02','Female',NULL,NULL,NULL);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`user_type`) values 
('admin','admin','admin'),
('psdevika95@gmail.com','10072000','staff'),
('liya@gmail.com','8987675645','health_care_team'),
('anu@gmail.com','Anu@1234567','staff'),
('athira@gmail.com','9895392501','health_care_team');

/*Table structure for table `medication` */

DROP TABLE IF EXISTS `medication`;

CREATE TABLE `medication` (
  `appointment_id` int(11) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `medication_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`medication_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `medication` */

insert  into `medication`(`appointment_id`,`title`,`description`,`medication_id`) values 
(4,'ghhdh','hhhh',1);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_des` varchar(255) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_des`,`date`,`user_type`) values 
('fggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg','2023-05-23','admin'),
('testing notification','2023-10-31','admin'),
('ssss','2023-11-22','admin');

/*Table structure for table `p_address` */

DROP TABLE IF EXISTS `p_address`;

CREATE TABLE `p_address` (
  `address_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `address_line1` varchar(100) DEFAULT NULL,
  `address_line2` varchar(100) DEFAULT NULL,
  `landmark` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`address_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `p_address` */

insert  into `p_address`(`address_id`,`username`,`address_line1`,`address_line2`,`landmark`,`pincode`,`city`,`state`,`country`) values 
(1,'psdevika95@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(2,'liya@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(3,'anu@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(4,'athira@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `booking_id` int(11) DEFAULT NULL,
  `type[booking]` varchar(50) DEFAULT NULL,
  `date_time` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `predicted_result` */

DROP TABLE IF EXISTS `predicted_result`;

CREATE TABLE `predicted_result` (
  `p_result_id` int(11) NOT NULL AUTO_INCREMENT,
  `p_result` varchar(255) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `p_value` varchar(222) DEFAULT NULL,
  PRIMARY KEY (`p_result_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `predicted_result` */

insert  into `predicted_result`(`p_result_id`,`p_result`,`staff_id`,`date`,`p_value`) values 
(1,'Moderate Depression',2,'2023-11-03','2'),
(6,'Moderate Depression',2,'2023-11-10','1.75'),
(7,'Moderate Depression',2,'2023-11-22','1.75'),
(8,'Moderate Depression',2,'2023-11-23','1.75');

/*Table structure for table `ratings` */

DROP TABLE IF EXISTS `ratings`;

CREATE TABLE `ratings` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `ratings` varchar(50) DEFAULT NULL,
  `date` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ratings` */

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `r1` varchar(200) DEFAULT NULL,
  `r2` varchar(200) DEFAULT NULL,
  `r3` varchar(200) DEFAULT NULL,
  `r4` varchar(200) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`result_id`,`r1`,`r2`,`r3`,`r4`,`staff_id`,`date`) values 
(1,'2.0','1','1','3',2,'2023-11-01'),
(2,'2.0','1','1','3',2,'2023-11-02'),
(3,'2.0','1','1','3',2,'2023-11-03'),
(4,'3.0','1','1','2',1,'2023-11-08'),
(5,'2.0','1','1','4',2,'2023-11-22');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `designation_id` int(11) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `s_phone_no` varchar(50) DEFAULT NULL,
  `as_phone_no` varchar(50) DEFAULT NULL,
  `s_email_id` varchar(50) DEFAULT NULL,
  `as_email_id` varchar(50) DEFAULT NULL,
  `s_photo` varchar(255) DEFAULT NULL,
  `s_resume` varchar(255) DEFAULT NULL,
  `s_certificate` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`designation_id`,`username`,`first_name`,`last_name`,`gender`,`dob`,`s_phone_no`,`as_phone_no`,`s_email_id`,`as_email_id`,`s_photo`,`s_resume`,`s_certificate`) values 
(1,1,'psdevika95@gmail.com','devika','p s','Female','2000-07-10','9846909433',NULL,'psdevika95@gmail.com',NULL,NULL,NULL,NULL),
(2,1,'anu@gmail.com','anu','R','Female','1999-10-27','9895328503',NULL,'anu@gmail.com',NULL,NULL,NULL,NULL);

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `age` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varbinary(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `users` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
