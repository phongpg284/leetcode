/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  this.cache = {};

  return function (...args) {
    const key = args.join("_");
    if (key in this.cache) {
      return this.cache[key];
    }
    const result = fn(...args);
    this.cache[key] = result;

    return result;
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
