# ZDI-23-1772: (0Day) OpenAI ChatGPT Improper Input Validation Model Policy Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1772
- **ZDI-CAN:** ZDI-CAN-22660
- **Date:** 2023-12-13
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** OpenAI
- **Affected Products:** ChatGPT
- **Credit:** Demeng Chen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1772/
## Vulnerability Details

This vulnerability allows remote attackers to bypass policy restictions on affected versions of OpenAI ChatGPT. Authentication is required to exploit this vulnerability. The specific flaw exists within the interface to the ChatGPT-Vision Data model. The issue results from the lack of proper validation of a user-supplied string before using it as a prompt to the model. An attacker can leverage this vulnerability to bypass model policy restrictions and obtain generated text concerning subjects in a picture.

## Additional Details

12/05/23 – ZDI reported the vulnerability to the vendor. 12/05/23 – The vendor states that this model vulnerability type is out of the scope of their bug bounty program and that they would pass the report on to the appropriate team. 12/06/23– ZDI acknowledged their rejection and informed the vendor that we’re publishing this case as a zero-day advisory. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-11-21 - Vulnerability reported to vendor
- 2023-12-13 - Coordinated public release of advisory
