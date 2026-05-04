# ZDI-14-029: EMC AlphaStor Library Manager 0x4f Command Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-029
- **ZDI-CAN:** ZDI-CAN-1811
- **Date:** 2014-02-13
- **CVE:** CVE-2013-0946
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AlphaStor
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-029/
## Vulnerability Details

This vulnerability potentially allows remote attackers to execute arbitrary code on vulnerable installations of EMC AlphaStor for EMC Networker. Authentication is not required to exploit this vulnerability. The specific flaw exists within Library Manager (robotd.exe) which listens by default on port 3500. When parsing the 0x4f command, the process copies an arbitrary user supplied string into fixed sized buffers. An attacker could leverage this vulnerability into remote execution of arbitrary code as SYSTEM. Vendor patched May 2013, but did not notify the ZDI. As a result this advisory is posted late.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/526568

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2014-02-13 - Coordinated public release of advisory
