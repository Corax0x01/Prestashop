<?php
/* Smarty version 3.1.43, created on 2022-11-01 20:14:30
  from 'module:blockwishlistviewstemplat' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.43',
  'unifunc' => 'content_63617016ca3f51_18717222',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'a6cf26c62a3d814aa3a70f19a62034bfdce54c8a' => 
    array (
      0 => 'module:blockwishlistviewstemplat',
      1 => 1667329647,
      2 => 'module',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_63617016ca3f51_18717222 (Smarty_Internal_Template $_smarty_tpl) {
?><!-- begin /var/www/html/modules/blockwishlist/views/templates/components/toast.tpl -->
<div
    class="wishlist-toast"
    data-rename-wishlist-text="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Wishlist name modified!','d'=>'Modules.Blockwishlist.Shop'),$_smarty_tpl ) );?>
"
    data-added-wishlist-text="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Product added to wishlist!','d'=>'Modules.Blockwishlist.Shop'),$_smarty_tpl ) );?>
"
    data-create-wishlist-text="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Wishlist created!','d'=>'Modules.Blockwishlist.Shop'),$_smarty_tpl ) );?>
"
    data-delete-wishlist-text="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Wishlist deleted!','d'=>'Modules.Blockwishlist.Shop'),$_smarty_tpl ) );?>
"
    data-copy-text="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Share link copied!','d'=>'Modules.Blockwishlist.Shop'),$_smarty_tpl ) );?>
"
    data-delete-product-text="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Product deleted!','d'=>'Modules.Blockwishlist.Shop'),$_smarty_tpl ) );?>
"
  ></div>
<!-- end /var/www/html/modules/blockwishlist/views/templates/components/toast.tpl --><?php }
}
