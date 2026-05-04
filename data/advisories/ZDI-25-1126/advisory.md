# ZDI-25-1126: Apple Safari JavaScriptCore HashTable Expansion Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1126
- **ZDI-CAN:** ZDI-CAN-28284
- **Date:** 2025-12-17
- **CVE:** CVE-2025-43501
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Hossein Lotfi (@hosselot) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1126/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HashTable expansion. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/125892

## Disclosure Timeline

- 2025-10-15 - Vulnerability reported to vendor
- 2025-12-17 - Coordinated public release of advisory
- 2025-12-17 - Advisory Updated
