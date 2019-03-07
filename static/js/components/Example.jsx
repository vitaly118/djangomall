import React, { useState } from 'react';
export const Example = function () {
      const [count, setCount] = useState(0);
        const [name, setName] = useState();

          return (
                      <div>
                            <p><i className="fas fa-shopping-cart"></i>{count}, {name}</p>
                                  <input type="radio" name="product" value="product1" onClick={(e) => setName(e.target.value)} />
                                        <input type="radio" name="product" onClick={() => setName('product2')} />
                                              <button className="btn btn-success" onClick={() => setCount(count + 1)}>
                                                      Add to Cart
                                                            </button>
                                                                </div>
                                                                  );
}
