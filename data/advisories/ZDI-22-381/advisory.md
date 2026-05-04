# ZDI-22-381: Microsoft Outlook for Mac Hyperlink UI Misrepresentation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-381
- **ZDI-CAN:** ZDI-CAN-14886
- **Date:** 2022-02-18
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Outlook for Mac
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-381/
## Vulnerability Details

This vulnerability allows remote attackers to disguise the target of hyperlinks on affected installations of Microsoft Outlook for Mac. User interaction is required to exploit this vulnerability in that the target must view a malicious email. The specific flaw exists within the rendering of HTML in email. By supplying crafted HTML, an attacker can cause Outlook to incorrectly display the target of a hyperlink upon mouse hover. An attacker can leverage this vulnerability to deceive an email recipient regarding the trustworthiness of a link.

## Additional Details

Fixed in version 16.53 and forward.

## Disclosure Timeline

- 2021-08-05 - Vulnerability reported to vendor
- 2022-02-18 - Coordinated public release of advisory
