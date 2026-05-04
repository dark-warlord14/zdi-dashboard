# ZDI-25-1180: Foxit PDF Reader PDF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1180
- **ZDI-CAN:** ZDI-CAN-28558
- **Date:** 2025-12-19
- **CVE:** CVE-2025-66499
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1180/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2025-11-27 - Vulnerability reported to vendor
- 2025-12-19 - Coordinated public release of advisory
- 2025-12-19 - Advisory Updated
