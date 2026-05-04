# ZDI-24-1302: Foxit PDF Reader PDF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1302
- **ZDI-CAN:** ZDI-CAN-24300
- **Date:** 2024-09-26
- **CVE:** CVE-2024-9248
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1302/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2024-06-26 - Vulnerability reported to vendor
- 2024-09-26 - Coordinated public release of advisory
- 2024-09-26 - Advisory Updated
