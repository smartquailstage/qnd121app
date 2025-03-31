///////////////
jQuery( () => {
///////////////

const tabbedContent = $(`form .tab-content, form .nice-padding`);
const topLevel = (tabbedContent.length > 0) ? tabbedContent.first() : $(`.content form`);
const languageCodeRegex = new RegExp(' \\[('+wagtailModelTranslations.languages.join('|')+')\\]');

if (topLevel.length === 0) {
  // obviously, if we don't have an element to attach
  // the picker to, we might as well stop right now.
  return;
}

if (topLevel.attr(`class`) && topLevel.attr(`class`).indexOf(`search`) > -1) {
  // if the only forms on the page are search forms,
  // we're not actually dealing with page/snippets
  return;
}

/**
 * ...
 */
function filterForLocale(index, element) {
  var tc = element.textContent;
  var res = languageCodeRegex.exec(tc);
  if (res === null) return;

  var code = res[0],
      locale = code.replace(/[ \[\]]/g,'');

  // Verify this is a known locale and not a fluke,
  // using the global "wagtailModelTranslations.languages"
  // variable, which is an
  // array of all language codes specified in the
  // settings.LANGUAGES variable for Django.
  if (wagtailModelTranslations.languages.indexOf(locale) === -1) return;

  // Bootstrap an empty bin if we don't have one.
  if (!localisedElements[locale]) {
    localisedElements[locale] = [];
  }

  // Add this element to our bin, provided it had
  // not already been added.
  var bin = localisedElements[locale];
  if (bin.indexOf(element) === -1) {
    bin.push(element);
    element.classList.add(`l10n-hidden`);

    // also note that "field-col" elements may now look horribly
    // wrong, due to how Wagtail computes which of "col3"..."col12"
    // to use. Because wagtail-modeltranslation introduces many more
    // elements to show in an "inline" element, things that were
    // "col6" before end up being "col1", looking terribly wrong indeed.
    element.classList.remove(...columnCSS);
  }
}

/**
 * Build the set of fields-per-locale. Each set will receive
 * a button to toggle visibility for all fields in that set,
 * with the note that unlocalised content (such as images)
 * will always stay visible.
 */
function buildSets(topElement) {
  $(`section.w-panel:not(#panel-child-content-panel-section), div.w-panel__wrapper`, topElement).each( filterForLocale );
  document.dispatchEvent(new CustomEvent('wagtail-modeltranslation:buildSets:done'));
}

/**
 * Gets all selected locales as array of strings
 */
function getSelectedLocales() {
  var selectedLocales = [];
  $('.showing-locale').each(function() {
    selectedLocales.push($(this).text());
  });
  return selectedLocales;
}

/**
 * Adds event listeners on click for inlines.
*/
$('a[id^=id_][id$=-ADD], button[id^=id_][id$=-ADD]').click(e => {
  e.preventDefault();
  // get the ul where all inlines will be added
  ulForms = $(e.currentTarget).parent().siblings('ul.multiple')[0];
  // register new fields in sets
  buildSets(ulForms);
  // remove visibility class for selected locales
  selectedLocales = getSelectedLocales();
  selectedLocales.forEach( locale => {
    toggleLocale(locale, true);
  });
});

/**
 * Build a locale picker bar, with buttons that toggle
 * visibility for each locale's fields.
 */
function buildLocaleToggler() {
  var bar = $(`<div class="locale-picker w-form-width"><h2>${wagtailModelTranslations.viewEditString}</h2></div>`);
  var ul = $(`<ul class="locales"></ul>`);
  bar.append(ul);

  var toggles = {};
  wagtailModelTranslations.languages.forEach( locale => {
    var li = $(`<li class="locale"><button type="button" class="locale-toggle">${locale}</button></li>`);
    ul.append(li);

    $(`button.locale-toggle`, li).each( (index, toggle) => {
      toggle.addEventListener(`click`, e => {
        e.preventDefault();
        toggle.classList.toggle(`showing-locale`);
        toggleLocale(locale, toggle.classList.contains(`showing-locale`));
      });

      toggles[locale] = toggle;
    });
  });

  bar.prependTo(topLevel);

  return toggles;
}

/**
 * This function allows either blind toggling
 * of a field's visibility, or explicitly
 * making visible/invisible based on the
 * value of `state` (a boolean).
 */
function toggleLocale(locale, state) {
  var action = state ? `remove` : `add`;

  localisedElements[locale].forEach(element => {
    element.classList[action](`l10n-hidden`);
  });

  //store current state
  let cur_state = JSON.parse(localStorage.getItem('initially_loaded_locale') || "{}");
  cur_state[locale] = state;
  localStorage.setItem('initially_loaded_locale', JSON.stringify(cur_state));
}

var default_locale = wagtailModelTranslations.defaultLanguage;
var localisedElements = {};
var columnCSS = [`field-col`];
for (var i=1; i<=12; i++) { columnCSS.push(`col${i}`); }

// Build the sets that track which fields
// belong to which language code.
buildSets(topLevel);

var locales = Object.keys(localisedElements).sort();

// If there are no locale sets, then there is
// no locale field picker to build, either.
if (locales.length === 0) return;

var localeToggler = buildLocaleToggler();


let initially_loaded_locale = wagtailModelTranslations.locale_picker_default;

// Restore enabled locale
if(wagtailModelTranslations.locale_picker_restore){
  let stored = localStorage.getItem('initially_loaded_locale');
  if(stored !== null){
    let stored_state = JSON.parse(stored);
    initially_loaded_locale = Object.keys(stored_state).filter(k=>stored_state[k]);
  }
}

for (language of initially_loaded_locale) {
    localeToggler[language].classList.add(`showing-locale`);
    toggleLocale(language, true);
}

///////////////
});
///////////////
