# -*- coding: utf-8 -*-
import os

new_content = """<!-- ═══ PAGE HEADER ═══ -->
<div class="pt-24 md:pt-32 pb-16 md:pb-24 bg-primary-900 relative overflow-hidden">
  <div class="absolute inset-0 opacity-10" style="background-image:url('data:image/svg+xml,%3Csvg width=\\'60\\' height=\\'60\\' viewBox=\\'0 0 60 60\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cpath d=\\'M54.627 0l1.43 1.43-56.056 56.056-1.43-1.43L54.627 0zm-33.94 0l1.43 1.43-22.118 22.117-1.43-1.43L20.686 0zm33.941 33.941l1.43 1.43-22.118 22.117-1.43-1.43 22.118-22.117z\\' fill=\\'%23ffffff\\' fill-opacity=\\'1\\' fill-rule=\\'evenodd\\'/%3E%3C/svg%3E');"></div>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 relative z-10 text-center">
    <div class="inline-flex items-center gap-2 bg-white/10 backdrop-blur-md border border-white/20 text-white text-xs font-semibold px-4 py-1.5 rounded-full mb-6 bangla">
      <i class="fa-solid fa-book-open text-primary-300"></i> আমাদের কথা
    </div>
    <h1 class="text-4xl md:text-5xl lg:text-6xl font-black text-white mb-6 bangla leading-tight">কেন আমি মাটিতে নামলাম</h1>
    <p class="text-primary-100 bangla text-base md:text-lg leading-relaxed max-w-3xl mx-auto mb-8">
      বাজারের খাবার নিয়ে এক ভয় থেকে আমার শুরু। আজ আমার একটা খামার আছে, একটা খোলা খাতা আছে, আর একটা নিয়ম আছে: <strong class="text-white">যে খাবার কীভাবে ফলেছে আমি বলতে পারি না, সেটা আমি বিক্রি করব না।</strong> এই পেজে আমি বলেছি আমি কেন এটা করছি, কী করছি, কোন নিয়মে করছি, আর কোথায় যেতে চাই।
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <a href="#rules" class="bg-primary-500 hover:bg-primary-600 text-white font-bold px-8 py-3.5 rounded-full transition-colors bangla shadow-lg">
        আমার নিয়মগুলো দেখুন ↓
      </a>
      <a href="https://wa.me/8801XXXXXXXXX" target="_blank" class="bg-white/10 hover:bg-white/20 border border-white/30 text-white font-bold px-8 py-3.5 rounded-full transition-colors bangla">
        ফার্মে এসে নিজ চোখে দেখুন
      </a>
    </div>
  </div>
</div>

<!-- ═══ WHY WE DO THIS ═══ -->
<section class="py-20 bg-white">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 fade-in">
    <h2 class="text-3xl md:text-4xl font-black text-gray-900 mb-8 bangla text-center">ভয়টা কোথা থেকে এল</h2>
    <div class="prose prose-lg bangla text-gray-600 max-w-none mb-12">
      <p>আমরা শহরে যা কিনি, তার কোথায় কী মেশানো হয়েছে বা কতটা ওষুধ পড়েছে, ক্রেতা হিসেবে জানার কোনো উপায় থাকে না। আমরা শুধু বিশ্বাস করি, আর বিশ্বাসটা অনেক সময় ভেঙে যায়।</p>
      <p>একদিন বাজার থেকে কিছু আম কিনে এনেছিলাম, রঙে এতটাই সুন্দর যে না কিনে পারিনি। বাসায় এসে আমার ছোট্ট ছেলে সেই আম হাতে নিয়ে খেতে যাচ্ছিল — ঠিক তখনই খেয়াল করলাম, আমের বোঁটার কাছে এক ধরনের অদ্ভুত রাসায়নিক গন্ধ। খোঁজ নিয়ে জানলাম, এটা ক্যালসিয়াম কার্বাইড দিয়ে পাকানো। আমি সেদিন ছেলের হাত থেকে আমটা সরিয়ে নিয়েছিলাম, কিন্তু প্রশ্নটা থেকে গিয়েছিল — এতদিন না জেনে আমরা কী খাইয়েছি?</p>
      <p>সেই রাতেই সিদ্ধান্ত নিই — এই চক্র থেকে বের হতেই হবে। শুধু নিজের পরিবারের জন্য না, আমার মতো যত পরিবার একই ভয়ে আছে, তাদের জন্যও।</p>
    </div>
    
    <div class="grid md:grid-cols-2 gap-8">
      <div class="bg-primary-50 p-8 rounded-2xl border border-primary-100">
        <div class="w-12 h-12 bg-primary-500 rounded-xl flex items-center justify-center mb-5 shadow-lg shadow-primary-500/30">
          <i class="fa-solid fa-leaf text-white text-xl"></i>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3 bangla">১. নিরাপদ খাবার, নিরাপদ কৃষি</h3>
        <p class="text-gray-600 bangla text-sm leading-relaxed">
          আমি এমন খাবার চাই, যেটা নিজের পরিবারকে খাওয়াতে পারি, আর অন্যকেও নির্ভয়ে দিতে পারি। কৃষি এমনভাবে হোক, যাতে মাটি, পানি আর চাষি, সবাই নিরাপদ থাকে।
        </p>
      </div>
      <div class="bg-amber-50 p-8 rounded-2xl border border-amber-100">
        <div class="w-12 h-12 bg-amber-500 rounded-xl flex items-center justify-center mb-5 shadow-lg shadow-amber-500/30">
          <i class="fa-solid fa-handshake text-white text-xl"></i>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3 bangla">২. ধৈর্যশীল মানুষের সঙ্গে পথ চলা</h3>
        <p class="text-gray-600 bangla text-sm leading-relaxed">
          এই কাজ একা দ্রুত করা যায় না। যাঁরা নিরাপদ কৃষিতে বিশ্বাস করেন, তাঁরা চাইলে আমার সঙ্গে অংশীদার হতে পারেন। সেটা নিয়ে আলাদা পেজে খোলাখুলি লিখেছি।
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ═══ WHAT WE DO ═══ -->
<section class="py-20 bg-gray-50 border-y border-gray-100">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 fade-in">
    <h2 class="text-3xl font-black text-gray-900 mb-10 bangla text-center">আমরা কী করি</h2>
    <div class="grid md:grid-cols-2 gap-6">
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 flex gap-4 items-start">
        <div class="w-10 h-10 bg-primary-100 text-primary-600 rounded-full flex items-center justify-center flex-shrink-0 mt-1"><i class="fa-solid fa-tractor"></i></div>
        <div>
          <h4 class="font-bold text-gray-900 mb-2 bangla text-lg">খামার গড়ছি</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">বগুড়ার মহাস্থানগড়ে ৭ বিঘা উঁচু জমি, ৫ বছরের লিজে। শুরুতে ৫টা ফসল: ড্রাগন ফল, চুইঝাল, আদা-হলুদ, হলুদ তরমুজ ও স্ট্রবেরি, আর সজিনা। ধীরে ধীরে বড় হবে।</p>
        </div>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 flex gap-4 items-start">
        <div class="w-10 h-10 bg-primary-100 text-primary-600 rounded-full flex items-center justify-center flex-shrink-0 mt-1"><i class="fa-solid fa-seedling"></i></div>
        <div>
          <h4 class="font-bold text-gray-900 mb-2 bangla text-lg">স্ট্রবেরি দিয়ে হাতে-কলমে শিখছি</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">২৮ শতক জমিতে ১,২০০টি মাদার চারা। এখান থেকে কাপে চারা তৈরি করে বিক্রির পরিকল্পনা আছে, ফল আসবে ডিসেম্বর–ফেব্রুয়ারিতে।</p>
        </div>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 flex gap-4 items-start">
        <div class="w-10 h-10 bg-primary-100 text-primary-600 rounded-full flex items-center justify-center flex-shrink-0 mt-1"><i class="fa-solid fa-book-open-reader"></i></div>
        <div>
          <h4 class="font-bold text-gray-900 mb-2 bangla text-lg">প্রতিটা টাকার হিসাব খোলা রাখি</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">"খোলা খাতা" পেজে লাভের সঙ্গে লোকসানের সম্ভাবনাও দেখিয়েছি।</p>
        </div>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 flex gap-4 items-start">
        <div class="w-10 h-10 bg-primary-100 text-primary-600 rounded-full flex items-center justify-center flex-shrink-0 mt-1"><i class="fa-solid fa-video"></i></div>
        <div>
          <h4 class="font-bold text-gray-900 mb-2 bangla text-lg">পুরো যাত্রা ভিডিওতে দেখাই</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">বর্ষার ধাক্কা, ভুল, শেখা, সাফল্য, সবই। সরাসরি ক্রেতার কাছে পৌঁছাই বগুড়ার সুপারশপ আর ফেসবুক পেজের মাধ্যমে।</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ RULES ═══ -->
<section id="rules" class="py-20 bg-white">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 fade-in">
    <div class="text-center mb-12">
      <span class="inline-block bg-primary-50 text-primary-700 font-bold px-4 py-1.5 rounded-full text-xs tracking-widest uppercase mb-4 bangla border border-primary-100">খোলা খাতা</span>
      <h2 class="text-3xl md:text-4xl font-black text-gray-900 mb-4 bangla">আমাদের নিরাপদ কৃষির নিয়ম</h2>
      <p class="text-gray-500 bangla max-w-2xl mx-auto">লক্ষ্য আর আজকের নিয়ম — দুটো আলাদা কথা</p>
    </div>

    <div class="flex flex-col md:flex-row gap-6 mb-12">
      <div class="flex-1 bg-green-50 p-6 rounded-2xl border border-green-100">
        <h4 class="text-green-800 font-bold mb-2 bangla text-lg flex items-center gap-2"><i class="fa-solid fa-bullseye"></i> আমাদের লক্ষ্য</h4>
        <p class="text-green-700 bangla text-sm">বিষমুক্ত কৃষির দিকে এগোনো</p>
      </div>
      <div class="flex-1 bg-blue-50 p-6 rounded-2xl border border-blue-100">
        <h4 class="text-blue-800 font-bold mb-2 bangla text-lg flex items-center gap-2"><i class="fa-solid fa-shield-check"></i> আজকের প্রতিশ্রুতি</h4>
        <p class="text-blue-700 bangla text-sm">নিরাপদ কৃষি: যা করি নিয়ম মেনে, খাতায় লিখে, ক্রেতাকে জানিয়ে</p>
      </div>
    </div>

    <p class="text-gray-600 bangla mb-10 max-w-3xl mx-auto text-center leading-relaxed">
      আমি এখনই "রাসায়নিকমুক্ত" বলছি না, কারণ সেটা সত্য হবে না। বর্ষায় ছত্রাক, পোকা আর আগাছা আমাকে ওষুধ ব্যবহার করতে বাধ্য করেছে, আর আমি সেটা লুকাই না। যা বলছি, তা হলো আমি কীভাবে ওষুধ ব্যবহার করি।
    </p>

    <h3 class="text-2xl font-black text-gray-900 mb-6 bangla text-center">আমার ৬টা নিয়ম</h3>
    <div class="grid md:grid-cols-2 gap-x-8 gap-y-6 mb-16 max-w-4xl mx-auto">
      <div class="flex gap-4">
        <div class="w-8 h-8 rounded-full bg-primary-100 text-primary-700 font-black flex items-center justify-center flex-shrink-0 mt-0.5 bangla">১</div>
        <div>
          <h4 class="font-bold text-gray-900 mb-1 bangla">আগে প্রতিরোধ, পরে ওষুধ</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">ড্রেনেজ ঠিক রাখা, মাটির পুষ্টি সংশোধন, ট্রাইকোডার্মা, নিম খৈল, ফাঁদ, নিড়ানি, এগুলোই আমার প্রথম উপায়।</p>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="w-8 h-8 rounded-full bg-primary-100 text-primary-700 font-black flex items-center justify-center flex-shrink-0 mt-0.5 bangla">২</div>
        <div>
          <h4 class="font-bold text-gray-900 mb-1 bangla">ওষুধ শেষ উপায়</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">দরকার হলে শুধু লেবেলে অনুমোদিত ওষুধ, লেবেলের মাত্রায়, প্রয়োজনের বেশি নয়।</p>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="w-8 h-8 rounded-full bg-primary-100 text-primary-700 font-black flex items-center justify-center flex-shrink-0 mt-0.5 bangla">৩</div>
        <div>
          <h4 class="font-bold text-gray-900 mb-1 bangla">অপেক্ষার সময় মানা</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">প্রতিটা ওষুধের জন্য লেবেলে নির্ধারিত অপেক্ষার সময় পূর্ণ না হলে আমি সেই ফসল তুলব না, বিক্রিও করব না।</p>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="w-8 h-8 rounded-full bg-primary-100 text-primary-700 font-black flex items-center justify-center flex-shrink-0 mt-0.5 bangla">৪</div>
        <div>
          <h4 class="font-bold text-gray-900 mb-1 bangla">প্রতিটা স্প্রে খাতায় লেখা</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">কোন ওষুধ, কেন, কত মাত্রায়, কোন জোনে, কবে, আর কবে থেকে ফসল তোলা যাবে।</p>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="w-8 h-8 rounded-full bg-primary-100 text-primary-700 font-black flex items-center justify-center flex-shrink-0 mt-0.5 bangla">৫</div>
        <div>
          <h4 class="font-bold text-gray-900 mb-1 bangla">খাতা সবার জন্য খোলা</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">আমাদের স্প্রে খাতা আমরা নিয়মিত হালনাগাদ করব।</p>
        </div>
      </div>
      <div class="flex gap-4">
        <div class="w-8 h-8 rounded-full bg-primary-100 text-primary-700 font-black flex items-center justify-center flex-shrink-0 mt-0.5 bangla">৬</div>
        <div>
          <h4 class="font-bold text-gray-900 mb-1 bangla">ভুল হলে জানাব</h4>
          <p class="text-gray-600 text-sm bangla leading-relaxed">কোনো নিয়ম ভাঙলে বা কোনো ফসল ফেলে দিতে হলে, সেটাও প্রকাশ করব।</p>
        </div>
      </div>
    </div>

    <!-- SPRAY LOG TABLE -->
    <div class="bg-white border border-gray-200 rounded-2xl overflow-hidden shadow-sm">
      <div class="bg-gray-50 px-6 py-4 border-b border-gray-200 flex justify-between items-center">
        <h4 class="font-bold text-gray-900 bangla"><i class="fa-solid fa-clipboard-list text-primary-600 mr-2"></i> স্প্রে খাতা (নমুনা)</h4>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full text-left text-sm bangla">
          <thead class="bg-gray-50 text-gray-600">
            <tr>
              <th class="px-6 py-3 font-semibold">তারিখ</th>
              <th class="px-6 py-3 font-semibold">জোন/ফসল</th>
              <th class="px-6 py-3 font-semibold">কী ব্যবহার / কেন</th>
              <th class="px-6 py-3 font-semibold">অপেক্ষার সময়</th>
              <th class="px-6 py-3 font-semibold">ফসল তোলা যাবে</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 text-gray-600">
            <tr class="hover:bg-gray-50 transition-colors">
              <td class="px-6 py-4 whitespace-nowrap">২৩ জুন ২০২৬</td>
              <td class="px-6 py-4">স্ট্রবেরি জমি</td>
              <td class="px-6 py-4"><span class="font-bold text-gray-900">আগাছানাশক</span><br/><span class="text-xs text-gray-500">গভীর আগাছা দমন</span></td>
              <td class="px-6 py-4">—</td>
              <td class="px-6 py-4"><span class="bg-green-100 text-green-800 px-2 py-1 rounded text-xs font-semibold">রোপণের আগে</span></td>
            </tr>
            <tr class="hover:bg-gray-50 transition-colors">
              <td class="px-6 py-4 whitespace-nowrap">১৩ জুলাই ২০২৬</td>
              <td class="px-6 py-4">স্ট্রবেরি</td>
              <td class="px-6 py-4"><span class="font-bold text-gray-900">ছত্রাকনাশক (গোল্ডাজিম)</span><br/><span class="text-xs text-gray-500">গোড়া পচা ও ছত্রাক</span></td>
              <td class="px-6 py-4 text-orange-600 font-semibold">১৪ দিন</td>
              <td class="px-6 py-4">২৭ জুলাই এর পর</td>
            </tr>
            <tr class="hover:bg-gray-50 transition-colors">
              <td class="px-6 py-4 whitespace-nowrap">৪ সেপ্টে. ২০২৬</td>
              <td class="px-6 py-4">স্ট্রবেরি</td>
              <td class="px-6 py-4"><span class="font-bold text-gray-900">কীটনাশক (রাগবি)</span><br/><span class="text-xs text-gray-500">নেমাটোড ও পোকা</span></td>
              <td class="px-6 py-4 text-orange-600 font-semibold">২১ দিন</td>
              <td class="px-6 py-4">২৫ সেপ্টে. এর পর</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

<!-- ═══ PLAN ═══ -->
<section class="py-20 bg-gray-50 border-t border-gray-100">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 fade-in text-center">
    <h2 class="text-3xl font-black text-gray-900 mb-4 bangla">আমাদের পরিকল্পনা</h2>
    <p class="text-gray-500 bangla mb-10">আমি তাড়াহুড়ো করি না। আগে ছোট করে প্রমাণ, তারপর বড়।</p>
    
    <div class="grid md:grid-cols-3 gap-6 text-left">
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 relative overflow-hidden">
        <div class="absolute top-0 left-0 w-1 h-full bg-amber-400"></div>
        <div class="text-xs font-bold text-amber-500 uppercase tracking-widest mb-2 bangla">ধাপ ১</div>
        <h4 class="text-lg font-bold text-gray-900 mb-2 bangla">প্রমাণ</h4>
        <p class="text-gray-600 text-sm bangla mb-3">২৮ শতকে স্ট্রবেরির প্রথম মৌসুম, খোলা খাতাসহ। প্রথম ফলনে আসল ডেটা।</p>
        <span class="inline-block bg-amber-50 text-amber-700 text-[10px] font-bold px-2 py-1 rounded bangla">চলমান (ফল আসবে ডিসেম্বরে)</span>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 relative overflow-hidden">
        <div class="absolute top-0 left-0 w-1 h-full bg-gray-300"></div>
        <div class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-2 bangla">ধাপ ২</div>
        <h4 class="text-lg font-bold text-gray-900 mb-2 bangla">ভিত্তি</h4>
        <p class="text-gray-600 text-sm bangla mb-3">৭ বিঘায় ৫ ফসল ধীরে ধীরে বসানো।</p>
        <span class="inline-block bg-gray-100 text-gray-500 text-[10px] font-bold px-2 py-1 rounded bangla">শীঘ্রই আসছে...</span>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 relative overflow-hidden">
        <div class="absolute top-0 left-0 w-1 h-full bg-gray-300"></div>
        <div class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-2 bangla">ধাপ ৩</div>
        <h4 class="text-lg font-bold text-gray-900 mb-2 bangla">বড় হওয়া</h4>
        <p class="text-gray-600 text-sm bangla mb-3">ভালো ফল পেলে নতুন ফসল, নতুন জমি।</p>
        <span class="inline-block bg-gray-100 text-gray-500 text-[10px] font-bold px-2 py-1 rounded bangla">প্রথম দুই ধাপের ওপর নির্ভর</span>
      </div>
    </div>
  </div>
</section>

<!-- ═══ MISTAKES & BELIEFS ═══ -->
<section class="py-20 bg-white">
  <div class="max-w-5xl mx-auto px-4 sm:px-6">
    <div class="grid md:grid-cols-2 gap-12 fade-in">
      
      <div>
        <h2 class="text-3xl font-black text-gray-900 mb-6 bangla">ভুল থেকে শেখা</h2>
        <div class="prose prose-sm bangla text-gray-600">
          <p>এই ১১১ দিনে আমি সবকিছু ঠিকঠাক করিনি। জুলাইয়ের বর্ষায় ড্রেনেজ, কেল্লা ঘাস আর গোড়া পচা একসঙ্গে এসেছিল। কিছু গাছ হারিয়েছি, তাই দুই দফায় মোট ২৫০টি চারা আবার বসাতে হয়েছে। এর প্রতিটা খরচ খোলা খাতায় লেখা আছে।</p>
          <p class="font-bold text-primary-700 border-l-4 border-primary-500 pl-4 py-1 my-4">
            আমি এটা লুকাই না, কারণ যে চাষি ভুলের কথা বলে না, তার কথায় ভরসা করা কঠিন।
          </p>
        </div>
      </div>

      <div class="bg-primary-900 p-8 rounded-3xl text-white shadow-xl">
        <h2 class="text-2xl font-black mb-6 bangla text-primary-300">আমি যা বিশ্বাস করি</h2>
        <ul class="space-y-4 bangla">
          <li class="flex gap-3">
            <i class="fa-solid fa-check-circle text-primary-400 mt-1"></i>
            <div><strong class="text-white block mb-0.5">সত্য আগে</strong> যা জানি না, বলি না। যা জানি, তার প্রমাণ দেখাই।</div>
          </li>
          <li class="flex gap-3">
            <i class="fa-solid fa-check-circle text-primary-400 mt-1"></i>
            <div><strong class="text-white block mb-0.5">ধৈর্য</strong> মাটি তাড়াহুড়ো মানে না।</div>
          </li>
          <li class="flex gap-3">
            <i class="fa-solid fa-check-circle text-primary-400 mt-1"></i>
            <div><strong class="text-white block mb-0.5">স্বচ্ছতা</strong> খাতা, স্প্রে, ভুল, সবই সবার জন্য।</div>
          </li>
          <li class="flex gap-3">
            <i class="fa-solid fa-check-circle text-primary-400 mt-1"></i>
            <div><strong class="text-white block mb-0.5">ধীরে বড় হওয়া</strong> ছোট প্রমাণ, তারপর বড় পদক্ষেপ।</div>
          </li>
        </ul>
      </div>

    </div>
  </div>
</section>

<!-- ═══ CALL TO ACTION ═══ -->
<section class="py-24 bg-section-alt relative overflow-hidden">
  <div class="max-w-4xl mx-auto px-4 text-center relative z-10 fade-in">
    <h2 class="text-3xl md:text-5xl font-black text-gray-900 mb-4 bangla">ধাপে ধাপে চিনুন।<br/><span class="text-primary-600">কিছুই দিতে হবে না আগে।</span></h2>
    <div class="flex flex-col md:flex-row justify-center gap-6 mb-10 mt-8 max-w-3xl mx-auto">
      <div class="bg-white p-4 rounded-xl shadow-sm flex-1 text-center border border-gray-100">
        <div class="w-10 h-10 bg-blue-50 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-2 font-bold bangla">১</div>
        <h4 class="font-bold text-gray-900 bangla mb-1">দেখুন</h4>
        <p class="text-gray-500 text-xs bangla">আমার ভিডিও ও খোলা খাতা</p>
      </div>
      <div class="bg-white p-4 rounded-xl shadow-sm flex-1 text-center border border-gray-100">
        <div class="w-10 h-10 bg-green-50 text-green-600 rounded-full flex items-center justify-center mx-auto mb-2 font-bold bangla">২</div>
        <h4 class="font-bold text-gray-900 bangla mb-1">ঘুরে যান</h4>
        <p class="text-gray-500 text-xs bangla">ফার্মে এসে গাছ আর খাতা নিজ চোখে দেখুন</p>
      </div>
      <div class="bg-white p-4 rounded-xl shadow-sm flex-1 text-center border border-gray-100">
        <div class="w-10 h-10 bg-amber-50 text-amber-600 rounded-full flex items-center justify-center mx-auto mb-2 font-bold bangla">৩</div>
        <h4 class="font-bold text-gray-900 bangla mb-1">তারপর ভাবুন</h4>
        <p class="text-gray-500 text-xs bangla">চাইলে "মাটির অংশীদার" হতে পারেন</p>
      </div>
    </div>
    
    <a href="https://wa.me/8801XXXXXXXXX" target="_blank" class="inline-flex items-center gap-3 bg-primary-600 hover:bg-primary-700 text-white font-bold px-10 py-4 rounded-full transition-colors bangla shadow-xl hover:scale-105">
      <i class="fa-brands fa-whatsapp text-2xl"></i> চলুন, কথা বলি →
    </a>
    <p class="text-gray-500 text-xs mt-5 bangla">📞 01XXXXXXXXX · সকাল ৮টা – রাত ১০টা · কোনো তাড়া নেই।</p>
  </div>
</section>
"""

with open('about.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_index = -1
end_index = -1
for i, line in enumerate(lines):
    if "<!-- ═══ PAGE HEADER ═══ -->" in line:
        start_index = i
    if "<!-- ═══ FOOTER ═══ -->" in line:
        end_index = i
        break

if start_index != -1 and end_index != -1:
    final_content = "".join(lines[:start_index]) + new_content + "".join(lines[end_index:])
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Replaced successfully")
else:
    print("Tags not found", start_index, end_index)
