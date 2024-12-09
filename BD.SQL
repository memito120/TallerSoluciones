-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 06-12-2024 a las 04:52:34
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `taller_4`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Calendario', 7, 'add_calendario'),
(26, 'Can change Calendario', 7, 'change_calendario'),
(27, 'Can delete Calendario', 7, 'delete_calendario'),
(28, 'Can view Calendario', 7, 'view_calendario'),
(29, 'Can add Perfil', 8, 'add_perfil'),
(30, 'Can change Perfil', 8, 'change_perfil'),
(31, 'Can delete Perfil', 8, 'delete_perfil'),
(32, 'Can view Perfil', 8, 'view_perfil'),
(33, 'Can add Horario', 9, 'add_horario'),
(34, 'Can change Horario', 9, 'change_horario'),
(35, 'Can delete Horario', 9, 'delete_horario'),
(36, 'Can view Horario', 9, 'view_horario'),
(37, 'Can add Servicio', 10, 'add_servicio'),
(38, 'Can change Servicio', 10, 'change_servicio'),
(39, 'Can delete Servicio', 10, 'delete_servicio'),
(40, 'Can view Servicio', 10, 'view_servicio'),
(41, 'Can add Imagen', 11, 'add_imagenes'),
(42, 'Can change Imagen', 11, 'change_imagenes'),
(43, 'Can delete Imagen', 11, 'delete_imagenes'),
(44, 'Can view Imagen', 11, 'view_imagenes'),
(45, 'Can add Estado', 12, 'add_estate'),
(46, 'Can change Estado', 12, 'change_estate'),
(47, 'Can delete Estado', 12, 'delete_estate'),
(48, 'Can view Estado', 12, 'view_estate'),
(49, 'Can add Comentario', 13, 'add_comentario'),
(50, 'Can change Comentario', 13, 'change_comentario'),
(51, 'Can delete Comentario', 13, 'delete_comentario'),
(52, 'Can view Comentario', 13, 'view_comentario'),
(53, 'Can add Ticket', 14, 'add_ticket'),
(54, 'Can change Ticket', 14, 'change_ticket'),
(55, 'Can delete Ticket', 14, 'delete_ticket'),
(56, 'Can view Ticket', 14, 'view_ticket'),
(57, 'Can add Calificacion', 15, 'add_calificacion'),
(58, 'Can change Calificacion', 15, 'change_calificacion'),
(59, 'Can delete Calificacion', 15, 'delete_calificacion'),
(60, 'Can view Calificacion', 15, 'view_calificacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$8sJgb0crbehsQmePTZ6yLd$4wCyIsU5siCAZpPoy5NqomfrwbvBfqDRoYSPEaRaEVs=', '2024-12-06 01:50:45.520173', 0, 'Joaquin', '', '', 'joacoaraya10a@gmail.cl', 0, 1, '2024-12-06 01:50:36.521086');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calendario`
--

DROP TABLE IF EXISTS `calendario`;
CREATE TABLE IF NOT EXISTS `calendario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `entrada` time(6) NOT NULL,
  `salida` time(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificacion`
--

DROP TABLE IF EXISTS `calificacion`;
CREATE TABLE IF NOT EXISTS `calificacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nota` int UNSIGNED NOT NULL,
  `id_perfil_id` bigint NOT NULL,
  `id_servicio_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `calificacion_id_perfil_id_id_servicio_id_7c6f5c84_uniq` (`id_perfil_id`,`id_servicio_id`),
  KEY `calificacion_id_perfil_id_11a9d4fc` (`id_perfil_id`),
  KEY `calificacion_id_servicio_id_d0791e9f` (`id_servicio_id`)
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comentario`
--

DROP TABLE IF EXISTS `comentario`;
CREATE TABLE IF NOT EXISTS `comentario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comentario` varchar(500) NOT NULL,
  `parent_id` bigint DEFAULT NULL,
  `id_perfil_id` bigint NOT NULL,
  `id_servicio_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comentario_parent_id_eb97159d` (`parent_id`),
  KEY `comentario_id_perfil_id_8a1e8fbb` (`id_perfil_id`),
  KEY `comentario_id_servicio_id_18ebd1fd` (`id_servicio_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'sitio', 'calendario'),
