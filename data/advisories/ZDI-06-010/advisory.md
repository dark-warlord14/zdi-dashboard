# ZDI-06-010: Mozilla Firefox CSS Letter-Spacing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-010
- **ZDI-CAN:** ZDI-CAN-015
- **Date:** 2006-04-17
- **CVE:** CVE-2006-1730
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 1.5.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-010/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the Mozilla/Firefox web browser and Thunderbird e-mail client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious e-mail. The specific flaw is due to incorrect handling of the CSS "letter-spacing" element. By specifying a large number, an attacker can overflow an integer used during memory allocation. The under-allocated buffer is later used to store user-supplied data leading to an exploitable heap overflow.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2006/mfsa2006-22.html

## Disclosure Timeline

- 2006-01-31 - Vulnerability reported to vendor
- 2006-04-17 - Coordinated public release of advisory
