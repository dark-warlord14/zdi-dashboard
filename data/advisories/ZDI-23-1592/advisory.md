# ZDI-23-1592: GIMP DDS File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1592
- **ZDI-CAN:** ZDI-CAN-22093
- **Date:** 2023-11-14
- **CVE:** CVE-2023-44441
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1592/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DDS files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GIMP has issued an update to correct this vulnerability. More details can be found at: https://www.gimp.org/news/2023/11/07/gimp-2-10-36-released/

## Disclosure Timeline

- 2023-09-22 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
