<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInitefa014b3ab807ae21ffc659c723b694b
{
    public static $prefixLengthsPsr4 = array (
        'B' => 
        array (
            'BluePayment\\' => 12,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'BluePayment\\' => 
        array (
            0 => __DIR__ . '/../..' . '/src',
        ),
    );

    public static $classMap = array (
        'BluePayment' => __DIR__ . '/../..' . '/bluepayment.php',
        'BluePayment\\Adapter\\ConfigurationAdapter' => __DIR__ . '/../..' . '/src/Adapter/ConfigurationAdapter.php',
        'BluePayment\\Analyse\\Amplitude' => __DIR__ . '/../..' . '/src/Analyse/Amplitude.php',
        'BluePayment\\Analyse\\AnalyticsTracking' => __DIR__ . '/../..' . '/src/Analyse/AnalyticsTracking.php',
        'BluePayment\\Api\\BlueAPI' => __DIR__ . '/../..' . '/src/Api/BlueAPI.php',
        'BluePayment\\Api\\BlueGateway' => __DIR__ . '/../..' . '/src/Api/BlueGateway.php',
        'BluePayment\\Api\\BlueGatewayChannels' => __DIR__ . '/../..' . '/src/Api/BlueGatewayChannels.php',
        'BluePayment\\Api\\BlueGatewayTransfers' => __DIR__ . '/../..' . '/src/Api/BlueGatewayTransfers.php',
        'BluePayment\\Api\\GatewayInterface' => __DIR__ . '/../..' . '/src/Api/GatewayInterface.php',
        'BluePayment\\Config\\Config' => __DIR__ . '/../..' . '/src/Config/Config.php',
        'BluePayment\\Configure\\Configure' => __DIR__ . '/../..' . '/src/Configure/Configure.php',
        'BluePayment\\Hook\\AbstractHook' => __DIR__ . '/../..' . '/src/Hook/AbstractHook.php',
        'BluePayment\\Hook\\Admin' => __DIR__ . '/../..' . '/src/Hook/Admin.php',
        'BluePayment\\Hook\\Design' => __DIR__ . '/../..' . '/src/Hook/Design.php',
        'BluePayment\\Hook\\HookDispatcher' => __DIR__ . '/../..' . '/src/Hook/HookDispatcher.php',
        'BluePayment\\Hook\\Payment' => __DIR__ . '/../..' . '/src/Hook/Payment.php',
        'BluePayment\\Install\\Installer' => __DIR__ . '/../..' . '/src/Install/Installer.php',
        'BluePayment\\Service\\FactoryPaymentMethods' => __DIR__ . '/../..' . '/src/Service/FactoryPaymentMethods.php',
        'BluePayment\\Service\\Gateway' => __DIR__ . '/../..' . '/src/Service/Gateway.php',
        'BluePayment\\Service\\PaymentMethods\\AliorInstallment' => __DIR__ . '/../..' . '/src/Service/PaymentMethods/AliorInstallment.php',
        'BluePayment\\Service\\PaymentMethods\\Blik' => __DIR__ . '/../..' . '/src/Service/PaymentMethods/Blik.php',
        'BluePayment\\Service\\PaymentMethods\\Card' => __DIR__ . '/../..' . '/src/Service/PaymentMethods/Card.php',
        'BluePayment\\Service\\PaymentMethods\\GatewayType' => __DIR__ . '/../..' . '/src/Service/PaymentMethods/GatewayType.php',
        'BluePayment\\Service\\PaymentMethods\\InternetTransfer' => __DIR__ . '/../..' . '/src/Service/PaymentMethods/InternetTransfer.php',
        'BluePayment\\Service\\PaymentMethods\\MainGateway' => __DIR__ . '/../..' . '/src/Service/PaymentMethods/MainGateway.php',
        'BluePayment\\Service\\PaymentMethods\\Smartney' => __DIR__ . '/../..' . '/src/Service/PaymentMethods/Smartney.php',
        'BluePayment\\Service\\PaymentMethods\\VirtualWallet' => __DIR__ . '/../..' . '/src/Service/PaymentMethods/VirtualWallet.php',
        'BluePayment\\Service\\Refund' => __DIR__ . '/../..' . '/src/Service/Refund.php',
        'BluePayment\\Service\\Transactions' => __DIR__ . '/../..' . '/src/Service/Transactions.php',
        'BluePayment\\Statuses\\CustomStatus' => __DIR__ . '/../..' . '/src/Statuses/CustomStatus.php',
        'BluePayment\\Statuses\\OrderStatusMessageDictionary' => __DIR__ . '/../..' . '/src/Statuses/OrderStatusMessageDictionary.php',
        'BluePayment\\Until\\AdminHelper' => __DIR__ . '/../..' . '/src/Until/AdminHelper.php',
        'BluePayment\\Until\\Helper' => __DIR__ . '/../..' . '/src/Until/Helper.php',
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInitefa014b3ab807ae21ffc659c723b694b::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInitefa014b3ab807ae21ffc659c723b694b::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInitefa014b3ab807ae21ffc659c723b694b::$classMap;

        }, null, ClassLoader::class);
    }
}
