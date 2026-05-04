# ZDI-21-1202: Foxit PDF Reader JPG2000 File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1202
- **ZDI-CAN:** ZDI-CAN-14812
- **Date:** 2021-10-15
- **CVE:** CVE-2021-34971
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Milan Kyselica of IstroSec.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1202/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2021-09-01 - Vulnerability reported to vendor
- 2021-10-15 - Coordinated public release of advisory
