methods {
  function start() external;
  function setOperator() external;
  function bid() external;
  function bidFor() external;
  function withdrawAmount() external;
  function withdrawFor() external;
  function end() external;

  function highestBidder() external returns address envfree;
  function highestBid() external returns uint256  envfree;
  function bids(address) external returns uint256 envfree;
}

invariant highestBidGreaterThanOtherBids(address a)
  highestBid() >= bids(a);

invariant highestBidderHasHighestBid()
  (highestBidder() != 0) => highestBid() == bids(highestBidder());