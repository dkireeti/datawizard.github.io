/**
 * Inject meta tags into the page head dynamically
 * This runs on every page load and adds verification + SEO meta tags
 */

(function() {
  // Meta tags to inject
  const metaTags = [
    {
      name: "google-site-verification",
      content: "-LWA7wrlxWsNletYqItd6Aza7EpvMY6DoCW0rXmPV0o"
    },
    {
      name: "description",
      content: "Wizardly - Hard Things Made Simple. Learn machine learning, Python, and more with deeper intuitive insights."
    },
    {
      name: "keywords",
      content: "machine learning, python, javascript, react, mathematics, education, data science, wizardly"
    },
    {
      name: "author",
      content: "Wizardly"
    },
    {
      property: "og:title",
      content: "Wizardly - Hard Things Made Simple"
    },
    {
      property: "og:description",
      content: "Learn machine learning, Python, and more with deeper intuitive insights."
    },
    {
      property: "og:type",
      content: "website"
    }
  ];

  /**
   * Check if a meta tag already exists
   */
  function metaTagExists(name, property) {
    const selector = property
      ? `meta[property="${property}"]`
      : `meta[name="${name}"]`;
    return document.querySelector(selector) !== null;
  }

  /**
   * Inject meta tag into head
   */
  function injectMetaTag(meta) {
    const tag = document.createElement("meta");
    
    if (meta.property) {
      tag.setAttribute("property", meta.property);
    } else if (meta.name) {
      tag.setAttribute("name", meta.name);
    }
    
    tag.setAttribute("content", meta.content);
    
    // Only add if it doesn't exist
    const exists = metaTagExists(meta.name, meta.property);
    if (!exists) {
      document.head.appendChild(tag);
      console.log(`[inject_meta.js] Added meta: ${meta.name || meta.property}`);
    }
  }

  /**
   * Run injection when DOM is ready
   */
  function injectAllMeta() {
    metaTags.forEach(injectMetaTag);
  }

  // Inject immediately if head is available, otherwise wait for DOMContentLoaded
  if (document.head) {
    injectAllMeta();
  } else {
    document.addEventListener("DOMContentLoaded", injectAllMeta);
  }
})();
