# ZDI-13-257: HP Business Process Monitor tp_bpm_admin.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-257
- **ZDI-CAN:** ZDI-CAN-1802
- **Date:** 2013-11-24
- **CVE:** CVE-2013-2366
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Business Process Monitor
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-257/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Business Process Monitor. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of requests to the tp_bpm_admin.exe server which listens by default on TCP port 2696. This server exposes file upload functionality that is vulnerable to a directory traversal. This can be leveraged by an attacker to gain remote code execution under the context of SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03844594

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
