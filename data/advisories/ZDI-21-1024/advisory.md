# ZDI-21-1024: Microsoft Word glTF-SDK Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1024
- **ZDI-CAN:** ZDI-CAN-13401
- **Date:** 2021-08-26
- **CVE:** CVE-2021-34478
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Word
- **Credit:** Thomas Bouzerar (@MajorTomSec) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1024/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the glTF-SDK component. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34478

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-08-26 - Coordinated public release of advisory
