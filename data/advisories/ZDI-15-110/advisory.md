# ZDI-15-110: (Pwn2Own) Mozilla Firefox resource: URL Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-110
- **ZDI-CAN:** ZDI-CAN-2826
- **Date:** 2015-04-03
- **CVE:** CVE-2015-0816
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Mariusz Mlynski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-110/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of documents loaded through the resource: URL. As the same flag was used for chrome: and resource: URLs, these pages were able to subsequently load privileged chrome pages. By combining this with a same-origin policy bypass, an attacker could execute arbitrary code in the context of the current user.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2015-33/

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-04-03 - Coordinated public release of advisory
