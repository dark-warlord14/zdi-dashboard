# ZDI-11-226: Citrix EdgeSight Launcher Service Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-226
- **ZDI-CAN:** ZDI-CAN-1045
- **Date:** 2011-06-27
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Citrix
- **Affected Products:** EdgeSight
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-226/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Citrix EdgeSight. Authentication is not required to exploit this vulnerability. The flaw exists within the LauncherService.exe component which listens by default on TCP port 18747. When handling a request the process trusts a user supplied field in the packet specifying the length of data to follow, the process then copies the user supplied data, without validation, into a fixed-length buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Citrix has issued an update to correct this vulnerability. More details can be found at: http://support.citrix.com/article/CTX129699

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-06-27 - Coordinated public release of advisory
