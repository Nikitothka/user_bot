<h1 align="center">Hi,to your attention <a href="https://github.com/Nikitothka/user_bot" target="_blank">USER BOT TELEGRAM</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">USER bot telegram with beautiful animation of creating custom hearts from emoticons in telegram</h3>

<h1 align="center"> 
<img  src="https://github.com/Nikitothka/user_bot/blob/master/example/gif.gif?raw=true" alt="Пример анимации"/>

<h1 align="center">Settings</h1>
<h3 >You need to do in order to set up a project with the framework.</h3>
<h3> Use the <a href="https://github.com/Nikitothka/user_bot" target="_blank">official documentation</a>
or the tips below:
  <h1>API Keys:
<h2>The very first step requires you to obtain a valid Telegram API key (API id/hash pair):

<h2>1.Visit https://my.telegram.org/apps and log in with your Telegram Account.<p>

2.Fill out the form with your details and register a new Telegram application.

3.Done. The API key consists of two parts: api_id and api_hash. Keep it secret.
 
  <div class="section" id="configuration">
<h2><ya-tr-span data-index="145-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Configuration" data-translation="Конфигурация" data-type="trSpan">Configuration</ya-tr-span></h2>
<p><ya-tr-span data-index="147-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="Having the API key from the previous step in handy, we can now begin to configure a Pyrogram project. " data-translation="Имея под рукой ключ API из предыдущего шага, мы теперь можем приступить к настройке проекта пирограммы. " data-type="trSpan">Having the API key from the previous step in handy, we can now begin to configure a Pyrogram project. </ya-tr-span><ya-tr-span data-index="148-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="There are two ways to do so, and you can choose what fits better for you:" data-translation="Есть два способа сделать это, и вы можете выбрать то, что вам больше подходит:" data-type="trSpan">There are two ways to do so, and you can choose what fits better for you:</ya-tr-span></p>
<ul>
<li><p><ya-tr-span data-index="149-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value="First option: create a new " data-translation="Первый вариант: создайте новый " data-type="trSpan">First option: create a new </ya-tr-span><code class="docutils literal notranslate"><span class="pre">config.ini</span></code><ya-tr-span data-index="149-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value=" file next to your main script, copy-paste the following and replace the " data-translation="файл рядом с вашим основным сценарием, скопируйте и вставьте следующее и замените значения " data-type="trSpan"> file next to your main script, copy-paste the following and replace the </ya-tr-span><em><ya-tr-span data-index="149-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value="api_id" data-translation="api_id" data-type="trSpan">api_id</ya-tr-span></em><ya-tr-span data-index="149-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value=" and " data-translation=" и " data-type="trSpan"> and </ya-tr-span><em><ya-tr-span data-index="149-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value="api_hash" data-translation="api_hash" data-type="trSpan">api_hash</ya-tr-span></em><ya-tr-span data-index="149-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value=" values with your own. " data-translation=" своими собственными. " data-type="trSpan"> values with your own. </ya-tr-span><ya-tr-span data-index="149-1" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value="This method allows you to keep your credentials out of your code without having to deal with how to load them." data-translation="Этот метод позволяет сохранить учетные данные в коде без необходимости решать, как их загружать." data-type="trSpan">This method allows you to keep your credentials out of your code without having to deal with how to load them.</ya-tr-span></p>
<div class="highlight-ini notranslate"><div class="highlight"><pre id="codecell0"><span></span><span class="k"><ya-tr-span data-index="150-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value="[pyrogram]" data-translation="[пирограмма]" data-type="trSpan">[pyrogram]</ya-tr-span></span>
<span class="na"><ya-tr-span data-index="150-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value="api_id" data-translation="api_id" data-type="trSpan">api_id</ya-tr-span></span> <span class="o"><ya-tr-span data-index="150-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="=" data-translation="=" data-type="trSpan">=</ya-tr-span></span> <span class="s"><ya-tr-span data-index="150-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="12345" data-translation="12345" data-type="trSpan">12345</ya-tr-span></span>
<span class="na"><ya-tr-span data-index="150-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value="api_hash" data-translation="api_hash" data-type="trSpan">api_hash</ya-tr-span></span> <span class="o"><ya-tr-span data-index="150-0" data-translated="true" data-source-lang="en" data-target-lang="ru" data-value="=" data-translation="=" data-type="trSpan">=</ya-tr-span></span> <span class="s"><ya-tr-span data-index="150-0" data-translated="false" data-source-lang="en" data-target-lang="ru" data-value="0123456789abcdef0123456789abcdef" data-translation="0123456789abcdef0123456789abcdef" data-type="trSpan">0123456789abcdef0123456789abcdef</ya-tr-span></span>
</pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell0">
      </div>
</div>
</li>

</ul>

</div>
  
  

  
