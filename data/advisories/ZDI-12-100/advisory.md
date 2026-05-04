# ZDI-12-100: HP OpenView Performance Manager PMParamHandler Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-100
- **ZDI-CAN:** ZDI-CAN-1340
- **Date:** 2012-06-21
- **CVE:** CVE-2012-0127
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Performance Manager
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-100/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP OpenView Performance Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PMParamHandler component of Performance Manager, which is served via an Apache Tomcat instance that listens on TCP port 8081. The process receives a filename from a remote user and performs insufficient validation of the provided file path. Additionally, the user can specify an arbitrary extension due to premature truncation resulting from an embedded null byte. Remote unauthenticated attackers can exploit this vulnerability by sending malformed message packets to the target, which could lead to a directory traversing arbitrary file write and ultimately remote code execution under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03255321

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-21 - Coordinated public release of advisory
