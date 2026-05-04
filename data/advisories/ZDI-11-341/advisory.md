# ZDI-11-341: Cisco WebEx Player WRF Type 0 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-341
- **ZDI-CAN:** ZDI-CAN-1236
- **Date:** 2011-12-07
- **CVE:** CVE-2011-3319
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Aniway (Aniway.Anyway@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-341/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within atdl2006.dll. The vulnerability is caused by lack of validation when parsing WRF files. A specially crafted WRF file will cause the application to incorrectly push a size value to a memcpy, allowing for corruption of heap memory. An attacker can leverage this vulnerability to execute arbitrary code on the target system under the context of the current user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20111026-webex

## Disclosure Timeline

- 2011-05-25 - Vulnerability reported to vendor
- 2011-12-07 - Coordinated public release of advisory