(8, 'sitio', 'perfil'),
(9, 'sitio', 'horario'),
(10, 'sitio', 'servicio'),
(11, 'sitio', 'imagenes'),
(12, 'sitio', 'estate'),
(13, 'sitio', 'comentario'),
(14, 'sitio', 'ticket'),
(15, 'sitio', 'calificacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-12-06 01:49:14.933653'),
(2, 'auth', '0001_initial', '2024-12-06 01:49:15.478286'),
(3, 'admin', '0001_initial', '2024-12-06 01:49:15.652389'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-12-06 01:49:15.660385'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-12-06 01:49:15.666861'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-12-06 01:49:15.733412'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-12-06 01:49:15.770449'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-12-06 01:49:15.807686'),
(9, 'auth', '0004_alter_user_username_opts', '2024-12-06 01:49:15.814517'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-12-06 01:49:15.848270'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-12-06 01:49:15.849278'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-12-06 01:49:15.858039'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-12-06 01:49:15.890834'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-12-06 01:49:15.923768'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-12-06 01:49:15.957402'),
(16, 'auth', '0011_update_proxy_permissions', '2024-12-06 01:49:15.963341'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-12-06 01:49:16.000213'),
(18, 'sessions', '0001_initial', '2024-12-06 01:49:16.036929'),
(19, 'sitio', '0001_initial', '2024-12-06 01:49:17.194724');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('9h2bye5cxtfnuizw0nup9uh6hpova7lu', '.eJxVjDsOwjAQBe_iGln-fyjpOYO19q5xADlSnFSIu0OkFNC-mXkvlmBbW9oGLWlCdmaSnX63DOVBfQd4h36beZn7ukyZ7wo_6ODXGel5Ody_gwajfWunpdMaihWhSBG891ilpFyyBYreaqtKRYeBrMlVCCSjfNZGqRptBMneH9O9N54:1tJNUT:VV6OGJaN2UJ1muMugCmiLYo2p99JoQb5Ca07SkLD5sg', '2024-12-20 01:50:45.522172');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

DROP TABLE IF EXISTS `estado`;
CREATE TABLE IF NOT EXISTS `estado` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `state` varchar(100) NOT NULL,
  `id_user_id` int NOT NULL,
  `id_servicio_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `estado_id_user_id_b87db52b` (`id_user_id`),
  KEY `estado_id_servicio_id_984a8cca` (`id_servicio_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario`
--

DROP TABLE IF EXISTS `horario`;
CREATE TABLE IF NOT EXISTS `horario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `id_calendario_id` bigint NOT NULL,
  `id_perfil_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `horario_id_calendario_id_1a6b14ed` (`id_calendario_id`),
  KEY `horario_id_perfil_id_21b67b19` (`id_perfil_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `imagenes`
--

DROP TABLE IF EXISTS `imagenes`;
CREATE TABLE IF NOT EXISTS `imagenes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `foto` varchar(200) NOT NULL,
  `id_servicio_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `imagenes_id_servicio_id_811f532b` (`id_servicio_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfil`
--

DROP TABLE IF EXISTS `perfil`;
CREATE TABLE IF NOT EXISTS `perfil` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fotoperfil` varchar(100) DEFAULT NULL,
  `fechanac` date NOT NULL,
  `verificacion` varchar(45) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `perfil`
--

INSERT INTO `perfil` (`id`, `fotoperfil`, `fechanac`, `verificacion`, `user_id`) VALUES
(1, '', '2001-01-25', '0', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio`
--

DROP TABLE IF EXISTS `servicio`;
CREATE TABLE IF NOT EXISTS `servicio` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fotoprincipal` varchar(100) DEFAULT NULL,
  `nombre` varchar(100) NOT NULL,
  `cate` varchar(45) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `costo` varchar(10) NOT NULL,
  `limite` int UNSIGNED NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `servicio_user_id_3ece3ce3` (`user_id`)
) ;

--
-- Volcado de datos para la tabla `servicio`
--

INSERT INTO `servicio` (`id`, `fotoprincipal`, `nombre`, `cate`, `descripcion`, `costo`, `limite`, `user_id`) VALUES
(2, 'fotos_services/Apple_Yit2jTB.png', 'Tecnico Apple', '1', '1', '25000', 5, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ticket`
--

DROP TABLE IF EXISTS `ticket`;
CREATE TABLE IF NOT EXISTS `ticket` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `descripcion` longtext NOT NULL,
  `estado` varchar(20) NOT NULL,
  `creado` datetime(6) NOT NULL,
  `actualizado` datetime(6) NOT NULL,
  `servicio_id` bigint DEFAULT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_servicio_id_12012a55` (`servicio_id`),
  KEY `ticket_usuario_id_e12b91ed` (`usuario_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `ticket`
--

INSERT INTO `ticket` (`id`, `descripcion`, `estado`, `creado`, `actualizado`, `servicio_id`, `usuario_id`) VALUES
(1, 'Aloka', '0', '2024-12-06 03:15:58.282747', '2024-12-06 03:15:58.282747', NULL, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
