# ZDI-22-1408: Microsoft Windows CDFS Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1408
- **ZDI-CAN:** ZDI-CAN-17576
- **Date:** 2022-10-14
- **CVE:** CVE-2022-38044
- **CVSS:** 7.7
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Bien Pham (@bienpnn) from Team Orca of Sea Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1408/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ISO files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-38044

## Disclosure Timeline

- 2022-06-14 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
