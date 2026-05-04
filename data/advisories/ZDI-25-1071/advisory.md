# ZDI-25-1071: IceWarp gmaps Cross-Site Scripting Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1071
- **ZDI-CAN:** ZDI-CAN-25441
- **Date:** 2025-12-10
- **CVE:** CVE-2025-14499
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** IceWarp
- **Affected Products:** IceWarp
- **Credit:** Nicolas Chatelain
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1071/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of IceWarp. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of a parameter passed to the gmaps webpage. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

IceWarp has issued an update to correct this vulnerability. More details can be found at: https://support.icewarp.com/hc/en-us/community/posts/40040542307729-EPOS-Update-2-build-8-14-2-0-8

## Disclosure Timeline

- 2025-08-20 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-11 - Advisory Updated
