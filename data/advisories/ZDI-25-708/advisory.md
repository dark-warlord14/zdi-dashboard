# ZDI-25-708: Mozilla Firefox Web Page Download Mark-Of-The-Web Protection Mechanism Failure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-708
- **ZDI-CAN:** ZDI-CAN-22536
- **Date:** 2025-07-29
- **CVE:** CVE-2024-3863
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-708/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Mark-Of-The-Web protection mechanism on affected installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must perform a specific action on a malicious page. The specific flaw exists within the web page download functionality. An attacker can abuse the functionality to create files without the Mark-Of-The-Web. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current user.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2024-18/#CVE-2024-3863

## Disclosure Timeline

- 2024-02-13 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated
