/** 
 * ERC20 Spec - Invariant prooving that address zero has balance zero
**/

methods {
  function balanceOf(address) external returns uint256 envfree;
}

/** 
 * @title Address has zero balance
 * This invaiant is violated by `transfer` and `transferFrom`
**/
invariant zeroHasNoBalance()
  balanceOf(0) == 0;