# ZDI-21-667: Microsoft Paint 3D GLB File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-667
- **ZDI-CAN:** ZDI-CAN-12873
- **Date:** 2021-06-10
- **CVE:** CVE-2021-31945
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Paint 3D
- **Credit:** garmin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-667/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Paint 3D. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GLB files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31945

## Disclosure Timeline

- 2021-02-02 - Vulnerability reported to vendor
- 2021-06-10 - Coordinated public release of advisory
