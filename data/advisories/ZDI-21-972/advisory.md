# ZDI-21-972: (Pwn2Own) Zoom Client Marketplace Use of Incorrectly-Resolved Name or Reference Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-972
- **ZDI-CAN:** ZDI-CAN-13616
- **Date:** 2021-08-17
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Zoom
- **Affected Products:** Client
- **Credit:** Daan Keuper and Thijs Alkemade from Computest
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-972/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Zoom Clients. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of Zoom Marketplace URLs. The issue results from the lack of proper validation of a user-supplied path prior to using it to access Marketplace resources. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current user.

## Additional Details

Zoom has issued an update to correct this vulnerability. More details can be found at: https://explore.zoom.us/en/trust/security/security-bulletin/

## Disclosure Timeline

- 2021-04-07 - Vulnerability reported to vendor
- 2021-08-17 - Coordinated public release of advisory
