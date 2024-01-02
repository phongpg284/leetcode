var TimeLimitedCache = function () {
  this.store = {};
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  let res = false;
  exist_data = this.store[key];
  if (exist_data) {
    const { duration, date } = exist_data;
    res = date + duration > Date.now();
  }
  this.store[key] = { value, duration, date: Date.now() };
  return res;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  const exist_data = this.store[key];
  if (!exist_data) {
    return -1;
  }
  const { value, duration, date } = exist_data;
  if (date + duration > Date.now()) {
    return value;
  }

  delete this.store[key];
  return -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  let count = 0;
  for (const { date, duration } of Object.values(this.store)) {
    if (date + duration > Date.now()) {
      count += 1;
    }
  }
  return count;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
