# GA4 Event Tracking Implementation Report for Iaroslav Zhakun's Webpage

## Introduction

This report outlines the key user interaction points identified on the given webpage, along with recommended GA4 event tracking specifications. The elements identified include Forms, Main CTAs, Phone links, and Email links. 

## Key Conversion Elements

### 1. Email Contact Link

- **Event Name:** `click_email_contact`
- **Trigger Type:** `All Elements Click`
- **CSS Selector:** `a[href^="mailto:"]`
- **Event Parameters:** 
  - `link_url`: The generated data will capture the `mailto` link, e.g., `yaroslav.zhakun@gmail.com`.

### 2. Phone Contact Link

- **Event Name:** `click_contact_phone`
- **Trigger Type:** `All Elements Click`
- **CSS Selector:** `a[href^="tel:"]`
- **Event Parameters:** 
  - `link_url`: The capture will include the phone number link, e.g., `tel:+123456789`.

### 3. Contact Form Submission

- **Event Name:** `submit_contact_form`
- **Trigger Type:** `Form Submission`
- **CSS Selector:** `form#contactForm` (Assuming the form has an ID of `contactForm`)
- **Event Parameters:** 
  - `form_id`: Contact Form
  - `email_submitted`: {{Email Field Variable}} (Dynamic variable to capture the email entered)

### 4. Main Call-To-Action (CTA) Button Click

- **Event Name:** `click_main_cta`
- **Trigger Type:** `All Elements Click`
- **CSS Selector:** `button#ctaButton` (Assuming the main button has an ID of `ctaButton`)
- **Event Parameters:**
  - `button_text`: The text on the CTA button, e.g., `Start Free Trial`.

## GTM Implementation Plan

```markdown
# GTM Implementation Plan for Iaroslav Zhakun's Webpage GA4 Events

## 1. Email Contact Link
- **Event Name:** click_email_contact
- **Trigger Type:** All Elements Click
- **CSS Selector:** `a[href^="mailto:"]`
- **Event Parameters:** 
  - link_url: `${Click URL}`

## 2. Phone Contact Link
- **Event Name:** click_contact_phone
- **Trigger Type:** All Elements Click
- **CSS Selector:** `a[href^="tel:"]`
- **Event Parameters:** 
  - link_url: `${Click URL}`

## 3. Contact Form Submission
- **Event Name:** submit_contact_form
- **Trigger Type:** Form Submission
- **CSS Selector:** `form#contactForm` (Confirm ID on the form)
- **Event Parameters:** 
  - form_id: Contact Form
  - email_submitted: `${Email Variable}` (enable field tracking)

## 4. Main Call-To-Action Click
- **Event Name:** click_main_cta
- **Trigger Type:** All Elements Click
- **CSS Selector:** `button#ctaButton` (Confirm button ID)
- **Event Parameters:**
  - button_text: `${Click Text}`
```

## JSON-Like Summary for Automated Setup

```json
{
  "tracking_events": [
    {
      "event_name": "click_email_contact",
      "trigger_type": "All Elements Click",
      "css_selector": "a[href^='mailto:']",
      "event_parameters": {
        "link_url": "{{Click URL}}"
      }
    },
    {
      "event_name": "click_contact_phone",
      "trigger_type": "All Elements Click",
      "css_selector": "a[href^='tel:']",
      "event_parameters": {
        "link_url": "{{Click URL}}"
      }
    },
    {
      "event_name": "submit_contact_form",
      "trigger_type": "Form Submission",
      "css_selector": "form#contactForm",
      "event_parameters": {
        "form_id": "Contact Form",
        "email_submitted": "{{Email Variable}}"
      }
    },
    {
      "event_name": "click_main_cta",
      "trigger_type": "All Elements Click",
      "css_selector": "button#ctaButton",
      "event_parameters": {
        "button_text": "{{Click Text}}"
      }
    }
  ]
}
```

## Conclusion

This report provides a comprehensive overview of the key user interaction points on the webpage, along with recommended GA4 event tracking specifications. The provided GTM implementation plan and JSON-like summary will facilitate automated setup within the Google Tag Manager environment.