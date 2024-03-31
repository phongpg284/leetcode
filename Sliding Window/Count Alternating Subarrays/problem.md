## 3101. Count Alternating Subarrays

<https://leetcode.com/problems/count-alternating-subarrays/>

<div class="elfjS" data-track-load="description_content"><p>You are given a <span data-keyword="binary-array" class=" cursor-pointer relative text-dark-blue-s text-sm"><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:r10:"><div>binary array</div></div><div style="position: fixed; z-index: 40; inset: 0px auto auto 0px; transform: translate(160px, 183px);"></div></div></div></span> <code>nums</code>.</p>

<p>We call a <span data-keyword="subarray-nonempty" class=" cursor-pointer relative text-dark-blue-s text-sm"><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:r12:"><div>subarray</div></div><div style="position: fixed; z-index: 40; inset: 0px auto auto 0px; transform: translate(111px, 220px);"></div></div></div></span> <strong>alternating</strong> if <strong>no</strong> two <strong>adjacent</strong> elements in the subarray have the <strong>same</strong> value.</p>

<p>Return <em>the number of alternating subarrays in </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The following subarrays are alternating: <code>[0]</code>, <code>[1]</code>, <code>[1]</code>, <code>[1]</code>, and <code>[0,1]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
 <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
 <li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
</div>
