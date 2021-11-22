-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2019 at 02:54 PM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `homeappliance`
--

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_billing`
--

CREATE TABLE `appliance_app_billing` (
  `id` int(11) NOT NULL,
  `bill_date` date NOT NULL,
  `gst` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `shipping_charge` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_deliverydtails`
--

CREATE TABLE `appliance_app_deliverydtails` (
  `id` int(11) NOT NULL,
  `Deliverydate` date NOT NULL,
  `Trackingno` varchar(200) NOT NULL,
  `Packingstatus` varchar(200) NOT NULL,
  `Shippingstatus` varchar(200) NOT NULL,
  `Delivery_status` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_exchangeoffer`
--

CREATE TABLE `appliance_app_exchangeoffer` (
  `id` int(11) NOT NULL,
  `exchngname` varchar(200) NOT NULL,
  `dscrptn` varchar(500) NOT NULL,
  `discount` int(11) NOT NULL,
  `Start_date` date NOT NULL,
  `finish_date` date NOT NULL,
  `coupon_code` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_mb_scheme`
--

CREATE TABLE `appliance_app_mb_scheme` (
  `id` int(11) NOT NULL,
  `Schemeno` varchar(200) NOT NULL,
  `Customer_name` varchar(200) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Email_Id` varchar(200) NOT NULL,
  `Mobileno` varchar(200) NOT NULL,
  `Month` varchar(200) NOT NULL,
  `Winner` varchar(200) NOT NULL,
  `Coupon_code` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appliance_app_mb_scheme`
--

INSERT INTO `appliance_app_mb_scheme` (`id`, `Schemeno`, `Customer_name`, `Address`, `Email_Id`, `Mobileno`, `Month`, `Winner`, `Coupon_code`) VALUES
(1, 'A1', 'Sumitra Patil', '3rd cross tolnaka dharwad', 'sumitra@gmail.com', '98745611122', 'January', '--', 'X1X'),
(2, 'A2', 'Suresh R', '5th cross whitefield Dhaarwad', 'suresh@gmail.com', '9874555566', 'January', '-----', 'X2X'),
(3, 'A3', 'Pavan T', '8th cross nilkant Dharwad', 'pavan@gmail.com', '9685741222', 'January', '--', 'X3X'),
(4, 'A4', 'Dhinkar Alnavar', '6th cross vayaur Dharwad', 'dhinkar@gmail.com', '8574569999', 'January', '---', 'X4X'),
(5, 'A5', 'Yuvraj S', 'Near bank of baroda 6th cross Dharwad', 'yuvraj@gmail.com', '9874566555', 'January', '--', 'X5X'),
(6, 'A6', 'Rithika T', 'uvapeth nagar Dharwad', 'rithika@gmail.com', '9874521453', 'January', '--', 'X6X');

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_order_details`
--

CREATE TABLE `appliance_app_order_details` (
  `id` int(11) NOT NULL,
  `Order_date` date NOT NULL,
  `Quantity` int(11) NOT NULL,
  `Unit_price` int(11) NOT NULL,
  `GST` int(11) NOT NULL,
  `CGST` int(11) NOT NULL,
  `SGST` int(11) NOT NULL,
  `Total_price` int(11) NOT NULL,
  `Order_status` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_payment`
--

CREATE TABLE `appliance_app_payment` (
  `id` int(11) NOT NULL,
  `Paymenttype` varchar(200) NOT NULL,
  `BankName` varchar(200) NOT NULL,
  `BankBranch` varchar(200) NOT NULL,
  `Couponno` varchar(200) NOT NULL,
  `Amountpaid` int(11) NOT NULL,
  `Paymentdate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_procategory`
--

CREATE TABLE `appliance_app_procategory` (
  `id` int(11) NOT NULL,
  `cat_name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appliance_app_procategory`
--

INSERT INTO `appliance_app_procategory` (`id`, `cat_name`) VALUES
(2, 'Cooker'),
(3, 'Gas Stove'),
(4, 'Mixer Grinder'),
(5, 'Aluminium fry pan'),
(6, 'Steel spoon'),
(7, 'Hand Blender'),
(8, 'Aluminium kadai'),
(9, 'Induction'),
(10, 'Steel utensil'),
(11, 'Steel bowl'),
(12, 'Steel spoon'),
(13, 'Iron box'),
(14, 'Tiffin box'),
(15, 'Non-Stick tava'),
(16, 'Steel Plate'),
(17, 'Dinner set'),
(18, 'China wear'),
(19, 'Kitchen wear');

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_product`
--

CREATE TABLE `appliance_app_product` (
  `id` int(11) NOT NULL,
  `pname` varchar(200) NOT NULL,
  `description` varchar(500) NOT NULL,
  `image1` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `gst` int(11) NOT NULL,
  `cgst` int(11) NOT NULL,
  `sgst` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `discount` int(11) NOT NULL,
  `category` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_purchase_items`
--

CREATE TABLE `appliance_app_purchase_items` (
  `id` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `Purchase_date` date NOT NULL,
  `Total_price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appliance_app_purchase_items`
--

INSERT INTO `appliance_app_purchase_items` (`id`, `Quantity`, `Purchase_date`, `Total_price`) VALUES
(1, 20, '2019-02-04', 1000),
(2, 23, '2019-02-04', 1000),
(3, 23, '2019-02-04', 1000),
(4, 23, '2019-02-04', 1000),
(5, 20, '2019-02-04', 2000),
(6, 20, '2019-02-04', 2000);

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_service`
--

CREATE TABLE `appliance_app_service` (
  `id` int(11) NOT NULL,
  `Product_name` varchar(200) NOT NULL,
  `Description` varchar(500) NOT NULL,
  `Price` int(11) NOT NULL,
  `Service_men_name` varchar(200) NOT NULL,
  `Service_men_Mbno` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appliance_app_service`
--

INSERT INTO `appliance_app_service` (`id`, `Product_name`, `Description`, `Price`, `Service_men_name`, `Service_men_Mbno`) VALUES
(1, 'Gas Stove', 'vissel and gasket repai', 50, 'Swaroop K', '9874566661'),
(2, 'Hand Blender', 'blades repair and other', 60, 'Nithin B', '9874563211'),
(3, 'Hand Blender', 'blades repair and other', 60, 'Nithin B', '9874563211'),
(4, 'Hand Blender', 'blades repair and other', 60, 'Nithin B', '9874563211'),
(5, 'Hand Blender', 'blades repair and other', 60, 'Nithin B', '9874563211');

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_stockitems`
--

CREATE TABLE `appliance_app_stockitems` (
  `id` int(11) NOT NULL,
  `transaction_no` varchar(200) NOT NULL,
  `price` int(11) NOT NULL,
  `gst` int(11) NOT NULL,
  `cgst` int(11) NOT NULL,
  `sgst` int(11) NOT NULL,
  `transport_charges` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `sdate` date NOT NULL,
  `sold_out` int(11) NOT NULL,
  `availability` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appliance_app_stockitems`
--

INSERT INTO `appliance_app_stockitems` (`id`, `transaction_no`, `price`, `gst`, `cgst`, `sgst`, `transport_charges`, `total`, `sdate`, `sold_out`, `availability`) VALUES
(1, '10001', 2000, 30, 20, 10, 100, 1000, '2019-02-06', 20, 10),
(2, '1111', 500, 20, 15, 5, 100, 800, '2019-02-06', 30, 10),
(3, '1112', 600, 20, 13, 7, 150, 900, '2019-02-07', 10, 30),
(4, '1113', 1500, 20, 12, 8, 80, 1800, '2019-02-06', 5, 50),
(5, '1114', 3000, 25, 10, 15, 250, 3400, '2019-02-07', 45, 10),
(6, '1115', 150, 10, 5, 5, 50, 200, '2019-02-05', 5, 30);

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_supplier`
--

CREATE TABLE `appliance_app_supplier` (
  `id` int(11) NOT NULL,
  `supplier_name` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `mobile_no` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `quantity` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appliance_app_supplier`
--

INSERT INTO `appliance_app_supplier` (`id`, `supplier_name`, `address`, `mobile_no`, `email`, `product_name`, `quantity`) VALUES
(1, 'Mahesh', 'yallanka Banglore', '9874566666', 'mahesh@gmail.com', 'Cooker', '50'),
(2, 'Girish H', 'old busstand Hubli', '9874563333', 'girish@gmail.com', 'Gas stove', '10'),
(3, 'Prakash L', 'Hossur road Hubli', '8574566666', 'prakash@gmail.com', 'Aluminium vessel', '50'),
(4, 'Dhanpal H', 'old town Hubli', '8745555555', 'dhanpal@gmail.com', 'Hand blender', '30'),
(5, 'Shantik G', 'BesideRamesh appartment, 3rd cross Hubli', '8547965444', 'shantik@gmail.com', 'Steel spoon', '40'),
(6, 'Sanjay K', 'old busstand Hubli', '9874521444', 'sanjay@gmail.com', 'Iron box', '40');

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_userlogin`
--

CREATE TABLE `appliance_app_userlogin` (
  `id` int(11) NOT NULL,
  `emailid` varchar(200) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appliance_app_userlogin`
--

INSERT INTO `appliance_app_userlogin` (`id`, `emailid`, `password`, `utype`) VALUES
(1, 'admin@gmail.com', 'guru', 'admin'),
(2, 'customer@gmail.com', '111', 'customer');

-- --------------------------------------------------------

--
-- Table structure for table `appliance_app_userregistration`
--

CREATE TABLE `appliance_app_userregistration` (
  `id` int(11) NOT NULL,
  `Firstname` varchar(200) NOT NULL,
  `Lastname` varchar(200) NOT NULL,
  `Address` varchar(400) NOT NULL,
  `City` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `MobileNumber` varchar(10) NOT NULL,
  `EmailID` varchar(100) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `ConfirmPassword` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appliance_app_userregistration`
--

INSERT INTO `appliance_app_userregistration` (`id`, `Firstname`, `Lastname`, `Address`, `City`, `Gender`, `Pincode`, `MobileNumber`, `EmailID`, `Password`, `ConfirmPassword`) VALUES
(1, 'Anusha', 'Bhardvaaj', '4th street tilakwadi', 'Dharwad', 'female', 580001, '9696857447', 'anusha@gmail.com', '123*aaaa', '123*aaaaaaa'),
(2, 'Anusha', 'Bhardvaaj', '4th street tilakwadi', 'Dharwad', 'female', 580001, '9696857447', 'anusha@gmail.com', '123*aaaa', '123*aaaaaaa'),
(3, 'Swapna', 'Patil', 'Rajatgiri', 'Dharwad', 'female', 584001, '9874563211', 'swapna@gmail.com', '1234', '1234'),
(4, 'Mukesh', 'Ambani', '6th cross hallur', 'Dharwad', 'male', 580002, '8596741233', 'mukesh@gmail.com', '7894', '7894'),
(5, 'Mukesh', 'Ambani', '6th cross hallur', 'Dharwad', 'male', 580002, '8596741233', 'mukesh@gmail.com', '7894', '7894'),
(6, 'Mukesh', 'Ambani', '6th cross hallur', 'Dharwad', 'male', 580002, '8596741233', 'mukesh@gmail.com', '7894', '7894');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-02-24 12:26:55.969739'),
(2, 'auth', '0001_initial', '2019-02-24 12:27:20.274129'),
(3, 'admin', '0001_initial', '2019-02-24 12:27:28.704612'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-02-24 12:27:28.885622'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-02-24 12:27:29.162638'),
(6, 'appliance_app', '0001_initial', '2019-02-24 12:27:29.756672'),
(7, 'appliance_app', '0002_userregistration', '2019-02-24 12:27:32.165810'),
(8, 'appliance_app', '0003_auto_20190206_1502', '2019-02-24 12:27:44.276502'),
(9, 'appliance_app', '0004_remove_category_category_id', '2019-02-24 12:27:45.354564'),
(10, 'appliance_app', '0005_auto_20190206_1523', '2019-02-24 12:28:09.232930'),
(11, 'appliance_app', '0006_auto_20190218_1800', '2019-02-24 12:28:12.933141'),
(12, 'appliance_app', '0007_auto_20190218_1928', '2019-02-24 12:28:13.141153'),
(13, 'appliance_app', '0008_auto_20190218_1930', '2019-02-24 12:28:32.291249'),
(14, 'appliance_app', '0009_auto_20190218_1935', '2019-02-24 12:28:33.054292'),
(15, 'appliance_app', '0010_auto_20190219_1844', '2019-02-24 12:28:35.156412'),
(16, 'appliance_app', '0011_auto_20190219_1849', '2019-02-24 12:28:35.653441'),
(17, 'appliance_app', '0012_auto_20190219_1858', '2019-02-24 12:28:36.334480'),
(18, 'appliance_app', '0013_auto_20190219_1922', '2019-02-24 12:28:36.642497'),
(19, 'appliance_app', '0014_auto_20190219_1938', '2019-02-24 12:28:39.330651'),
(20, 'appliance_app', '0015_auto_20190222_1551', '2019-02-24 12:28:40.051692'),
(21, 'appliance_app', '0016_auto_20190223_1443', '2019-02-24 12:28:50.226274');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appliance_app_billing`
--
ALTER TABLE `appliance_app_billing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_deliverydtails`
--
ALTER TABLE `appliance_app_deliverydtails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_exchangeoffer`
--
ALTER TABLE `appliance_app_exchangeoffer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_mb_scheme`
--
ALTER TABLE `appliance_app_mb_scheme`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_order_details`
--
ALTER TABLE `appliance_app_order_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_payment`
--
ALTER TABLE `appliance_app_payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_procategory`
--
ALTER TABLE `appliance_app_procategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_product`
--
ALTER TABLE `appliance_app_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_purchase_items`
--
ALTER TABLE `appliance_app_purchase_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_service`
--
ALTER TABLE `appliance_app_service`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_stockitems`
--
ALTER TABLE `appliance_app_stockitems`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_supplier`
--
ALTER TABLE `appliance_app_supplier`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_userlogin`
--
ALTER TABLE `appliance_app_userlogin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appliance_app_userregistration`
--
ALTER TABLE `appliance_app_userregistration`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appliance_app_billing`
--
ALTER TABLE `appliance_app_billing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `appliance_app_deliverydtails`
--
ALTER TABLE `appliance_app_deliverydtails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `appliance_app_exchangeoffer`
--
ALTER TABLE `appliance_app_exchangeoffer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `appliance_app_mb_scheme`
--
ALTER TABLE `appliance_app_mb_scheme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `appliance_app_order_details`
--
ALTER TABLE `appliance_app_order_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `appliance_app_payment`
--
ALTER TABLE `appliance_app_payment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `appliance_app_procategory`
--
ALTER TABLE `appliance_app_procategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `appliance_app_product`
--
ALTER TABLE `appliance_app_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `appliance_app_purchase_items`
--
ALTER TABLE `appliance_app_purchase_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `appliance_app_service`
--
ALTER TABLE `appliance_app_service`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `appliance_app_stockitems`
--
ALTER TABLE `appliance_app_stockitems`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `appliance_app_supplier`
--
ALTER TABLE `appliance_app_supplier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `appliance_app_userlogin`
--
ALTER TABLE `appliance_app_userlogin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `appliance_app_userregistration`
--
ALTER TABLE `appliance_app_userregistration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
