# ZDI-22-813: Microsoft Word glTF-SDK Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-813
- **ZDI-CAN:** ZDI-CAN-15443
- **Date:** 2022-06-02
- **CVE:** CVE-2021-43875
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Word
- **Credit:** Thomas Bouzerar (@MajorTomSec) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-813/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the glTF-SDK component. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43875

## Disclosure Timeline

- 2021-10-27 - Vulnerability reported to vendor
- 2022-06-02 - Coordinated public release of advisory
