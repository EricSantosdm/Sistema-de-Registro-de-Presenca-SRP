module.exports = {
  content: [
    "./templates/*.html",
    "./templates/*/*.html",
    "./*/templates/*.html",
    "./*/templates/*/*.html",
    "./*/templates/*/*/*.html",
    "./*/templates/*/*/*/*.html",
    "./front_assets/static/front_assets/src/js/modules/*.js",
    "./front_assets/static/front_assets/src/js/vue/*/*.js",
    "./front_assets/static/front_assets/src/js/vue/**/*.js",
    // "./test/index.html"
  ],

  theme: {
    colors: {
      transparent: "transparent",
      current: "currentColor",
      white: "#fff",

      "neutral-10": "#F8F9FA",
      "neutral-20": "#F1F3F5",
      "neutral-30": "#E9ECEF",
      "neutral-40": "#DEE2E6",
      "neutral-50": "#CED4DA",
      "neutral-60": "#b8bcbf",
      "neutral-70": "#949799",
      "neutral-75": "#6d6f71",
      "neutral-80": "#495057",
      "neutral-90": "#3e3e40",
      "neutral-100": "#252526",

      "primary-20": "#FF871E",
      "primary-40": "#FF871E",
      "primary-60": "#FF871E",
      "primary-70": "#FF871E",
      "primary-80": "#FF871E",
      "primary-90": "#FF871E",
      "primary-100": "#FF871E",

      "yellow-50": "#FFBB0B",
      "green-50": "#18B25D",
      "laranja-50": "#D83232",

      //alerts
      "alert-red-100": "#EC3539",
      "alert-red-10": "#FEEBEC",
      "alert-red-10-o": "rgba(236, 53, 57, 0.1)",

      "alert-green-100": "#A6CE44",
      "alert-green-10": "#F7FBED",
      "alert-green-10-o": "rgba(24, 178, 93, 0.1)",

      "alert-warning-100": "#FDD426",
      "alert-warning-10": "#FFFBEA",
      "alert-warning-10-o": "rgba(253, 212, 38, 0.1)",
    },

    spacing: {
      0: "0",
      1: "1px",
      2: "0.125rem",
      4: "0.25rem",
      6: " 0.38rem",
      8: "0.5rem",
      10: ".625rem",
      12: "0.75rem",
      14: "0.875rem",
      16: "1rem",
      18: "1.13rem",
      20: "1.25rem",
      24: "1.5rem",
      28: "1.75rem",
      32: "2rem",
      34: "2.75rem",
      40: "2.5rem",
      42: "2.63rem",
      48: "3rem",
      56: "3.5rem",
      64: "4rem",
      72: "4.5rem",
      80: "5rem",
      96: "6rem",
      120: "7.5rem",
      160: "10rem",
    },

    fontFamily: {
      sans: ["Roboto Flex", "sans-serif"],
    },

    lineHeight: {
      100: "100%",
      140: "140%",
      150: "150%",
    },

    screens: {
      min2xl: { min: "1441px" },
      // => @media (max-width: 1535px) { ... }

      "2xl": { max: "1667px" },
      // => @media (max-width: 1535px) { ... }

      xl: { max: "1367px" },
      // => @media (max-width: 1279px) { ... }

      lg: { max: "1281px" },
      // => @media (max-width: 1023px) { ... }

      md2: { max: "1180px" },
      // => @media (max-width: 767px) { ... }

      md: { max: "767px" },
      // => @media (max-width: 767px) { ... }

      sm: { max: "639px" },
      // => @media (max-width: 639px) { ... }
    },

    extend: {
      gridTemplateColumns: {
        teste: "350px minmax(300px, 1fr) 50px",
        home: "minmax(auto, 814px) minmax(auto, 570px)",
      },

      letterSpacing: {
        tight: "-0.02em",
      },

      fontSize: {
        "2xl": [
          "1.5rem",
          {
            lineHeight: "150%",
          },
        ],
        xl: [
          "1.125rem",
          {
            lineHeight: "150%",
          },
        ],
        base: [
          "1rem",
          {
            lineHeight: "150%",
          },
        ],
        sm: [
          "0.875rem",
          {
            lineHeight: "150%",
          },
        ],
        xs: [
          ".75rem",
          {
            lineHeight: "150%",
            letterSpacing: "0.03em",
          },
        ],
        "xs-space": [
          ".75rem",
          {
            lineHeight: "150%",
            letterSpacing: "0.1em",
          },
        ],
      },

      boxShadow: {
        xs: "0px 1px 2px #CED4DA",
        sm: "0px 8px 16px rgba(206, 212, 218, 0.3)",
        lg: "0px 24px 32px rgba(206, 212, 218, 0.25)",
        regular: "0px 8px 16px rgba(206, 212, 218, 0.3)",
        medium: "0px 8px 16px rgba(212, 213, 217, 0.3)",
      },
    },
  },
};
